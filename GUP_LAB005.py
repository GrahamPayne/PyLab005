def is_valid_part(part):
    # Check if part is digits only
    if not part.isdigit():
        return False

    # Conv to int
    num = int(part)

    #
    # Checking  0–255
    if num < 0 or num > 255:
        return False

    # Checking for 0 (except single "0")
    if len(part) > 1 and part[0] == '0':
        return False

    return True


# Test cases
print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))   # False
print(is_valid_part("0"))    # True
