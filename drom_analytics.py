import statistics

def amount_statistics(params):
    print("Среднее занчение: ", statistics.mean(params))
    print("Минимальное значение: ", min(params))
    print("Максимальное значение: ", max(params))