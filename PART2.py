
def is_valid_part(part):
    if not part.isdigit():
        return False
    num = int(part)
    if num < 0 or num > 255:
        return False
    if len(part) > 1 and part[0] == '0':
        return False
    return True


# This defines is_valid_ip
def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for p in parts:
        if not is_valid_part(p):
            return False

    return True


print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

#Recursion and Number Conversion
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


# Test cases
print(decimal_to_binary(10))    # "1010"
print(decimal_to_binary(255))   # "11111111"
print(decimal_to_binary(1))     # "1"

#Convert Binary to Decimal (Recursion)
def binary_to_decimal(b):
    if b == "":
        return 0
    else:

        left_bit = int(b[0])
        # Remaining bits
        rest = b[1:]
        return left_bit * (2 ** (len(b) - 1)) + binary_to_decimal(rest)


# Test cases
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
