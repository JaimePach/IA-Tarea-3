import Listas as lis


def ASearch(lista,capacidad):
    espacioUsado = 0
    objAgregados =[]
    valorTotal = 0

    while espacioUsado <= capacidad: 
       numMayor = 0
       
       for i in lista:
           if i[0] not in objAgregados:
               if i[3] >= numMayor and i[2] + espacioUsado <= capacidad:
                  numMayor = i[3]
                  numObjeto = i[0]
                  pesoObjeto = i[2]
                  valor = i[1]  
                 
       objAgregados.append(numObjeto)   
       espacioUsado = espacioUsado + pesoObjeto
       valorTotal = valorTotal + valor
    espacioUsado = espacioUsado - pesoObjeto
    valorTotal = valorTotal - valor
    objAgregados.pop()
    print(f'Los objetos agregados en la mochila son {objAgregados}')
    print(f'El valor optimo es: {valorTotal}')
    print(f'Con un peso de: {espacioUsado}')
         
if __name__ == '__main__':

   ASearch(lis.listagrande, 10000)         