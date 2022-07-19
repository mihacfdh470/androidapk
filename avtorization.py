from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


#region АВТОРИЗАЦИЯ
shirina, dlina=200, 50
startx, starty=50, 400
UserInfo = [None, None, None]
Avtoriz = []
class acc():
    InAccount = False
class avtorisationApp(App):
    def build(self):
        if acc.InAccount == True:
            exit()
        global Avtoriz
        with open('userInfo.txt', 'r') as file:
            for line in file:
                Avtoriz.append(line)

        global shirina, dlina
        global startx, starty
        global UserInfo
        fll = FloatLayout()
        self.ti = TextInput(text="имя", size_hint_x=None, width=shirina, size_hint_y=None, 
            height=dlina, pos=(startx, starty))
        self.ti2 = TextInput(text="Фамилия", size_hint_x=None, width=shirina, size_hint_y=None, 
            height=dlina, pos=(startx+shirina, starty))
        self.password = TextInput(text="пароль", size_hint_x=None, width=shirina, size_hint_y=None, 
            height=dlina, pos=(startx, starty-dlina))
        self.btn = Button(text="""зарегистрироваться/
войти в аккаунт""", 
            color="red",font_size="20", size_hint_x=None, size_hint_y=None, 
            width=shirina, height=dlina, pos=(startx+shirina, starty-dlina))
        self.btn.bind(on_press=self.saveuserinfo)
        fll.add_widget(self.btn)
        fll.add_widget(self.ti)
        fll.add_widget(self.ti2)
        fll.add_widget(self.password)
        return fll
    def saveuserinfo(self, instance):
        global Avtoriz, InAccount
        UserInfo[0] = self.ti.text
        UserInfo[1] = self.ti2.text
        UserInfo[2] = self.password.text
        if UserInfo == Avtoriz or len(Avtoriz) == 0:
            print("UserInfo: " + str(list(UserInfo)))
            InAccount = True
            with open('userInfo.txt', 'w') as file:
                for nnnn in range(0, len(UserInfo)):
                    file.writelines(str(UserInfo[nnnn]))
                    file.write("""
""")
#enrigion
