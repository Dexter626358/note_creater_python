from Checker import check_file
from Reading import read_all_notes
import json
def download_notes(path):
    if check_file(path):
        note_dct = read_all_notes(path)
        with open("downloads.json", "w", encoding="utf-8") as file:
            json.dump(note_dct, file, indent=4)
        print("Записи выгружены в файл 'downloads.json'")
    else:
        print("Нет записей для загрузки")

