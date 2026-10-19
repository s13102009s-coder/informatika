import os
import sys
import json

# 1. Функция для получения текущей папки запуска
def get_base_dir():
    # Если программа запущена как собранный .exe файл (через PyInstaller)
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # Если программа запущена как обычный файл .py
    else:
        return os.path.dirname(os.path.abspath(__file__))

# 2. Функция для создания файла сохранений при первом запуске
def insure_save_file():
    # Получаем путь к папке, где находится наша программа
    base_dir = get_base_dir()
    # Формируем полный путь к файлу сохранения (он будет называться save.json)
    save_path = os.path.join(base_dir, "save.json")
    
    # Если такого файла еще нет, создаем его
    if not os.path.exists(save_path):
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)  # Создаем пустой файл сохранения (в виде пустого словаря)
        print("Файл сохранений успешно создан!")
    else:
        print("Файл сохранений уже существует.")
        
    return save_path

# --- Проверка работы (чтобы вы видели, что всё работает) ---
if __name__ == "__main__":
    print("Папка запуска:", get_base_dir())
    insure_save_file()
    input("\nНажмите Enter, чтобы закрыть программу...") # Чтобы окно не закрылось сразу