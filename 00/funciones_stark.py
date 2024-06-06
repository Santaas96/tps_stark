from utils import *

def mostrar_nombres(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  print(f"Nombre de cada superheroe\n")
  map_list(lambda sh: print(sh["nombre"]), shs)
  print(f"\n-------------------------------------------------------\n")

def mostrar_nombres_altura(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  print(f"\nNombre y altura de cada superheroe de cada superheroe\n")
  map_list(lambda sh: print(f'Nombre: {sh["nombre"]}, Altura: {float(sh["altura"])}'), shs)
  print(f"\n-------------------------------------------------------\n")

def mostrar_mas_alto(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  mas_alto = reduce_list(lambda ant, act: ant if float(ant["altura"]) > float(act["altura"]) else act, shs)
  print(f'Superheroe mas alto: {mas_alto["nombre"]} / {round(float(mas_alto["altura"]),2)}')
  print(f"\n-------------------------------------------------------\n")

def mostrar_mas_bajo(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  mas_bajo = reduce_list(lambda ant, act: ant if float(ant["altura"]) < float(act["altura"]) else act, shs)
  print(f'Superheroe mas bajo: {mas_bajo["nombre"]} / {round(float(mas_bajo["altura"]),2)}')
  print(f"\n-------------------------------------------------------\n")

def mostrar_promedio_altura(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  alturas_float = map_list(lambda sh: float(sh["altura"]), shs)
  sumatoria = reduce_list(lambda ant, act: ant + act, alturas_float)
  print(f"Altura promedio: {round(sumatoria/len(shs),2)}")
  print(f"\n-------------------------------------------------------\n")

def mostrar_identidad_bajo_alto(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  mas_alto = reduce_list(lambda ant, act: ant if float(ant["altura"]) > float(act["altura"]) else act, shs)
  print(f'Identidad superheroe mas alto: {mas_alto["identidad"]}')
  mas_bajo = reduce_list(lambda ant, act: ant if float(ant["altura"]) < float(act["altura"]) else act, shs)
  print(f'\nIdentidad superheroe mas bajo: {mas_bajo["identidad"]}')
  (f"\n-------------------------------------------------------\n")

def mostrar_pesado_liviano(shs: list) -> None:
  print(f"\n-------------------------------------------------------\n")
  mas_pesado = reduce_list(lambda ant, act: ant if float(ant["peso"]) > float(act["peso"]) else act, shs)
  print(f'Superheroe mas pesado: {mas_pesado["nombre"]} / {round(float(mas_pesado["peso"]),2)}')
  mas_liviano = reduce_list(lambda ant, act: ant if float(ant["peso"]) < float(act["peso"]) else act, shs)
  print(f'\nSuperheroe mas liviano: {mas_liviano["nombre"]} / {round(float(mas_liviano["peso"]),2)}')
  print(f"\n-------------------------------------------------------\n")