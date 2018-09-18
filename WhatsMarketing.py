from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class WhatsMarketing(GridLayout):
    pass


class WhatsMarketingApp(App):
    def build(self):
        return WhatsMarketing()


if __name__ == '__main__':
    WhatsMarketingApp().run()
