from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (360, 600)

KV = '''
MDScreen:
    MDBottomNavigation:
    
        #Jogar
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Jogar'
            icon: 'home-circle-outline'    
                                   
            Screen:
                MDNavigationLayout:
                    ScreenManager:
                        Screen:
                            MDBoxLayout:
                                orientation: 'vertical'
                                MDToolbar:
                                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                                    elevation: 8
                                
                                Widget:

                            BoxLayout:
                                spacing: 40
                                orientation: 'vertical'
                                padding: 0, 120, 0, 70
                                size: root.width, root.height
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: 0, 0, 0, 40
                                    
                                    #Label Jogar
                                    MDLabel:
                                        text: "Título"
                                        halign: 'center'
                                        bold: True
                                        font_size: '35sp'
                                    #FONTE ROBOTO BLACK
                                        font_name: 'fontes/Roboto-Black.ttf'
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: 0, 0, 0, 0
                                    
                                    #Logo Jogo
                                    MDIconButton:
                                        icon:
                                        pos_hint: {"center_x": .5}
                                        user_font_size: "120sp"
                                BoxLayout:
                                    spacing: 10
                                    orientation: 'vertical'
                                    padding: 0, 0, 0, 30
                                    size: root.width, root.height
                                    
                                    #Botão Jogar
                                    MDFillRoundFlatButton:
                                        text: 'Jogar'
                                        pos_hint: {'center_x': .5}
                                        size_hint_x: .8
                        
                    MDNavigationDrawer:
                        id: nav_drawer   
                        MDToolbar: 
                            pos_hint: {"top": 1}
                            title: "Configurações"
                            left_action_items: [["cog"]]
                        
                        
                               
        #Perfil
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Perfil'
            icon: 'account-circle-outline'
            
            MDToolbar:
                left_action_items: [["arrow-left"]]
                elevation: 7
                pos_hint: {"top": 1}
                #adaptive_height: True
            
        #Sobre nós  
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Sobre nós'
            icon: 'book-information-variant'
            
            MDToolbar:
                left_action_items: [["arrow-left"]]
                elevation: 7
                pos_hint: {"top": 1}
                adaptive_height: True


'''



class PaginaInicial(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(KV)

        return screen



PaginaInicial().run()
