import fileB

whatever = True

def thefunc():
    print("smtp fucker by @hani_j85")

while whatever == True:

    print("""
        1-spotfy checker
        2-smtp checker gmail
        3-smtp checker yahoo
    """)

    choice = input("Choice: ")

    if choice == "1":
        fileB.my_func()
        execfile('spotify-fucker.py')


    elif choice == "2":
                fileB.my_func()
        execfile('gmail-smtp-fucker.py')



    elif choice == "3":
                         fileB.my_func()
        execfile('yahoo-smtp-fucker.py')

    else:
        print("... again")