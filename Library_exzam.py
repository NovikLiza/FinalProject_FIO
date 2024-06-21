class Library:
    # Конструктор
    def __init__(self, title, author, year_of_publication):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.status = "Свободна"

    def give_book(self):
        self.status = "На руках"

    def accept_book(self):
        self.status = "Свободна"

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year_of_publication}, Статус: {self.status}"

