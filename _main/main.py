from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Teste(App):
    def build(self):
        box = BoxLayout()
        button = Button(text = 'Olá mundo')
        label = Label(text = 'Oie')
        box.add_widget(label)
        box.add_widget(button)

        box1 = BoxLayout(orientation='vertical')
        button1 = Button(text='Olá mundo')
        label1 = Label(text='Oie')
        box1.add_widget(label1)
        box1.add_widget(button1)
        box.add_widget(box1)
        return box
App.run(Teste())
