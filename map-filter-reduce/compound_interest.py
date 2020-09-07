import functools


def compount_interest(aportaciones):
    total = functools.reduce(lambda x, y: (x * 1.03) + (y * 1.01), aportaciones)
    return total


aportaciones = [10, 3, 45, 22, 50, 8, 12, 70]
total = compount_interest(aportaciones)
print("Saldo total: ", round(total, 2))
