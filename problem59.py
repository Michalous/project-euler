permissible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.;:()[]{}<>!? _+-*/=&@£$%^*\\\'"'

def main():
    with open("0059_cipher.txt", "r") as handle:
        data = handle.read()    
    cipher_array = data.split(',')
    
    for a in permissible_chars[0:26]:
        for b in permissible_chars[0:26]:
            for c in permissible_chars[0:26]:
                test_string = ""
                for i in range(0, len(cipher_array) - 2, 3):
                    d = chr(xor_cipher(cipher_array[i], ord(a)))
                    e = chr(xor_cipher(cipher_array[i + 1], ord(b)))
                    f = chr(xor_cipher(cipher_array[i + 2], ord(c)))
                    if d not in permissible_chars or e not in permissible_chars or f not in permissible_chars:
                        break
                    test_string += (d + e + f)
                if test_string.count('the') > 5:
                    print(test_string)
                    print('======')
                    print(a,b,c)
                    print(sum([ord(x) for x in test_string]))
                    print('======')


def xor_cipher(num, key):
    return int(num) ^ key

if __name__ == "__main__":
    main()