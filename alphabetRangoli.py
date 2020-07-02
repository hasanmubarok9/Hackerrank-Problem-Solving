def print_rangoli(size):
    for i in range(size):
        alphabets = '-'.join(chr(ord('a') + size - j - 1)
                             for j in range(i + 1))
        print((alphabets + alphabets[::-1][1:]
               ).center(4 * size - 3, '-'))

    for i in range(size-2, -1, -1):
        alphabets = '-'.join(chr(ord('a') + size - j - 1)
                             for j in range(i + 1))
        print((alphabets + alphabets[::-1][1:]
               ).center(4 * size - 3, '-'))


print_rangoli(3)
print_rangoli(5)
