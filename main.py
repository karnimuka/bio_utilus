from helpers.fastq import read_fastq, check_gc, check_length, check_quality
import os


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)
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
