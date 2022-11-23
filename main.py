from string import ascii_letters, digits
from random import choices
from typing import Optional
from tkinter import Button, Frame, Entry, LabelFrame, Tk, END


def generate_password(pass_len: int) -> Optional[str]:
    """Основная функция генерации пароля."""
    if not isinstance(pass_len, int): 
        print(f'Введите число. Вы ввели {pass_len}')
        return
    possible_elements = ascii_letters + digits + '*-+/><.,'
    password = choices(possible_elements, k=pass_len)
    return ''.join(password)


def prepair_password():
    password_entry.delete(0, END)  # очистить предыдущий пароль
    pw_len = int(entry_box.get())  # получить ввод пользователя
    password = str(generate_password(pw_len))
    password_entry.insert(0, password)  # вывести новый пароль


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    password = root.clipboard_get()
    return password


root = Tk()
root.title('Генератор паролей')
root.geometry('500x300')

# Label Frame
label_frame = LabelFrame(root, text='Введите количество символов пароля')
label_frame.pack(pady=25)

# Entry Box
entry_box = Entry(label_frame, font=('Arial', 20))
entry_box.pack(pady=25, padx=25)

# Generated Password
password_entry = Entry(root, font=('Times New Roman', 25), bd=0)
password_entry.pack(pady=20)

# Frame for Button
button_frame = Frame(root)
button_frame.pack(pady=20)

# Button
button = Button(button_frame, text='Генерировать', command=prepair_password)
button.grid(row=0, column=0, padx=10)

# Copy to clipboard button
clipboard_button = Button(button_frame, text='Копировать', command=copy_to_clipboard)
clipboard_button.grid(row=0, column=1, padx=10)

root.mainloop()
