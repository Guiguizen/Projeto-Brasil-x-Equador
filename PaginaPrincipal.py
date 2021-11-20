from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 600)

KV = '''

BoxLayout:
    spacing: 40
    orientation: 'vertical'
    padding: 0, 0, 0, 80
    size: root.width, root.height
    
    MDToolbar:
        right_action_items: [["cog"]]
        elevation: 7
        pos_hint: {"top": 1}
        adaptive_height: True
        
        
    BoxLayout:
        orientation: 'vertical'
        padding: 0, 0, 0, 20
        MDLabel:
            text: "Título"
            halign: 'center'     
            bold: True
            font_size: '35sp'
        ##FONTE ROBOTO BLACK
            font_name: 'fontes/Roboto-Black.ttf'
    
    BoxLayout:
        orientation: 'vertical'
        padding: 0, 0, 0, 40
        MDIconButton:
            icon: 
            pos_hint: {"center_x": .5}
            user_font_size: "120sp"
        
    BoxLayout:
        spacing: 10
        orientation: 'vertical'
        padding: 0, 0, 0, 0
        size: root.width, root.height
        
        MDFillRoundFlatButton:
            text: 'Jogar'
            pos_hint: {'center_x': .5}
            size_hint_x: .8
            
        MDFillRoundFlatButton:
            text: 'Ranking'
            pos_hint: {'center_x': .5}
            size_hint_x: .8
            
        MDFillRoundFlatButton:
            text: 'Escolher Perfil'
            pos_hint: {'center_x': .5}
            size_hint_x: .8
        ##ESCOLHER A COR
            md_bg_color:
            
        MDFillRoundFlatButton:
            text: 'Sobre Nós'
            pos_hint: {'center_x': .5}
            size_hint_x: .8
        ##ESCOLHER A COR
            md_bg_color:
        
    


'''

class PaginaInicial(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


PaginaInicial().run()