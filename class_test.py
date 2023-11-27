class User:
    '''Creates a user that can interact with the library'''
    def __init__(self, username):
        self.username = username
        self.loans = []  # Each element is a dictionary {'book': book_info, 'loaned_by': username}
        self.library = []  # Each user has their own library

    def sign_up(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        with open("users.txt", "r") as file:
            for line in file:
                existing_username = line.strip().split(',')[0]
                if existing_username == username:
                    print("Username already taken. Please try again.")
                    return
        
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        print("Signup successful!")
        return username

    def sign_in(self, library):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open("users.txt", "r") as file:
            for line in file:
                existing_username, existing_password = line.strip().split(',')
                if existing_username == username and existing_password == password:
                    print(f"Welcome back, {username}!")
                    self.library = library.copy() 
                    return username
        print("Wrong username or password. Please try again.")
        return None

    def loan_out(self, title, author):
        for book in self.library:
            if book['title'] == title and book['author'] == author and book['stock'] > 0:
                book['stock'] -= 1
                loan_info = {'book': book, 'loaned_by': self.username}
                self.loans.append(loan_info)
                print(f"Book '{title}' by {author} loaned successfully by {self.username}")
                return True
        print(f"Book '{title}' by {author} not available for loan.")
        return False

    def return_in(self, title, author):
        for loan_info in self.loans:
            if loan_info['book']['title'] == title and loan_info['book']['author'] == author:
                if loan_info['loaned_by'] == self.username:
                    book = loan_info['book']
                    book['stock'] += 1
                    self.loans.remove(loan_info)
                    print(f"Book '{title}' by {author} returned successfully by {self.username}")
                    return True
                else:
                    print(f"You can't return a book loaned by another user.")
                    return False
        print(f"Book '{title}' by {author} not found in the user's loans.")
        return False

    def display_loans(self):
        print(f"{self.username}'s Loans:")
        for loan_info in self.loans:
            book = loan_info['book']
            print(f"Title: {book['title']}, Author: {book['author']}, Loaned by: {loan_info['loaned_by']}")

if __name__ == "__main__":
    global_library = [
        {'title': 'Book_1', 'author': 'Author_1', 'stock': 3},
        {'title': 'Book_2', 'author': 'Author_2', 'stock': 2},
        {'title': 'Book_3', 'author': 'Author_3', 'stock': 1}
    ]

    user_manager = User(None)
    logged_in = False

    while True:
        print("1. Sign up")
        print("2. Sign in")
        if logged_in:
            print("3. Loan a book")
            print("4. Return a book")
            print("5. Display user's loans")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            user_manager.username = user_manager.sign_up()
        elif choice == '2':
            username = user_manager.sign_in(global_library)
            if username:
                user_manager.username = username
                logged_in = True
        elif logged_in:
            if choice == '3':
                title = input("Enter the title of the book to loan: ")
                author = input("Enter the author of the book to loan: ")
                user_manager.loan_out(title, author)
            elif choice == '4':
                title = input("Enter the title of the book to return: ")
                author = input("Enter the author of the book to return: ")
                user_manager.return_in(title, author)
            elif choice == '5':
                user_manager.display_loans()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")

class Book:
    '''Defines the books with their attributes'''
    #Attributes of the book:
    def __init__(self, isbn, title, author, section, stock=0):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.section = section #A float (ex. 341.54) which indicates the section of the book based on the dewy decimal system 
        self.stock = stock

    def __repr__(self):
        return f"({self.isbn}, {self.title}, {self.author}, {self.stock})"

    def sectionPointer(self, sectionDecimal):
        '''Takes as input a decimal number and matches it with a pretty string of the section of the library (ex. 101.2-->'Euclidian Geometry')'''
        return

class Library:
    ''''''
    def __init__(self, books):
        self.books = []

    def __repr__(self):
        return f"{self.books}"

    def update(self):
        '''Updates the content of the list of books based on the database'''
        with open("database.txt", "r", encoding="utf-8") as database:
            for line in database:
                line = line.strip().split("\t")
                if line == [""]: continue
            #Defines the attributes of the book on the line
                isbn = line[0]
                title = line[1]
                author = line[2]
                stock = line[3]
                book = Book(isbn, title, author, stock)
                self.books.append(book)
        return self.books

    def add_book(self, book):
        #Adds a book to the database.txt and the list books of the library
        if isinstance(book, Book):
            with open("database.txt", "a", encoding="utf-8") as database:
                attributes = [str(book.isbn), book.title, book.author, str(book.stock)]
                book_str = "\t".join(attributes) + "\n"#The book attributes in a line seperated by tab spaces

            #Adds a new book only when it's not in the database
                if str(book) in str(self.books): pass
                else: database.write(book_str)

    def add_stock(self, book):
        return #To do

    def sub_stock(self, book):
        return #To do

    def find(self, book):
        return #To do

def ask_book():
    user_input = input("Enter book attributes seperated by tabs(isbn, title, author, stock): ")
    user_input = user_input.strip(" ").split("\t")
    book = Book(user_input[0], user_input[1], user_input[2], user_input[3])
    return book

def main():
    library = Library([])
    library.update()
    library.add_book(ask_book())
    library.update()
    print(library)


if __name__ == "__main__":
    main()









