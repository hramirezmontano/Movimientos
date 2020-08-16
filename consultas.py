from kivymd.uix import datatables
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import os
import sqlite3
# import win10toast
from win10toast import ToastNotifier
from formularios.ingresos import Fun_Ingresos


def self(args: object) -> object:
    pass

class Fun_Consultas():
    data_tables: MDDataTable

    def __init__(self,**kwargs):
        super(Fun_Consultas,self).__init__()

    def md_table(self):
        try:
            self.APP_PATH = os.getcwd()
            self.DB_PATH = self.APP_PATH + "/bd_example.db"

            con = sqlite3.connect(self.DB_PATH)
            cursor = con.cursor()

            query = "select id,patente,Bultos,Tienda,Guia,Odometro from Movimientos "
            cursor.execute(query)
            record = cursor.fetchall()

        except Exception as e:
            print(e)

        self.data_tables = MDDataTable(
            use_pagination=True,
            size_hint=(0.9, 0.6),
            check=False,
            sort=True,
            # name column, width column
            column_data=[
                ("Id", dp(20)),
                ("Patente", dp(20)),
                ("Bultos", dp(20)),
                ("Tienda", dp(40)),
                ("Guia", dp(20)),
                ("Odometro", dp(20)),
            ],

            row_data=record
        )
        self.data_tables.bind(on_row_press=Fun_Consultas.on_row_press)
        self.data_tables.bind(on_check_press=Fun_Consultas.on_check_press)

        self.data_tables.open()

    def on_row_press(instance_table, instance_row):
        no = instance_row.text
        print(no)


    def on_check_press(instance_table, current_row):
        print(instance_table, current_row)
