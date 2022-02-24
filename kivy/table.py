from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from kivy.uix.widget import Widget

from kivy.properties import StringProperty


resource_add_path("c:\Windows\Fonts")
LabelBase.register(DEFAULT_FONT, "HGRGM.TTC")

class TextWidget(Widget):
    pass

class TextsWidget(Widget):
    pass

class TableApp(App):
    def __init__(self, **kwargs):
        super(TableApp, self).__init__(**kwargs)
        self.title = "時間割管理"

    def build(self):
        return TextWidget()

if __name__ == "__main__":
    TableApp().run()
