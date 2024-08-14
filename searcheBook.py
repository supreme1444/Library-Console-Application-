import json

import pandas as pd


class SearcheBooks:
    def searche_books(self):
        try:
            df = pd.read_json('books.json', orient='records')
            searche = input("По каким критериям будем искать." + '\n' + "введите Автор,Название,Жанр" + '\n').title()
            if searche == "Автор":
                surname_autor = input("Введите имя и фамилию автора: ").lower()
                for index, row in df.iterrows():
                    if surname_autor.lower() in row["Автор"].lower():
                        print(f"Есть такая книга: {row['Название']}")
                    else:
                        print(searche+" не найден")
                        break
            elif searche == "Название":
                surname_autor = input("Введите название книги: ").lower()
                for index, row in df.iterrows():
                    if surname_autor.lower() in row["Название"].lower():
                        print(f"Есть такая книга: {row['Автор']}")
                    else:
                        print(searche+" не найден")
                        break
            elif searche == "Жанр":
                surname_autor = input("Введите название жанра: ").lower()
                for index, row in df.iterrows():
                    if surname_autor.lower() in row["Жанр"].lower():
                        print(f"Есть такая книга: {row['Автор']}")
                    else:
                        print(searche+" не найден")
                        break
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")