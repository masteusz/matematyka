from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class EquationView(GridLayout):
    def __init__(self, **kwargs):
        super(EquationView, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text=""))
        self.first_tens = TextInput(multiline=False)
        self.first_singles = TextInput(multiline=False)
        self.add_widget(self.first_tens)
        self.add_widget(self.first_singles)
        self.add_widget(Label(text='+'))
        self.second_tens = TextInput(multiline=False)
        self.second_singles = TextInput(multiline=False)
        self.add_widget(self.second_tens)
        self.add_widget(self.second_singles)
        self.res_hundreds = TextInput(multiline=False)
        self.res_tens = TextInput(multiline=False)
        self.res_singles = TextInput(multiline=False)
        self.add_widget(self.res_hundreds)
        self.add_widget(self.res_tens)
        self.add_widget(self.res_singles)


class MyApp(App):

    def build(self):
        return EquationView()


if __name__ == '__main__':
    MyApp().run()
