class liabrary:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenddict - {}

    def displaybook(self):
        print(f"we have following books in our liabrary: {self.name}")
        for book in self.booklist:
            print(book)
    
    def lendbook(self, user, book):
        if book is not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("lender-book database has been updated. You can take the book now")

        else:
            print(f"book is already being used by {self.lenddict[book]}")
    
    def addbook(self, book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    books = liabrary (['python', 'rich dad poor dad', 'harry potter', 'figdet spinner', 'c++ basic'], "lets upskill")
    while (true):
        print(f"welcome to the {books.name} library. enter your choice to continue")
        print("1. display books")
        print("2. lend a book")
        print("3. add a book")
        print("4. return a book")
        user_choice = input()
        if user_choice not in [1, 2, 3, 4]:
            print("please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            book.displaybooks()
        
        elif user_choice == 2:
            book = input("enter the name of the book you want to lend:")
            user = input("enter your name")
            book.lendbook(user, book)

        elif user_choice == 3:
            book = input("enter the name of the book you want to add:")
            book.addbook(book)

        elif user_choice == 4:
            book = input("enter the book of the name you want to return:")
            book.returnbook(book)
        
        else:
            print("not a valid option")

            