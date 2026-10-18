# ==========================================
# DAY-16 : RECURSION BASICS
# ==========================================

# 1. Print N to 1

def print_n_to_1(n):
    if n == 0:
        return

    print(n)
    print_n_to_1(n)


# 2. Print 1 to N

def print_1_to_n(n):
    if n == 0:
        return

    print_1_to_n(n-1)
    print(n)


# 3. Sum of First N Numbers

def sum_of_n(n):
    if n == 0:
        return 0

    return n + sum_of_n(n-1)


# 4. Factorial

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


# 5. Parameterized Recursion

def parameterized_sum(n, total):

    if n == 0:
        print(total)
        return

    parameterized_sum(n-1, total+n)


print("Print N to 1")
print_n_to_1(5)

print()

print("Print 1 to N")
print_1_to_n(5)

print()

print("Sum =", sum_of_n(5))

print("Factorial =", factorial(5))

print()

parameterized_sum(5,0)