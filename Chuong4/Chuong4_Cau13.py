def sum_of_divisors(n):
    """Tính tổng các ước số của n (không kể n)."""
    total = 1  # 1 luôn là ước của mọi số > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # tránh cộng trùng nếu i là căn bậc 2
                total += n // i
    return total if n > 1 else 0


def is_perfect(n):
    """Kiểm tra số hoàn thiện."""
    return sum_of_divisors(n) == n


def is_abundant(n):
    """Kiểm tra số thịnh vượng."""
    return sum_of_divisors(n) > n


# ===== Test thử =====
def main():
    numbers = [6, 12, 28, 15, 18]
    for num in numbers:
        print(f"Số {num}: ", end="")
        if is_perfect(num):
            print("Là số hoàn thiện")
        elif is_abundant(num):
            print("Là số thịnh vượng")
        else:
            print("Không phải số hoàn thiện/thịnh vượng")

if __name__ == "__main__":
    main()