class CommandView(object):

    @staticmethod
    def show_notes_list(notes):
        for note in notes:
            print(note)
            print("--------------------------------------------------------------")

    @staticmethod
    def show_note(note):
        print("--------------------------------------------------------------")
        print(note)
        print("--------------------------------------------------------------")

    @staticmethod
    def show_note_add():
        print("--------------------------------------------------------------")
        print("Заметка успешно добавлена!")
        print("--------------------------------------------------------------")

    @staticmethod
    def show_note_update(note_id):
        print("--------------------------------------------------------------")
        print("Заметка с ID№: {} обновлена !".format(note_id))
        print("--------------------------------------------------------------")

    @staticmethod
    def show_note_delete(note_id):
        print("--------------------------------------------------------------")
        print("Заметка с ID№: {} удалена !".format(note_id))
        print("--------------------------------------------------------------")

    @staticmethod
    def show_all_note_delete():
        print("--------------------------------------------------------------")
        print("Все заметки удалены!")
        print("--------------------------------------------------------------")

    @staticmethod
    def show_notes_null():
        print("--------------------------------------------------------------")
        print("Заметки отсутствуют !")
        print("--------------------------------------------------------------")

    @staticmethod
    def show_note_null(note_id):
        print("--------------------------------------------------------------")
        print("Заметка с ID№: {} отсутствует !".format(note_id))
        print("--------------------------------------------------------------")