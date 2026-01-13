


def seq(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return seq(n-1) + seq(n-2)


print(seq(4))
