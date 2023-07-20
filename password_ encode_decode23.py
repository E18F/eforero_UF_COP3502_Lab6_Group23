# Student name: Edison Forero

# encrypting password
def encode(pwrd):
    encrypted_pwrd = ''

    for n in pwrd:
        num = (int(n) + 3) % 10
        encrypted_pwrd += str(num)

    return encrypted_pwrd

def decode(passwd):
    s_to_int = [(int(i) - 3) % 10 for i in passwd]
    out = [str(i) for i in s_to_int]
    out_1 = "".join(out)
    return out_1



# User input menu
def print_menu():
    print('Menu \n-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def main():
    option = 0
    encrypted_pwrd = ''

    while option != 3:
        print_menu()
        option = int(input('Please enter an option: '))

        # entering and encrypting user password
        if option == 1:
            pwrd = input('Please enter your password to encode: ')
            encrypted_pwrd = encode(pwrd)
            print('Your password has been encoded and stored!')
            print()

        if option == 2:
            original = decode(encrypted_pwrd)
            print(f'The encoded password is {encrypted_pwrd}, and the original password is {original}.')
            print() 

    # option 3 to exit the program
    exit()


if __name__ == '__main__':
    main()
