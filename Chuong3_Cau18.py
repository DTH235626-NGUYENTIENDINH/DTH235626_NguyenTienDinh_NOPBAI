n = int(input("Nhập n: "))
#hình 1
for i in range(n):
    if i==0 or i==n-1:
        print('* '*n)
    else:
        print('*' + ' '*(2*n - 3) + '*')
#Hình 2
print("---------------------------------------------------")
for i in range(1, n+1):
    print("  "*(n-i)+"* " * i)

print("---------------------------------------------------")
#hình 3
h = n // 2

# Tạo các dòng
lines = ['*' * i for i in range(1, h + 1)] + ['*' * n] + [' ' * (n - i) + '*' * i for i in range(h, 0, -1)]

# In ra, giữ nguyên dòng giữa
for idx, row in enumerate(lines):
    if idx == h:  # dòng giữa=
        print(row)
    else:
        print(''.join(c if i == 0 or i == len(row)-1 or row[i-1] != '*' or row[i+1] != '*' else ' '
                      for i, c in enumerate(row)))
