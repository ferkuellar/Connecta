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

