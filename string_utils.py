def explode_string(a_string):
    # transforma una cadena de caracteres 'Han' => ['H', 'a', 'n']
    
    return list(a_string)

def explode_list_of_strings(list_of_strings):
    # aplica explode_string a cadena de la lista

    result = []
    for each_string in list_of_strings:
        result.append(explode_string(each_string))
    return result