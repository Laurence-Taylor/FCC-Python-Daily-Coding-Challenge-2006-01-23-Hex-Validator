def is_valid_hex(s):
    # Create a set of permesible values
    set_valid_hex = set('0123456789abcdefABCDEF')
    # Validate bounderies cases
    if len(s) > 7 or s[0] != '#': return False
    # iterate over the possible next 6 characters
    for char in s[1:]:
        # if some character is not valid return False
        if not char in set_valid_hex: return False
    return True

if __name__ == '__main__':
    print(is_valid_hex("#123"))
    print('-------')
    print(is_valid_hex("#123abc"))
    print('-------')
    print(is_valid_hex("#ABCDEF"))
    print('-------')
    print(is_valid_hex("#0a1B2c"))
    print('-------')
    print(is_valid_hex("#12G"))
    print('-------')
    print(is_valid_hex("#1234567"))
    print('-------')
    print(is_valid_hex("#12 3"))
    print('-------')
    print(is_valid_hex("fff"))