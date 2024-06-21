from tkinter import Tk, Label, Entry, Button, Variable, Listbox

# Импортируем класс Library из файла Library_exzam
from Library_exzam import Library

# Функция для добавления Книги
def add_library():
    title = entry_title.get()
    author = entry_author.get()
    year_of_publication = entry_year_of_publication.get()
    library = Library(title, author, year_of_publication)
    list_flat.append(library)
    list_flat_var.set(list_flat)

# Функция для удаления Книги из списка
def delete():
    index = library_listbox.curselection()
    list_flat.remove(list_flat[index[0]])
    list_flat_var.set(list_flat)

# Функция для выдачи книги на руки
def give_out():
    index = library_listbox.curselection()
    list_flat[index[0]].give_book()
    list_flat_var.set(list_flat)

# Функция для приемки книги в библиотеку
def accept():
    index = library_listbox.curselection()
    list_flat[index[0]].accept_book()
    list_flat_var.set(list_flat)

if __name__ == '__main__':
    root = Tk()  # создаем корневой объект
    root.title('Библиотека')  # устанавливаем заголовок окна
    root.geometry("600x500")  # устанавливаем размеры окна

    # Поле ввода для названия книги
    label_title = Label(text="Введите название")
    label_title.pack()
    entry_title = Entry(width=50)
    entry_title.pack()

    # Поле ввода для автора
    label_author = Label(text="Автор")
    label_author.pack()
    entry_author = Entry(width=50)
    entry_author.pack()

    # Поле ввода для года издания
    label_year_of_publication = Label(text="Год издания")
    label_year_of_publication.pack()
    entry_year_of_publication = Entry(width=50)
    entry_year_of_publication.pack()

    # Поле отображения статуса придобавлении в бибилиотеку
    label_status = Label(text="Статус")
    label_status.pack()
    label_status = Label(text="Свободна")
    label_status.pack()

    # Кнопка для добавления книги в библиотеку
    btn_add_library = Button(root, text="Добавить книгу", command=add_library)
    btn_add_library.pack()

    # Список для хранения книг
    list_flat = []
    # Сохраненный список в переменной типа Variable
    list_flat_var = Variable(value=list_flat)
    # ListBox для отображения списка книг
    library_listbox = Listbox(width=50, listvariable=list_flat_var)
    library_listbox.pack()

    #  Кнопка для удаления книги из списка
    btn_add_library = Button(text="Удалить", command=delete)
    btn_add_library.pack()
    # Кнопка для выдачи книги на руки
    btn_add_library = Button(text="Выдать", command=give_out)
    btn_add_library.pack()
    # Кнопка для приемки книги от пользователя
    btn_add_library = Button(text="Принять", command=accept)
    btn_add_library.pack()

    root.mainloop()