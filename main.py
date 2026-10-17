from helpers.fastq import read_fastq, check_gc, check_length, check_quality
import os
from helpers.bio_files import write_sequence


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
) -> None:
    """
    Filters FASTQ reads by GC content, length and quality

    Arguments:
    input_fastq: str - path to input FASTQ file
    output_fastq: str - output FASTQ filename
    gc_bounds: tuple/number - GC content limits
    length_bounds: tuple/number - sequence length limits
    quality_threshold: int/float - minimum average Phred33 quality

    Returns:
    None - saves filtered reads to the filtered folder
    """
    # Создаём папку для результатов
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)
    # Открываем
    with open(input_fastq) as input_file, open(output_path, "w") as output_file:
        while True:
            name, sequence, plus, quality = read_fastq(input_file)
            if name == "":
                break

            seq = sequence.strip()
            qual = quality.strip()
            if (
                check_gc(seq, gc_bounds)
                and check_length(seq, length_bounds)
                and check_quality(qual, quality_threshold)
            ):
                output_file.write(name)
                output_file.write(sequence)
                output_file.write(plus)
                output_file.write(quality)


# Converts multiline FASTA to one line FASTA
def convert_multiline_fasta_to_oneline(input_fasta, output_fasta) -> None:
    """
    Converts  FASTA to oneline FASTA

    Arguments:
    input_fasta: str - input FASTA file
    output_fasta: str - output FASTA file

    Returns:
    None - saves sequences to a new FASTA file
    """
    sequence = ""

    with open(input_fasta) as input_file, open(output_fasta, "w") as output_file:
        for line in input_file:
            line = line.strip()

            if line.startswith(">"):
                if sequence != "":
                    write_sequence(output_file, sequence)

                output_file.write(line + "\n")
                sequence = ""
            # собираем
            else:
                sequence += line
        # Записываем последнюю последовательность
        if sequence != "":
            write_sequence(output_file, sequence)


# вытаскиваем наилучшие совпадения
from helpers.bio_files import get_description


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Extracts the best BLAST matches

    Arguments:
    input_file: str - input BLAST file
    output_file: str - output file

    Returns None.
    """
    proteins = []
    with open(input_file) as file:
        for line in file:
            # Находим таблицу совпадений
            if "Sequences producing significant alignments:" in line:
                # Пропускаем заголовоки
                file.readline()
                file.readline()
                # Читаем первое совпадение
                best_hit = file.readline()

                # Получаем название белка
                if best_hit.strip() != "":
                    protein = get_description(best_hit)
                    proteins.append(protein)
    # Сортируем названия
    proteins.sort()
    # Записываем результат
    with open(output_file, "w") as file:
        for protein in proteins:
            file.write(protein + "\n")
