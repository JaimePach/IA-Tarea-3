import Listas as list
from operator import itemgetter

def funcion(e):
    return e[2]

def uniformCostSearch(lista, capacidad):
    
    espacioUsado = 0
    objAgregados = []
    valorTotal = 0

    lista_ordenada = sorted(lista, key=itemgetter(2)) 

    for l in lista_ordenada:
         if l[2] + espacioUsado <= capacidad:
             espacioUsado = espacioUsado + l[2]
             objAgregados.append(l[0])
             valorTotal = valorTotal + l[1]
         else:
           break      
    print(f'Los objetos agregados son:  {objAgregados}')
    print(f'El valor optimo es: {valorTotal}')
    print(f'Con un peso de: {espacioUsado}')

if __name__ == '__main__':
 
    uniformCostSearch(list.listagrande, 10000) 