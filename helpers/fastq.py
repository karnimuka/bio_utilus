# интервал GC состава (в процентах) для фильтрации
# где sequence: str - нуклеотидная последовательность, а gc_bounds: tuple - верхняя и нижняя границы
def check_gc(sequence: str, gc_bounds: tuple = (0, 100)) -> bool:
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    gc = (g + c) / len(sequence) * 100
    if gc_bounds[0] <= gc <= gc_bounds[1]:
        return True
    else:
        return False


# проверка длины последовательности
def check_length(sequence: str, length_bounds: tuple = (0, 2**32)) -> bool:
    length = len(sequence)
    if length_bounds[0] <= length <= length_bounds[1]:
        return True
    else:
        return False


# проверка среднего качества рида для фильтрации
def check_quality(quality: str, quality_threshold: int = 0) -> bool:
    total_quality = 0

    for symbol in quality:
        total_quality += ord(symbol) - 33

    average_quality = total_quality / len(quality)

    if average_quality >= quality_threshold:
        return True
    else:
        return False
