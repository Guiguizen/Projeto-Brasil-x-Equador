from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360, 600)


# CRIAÇÃO DO ARQUIVO KIVY
KV = '''

BoxLayout:
    spacing: 10
    orientation: 'vertical'
    padding: 0, 50, 0, 150
    size: root.width, root.height

    
    MDIconButton:
        icon: 
        pos_hint: {"center_x": .5, "center_y": .5}
        user_font_size: "120sp"
        
    BoxLayout:    
        orientation: 'vertical'
        padding: 0, 40, 0, 50
        
        MDLabel:
            text: "Selecionar Idioma"
            halign: 'center'     
            bold: True
            font_size: '35sp'
    ##FONTE ROBOTO BLACK
            font_name: 'fontes/Roboto-Black.ttf'
            
        MDLabel:
            text: "Seleccione el idioma"
            halign: 'center'     
            bold: True
            font_size: '20sp'
    ##FONTE ROBOTO
            font_name: 'fontes/Roboto-Thin.ttf'
        
    MDRoundFlatButton:
        text: 'Português'
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_x: .8
    ##ESCOLHER A COR
        md_bg_color: 
        
    MDRoundFlatButton:
        text: 'Español'
        pos_hint: {'center_x': .5, 'center_y': .4}
        size_hint_x: .8 
    ##ESCOLHER A COR
        md_bg_color:
        

'''

#CLASSE PRINCIPAL DO APLICATIVO
class EscolherIdioma(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


EscolherIdioma().run()
