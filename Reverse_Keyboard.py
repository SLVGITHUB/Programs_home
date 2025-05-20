import pyperclip
import keyboard
import time
import sys

# Словарь для замены символов
LAYOUT_MAP = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '`': 'ё', 'Q': 'Й',
    'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш',
    'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы', 'D': 'В',
    'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж',
    '"': 'Э', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т',
    'M': 'Ь', '<': 'Б', '>': 'Ю', '?': 'б', '~': 'Ё'
}

REVERSE_LAYOUT_MAP = {v: k for k, v in LAYOUT_MAP.items()}


def fix_selected_text():
    original_clipboard = pyperclip.paste()

    try:
        # Очищаем буфер перед копированием
        pyperclip.copy('')
        time.sleep(0.1)

        # Копируем выделенный текст
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.2)

        selected_text = pyperclip.paste()
        if not selected_text.strip():
            return

        # Преобразуем текст
        fixed_text = []
        for char in selected_text:
            if char in REVERSE_LAYOUT_MAP:
                fixed_text.append(REVERSE_LAYOUT_MAP[char])
            elif char in LAYOUT_MAP:
                fixed_text.append(LAYOUT_MAP[char])
            else:
                fixed_text.append(char)

        fixed_text = ''.join(fixed_text)

        # Вставляем исправленный текст
        pyperclip.copy(fixed_text)
        time.sleep(0.2)
        keyboard.press_and_release('delete')
        time.sleep(0.1)
        keyboard.press_and_release('ctrl+v')

    finally:
        time.sleep(0.3)
        pyperclip.copy(original_clipboard)


def main_loop():
    print("Программа запущена. Нажмите Ctrl+D для исправления раскладки выделенного текста.")
    print("Нажмите Esc для выхода.")

    # Регистрируем горячую клавишу
    keyboard.add_hotkey('caps lock', fix_selected_text)

    # Основной цикл программы
    try:
        while True:
            # Проверяем нажатие Esc каждые 0.1 секунды
            if keyboard.is_pressed('esc'):
                print("\nВыход из программы...")
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
    finally:
        # Удаляем все горячие клавиши перед выходом
        keyboard.unhook_all()


if __name__ == "__main__":
    main_loop()
