from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionGroup, ActionPrevious, ActionOverflow, ActionButton
from kivy.base import runTouchApp


class WhatsMarketing(GridLayout):
    pass


class WhatsMarketingApp(App):
    def build(self):
        actionbar = ActionBar(pos_hint={'top': 1})

        av = ActionView()
        av.add_widget(ActionPrevious(title='Action Bar', with_previous=False))
        av.add_widget(ActionOverflow())
        av.add_widget(ActionButton(text='Btn0'))

        for i in range(1, 3):
            av.add_widget(ActionButton(text='Btn{}'.format(i)))

        ag = ActionGroup(text='Group1')
        for i in range(5, 8):
            ag.add_widget(ActionButton(text='Btn{}'.format(i)))

        av.add_widget(ag)

        actionbar.add_widget(av)

        av.use_separator = True

        runTouchApp(actionbar)

        return WhatsMarketing()


if __name__ == '__main__':
    WhatsMarketingApp().run()
