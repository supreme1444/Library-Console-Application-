import json
import pandas as pd

class DeleteBookLibrary:
    def choice_delete_book_from_library(self,index_searche):
        print("Книгу какого автора хотите удалить,введите название и автора")
        name_autor = input("Введите автора")
        name_book = input("Введите название книги")
        self.delete_book_from_library(name_autor, name_book)
    def delete_book_from_library(self,name_autor, name_book):
        try:
            df = pd.read_json('books.json', orient='records')
            for index, row in df.iterrows():
                if row["Автор"] == name_autor and row["Название"] == name_book:
                    print("Есть такая книга и она удалена")
                    df.drop(index, inplace=True)
                    with open('books.json', 'w', encoding='utf-8') as file:
                        json.dump(df.to_dict(orient='records'), file, ensure_ascii=False, indent=2)
                    break
            else:
                print("Такой книги нет")
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")







