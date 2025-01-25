# Arithmetic Operators
x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


# Assignment Operators
x = 5
print(x)

x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x //= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)

print(x := 3)


# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical Operators
x = 5

print(x < 5 and  x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))


# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)


# Membership Operators
print("banana" in x)
print("pineapple" not in x)


# Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)