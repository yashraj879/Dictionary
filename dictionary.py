import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from PyDictionary import PyDictionary
from googletrans import Translator

root = tk.Tk()
root.title('Dictionary')
root.geometry('600x300')
root['bg'] = 'white'

frame = tk.Frame(root, width=200, height=300, borderwidth=1, relief=tk.RIDGE)
frame.grid(sticky="W")

def get_meaning():
    dictionary = PyDictionary()
    get_word = entry.get()
    languages = language_combobox.get()

    if get_word == "":
        messagebox.showerror('Dictionary', 'Please write the word')
    else:
        output.delete(1.0, tk.END)  # Clear previous output

        if languages == 'English-to-English':
            try:
                d = dictionary.meaning(get_word)
                if 'Noun' in d:
                    output.insert('end', '\n'.join(d['Noun']))
                else:
                    output.insert('end', 'No Noun meaning available.')
            except:
                output.insert('end', 'Error fetching meaning.')
        elif languages == 'English-to-Hindi':
            try:
                translator = Translator()
                t = translator.translate(get_word, dest='hi')
                output.insert('end', t.text)
            except:
                output.insert('end', 'Error translating word.')

def exit_program():
    root.destroy()

img = ImageTk.PhotoImage(Image.open('dict.png'))
pic = tk.Label(root, image=img)
pic.place(x=40, y=70)

word_label = tk.Label(root, text="Enter Word", bg="white", font=('verdana', 10, 'bold'))
word_label.place(x=250, y=23)

a = tk.StringVar()
language_combobox = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'))
language_combobox['values'] = ('English-to-English', 'English-to-Hindi')
language_combobox.place(x=380, y=10)
language_combobox.current(0)

entry = tk.Entry(root, width=50, borderwidth=2, relief=tk.RIDGE)
entry.place(x=250, y=50)

search_button = tk.Button(root, text="Search", font=('verdana', 10, 'bold'), cursor="hand2", relief=tk.RIDGE, command=get_meaning)
search_button.place(x=430, y=80)

quit_button = tk.Button(root, text="Quit", font=('verdana', 10, 'bold'), cursor="hand2", relief=tk.RIDGE, command=exit_program)
quit_button.place(x=510, y=80)

meaning_label = tk.Label(root, text="Meaning", bg="white", font=('verdana', 15, 'bold'))
meaning_label.place(x=230, y=120)

output = tk.Text(root, height=8, width=40, borderwidth=2, relief=tk.RIDGE)
output.place(x=230, y=160)

root.mainloop()
