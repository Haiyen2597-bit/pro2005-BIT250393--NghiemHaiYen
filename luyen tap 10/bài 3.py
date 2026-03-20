def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input("Nhập số nguyên không âm: "))


if n < 0:
    print("Không có giai thừa cho số âm!")
else:
    print(f"Giai thừa của {n} là {factorial(n)}")
