from utils import *

def imprimir_por_campo(lista: list, campo: str):
  map_list(lambda sh: print(sh[campo]), lista)

def filtrar_por_valor_campo(lista: list, campo: str, valor: str):
  return filter_list(lambda sh: sh[campo] == valor, lista)

def calcular_mayor(lista: list, campo: str):
  return reduce_list(lambda ant, act: ant if float(ant[campo]) > float(act[campo]) else act, lista)

def calcular_menor(lista: list, campo: str):
  return reduce_list(lambda ant, act: ant if float(ant[campo]) < float(act[campo]) else act, lista)

def calcular_promedio(lista: list, campo: str):
  floats_list = map_list(lambda sh: float(sh[campo]), lista)
  return reduce_list(lambda ant, act: ant + act, floats_list)

def reductora_cantidades_por_campo(ant: dict, act: dict, campo: str):
  if(act[campo] == ""):
    ant["No Tiene"] = ant["No Tiene"] + 1
  else:
    ant[act[campo]] = ant[act[campo]] + 1
  return ant

def calcular_cantidades_por_campo(lista: list, campo: str):
  maped_set = list(set(map_list(lambda sh: sh[campo] if sh[campo] != "" else "No Tiene", lista)))
  initial_reduce_value = {}
  for item in maped_set:
    initial_reduce_value[item] = 0
  cantidades = reduce_list(lambda ant, act: reductora_cantidades_por_campo(ant, act, campo), lista, initial_reduce_value)
  return cantidades

def reductora_shs_por_campo(ant: list, act: dict, campo: str):
  if(act[campo] == ""):
    ant["No Tiene"].append(act["nombre"])
  else:
    ant[act[campo]].append(act["nombre"])
  return ant

def calcular_shs_por_campo(lista: list, campo: str):
  maped_set = list(set(map_list(lambda sh: sh[campo] if sh[campo] != "" else "No Tiene", lista)))
  initial_reduce_value = {}
  for item in maped_set:
    initial_reduce_value[item] = []
  cantidades = reduce_list(lambda ant, act: reductora_shs_por_campo(ant, act, campo), lista, initial_reduce_value)
  return cantidades