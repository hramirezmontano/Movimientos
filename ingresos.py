import kivy
import os
import sqlite3
# import win10toast
from win10toast import ToastNotifier

class Fun_Ingresos():
    def __init__(self,**kwargs):
        super(Fun_Ingresos,self).__init__()
        self.input_patente = None
        self.input_bultos=None
        self.input_tienda = None
        self.input_guia = None
        self.input_odometro = None

    def Agrega_Movimientos_patente(self):
        try:
            self.APP_PATH = os.getcwd()
            self.DB_PATH = self.APP_PATH + "/bd_example.db"

            con = sqlite3.connect(self.DB_PATH)
            cursor = con.cursor()

            #Construir el insert
            patente = self.input_patente.text
            bultos = self.input_bultos.text
            tienda = self.input_tienda.text
            guia = self.input_guia.text
            odo_final = self.input_odometro.text

            sqlite_insert_with_param = """
            INSERT INTO Movimientos(Patente,Bultos,Tienda,Guia,Odometro)
            VALUES(?,?,?,?,?)
            """
            data_tuple = (patente, bultos, tienda, guia, odo_final)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            con.commit()
            print("Movimiento Agregado con Exito")
            cursor.close
        except sqlite3.Error as error:
            print("Error en el Insert", error)
        finally:
            if con:
                con.close()
                n = ToastNotifier()
                n.show_toast("Nuevo Ingreso", "Ingreso agregado con exito", duration=5,
                icon_path="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")
