import kivy
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.widget import MDWidget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,Rectangle
import os
import datetime
#import sqlite3
from google import genai
from google.genai import types
from queue import Queue
import asyncio
import threading
kivy.require('1.0.1')
GEMINI_API_KEY = 'AIzaSyDjh8Xe7azuAhOWBWAoiJbbg8OqOncWvSQ '
def ai_chat(contents):
		try:
			client = genai.Client(api_key =GEMINI_API_KEY)
			response = client.models.generate_content(model="gemini-2.5-flash",contents=contents,config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0), ), )
			return response.text
		except Exception as e:
			error_msg=f"No internet connection \n please connect to the internet and try again \n {e} "
			return error_msg
"""def threader(content):
	resp = ai_chat(content)
	q.put(resp)
	q.join()"""
'''class AiChat(genai):
	def __init__(self,contents,**kwargs):
		super().__init__(**kwargs)
		self.cont = contents
		self.client = genai.Client(api_key=GEMINI_API_KEY)
		self.gen_resp()
	def update_content(self,contents):
		self.contents = contents
	def gen_resp(self):
		try:
			resp = self.client.models.generate_content(model="gemini-2.5-flash",contents=self.contents)
			self.response = resp.text
		except Exception as e:
			error_msg=f"No internet connection \n please connect to the internet and try again \n {e} "
			self.response = error_msg
		'''	
		
		
"""class ScrollableLabel(ScrollView):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.layout = GridLayout(cols=2,size_hint_y=None)
		self.chat_history = Label(halign='right',size_hint_y=None,markup=True)
		self.ai_chat_history = Label(halign='left',size_hint_y=None,markup=True)
		self.scroll_to_point = Label()
		self.scroll_to_point2 = Label()
		self.layout.add_widget(Label())
		self.layout.add_widget(self.chat_history)
		self.layout.add_widget(Label())
		self.layout.add_widget(self.scroll_to_point)
		self.layout.add_widget(self.ai_chat_history)
		self.layout.add_widget(Label())
		self.layout.add_widget(Label())
		self.layout.add_widget(self.scroll_to_point2)
		self.add_widget(self.layout)
	def update_chat_history(self,message):
		self.chat_history.text += '\n\n' + message + '\n\n'
		self.layout.height = self.chat_history.texture_size[1]  + 15
		self.chat_history.height = self.chat_history.texture_size[1]
		self.chat_history.text_size = (self.chat_history.width * 0.98, None)
		self.scroll_to(self.scroll_to_point)
	def update_ai_chat_history(self,message):
		self.ai_chat_history.text += '\n\n\n\n\n' + message + '\n\n\n'

		self.layout.height = self.ai_chat_history.texture_size[1]  + 15
		self.ai_chat_history.height = self.ai_chat_history.texture_size[1]
		self.ai_chat_history.text_size = (self.ai_chat_history.width * 0.98, None)
		self.scroll_to(self.scroll_to_point2)"""
		
	
		
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
        self.button = Button(text="Join")
        self.add_widget(Label( ))
        self.add_widget(Label(markup=True,text=f"[b]Login page[/b]",font_size=40))
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
        chat_app.screen_manager.current = 'home'
        
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
        self.message = Label(halign="center",valign="middle",font_size=45) 
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)    
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self,*_):
        self.message.text_update = (self.message.width *0.9,None)
