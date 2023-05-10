#!/usr/bin/env python3 
# programa para ingreso de contactos contactos para crear respaldo
# create by: Hans Saldias 
# uso personal 
import os
from colorama import init, Back, Fore, Style 
init()
mensaje = Fore.GREEN + Style.BRIGHT+ """
*** Programa para respaldos de numero de contactos telefonicos\n
                                       el uso de este scrip es personal :) ****\n\n         create by: Hans Saldias :)""".title()




def Ingreso():
    os.system("clear")
    
    print(mensaje,"\n")
    nombre=input("Ingrese nombre : ")
    numero=input("Ingrese numero telefonico: ")
    with open("respaldo_contacto.txt", "a") as con:
        con.write(f"\n\nNombre: {nombre}\nNumero: {numero}")
        print("Cargando datos al sistema ...\n\n")
        print("Contacto guardado con  exito".upper())



def ver_listado():
      os.system("clear")
      print(                    "*** datos  guardados ***\n\n")
      archivo = open("respaldo_contacto.txt", "r")
      for con in archivo.read():
                  print(con, end="")
      
      

def reiniciar():
      os.system("python3 respaldo_contactos.py")              


def menu():
      
      while True:
            print(mensaje,"\n")
            print("""
            [1]  Ingresar contacto

            [2]  ver listado de contactos

            [3]  salir escriba 3 'Enter'

            [4]  Reiniciar Script 


            """)
            op = input("Ingrese opcion: ")

            if op == "1":
                  Ingreso()
            elif op == "2":
                  ver_listado()

            elif op == "4":
                  reiniciar()
            elif op == "3":
                  break
menu()
               

            
         


    

