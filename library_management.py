
class Library:
    books = ['harrypotter', 'blackbeauty', 'cindrella', 'beautyandbeast']

    def __init__(self):
        print('Welcome to The Daily read')

    def displaybooks(self):
        print (f'We have the following books {Library.books}')

    def loan(self):
        dicct={}
        name = input('Please tell us your name :')
        name_book=input('Enter the book you want to choose :')
        if name_book in Library.books:
            dicct[name_book] = name
            with open('data.txt', 'a+') as f:
                f.write(str(dicct)+'\n')
                Library.books.remove(name_book)
        else:
            print('Book not available or wrong book entered')

    def addbook(self):
        new_book = input('Enter the book you want to donate :')
        Library.books.append(new_book)
        return f'The books now available are {Library.books}'


self = Library()
while True:
    user_select = input('Enter what do you want to do ?\n\n\n1)See books available (1)\n\n\n2)Take loan of the book (2)\n\n\n3)Donate any book (3):')
    print('Your choice is : ')

    # self=Library()
    # user_select=input('Enter what do you want to do ?\n1)See books available (1)\n2)Take loan of the book (2)\n3)Donate any book (3):')
    if user_select == '1' or user_select == 'A' or user_select == 'a' or user_select == 'See books available':
        self.displaybooks()
        print()
        print()
        select=input('Do you want to do anything else ?\n'
                     '1)Yes (Y)\n'
                     '2)No (N)\n'
                     'Your choice :')
        if select=='Y' or select=='y':
            continue
        elif select=='N' or select=="n":
            break

    elif user_select == '2' or user_select == 'B' or user_select == 'b':
        self.displaybooks()
        self.loan()
        select=input('Enter do you want to do anything else ?\n'
                     '1)Yes (Y)\n'
                     '2)No (N)\n'
                     'Your choice :')
        if select=='Y' or select=='y':
            continue
        elif select=='N' or select=="n":
            break

    elif user_select == '3' or user_select == 'C' or user_select == 'c':
        self.addbook()
        select=input('Enter do you want to do anything else ?\n'
                     '1)Yes (Y)\n'
                     '2)No (N)\n'
                     'Your choice :')
        if select=='Y' or select=='y':
            continue
        elif select=='N' or select=="n":
            break

    else:
        print('Invalid input')
        continue