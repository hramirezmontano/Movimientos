screen_helper = """
ScreenManager:
    LoginScreen:
    Ingresos:
    NoLogin:
    Consulta:

<LoginScreen>:
    name:"login_screen"
    id:login_screen

    input_usuario : usuario
    input_password : password

    MDToolbar:
        title: "Acceso Restringido"
        pos_hint: {"top": 1}
        elevation: 10

    MDCard:
        orientation:"horizontal"
        size_hint: None, None
        #Tamaño de objeto
        size: dp(500), dp(340)
        #Posision Objeto
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Image:
            size_hint: .3, .9
            source: 'logo.png'
            pos_hint: {'left': 0.5, 'center_y': 0.5}

        BoxLayout:
            orientation:'vertical'
            padding: dp(10)
            spacing:20

            MDLabel:
                text: 'Acceso de Usuario'
                theme_text_color: 'Secondary'
                size_hint_y: None
                height: dp(1)
            MDSeparator:
                height: dp(1)

            MDTextField:
                id: usuario
                max_text_length:10
                hint_text: "Usuario "
                helper_text_mode: "on_focus"
            MDTextField:
                id: password
                password: True
                max_text_length:10
                hint_text: "Password "
                helper_text_mode: "on_focus"
            MDFlatButton:
                text: "Ingresar"
                pos_hint: {'center_x': 0.5}
                on_release: login_screen.busca_usuarios()

    MDToolbar:
        title: "Servicios Terrestres Sur Austral."
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}

<Ingresos>:  
    name:"Ingresos"
    id:Ingresos    
  
    input_patente : tx_patente
    input_bultos : tx_bultos
    input_tienda : tx_tienda
    input_guia : tx_guia
    input_odometro : tx_odometro
    
    MDToolbar:
        title: "                 Acceso Restringido"
        pos_hint: {"top": 1}
        elevation: 10
        
    MDRaisedButton:
        id: button
        text: "Menu"
        pos_hint: {"top": .98}
        pos_hint_y:{"left":20}
        on_release: Ingresos.menu_p()
        
    BoxLayout:
        top:25                
        GridLayout:
            cols:4
            #adaptive_height: True
           
            #Primera Linea
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
            MDLabel:  
                halign:"left"
                text: "Ingrese Patente"
                size_hint_y:.1

            MDTextFieldRect:  
                id:tx_patente
                hint_text: "Patente"                
                size_hint_y:.1
                
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1

            #Segunda Linea
            MDLabel: 
                #Separador
                text:" "
                size_hint_y:.1
                
            MDLabel:  
                halign:"left"
                text: "Ingrese Bultos"
                size_hint_y:.1
            
            MDTextFieldRect: 
                id:tx_bultos
                hint_text: "Bultos"                
                size_hint_y:.1
            
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
                
            #Tercera Linea
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
                
            MDLabel: 
                halign:"left"
                text: "Ingrese Tienda"
                size_hint_y:.1
            
            MDTextFieldRect:  
                id:tx_tienda
                hint_text: "Tienda"                
                size_hint_y:.1
            
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1

            #Cuarta Linea 
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
                
            MDLabel: 
                halign:"left"
                text: "Ingrese Guia"
                size_hint_y:.1
            
            MDTextFieldRect:  
                id:tx_guia
                hint_text: "Guia"                
                size_hint_y:.1
            
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1

            #Quinta Linea
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1

            MDLabel:  
                halign:"left"
                text: "Ingrese Odometro Final"
                size_hint_y:.1
                
            MDTextFieldRect:  
                id:tx_odometro
                hint_text: "Odometro"                
                size_hint_y:.1
            
            MDLabel:
                #Separador
                text:""
                size_hint_y:.1
            
            #Sexta Linea
            MDLabel:
                text:""  
                size_hint_y:.1      
            MDLabel:
                text:""
                size_hint_y:.1        
            MDLabel:
                text:""
                size_hint_y:.1        
            MDLabel:
                text:""
                size_hint_y:.1
            
            
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
                
            MDRaisedButton:
                left: 68
                text:"Agregar"
                #text_color: 0, 0, 1, 2
                size_hint_y:.1
                on_release: Ingresos.Agrega_Movimientos()
                
            MDRaisedButton:
                text:"Salir"
                #text_color: 0, 0, 1, 2            
                size_hint_y:.1
                         
            MDLabel:
                #Separador
                text:" "
                size_hint_y:.1
            
            MDLabel:
                text:""    
            Image:
                source:'camion.png'

            MDLabel:
                text:""               
                
            MDLabel:
                text:""               
     
            #Sube el camion
            MDLabel:
                text:""    
                size_hint_y:.6
                size_hint_x:.9
    
    MDToolbar:
        title: "Servicios Terrestres Sur Austral."
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}

<NoLogin>:
    name:"NoLogin"
    id:nologin    

    MDToolbar:
        title: "Usuario No Registrado"
        pos_hint: {"top": 1}
        elevation: 10
    MDRectangleFlatButton:
        text:"Atras"
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current="login_screen" 

    MDToolbar:
        title: "Aplicweb"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}

<Consulta>:
    name: "Consulta"
    id: Consulta
    
    MDToolbar:
        title: "                Consulta de Movimientos"
        pos_hint: {"top": 1}
        elevation: 10
        
    MDRaisedButton:
        id: button
        text: "Menu"
        pos_hint: {"top": .98}
        pos_hint_y:{"left":20}
        on_release: Consulta.menu_p()

    BoxLayout:
        top:25    
       
        MDLabel:
            id:separator1
            pos_hint: {'center_x': .5, 'center_y': .5}
       
        MDLabel:
            id:separator2
            pos_hint: {'center_x': .5, 'center_y': .5}
       
        MDRaisedButton:
            text: 'Abrir Consulta'
            on_release: Consulta.habre_md_table()
            pos_hint: {'center_x': .5, 'center_y': .5}
       
        MDLabel:
            id:separator3
            pos_hint: {'center_x': .5, 'center_y': .5}
       
        MDLabel:
            id:separator4
            pos_hint: {'center_x': .5, 'center_y': .5}
  
"""
