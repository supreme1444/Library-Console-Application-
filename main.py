from addBook import AddBookfromlibr
from deleteBook import DeleteBookLibrary
from searcheBook import SearcheBooks
from viewBooks import Viewbooks


class Welcom:

    def welcom_library(self):
        print("Добро пожаловать в приложение для поиска книг")
        while True:
            choise=input("Что вы хотите сделать?"+ '\n' +"1)Добавить книгу"+'\n'+"2)Удалить книгу"+'\n'+"3)Просмотреть список книг"+'\n'+"4)Поиск книг"+'\n'+"5)Выход"+'\n')
            try:
                choise = int(choise)
                if choise==1:
                    book = AddBookfromlibr()
                    book.add_book()
                elif choise == 2:
                    delete_book = DeleteBookLibrary()
                    delete_book.choice_delete_book_from_library()
                elif choise ==3:
                    view_books = Viewbooks()
                    print(view_books.view_books_all_books())
                elif choise == 4:
                    searche_book = SearcheBooks()
                    searche_book.searche_books()
                elif choise == 5:
                    break

                break
            except ValueError:
                    print('Недопустимый ввод')

if __name__ == "__main__":
    welcom = Welcom()
    welcom.welcom_library()

