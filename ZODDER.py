# ZODDER.py
# created by ZAYD <3
# linktr.ee/cantstopdivided

import webbrowser
try:
  import tkinter as tk
  import pyperclip
except ImportError:
  os.system("pip install -r requirements.txt")
  os.system("pip3 install -r requirements.txt")

zod_letters = {
    'J': 'A',
    'B': 'B',
    'Z': 'C',
    'F': 'D',
    'U': 'E',
    'Y': 'F',
    'T': 'G',
    'W': 'H',
    'K': 'I',
    'O': 'J',
    'E': 'K',
    'P': 'L',
    'A': 'M',
    'Q': 'N',
    'N': 'O',
    'D': 'P',
    'G': 'Q',
    'V': 'R',
    'H': 'S',
    'I': 'T',
    'C': 'U',
    'X': 'V',
    'M': 'W',
    'S': 'X',
    'R': 'Y',
    'L': 'Z'
}

english_letters = {v: k for k, v in zod_letters.items()}

def convert_to_zod(word):
    converted_word = ''
    for letter in word:
        if letter.upper() in english_letters:
            converted_word += english_letters[letter.upper()]
        else:
            converted_word += letter
    return converted_word

def convert_to_english(word):
    converted_word = ''
    for letter in word:
        if letter.upper() in zod_letters:
            converted_word += zod_letters[letter.upper()]
        else:
            converted_word += letter
    return converted_word

def copy_to_clipboard():
    converted_text = output_label.cget("text")
    pyperclip.copy(converted_text)

def convert_button_click():
    input_word = entry.get()
    if conversion_mode.get() == 1:
        output_word = convert_to_english(input_word)
    else:
        output_word = convert_to_zod(input_word)
    output_label.config(text=output_word)

def open_translate_website():
    webbrowser.open_new_tab('https://translate.google.com/')

window = tk.Tk()
window.title('Zod Language Converter')
entry = tk.Entry(window, width=30)
entry.pack(padx=10, pady=10)
conversion_mode = tk.IntVar(value=0)
to_zod_radio = tk.Radiobutton(window, text='Convert to Zod', variable=conversion_mode, value=0)
to_zod_radio.pack(padx=10, pady=2)
to_english_radio = tk.Radiobutton(window, text='Convert to English', variable=conversion_mode, value=1)
to_english_radio.pack(padx=10, pady=2)
convert_button = tk.Button(window, text='Convert', command=convert_button_click)
convert_button.pack(padx=10, pady=10)
translate_button = tk.Button(window, text='Open Google Translate', command=open_translate_website)
translate_button.pack(padx=10, pady=10)
output_label = tk.Label(window, text='', font=('Arial', 16))
output_label.pack(padx=10, pady=10)

copy_button = tk.Button(window, text='Copy to Clipboard', command=copy_to_clipboard)
copy_button.pack(padx=10, pady=10)
window.mainloop()
