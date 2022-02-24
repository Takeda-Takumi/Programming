from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# フォント設定
resource_add_path("C:\Windows\Fonts")
LabelBase.register(DEFAULT_FONT, 'HGRGM.TTC')

class ImageWidget(Widget):
    source = StringProperty('./image/sample.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
    
    def buttonClicked(self):
        self.source = './image/sample.jpg'

    def buttonClicked2(self):
        self.source = './image/sample2.jpg'
    
    def buttonClicked3(self):
        self.source = './image/sample3.jpg'

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '画像表示'

if __name__  == '__main__':
    TestApp().run()



