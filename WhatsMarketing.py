from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class WhatsMarketing(BoxLayout):
    pass


class WhatsMarketingApp(App):
    def build(self):
        return WhatsMarketing()


if __name__ == '__main__':
    WhatsMarketingApp().run()
