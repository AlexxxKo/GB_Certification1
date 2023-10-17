from datetime import datetime
import json

id = 0
def main():
    while True:
        print("\n1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Фильтровать заметки по дате")
        print("5. Вывести список заметок")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            filter_notes_by_date()
        elif choice == "5":
            print_notes()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор.")

def add_note():
    notes = load_notes()
    global id
    id = id + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        new_title = input("Введите новый заголовок заметки: ")
        new_body = input("Введите новый текст заметки: ")
        note["title"] = new_title
        note["body"] = new_body
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка отредактирована.")
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка удалена.")
    else:
        print("Заметка с таким ID не найдена.")

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    global id
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            id = notes[-1]['id']
    except FileNotFoundError:
        notes = []
    return notes

def filter_notes_by_date():
    notes = load_notes()
    date_str = input("Введите дату для фильтрации (гггг-мм-дд): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date() == date.date()]
        if filtered_notes:
            print("Заметки за выбранную дату:")
            for note in filtered_notes:
                print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}")
        else:
            print("Заметки за выбранную дату не найдены.")
    except ValueError:
        print("Некорректный формат даты.")

def print_notes():
    notes = load_notes()
    print()
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Дата/время: {note['timestamp']}")
    else:
        print("Список заметок пуст.")

if __name__ == "__main__":
    main()