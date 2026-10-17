def write_sequence(file, sequence):
    file.write(sequence + "\n")


import re


# Извлекаем название белка из строки BLAST
def get_description(line: str):
    columns = re.split(r"\s{2,}", line.strip())

    return columns[0]
