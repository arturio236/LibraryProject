from services.library_service import LibraryService

def main():
    library_service = LibraryService("library.json")
    library_service.load_data()

    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library_service.add_book(title, author)
        elif option == "2":
            title = input("Enter book title: ")
            library_service.remove_book(title)
        elif option == "3":
            user_name = input("Enter your name: ")
            book_title = input("Enter book title: ")
            library_service.borrow_book(user_name, book_title)
        elif option == "4":
            user_name = input("Enter your name: ")
            book_title = input("Enter book title: ")
            library_service.return_book(user_name, book_title)
        elif option == "5":
            break

if __name__ == "__main__":
    main()