class HomePage(GridLayout):
	def __init__(self,*args,**kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.intro = Label(height=dp(950))
		self.panel= BoxLayout(orientation="horizontal",size_hint_y=0.3,height=dp(10))
		self.btn = Button(text="Back")
		self.btn.bind(on_press=self.go_back)
		self.chat_btn = Button(text="Start Chat",height= dp(10),size_hint_y=Window.size[1]*0.000192)
		self.img_btn = Button(text="Generate Imange",height= dp(10) ,size_hint_y=Window.size[1]*0.000192)
		self.chat_btn.bind(on_press=self.goto_chatpage)
		self.heading = Label(text= "Homepage",width= Window.size[0]*0.058,size_hint_x=Window.size[0]*0.0048)
		self.panel.add_widget(self.btn)
		self.panel.add_widget(self.heading)
		self.add_widget(self.panel)
		self.add_widget(self.intro)
		self.add_widget(self.chat_btn)
		self.add_widget(Label(size_hint_y=Window.size[1]*0.00008))
		self.add_widget(self.img_btn)
		self.add_widget(Label(size_hint_y=Window.size[1]*0.00008))
		
	def go_back(self,instance):
		chat_app.screen_manager.transition.direction = 'right'
		previous_page = chat_app.screen_manager.previous()
		chat_app.screen_manager.current = previous_page
	def goto_chatpage(self,instance):
		chat_app.create_chat_page()
		chat_app.screen_manager.current = 'chat'
class LogoDisplay(FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		Window.clearcolor = (0.05,0.05,0.101)
		self.orientation = 'vertical'
		self.size_hint_y = None
		size_hint_x = None
		self.pos_hint_y = None
		self.logo = 'logos/logo1.png'
		self.display_image = Image(source=self.logo,
		pos_hint={'x':0.007,'y':6.95},size_hint_y=1.53)
		#self.display_image = MDIconButton(icon=self.logo,pos_hint={"center_x":0.5587,'y':6.95},size_hint_y=4.53)
		self.app_name = Label(text='[b]ChatAI[/b]',pos_hint={'center_x' : 0.485,'center_y':5.86},markup=True)
		self.add_widget(self.display_image)
		self.add_widget(self.app_name)
		Clock.schedule_once(self.goto_connectpage,19)
	def goto_connectpage(self,dt):
		chat_app.screen_manager.current = 'connect'
		pass
class ChatMessage(BoxLayout):
    def __init__(self, text,halign,is_user=True, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = dp(40) # Minimum height, will adjust based on content
        self.spacing = dp(5)

        # Create a label for the message
        message_label = Label(
            text=text,
            size_hint_y=None,
            padding=[dp(10), dp(5)],
            halign=halign,# Text alignment
            valign='top',
            markup=True,
            font_size='15sp'
        )
        message_label.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + dp(10)))
        # Adjust parent height based on label's height
        message_label.bind(height=lambda instance, value: setattr(self, 'height', value))
        """with message_label.canvas:
        	Color(0.4,0.08,0.6)
        	Rectangle(pos=(message_label.x,message_label.y - message_label.texture_size[1]),size=(message_label.size[0]+185,message_label.texture_size[1]+195))"""

        # Styling for chat bubbles
        if is_user:
            message_label.background_color = (0.2, 0.6, 1, 1) # Blue
            message_label.color = (1, 1, 1, 1) # White text
            message_label.text_size = (Window.width * 0.7 - dp(20), None) # Limit width for wrapping
            self.add_widget(BoxLayout(size_hint_x=0.3)) # Spacer on left
            self.add_widget(message_label)
        else:
            message_label.background_color = (0.9, 0.9, 0.9, 1) # Light gray
            message_label.color = (0, 0, 0, 1) # Black text
            message_label.text_size = (Window.width * 0.7 - dp(20), None) # Limit width for wrapping
            self.add_widget(BoxLayout(size_hint_x=0.3))
            self.add_widget(message_label) # Spacer on right
class AiChatMessage(BoxLayout):
    def __init__(self, text,halign,is_user=True, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = dp(40) # Minimum height, will adjust based on content
        self.spacing = dp(5)

        # Create a label for the message
        message_label = Label(
            text=text,
            size_hint_y=None,
            padding=[dp(10), dp(5)],
            halign=halign,# Text alignment
            valign='top',
            markup=True,
            font_size='15sp'
        )
        message_label.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1] + dp(10)))
        # Adjust parent height based on label's height
        message_label.bind(height=lambda instance, value: setattr(self, 'height', value))

        # Styling for chat bubbles
        if is_user:
            message_label.background_color = (0.2, 0.6, 1, 1) # Blue
            message_label.color = (1, 1, 1, 1) # White text
            message_label.text_size = (Window.width * 0.7 - dp(20), None)
              # Spacer on left
            self.add_widget(message_label)
            # Limit width for wrapping
            self.add_widget(BoxLayout(size_hint_x=0.3))
        else:
            message_label.background_color = (0.9, 0.9, 0.9, 1) # Light gray
            message_label.color = (0, 0, 0, 1) # Black text
            message_label.text_size = (Window.width * 0.7 - dp(20), None) # Limit width for wrapping
            self.add_widget(message_label) 
            self.add_widget(BoxLayout(size_hint_x=0.3))
            #Spacer on right
