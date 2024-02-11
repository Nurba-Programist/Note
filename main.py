import os
import json
import datetime

# Получаем текущую дату и время
now = datetime.datetime.now()

def create_note():
    note_title = input("\nВведите заголовок заметки: ")
    note_content = input("Введите содержимое заметки: ")
    
    note = {
        "title": note_title,
        "content": note_content
    }
    
    return note

def save_note(note):
    with open("notes.json", "a+") as file:
        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")
        json.dump(note, file)
        print("\nЗаметка добавлена")
        print("________________________")

def read_notes():
    if not os.path.isfile("notes.json"):
        print("Нет созданных заметок")
    else:
        with open("notes.json", "r") as file:
            notes = file.readlines()
            print("\nСписок заметок: ")
            for note in notes:
                note_data = json.loads(note)
                print("Заголовок:", note_data["title"])
                print("Содержимое:", note_data["content"] + now.strftime('\n%d.%m.%Y %H:%M'))
                print("---------------------------------")

def edit_note():
    note_index = int(input("Введите индекс заметки, которую вы хотите отредактировать: "))
    with open("notes.json", "r") as file:
        notes = file.readlines()
    
    if note_index >= len(notes) or note_index < 0:
        print("Недопустимый индекс заметки")
        return
    
    edited_note = create_note()
    notes[note_index] = json.dumps(edited_note)
    
    with open("notes.json", "w") as file:
        file.writelines(notes)
    
    print("Заметка успешно отредактирована")

def delete_note():
    note_number = int(input("Введите номер заметки, которую хотите удалить: "))
    with open("notes.json", "r") as file:
        notes = file.readlines()
    if note_number <= len(notes):
        del notes[note_number-1]
        with open("notes.json", "w") as file:
            file.writelines(notes)
        print("Заметка успешно удалена.")
    else:
        print("Заметка с таким номером не существует.")

def main():
    while True:
        print("\n Меню: ")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        
        choice = input("\nВведите номер операции: ")
        
        if choice == "1":
            note = create_note()
            save_note(note)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Вы вышли из программы")
            break
        else:
            print("Недопустимый номер операции")


if __name__ == "__main__":
    main()