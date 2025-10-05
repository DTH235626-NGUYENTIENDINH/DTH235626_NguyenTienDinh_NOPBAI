def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


# ===== Trường hợp 1 =====
def main1():
    global val
    val = 5
    print("Trường hợp 1:")
    print(sum1(5))  # in kết quả sum1
    print(sum2())   # in kết quả sum2
    print(sum3())   # in kết quả sum3

# ===== Trường hợp 2 =====
def main2():
    global val
    val = 5
    print("Trường hợp 2:")
    print(sum1(5))
    print(sum3())
    print(sum2())

# ===== Trường hợp 3 =====
def main3():
    global val
    val = 5
    print("Trường hợp 3:")
    print(sum2())
    print(sum1(5))
    print(sum3())


# Gọi thử 3 trường hợp
main1()
main2()
main3()