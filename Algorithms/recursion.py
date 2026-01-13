

def sum_range(k):
  if k > 0:   # base case
    return k + sum_range(k - 1)
  else:
    return 0

result = sum_range(6)
print(result)


# 6 + sum(5)
# 6 + (5 + sum(4))
# 6 + (5 + (4 + sum(3)))
# 6 + (5 + (4 + (3 + sum(2))))
# 6 + (5 + (4 + (3 + (2 + sum(1)))))
# 6 + (5 + (4 + (3 + (2 + (1 + sum(0))))))


def countdown(n):
  if n == 0:   # base case
    print("Done!")
  else:
    print(n)
    countdown(n - 1)   # recursive call

countdown(5)

def factorial(n):
  if n == 1:   # base case
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))


# 5 * fact(4)
# 5 * (4 * fact(3))
# 5 * (4 * (3 * fact(2)))
# 5 * (4 * (3 * (2 * fact(1)))) # Base Case
# 5 * (4 * (3 * (2 * 1)
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120





