from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window
from functools import partial
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty, NumericProperty
import sqlite3 as lite
#con = lite.connect('test.db')

#con.text_factory = str
#cur = con.cursor()
Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (600, 600)

class MyLabel(Label):
    pass

class EditPopup(Popup):
    mode = StringProperty("")
    label_rec_id = StringProperty("Id")
    col_data = ListProperty(["?", "?", "?"])
    index = NumericProperty(0)

    def __init__(self, obj, **kwargs):
        super(EditPopup, self).__init__(**kwargs)

        if obj.mode == "Update":
            #cur.execute("SELECT * FROM `item` WHERE itemId=?", (edit_id,))
            #row = cur.fetchone()
            row = (11, 'Item1', '1001')
            print(row[0])
            self.col_data[0] = str(row[0])
            self.col_data[1] = row[1]
            self.col_data[2] = row[2]

    def update(self,obj):
        #cur.execute("UPDATE `item` SET itemName=?, itemCode=? WHERE itemId=?",
                #('Item1', 9999, 11))
        #con.commit()
        Invoice().abc()

class Invoice(Screen):
    def __init__(self, **kwargs):
        super(Invoice, self).__init__(**kwargs)

    def abc(self):
        #fetching from database
        #cur.execute("SELECT * FROM `item` order by itemId asc")
        #rows = cur.fetchall()
        rows = [(11, 'Item1', '1001'), (12, 'Item2', '2001'), (13, 'Item3', '102')]
        print(rows)
        layout = self.ids['invoices']
        for row in rows:
            layout.add_widget(MyLabel(text=str('[ref=world]' + row[1]) + '[/ref]',
                                      size_hint_x=.35,
                                      halign='left',
                                      markup=True,
                                      on_ref_press=partial(self.open_form, row[0])))

    def open_form(self, id, *args):
        global edit_id
        edit_id = id
        self.mode = "Update"
        popup = EditPopup(self)
        popup.open()

class Test(App):

    def build(self):
        return Invoice()

if __name__ == '__main__':
    Test().run()
