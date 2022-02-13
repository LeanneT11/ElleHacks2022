from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from googlesearch import search
import requests
from bs4 import BeautifulSoup

Window.clearcolor = (0.24, 0.71, 0.54, 1)

Builder.load_file("ElleHacks.kv")

class WelcomeScreen(Screen):
    def photo(self):
        self.ids.logo.source = 'RE-FARBIC.png'

class HomeScreen(Screen):
    pass

class DonationScreen(Screen):

    def search_address(self):
        search_result = self.ids.address.text
        query = search_result + ' clothing donation centre'
        locations = {}

        for item in search(query, tld='co.in', num=5, stop=5, pause=2):
            reqs = requests.get(item)
            web_name = BeautifulSoup(reqs.text, 'html.parser')

            for title in web_name.find_all('title'):
                web_str = title.get_text().strip()
                locations[web_str] = item

        i = 1
        text1 = ''
        for name in locations:
            text1 += str(i) + '. ' + name + '\n'
            text1 += locations[name] + '\n\n'
            i += 1

        my_results = self.manager.get_screen('display').ids.results
        my_results.text = text1


class PictureScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class DisplayScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(PictureScreen(name="picture"))
        sm.add_widget(DonationScreen(name='directory'))
        sm.add_widget(DisplayScreen(name='display'))

        return RootWidget()
        return PictureScreen()




if __name__ == '__main__':
    TestApp().run()


