def intToRoman(num: int) -> str:
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    res = []
    for v, s in zip(vals, syms):
        if num == 0:
            break
        count = num // v
        if count:
            res.append(s * count)
            num -= v * count
    return "".join(res)

# Quick tests
if __name__ == "__main__":
    tests = [3, 4, 9, 58, 1994, 3999, 1]
    for t in tests:
        print(t, "->", intToRoman(t))
