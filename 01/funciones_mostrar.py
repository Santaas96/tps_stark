from funciones_calcular import *

def mostrar_nombres_filtrado(shs: list, campo_filtro: str, valor_filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  print(f"Nombre de cada superheroe {valor_filtro}\n")
  filtered_list = filtrar_por_valor_campo(shs, campo_filtro, valor_filtro)
  imprimir_por_campo(filtered_list, "nombre")
  print(f"\n-------------------------------------------------------\n")

def mostrar_mas_alto_filtrado(shs: list, campo_filtro: str, valor_filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  filtered_list = filtrar_por_valor_campo(shs, campo_filtro, valor_filtro)
  mas_alto = calcular_mayor(filtered_list, "altura")
  print(f'Superheroe mas alto {valor_filtro}: {mas_alto["nombre"]} / {round(float(mas_alto["altura"]),2)}')
  print(f"\n-------------------------------------------------------\n")

def mostrar_mas_bajo_filtrado(shs: list, campo_filtro: str, valor_filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  filtered_list = filtrar_por_valor_campo(shs, campo_filtro, valor_filtro)
  mas_bajo = calcular_menor(filtered_list, "altura")
  print(f'Superheroe mas bajo {valor_filtro}: {mas_bajo["nombre"]} / {round(float(mas_bajo["altura"]),2)}')
  print(f"\n-------------------------------------------------------\n")

def mostrar_promedio_altura_filtrado(shs: list, campo_filtro: str, valor_filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  filtered_list = filtrar_por_valor_campo(shs, campo_filtro, valor_filtro)
  promedio = calcular_promedio(filtered_list, "altura")
  print(f"Altura promedio {valor_filtro}: {round(promedio/len(filtered_list),2)}")
  print(f"\n-------------------------------------------------------\n")

def mostrar_cantidad_por_campo(shs:list, campo: str, filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  elementos = calcular_cantidades_por_campo(shs, campo)
  print(f"Cantidad de Superheroes {filtro}\n")
  for key, value in elementos.items():
    print(f"{key} :  {value}")
  print(f"\n-------------------------------------------------------\n")

def mostrar_shs_por_campo(shs:list, campo: str, filtro: str) -> None:
  print(f"\n-------------------------------------------------------\n")
  elementos = calcular_shs_por_campo(shs, campo)
  print(f"Superheroes {filtro}\n")
  for key, value in elementos.items():
    print(f"{key} :  {value}")
  print(f"\n-------------------------------------------------------\n")