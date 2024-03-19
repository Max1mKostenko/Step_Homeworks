def arithmetic_progression(start, step):
    current = start
    while True:
        yield current
        current += step


progression = arithmetic_progression(2, 3)
for _ in range(10):
    print(next(progression))
