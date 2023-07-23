import json
import os

class Note:
    def __init__(self, note_id, title, body, created_time, last_modified_time):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_time = created_time
        self.last_modified_time = last_modified_time

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        created_time = self.get_current_time()
        last_modified_time = created_time
        note = Note(note_id, title, body, created_time, last_modified_time)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.last_modified_time = self.get_current_time()
            self.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Заметка с таким ID не найдена.")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Заметка с таким ID не найдена.")

    def read_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.show_note(note)
        else:
            print("Заметка с таким ID не найдена.")

    def get_notes_list(self):
        for note in self.notes:
            print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_time}")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def get_current_time(self):
        # Здесь можно использовать любую библиотеку для работы с датой/временем
        import datetime
        return str(datetime.datetime.now())

    def save_notes(self):
        with open("notes.json", "w") as file:
            data = json.dumps([note.__dict__ for note in self.notes])
            file.write(data)

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                data = json.load(file)
                self.notes = [Note(**note_data) for note_data in data]

    def show_note(self, note):
        print(f"\nID: {note.note_id}")
        print(f"Заголовок: {note.title}")
        print(f"Дата создания: {note.created_time}")
        print(f"Дата последнего изменения: {note.last_modified_time}")
        print("Текст заметки:")
        print(note.body)


if __name__ == "__main__":
    note_manager = NoteManager()
    note_manager.load_notes()

    while True:
        print("\n1. Показать список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Прочитать заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            note_manager.get_notes_list()

        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)

        elif choice == "3":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note_manager.edit_note(note_id, title, body)

        elif choice == "4":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            note_manager.delete_note(note_id)

        elif choice == "5":
            note_id = int(input("Введите ID заметки, которую хотите прочитать: "))
            note_manager.read_note(note_id)

        elif choice == "6":
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")
