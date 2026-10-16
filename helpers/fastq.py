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
