from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Rectangle


import requests

Window.size = (500, 500)

bg_color = (0.1, 0.1, 1.1, 1)
Window.clearcolor = bg_color

token_weather = '6e8d79779a0c362f14c60a1c7f363e29'

#global
city_name = ""

# class ScrButton(Button):
#   def __init__(self, screen, direction='right', goal='main', **kw):
#     super().__init__(**kw)
#     self.screen = screen
#     self.direction = direction
#     self.goal = goal
    

  # def on_press(self):
  #   self.screen.manager.transition.direction = self.direction
  #   self.screen.manager.current = self.goal

class MainScr(Screen):
  def __init__(self, **kw):
    super().__init__(**kw)
    v_line = BoxLayout(orientation='vertical', padding=100, spacing=100)
    with self.canvas:
      self.rect = Rectangle(source='weather2.jpg', size=[500, 500])
    txt = Label(text = '[size=30][b][color=#000000]' + 'Введіть місто' + '[/color][/b][/size]' , size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5}, markup=True)
    self.input_city = TextInput(multiline=False, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
    btn = Button(text="Далі", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
    btn.on_press = self.next
    v_line.add_widget(txt)
    v_line.add_widget(self.input_city)
    v_line.add_widget(btn)
    self.add_widget(v_line)

  def next(self):
    global city_name
    city_name = self.input_city.text
    self.manager.current = 'second'

class SecondScr(Screen):
  def __init__(self, **kw):
    super().__init__(**kw)
    h_line = BoxLayout(orientation='vertical', padding=150, spacing=100)
    with self.canvas:
      self.rect = Rectangle(source='weather2.jpg', size=[500, 500])
    self.txt = Label(text = city_name, markup = True)
    btn = Button(text = "Назад",size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
    btn.on_press = self.next
    h_line.add_widget(self.txt)
    h_line.add_widget(btn)
    self.add_widget(h_line)
    self.on_enter = self.set_var

  def next(self):
    self.manager.current = 'main'

  def set_var(self):
    try:
      url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={token_weather}&units=metric'
      data = requests.get(url).json()
      temp = data['main']['temp']
      pressure = data['main']['pressure']
      humidity = data['main']['humidity']
      wind = data['wind']['speed']
      answer = f"[size=20][b][color=#000000] Погода в місті: {city_name}\nТемпература: {temp}°C\nТиск: {pressure} Па\nВологість: {humidity} кг/м3\nШвидкість вітру: {wind} м\с [/color][/b][/size]"
      
      self.txt.text = answer
    except:
      self.txt.text = "Введеного міста не знайдено."



class MyApp(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScr(name='main'))
    sm.add_widget(SecondScr(name='second'))
    return sm



# class MyApp(App):
#     def build(self):
#         self.title = "Lol"
#         txt = Label(text = 'Hello!')
#         button = Button(text = 'Lol!')
#         h_line = BoxLayout()
#         h_line.add_widget(button)
#         h_line.add_widget(txt)
    
      
#         btn1 = Button(text = "1")
#         btn2 = Button(text = "2")
#         btn3 = Button(text = "3")
#         btn4 = Button(text = "4")

#         v_line = BoxLayout(orientation = 'vertical')
#         h_line.add_widget(v_line)
#         v_line.add_widget(btn1)
#         v_line.add_widget(btn2)
#         v_line.add_widget(btn3)
#         v_line.add_widget(btn4)

#         return h_line


app = MyApp()
app.title = "Weather"
app.run()