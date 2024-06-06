from data import lista_personajes
from funciones_stark import *

def desplegar_menu():
    """Muestra el menú principal."""
    print(f"\n-------------- Menu Principal Data Stark 00 --------------\n")
    print(f"A. Nombre de cada superheroe")
    print(f"B. Nombre y altura de cada superheroe de cada superheroe")
    print(f"C. Superheroe mas alto")
    print(f"D. Superheroe mas bajo")
    print(f"E. Altura promedio de los superheroes")
    print(f"F. Identidad del superheroe mas alto y mas bajo")
    print(f"G. Superheroe mas pesado y mas liviano")
    print(f"0. Salir del programa")
    print(f"\n-------------------------------------------------------\n")

def main():
  while True:
    desplegar_menu()
    opcion_elegida = input("Seleccionar una opción: ").lower()

    match opcion_elegida:
       case "a":
          mostrar_nombres(lista_personajes)
       case "b":
          mostrar_nombres_altura(lista_personajes)
       case "c":
          mostrar_mas_alto(lista_personajes)
       case "d":
          mostrar_mas_bajo(lista_personajes)
       case "e":
          mostrar_promedio_altura(lista_personajes)
       case "f":
          mostrar_identidad_bajo_alto(lista_personajes)
       case "g":
          mostrar_pesado_liviano(lista_personajes)
       case "0":
          break

main()