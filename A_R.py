from py._builtin import execfile


def main():
    while True:
        again = input("Enter 1 for Transient Response.\nEnter 2 for Load-Regulation."
                      "\nEnter 3 for Start-up Response.\nEnter 0 for exit.\n")
        again = int(again)
        if again == 3:
            print(f'you have selected Start-up Response ')
            # import test_code3
            execfile('test_code3.py')
        elif again == 2:
            print(f'you have selected Load Regulation ')
            # import test_code
            execfile('test_code2.py')

            # return
        elif again == 1:
            print(f'you have selected Transient Response ')
            # import test_code
            execfile('test_code.py')
        elif again == 0:
            print("you are exiting")
            exit(0)
        else:
            print("wrong selection You should enter from 0 to 3 only.")


if __name__ == "__main__":
    main()
