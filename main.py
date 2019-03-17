import kivy
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MainScreen(BoxLayout):
	
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		

				
		
class Main(App):
 	
 	def build(self):
 		return MainScreen()



if __name__ == '__main__':
	Main().run()