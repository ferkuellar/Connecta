def find_one(list, needle):
    # Devuelve True si ecuentra una o mas ocurrencias de needle en List
    return find_n(list, needle, 1)

def find_n(list, needle, n):
    # Devuelve True ein list si hay n o mas ocurrencias de needle
    # Flase si ha menos o si n < 0
    
    # Si n >= 0 
    if n >= 0:
        # Inicializamos el index y el count
        index = 0
        count = 0
        # Mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...

        while count < n and index < len(list):
            # Si lo encontramos, actualizamos el contador
            if needle == list[index]:
                count = count + 1
            # Avanzamos al siguente elemento
            index = index + 1
        # Devolvemos el resultado de comparar contador
        return count >= n
    else:
        return False
    
def find_streak(list, needle, n):
    # Devuelve True si en list hay n o mas needel´snseguidos
    # False para todo lo demas

    # Si n >= 0
    if n >= 0:
        # Inicializo el index, el count y el indicador de racha
        index = 0
        count = 0
        streak = False
        # Mientras no haya encontrado a n seguidos y la lilsta no se haya acabado....
        while count < n and index < len(list):
            # Si lo encuentro, activo el indicador de rachas y actualiza el count.
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                # Si no encuentra, desactivo el indiciador de racha y pongo en cero el contador
                streak = False
                count = 0
            # Avanza al siguiente elemento
            index = index + 1
        # Por ultimo devolvemos el resultado de comparar el contador con n y simpre y cuando estemos en racha.
        return count >= n and streak
    else:
        # Para valores de n < 0 ,  no tiene sentido
        return False

def first_elements(list_of_list):
    #Recibe una lista de listas y devuelve una lista con los primero elementos elementos de la original
    return nth_elements(list_of_list, 0)

def nth_elements(list_of_lists, n):
    #Recibe una lista de listas y devuelve una lista con los primero elementos elementos de la original
    result = []
    for list in list_of_lists:
        result.append(list[n])
    return result

def transpose(matrix):
    """
    Recibe una matriz y devuelve su transpuesta
    """
    # Creo un amatriz vacía y la llamo transp
    transp = []
    # Recorremos todas las columnas de la matriz original
    for n in range(len(matrix[0])):
        # extraigo los elementos enésimos y los encasqueto a transp
        transp.append(nth_elements(matrix, n))
    # devuelvo trnasp
    return transp

def displace(l, distance, filler=None):
    if distance == 0:
        return l
    elif distance > 0:
        filling = [filler] * distance
        res = filling + l
        res = res[:-distance]
        return res
    else:
        filling = [filler] * abs(distance)
        res = l + filling
        res = res[abs(distance):]
        return res

def displace_matrix(m, filler=None):
    # creamos una matriz vacía
    d = []
    # por cada calumna de la matriz original la desplazamos su índice -1
    for i in range(len(m)):
        # añadimos la columna desplazada a m
        d.append(displace(m[i], i - 1, filler))
        
    # devolvemos d
    return d

def reverse_list(l):
    return list(reversed(l))

def reverse_matrix(matrix):
    rm = []
    for col in matrix:
        rm.append(reverse_list(col))
    return rm

def all_same(l):
    # devuelve True si todos los elementos de la lista son iguales o la lista vacia

    if l == []:
        return True
    else:
        same = True
        first = l[0]
        for elt in l:
            if elt != first:
                same = False
                break
        return same
    
def collapse_list(l, empty = '.'):
    # concatena todas las cadenas de la lista en una sola lista
    collapsed = ''
    for elt in l:
        if elt == None:
            collapsed = collapsed + empty
        else:
            collapsed = collapsed + elt
    return collapsed

def collapse_matrix(m, empty = '.', fence = '|'):
    # concatena todas las cadenas en una sola separada por |

    collapsed = ''
    for elt in m:
        collapsed = collapsed + fence + collapse_list(elt, empty)
    return collapsed[1:]

def replace_all_in_list(original, old, new):
    # cambia todas las ocurrencias de old por new
    result = []
    for elt in original:
        if elt == old:
            result.append(new)
        else:
            result.append(elt)
    return result

def replace_all_in_matrix(original, old, new):
    # aplica replace_all_in_matrix a todas las listas
    result = []
    for each_list in original:
        result.append(replace_all_in_list(each_list, old, new))
    return result