def oscillate(start, count):
    for i in range(start, count):
        yield i      # giá trị gốc
        yield -i     # giá trị đối xứng qua 0


# Test
def main():
    for n in oscillate(-3, 5):
        print(n, end=' ')
    print()  # xuống dòng

if __name__ == "__main__":
    main()