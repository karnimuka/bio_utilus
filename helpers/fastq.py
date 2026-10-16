# интервал GC состава (в процентах) для фильтрации
# где sequence: str - нуклеотидная последовательность, а gc_bounds: tuple - верхняя и нижняя границы
def check_gc(sequence: str, gc_bounds: tuple = (0, 100)) -> bool:
    if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)

    sequence = sequence.upper()
    if len(sequence) == 0:
        return False
    g = sequence.count("G")
    c = sequence.count("C")

    gc = (g + c) / len(sequence) * 100
    if gc_bounds[0] <= gc <= gc_bounds[1]:
        return True
    else:
        return False


# проверка длины последовательности
def check_length(sequence: str, length_bounds: tuple = (0, 2**32)) -> bool:
    if type(length_bounds) == int or type(length_bounds) == float:
        length_bounds = (0, length_bounds)
    length = len(sequence)
    if length_bounds[0] <= length <= length_bounds[1]:
        return True
    else:
        return False


# проверка среднего качества рида для фильтрации
def check_quality(quality: str, quality_threshold: int = 0) -> bool:
    total_quality = 0
    if len(quality) == 0:
        return False

    for symbol in quality:
        total_quality += ord(symbol) - 33

    average_quality = total_quality / len(quality)

    if average_quality >= quality_threshold:
        return True
    else:
        return False


# чтение файла
def read_fastq(file):
    name = file.readline()
    sequence = file.readline()
    plus = file.readline()
    quality = file.readline()

    return name, sequence, plus, quality
