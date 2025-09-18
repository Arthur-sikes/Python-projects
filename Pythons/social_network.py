import kivy
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import os
import datetime
import sqlite3
kivy.require('1.0.1')
#This class is an improved version of label
time_now = datetime.datetime.now()
class ScrollableLabel(ScrollView):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.layout = GridLayout(rows=2,cols=2,size_hint_y=None)
		time = str(time_now)
		self.chat_history = Label(halign='right',size_hint_y=None,markup=True)
		self.scroll_to_point = Label()
		self.layout.add_widget(Label())
		self.layout.add_widget(self.chat_history)
		self.layout.add_widget(Label(text=str(time_now)[:-7]))
		self.layout.add_widget(self.scroll_to_point)		
		self.add_widget(self.layout)
	def update_chat_history(self,message):
		self.chat_history.text += '\n\n' + message + '\n\n'
		self.layout.height = self.chat_history.texture_size[1]  + 15
		self.chat_history.height = self.chat_history.texture_size[1]
		self.chat_history.text_size = (self.chat_history.width * 0.98, None)
		self.scroll_to(self.scroll_to_point)
		
	
		
class Login(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        input_width = 2.99
        input_height = 0.01
        if os.path.exists("prev_details.txt"):
             with open("prev_details.txt",'r') as f:
                 d = f.read().split(",")
                 prev_ip = d[0]
                 prev_port = d[1]
                 prev_username = d[2]
                 prev_password = d[3]
        else:
            prev_ip = ""
            prev_port = ""
            prev_username = ""
            prev_password = "" 
         
        self.ip_txt = Label(text="IP:")
        self.ip = TextInput(text=prev_ip,multiline=False,size_hint_y=input_height,size_hint_x=Window.size[0]*0.0098)
        self.password = TextInput(text=prev_password,multiline=False,password=True)
        self.port = TextInput(text=prev_port,multiline=False,size_hint_y=input_height,size_hint_x=Window.size[0]*0.0098)
        self.username = TextInput(text=prev_username,multiline=False,size_hint_y=input_height,size_hint_x=Window.size[0]*0.0098)
        self.button = Button(text="Login")
        self.add_widget(Label( ))
        self.add_widget(Label(text="Login page"))
        self.add_widget(Label())
        self.add_widget(self.ip_txt)
        self.add_widget(self.ip)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text="Port:"))
        self.add_widget(self.port)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text="Username:"))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.username)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text="Password:"))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.password)
        self.add_widget(Label())
        self.add_widget(Label(height=Window.size[1]*0.001))
        self.add_widget(Label(height=Window.size[1]*0.001))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.button)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        
        self.button.bind(on_press=self.join_button)
    def connect(self,_):
        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'chat'
        
    def join_button(self,instance):
        username = self.username.text 
        password = self.password.text
        ip = self.ip.text
        port = self.port.text
        with open("prev_details.txt",'w') as f:
            f.write(f"{ip},{port},{username},{password}")
            info = f"connecting {ip}:{port} as {username} to server"
        if username and password and ip and port !="":
            chat_app.info_page.update_info(" Welcome to the Social Network ")
            chat_app.screen_manager.current = "Info"
            Clock.schedule_once(self.connect,3)
        
class Info(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center",valign="middle",font_size=30) 
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)    
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self,*_):
        self.message.text_update = (self.message.width *0.9,None)
class ChatPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        Window.clearcolor = (0.91,0.898,0.890,1.1)
        adjustable_height = Window.size[1]*0.86
        self.history = ScrollableLabel(height=adjustable_height,size_hint_y=None,)
        self.add_widget(self.history)
        self.new_message = TextInput(width=Window.size[0]*0.8,size_hint_x=None)
        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)
        Clock.schedule_once(self.focus_text_input)
    def send_message(self,instance):
        message = self.new_message.text
        self.new_message.text = " "
        if message:       	
        	self.history.update_chat_history(f"[color=dd2020]{chat_app.login_page.username.text}[/color]>\n[color=202020]{message}[/color]  ")
        Clock.schedule_once(self.focus_text_input,0.1)
        pass
    def focus_text_input(self,_):
    	self.new_message.focus = True
class ChatApp(App):
    def build(self):
        self.title = "ChatApp"
        Window.clearcolor = (0.8798,0.78,0.55,0)
        self.screen_manager = ScreenManager()
        self.login_page = Login()
        screen = Screen(name="connect")
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)
        screen = Screen(name="Info")
        self.info_page = Info()
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return  self.screen_manager
    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name="chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)
        
if __name__ == '__main__':     
    chat_app=ChatApp()
    chat_app.run()