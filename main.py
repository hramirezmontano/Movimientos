from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from formularios.screen_nav import screen_helper
from formularios.ingresos import Fun_Ingresos
from formularios.consultas import Fun_Consultas

from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
import os
import sqlite3


from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

def connect_to_database(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        crea_tabla_movimientos(cursor)
        crea_tabla_usuarios(cursor)
        #Falta crear un usuario generico ejemplo Admin

        con.commit()
        con.close()

    except Exception as e:
        print(e)

def crea_tabla_movimientos(cursor):
    cursor.execute(
        """
        CREATE TABLE Movimientos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Patente  TEXT NOT NULL,
        Bultos   INT NOT NULL,
        Tienda   TEXT NOT NULL,
        Guia     TEXT NOT NULL,
        Odometro TEXT NOT NULL
        )
        """
    )
def crea_tabla_usuarios(cursor):
    cursor.execute(
        """
        CREATE TABLE Usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuarios  TEXT NOT NULL,
        password  TEXT NOT NULL
        )
        """
    )

class LoginScreen(Screen):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__()

        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/bd_example.db"

    input_usuario = ObjectProperty()
    input_password = ObjectProperty()

    def busca_usuarios(self):
        try:
            connect_to_database(self.DB_PATH)

            usuario=self.input_usuario.text
            password=self.input_password.text

            con=sqlite3.connect(self.DB_PATH)
            cursor = con.cursor()
            query = "select * from Usuarios where usuarios = '%s' and password = '%s'" %(usuario,password)
            cursor.execute(query)
            record = cursor.fetchone()

            if record is None:
                self.manager.current = 'NoLogin'
            else:
                self.manager.current = 'Ingresos'

        except Exception as e:
            print(e)

class Ingresos(Screen):
    def __init__(self,**kwargs):
        super(Ingresos,self).__init__()

    #variables globales
    input_patente = ObjectProperty()

    def Agrega_Movimientos(self):
        Fun_Ingresos.Agrega_Movimientos_patente(self)

    def menu_p(self):
        menu_items = [
            {"text": "Ingreso Movimientos"},
            {"text": "Consulta de Movimientos"},
            {"text": "Salir"}
        ]

        self.menu = MDDropdownMenu(
        caller=self.ids.button,
        items=menu_items,
        width_mult=5,
        callback=self.menu_callback)
        self.menu.open()

    def menu_callback(self, instance):
        opcion=instance

        if opcion.text == "Consulta de Movimientos":
            self.manager.current = 'Consulta'
            #self.menu.close()
        else:
            print("Opcion seleccionada es :", opcion.text)


class NoLogin(Screen):
    pass

class Consulta(Screen):
    data_tables: MDDataTable

    def __init__(self,**kwargs):
        super(Consulta,self).__init__()

    def menu_p(self):
        menu_items = [
            {"text": "Ingreso Movimientos"},
            {"text": "Consulta de Movimientos"},
            {"text": "Salir"}
        ]

        self.menu = MDDropdownMenu(
        caller=self.ids.button,
        items=menu_items,
        width_mult=5,
        callback=self.menu_callback)
        self.menu.bind(on_release=self.menu_callback)
        self.menu.open()

    def menu_callback(self, instance):
        opcion=instance

        if opcion.text == "Ingreso Movimientos":
            self.manager.current = 'Ingresos'

        else:
            print("Opcion seleccionada es :", opcion.text)

    def habre_md_table(self):
        Fun_Consultas.md_table(self)




sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(LoginScreen(name="Ingresos"))
sm.add_widget(LoginScreen(name="NoLogin"))
sm.add_widget(LoginScreen(name="Consulta"))

class Example(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)

Example().run()
