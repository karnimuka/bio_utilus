def write_sequence(file, sequence) -> None:
    """Writes a sequence to a file"""
    file.write(sequence + "\n")


import re


# Извлекаем название белка из строки BLAST
def get_description(line: str) -> str:
    """
    Extracts protein description from BLAST

    Arguments:
    line: str - BLAST result line

    Returns str
    """
    columns = re.split(r"\s{2,}", line.strip())
    return columns[0]
