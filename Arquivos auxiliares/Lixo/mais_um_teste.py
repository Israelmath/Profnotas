from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button

class TestBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        grid = GridLayout(cols = 2, padding = 10, spacing = 10)
        
        grid.add_widget(BotaoDrop())

        self.add_widget(grid)

class BotaoDrop(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return TestBox()

MyApp().run()