import json


class AddBookfromlibr:
    def add_book(self):
        print("Введите информацию о книге:")
        name_autor = "Автор"
        name_book = "Название"
        year_book = "Год издания"
        stile_book = "Жанр"
        book = input("Введите автора ")
        name = input("Название книги ")
        year = input("Год издания ")
        stile = input("Жанр книги ")
        json_data={name_autor:book,name_book:name,year_book:year,stile_book:stile}
        self.append_book(json_data)
    def append_book(self,json_book):
        try:
            with open('books.json', 'r',encoding='utf-8') as file:
                data = json.load(file)
                data.append(json_book)

            with open('books.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False,indent=2)
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")


