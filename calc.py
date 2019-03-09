from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text = "Button", font_size = 20, on_press = self.btn_press)
    def btn_press(self, instance):
        print("Button is pressed")
        if instance.text == "iamPressed":
            instance.text = "Pressed_test"
        else:
            instance.text = "iamPressed"

if __name__ == "__main__":
    MyApp().run()