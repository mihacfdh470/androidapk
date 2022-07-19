from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
import time
from paho.mqtt import client as mqtt_client
from avtorization import *





base_data = []


p = 500
i = 1
info = []
myname = ''
v = 0
inf = 1
broker = None
port = None
topic = None
client_id = None
global myMode
myMode = 1
def connect_mqtt():   # ФУНКЦИЯ ДЛЯ КОННЕКТА К MQTT
    global client_id
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            pass
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):                 #
    def on_message(client, userdata, msg):          #
        global base_data
        print(f"{msg.payload.decode()} ")#
        #print(str(list(base_data)))
                                                    #
    client.subscribe(topic)                         #
    client.on_message = on_message                  #
                                                    #   ЭТО ВСЁ ДЛЯ ПОЛУЧЕНИЯ
                                                    #
def running():                                      #
    client = connect_mqtt()                         #
    subscribe(client)                               #
    client.loop_start()                             #



class mainApp(App):
    def build(self):
        global topic, client_id, port, broker, p
        self.FL = BoxLayout(orientation="vertical")
        self.BL = FloatLayout()

        self.ti2 = TextInput(text="Group", pos=(250, 550), size_hint_x=None, 
            width=200, size_hint_y=None, height=50)
        btn4 = Button(text = 'Перезагрузить группу', color='red', font_size='15', background_color='grey', 
            size_hint_x=None, width=200, size_hint_y=None, height=50, pos=(450, 550))
        btn4.bind(on_press=self.rl)
        
        
        p -= 100
        self.BL.add_widget(self.ti2)
        self.FL.add_widget(self.BL)
        self.BL.add_widget(btn4)
        return self.FL
    def StuentInfo(self, instance):
        global info
        global myname
        b = False
        global v
        global inf 
        inf *= -1
        b = False
        if inf == 1:
            b=False
        if inf == -1:
            b= True
        info.append(b)
        print (str(b))
    def tag(self, instance):
        tag = 0
        tag += 1

    def rl(self, instance):
        global broker, port, topic, client_id
        myinput = self.ti2.text
        b = ''
        b = myinput
        broker = 'broker.hivemq.com'
        port = 1883
        topic = b
        client_id = f'python-mqtt-{random.randint(0, 1000)}'
        running()
        print(str(list(base_data)))
        time.sleep(0.1)

    
    def save(self):
        with open('file.txt', 'w') as file:
            for nn in range(0, len(base_data)):
                file.writelines(str(base_data[nn]))
                file.write("""
""")

    def cl(self, instance):
        with open('file.txt', 'w') as file:
            file.write("")
        

avtorisationApp().run()

if __name__ == "__main__":
    mainApp().run()
