while True:
    n = int(input("Nhập n (n > 0): "))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("{0} là số nguyên tố".format(n))
        break
    else:
        print("{0} không phải số nguyên tố.".format(n))
    hoi = input("Tiếp tục hông ní? (c/k): ")
    if hoi == 'k' or hoi == 'K':
        break
print("Matane~!")