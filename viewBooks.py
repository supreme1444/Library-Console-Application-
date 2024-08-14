import json

import pandas as pd


class Viewbooks:

    def view_books_all_books(self):
        try:
            df = pd.read_json('books.json', orient='records')
            return df
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")



