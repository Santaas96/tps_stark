from data import lista_personajes
from funciones_mostrar import *

def desplegar_menu():
   """Muestra el menú principal."""
   print(f"\n-------------- Menu Principal Data Stark 01 --------------\n")
   print(f"A. Nombre de cada superheroe Masculino")
   print(f"B. Nombre de cada superheroe Femenino")
   print(f"C. Superheroe mas alto Masculino")
   print(f"D. Superheroe mas alto Femenino")
   print(f"E. Superheroe mas bajo Masculino")
   print(f"F. Superheroe mas bajo Femenino")
   print(f"G. Promedio altura superheroe Masculino")
   print(f"H. Promedio altura superheroe Femenino")
   print(f"I. Nombre superheroes items C a F")
   print(f"J. Cantidad de Superheroes por cada color de ojos")
   print(f"K. Cantidad de Superheroes por cada color de pelo")
   print(f"L. Cantidad de Superheroes por cada valor de inteligencia")
   print(f"M. Nombre de Superheroes por cada color de ojos")
   print(f"N. Nombre de Superheroes por cada color de pelo")
   print(f"O. Nombre de Superheroes por cada valor de inteligencia")
   print(f"\n-------------------------------------------------------\n")

def main():
   while True:
      desplegar_menu()
      opcion_elegida = input("Seleccionar una opción: ").lower()

      match opcion_elegida:
         case "a":
            mostrar_nombres_filtrado(lista_personajes, "genero", "M")
         case "b":
            mostrar_nombres_filtrado(lista_personajes, "genero", "F")
         case "c":
            mostrar_mas_alto_filtrado(lista_personajes, "genero", "M")
         case "d":
            mostrar_mas_alto_filtrado(lista_personajes, "genero", "F")
         case "e":
            mostrar_mas_bajo_filtrado(lista_personajes, "genero", "M")
         case "f":
            mostrar_mas_bajo_filtrado(lista_personajes, "genero", "F")
         case "g":
            mostrar_promedio_altura_filtrado(lista_personajes, "genero", "M")
         case "h":
            mostrar_promedio_altura_filtrado(lista_personajes, "genero", "F")
         case "i":
            mostrar_mas_alto_filtrado(lista_personajes, "genero", "M")
            mostrar_mas_alto_filtrado(lista_personajes, "genero", "F")
            mostrar_mas_bajo_filtrado(lista_personajes, "genero", "M")
            mostrar_mas_bajo_filtrado(lista_personajes, "genero", "F")
         case "j":
            mostrar_cantidad_por_campo(lista_personajes, "color_ojos", "con cada color de ojos")
         case "k":
            mostrar_cantidad_por_campo(lista_personajes, "color_pelo", "con cada color de pelo")
         case "l":
            mostrar_cantidad_por_campo(lista_personajes, "inteligencia", "con cada valor de inteligencia")
         case "m":
            mostrar_shs_por_campo(lista_personajes, "color_ojos", "con cada color de ojos")
         case "n":
            mostrar_shs_por_campo(lista_personajes, "color_pelo", "con cada color de pelo")
         case "o":
            mostrar_shs_por_campo(lista_personajes, "inteligencia", "con cada valor de inteligencia")
         case "0":
            break

main()