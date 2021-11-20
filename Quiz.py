from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (360, 600)

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        padding: [0, 0, 0, 0,]
        MDToolbar:
            #title: "MDToolbar"
            #anchor_title: "center"
            left_action_items: [["arrow-left"]]
        #PRINCIPAL 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                orientation: "horizontal"
                padding: 10
                
                MDProgressBar:
                    orientation: "horizontal"
                    value: 50
                ####### COLOCAR PROGRESS BAR
                
                
            MDBoxLayout:
                orientation: "vertical"
                MDLabel:
                    text: "ESPAÇO PARA PERGUNTA"
                    halign: "center"
        #LAYOUT PRINCIPAL 2    
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: [0, 0, 0, 0]
                    spacing: 10
                    MDRaisedButton:
                        text: "Pergunta 1"
                        pos_hint: {"center_x": .5}
                    MDRaisedButton:
                        text: "Pergunta 2"
                        pos_hint: {"center_x": .5}
                    MDRaisedButton:
                        text: "Pergunta 3"
                        pos_hint: {"center_x": .5}
                    MDRaisedButton:
                        text: "Pergunta 4"
                        pos_hint: {"center_x": .5}
            MDBoxLayout:
                orientation: "vertical" 
                MDRaisedButton:
                    text:
                    pos_hint: {"center_x": .5}
'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()