class ChatPage(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #Window.clearcolor = (0.91,0.898,0.890,1.1)
        Window.clearcolor = (0.04,0.04,0.09)
        self.history = BoxLayout(orientation='vertical',size_hint_y=None)
        self.chat_scroll_view = ScrollView(size_hint=(1,None),
        pos_hint={'x':0,'top':1},
        do_scroll_x=False)
        self.chat_scroll_view.add_widget(self.history)
        self.add_widget(self.chat_scroll_view)
        self.input_panel = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None), # Full width, fixed height
            height=dp(48),
            pos_hint={'x': 0, 'y': 0.44} # Initially at bottom
        )
        self.new_message = TextInput(width=Window.size[0]*0.8,size_hint_x=None,hint_text="Type your message here",font_size="16sp")
        self.message = ""
        self.button = Button(text="send",on_press=self.send_message)
        self.input_panel.add_widget(self.new_message)
        self.input_panel.add_widget(self.button)
        self.on_keyboard()
        Clock.schedule_once(self.update_layout, 0) # Call once after build     
        self.add_widget(self.input_panel)
        
        #self.ai_chat = AiChat("hello")
    def add_message(self,message):
     	msg= ChatMessage(text=message,halign='right',is_user=True)
     	self.history.add_widget(msg)
     	self.history.height = self.history.minimum_height
    def add_ai_message(self,message):
     	msg= AiChatMessage(text=message,halign='left',is_user=True)
     	msg.bind(height=lambda instance, value: setattr(self, 'height', value))
     	self.history.add_widget(msg)
     	self.history.height = self.history.minimum_height
     	
    def update_layout(self, dt):
        """
        Initializes or updates the layout positions and sizes.
        Called after build and on keyboard height changes.
        """
        # Ensure the chat history container's height is correctly calculated
        self.history.height = self.history.minimum_height

        # Calculate remaining height for the scroll view
        # Window.height - input_panel_height - keyboard_height
        remaining_height = Window.height - self.input_panel.height - self.input_panel.y

        # Set the height of the scroll view
        self.chat_scroll_view.height = remaining_height

        # Position the scroll view at the top (pos_hint={'top':1} handles y)
        self.history.pos_hint = {'x': 0, 'top': 1}

        # Scroll to bottom if new messages added or keyboard state changes
        self.scroll_to_bottom()
    def scroll_to_bottom(self, dt=None):
        """
        Scrolls the chat history to the bottom to show the latest message.
        """
        if self.chat_scroll_view.scroll_y == 0: # Already at bottom or empty
            return

        # Ensure layout is updated before scrolling, especially if new messages were added
        self.history.height = self.history.minimum_height
        # A small delay often helps Kivy's layout engine catch up
        Clock.schedule_once(lambda dt: setattr(self.chat_scroll_view, 'scroll_y', 0), 0.05)
    def send_message(self,instance):
        self.message = self.new_message.text
        self.new_message.text = " "
        if self.message:       	
        	self.add_message(f"[color=dd2020]{chat_app.login_page.username.text}[/color]>\n[color=e0e0e0]{self.message}[/color]  ")
        	#self.ai_chat.update_content(self.message)
        	#response.daemon = True
        	#response.start()
        	response = ai_chat(self.message)
        	self.add_ai_message(f"[color=10dd20]Scyta Ai[/color]>\n[color=e0e0e0]{response}[/color] ")
        	Clock.schedule_once(self.scroll_to_bottom, 0.1)
        	Clock.schedule_once(self.focus_text_input,0.1)
    def focus_text_input(self,_):
    	self.new_message.focus = True
    def on_keyboard(self):
    	if self.new_message.focus:
    		print(self.new_message.focus)
    		self.input_panel.pos_hint_y = 0.44
class ChatApp(App):
    def build(self):
        self.title = "ChatApp"
        Window.clearcolor = (0.8798,0.78,0.55,0.8)
        
        self.screen_manager = ScreenManager()
        screen = Screen(name="logo")
        self.logo_page = LogoDisplay()
        screen.add_widget(self.logo_page)
        self.screen_manager.add_widget(screen)
        screen = Screen(name="connect")
        self.login_page = Login()
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)
        screen = Screen(name="Info")
        self.info_page = Info()
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        screen = Screen(name="home")
        self.home_page = HomePage()
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)
        self.screen_manager.current = 'logo'
        return  self.screen_manager
    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name="chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)
        
if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    chat_app=ChatApp()
    chat_app.run()
    #loop.close()