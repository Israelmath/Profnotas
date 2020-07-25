from kivy.uix.textinput import TextInput

class RedacoesInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() or substring == '.' or substring == ',':
            if substring == ',' or substring == '.':
                return super().insert_text('.', from_undo=from_undo)
            else:
                if (float(substring) >= 0 and float(substring) <= 8) or substring == '.':
                    return super().insert_text(substring, from_undo=from_undo)
                else:
                    return super().insert_text('', from_undo=from_undo)