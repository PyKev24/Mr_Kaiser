# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:31:27 2024

@author: Kevin

FreeCodeCamp - Build an Arithmetic Formatter Project
"""
def transformer(problems):
    """
    

    Parameters
    ----------
    problems : LIST
        Lista con los problemas con la forma ['23 + 4', '33 - 7'].

    Returns
    -------
    problems_dict : DICT
        La función devuelve un diccionario con el objetivo de tener seperado las filas,
        de la forma {'top': [], 'operator': [], 'botton': []}.

    """
    problems_dict = {'top': [], 'operator': [], 'botton': []}
    for problem in problems:
        for key, value in zip(problems_dict, problem.split()):
            problems_dict[key].append(value)
    return problems_dict


def normalizer(list_1, list_2):
    """
    La función devuelve las listas de modo que los i-elementos de cada lista tengan misma longitud.
    Se rellena con espacios, en el ejemplo es con underscore para su legibilidad.    
    *Se agregan los 2 espacios a la izquierda porque es el objetivo.
    
    Parameters
    ----------
    list_1 : LIST
        Una lista de strings. Ejemplo: ['234', '9']
    list_2 : LIST
        Una lista de strings. Ejemplo: ['34', '10']

    Returns
    -------
    list_1_normal : LIST
        Una lista de strings. Ejemplo: ['_ _234', '_ _ _9']
    list_2_normal : LIST
        Una lista de strings. Ejemplo: ['_ _ _34', '_ _10']

    """
    list_1_normal = []
    list_2_normal = []
    space = lambda a, b: abs(len(a) - len(b)) + 2   # el mas chico necesita la diferencia + 2 espacios
    
    for a, b in zip(list_1, list_2):
        if len(a) > len(b):
            list_1_normal.append('  ' + a)          # '__numero'
            list_2_normal.append(' ' * space(a, b) + b)
        elif len(a) < len(b):
            list_1_normal.append(' ' * space(a, b) + a)
            list_2_normal.append('  ' + b)
        else:
            list_1_normal.append('  '  + a)
            list_2_normal.append('  ' + b)
    return list_1_normal, list_2_normal
            

def add_operator(botton, operators):
    # agregamos la operacion a la fila botton:
    # si es una suma '   43' ---> '+  43'
    
    botton_with_sign = []
    for i in range(len(botton)):
        botton_with_sign.append(operators[i] + botton[i][1:])
    return botton_with_sign


def answer(problems):
    # Resolvemos la suma o la resta, tambien utilizamos el i como index de top o botton
    
    results = []
    for i in range(len(problems['top'])):
        if problems['operator'][i] == '+':
            results.append(str(int(problems['top'][i]) + int(problems['botton'][i])))
        elif problems['operator'][i] == '-':
            results.append(str(int(problems['top'][i]) - int(problems['botton'][i])))
    return results


def glue(top, botton, results):
    dashes = lambda x: '-' * len(x)
    string_dashes = list(map(dashes, botton))
    
    
    # falta normalizar los resultados
    tmp_1, tmp_2 = normalizer(botton, results)
    del_two_spaces = lambda string: string[2:]
    results = list(map(del_two_spaces, tmp_2))
    
    end = ''
    for row in [top, botton, string_dashes, results]:
        end += '    '.join(row) + '\n'
    
    # le quitamos la cola de espacios con el rstrip
    # es lo que pide en los test :(
    return end[:-1].rstrip()



def arithmetic_arranger(problems, show_answers=False):
    n = len(problems)
    
    # primero: lo dividimos en top, operator y botton
    problems_dict = transformer(problems)
    
    
    # Errores - Raises!
    # para los test solo hay que devolver strings
    if n > 5:
        #raise TypeError('Error: Too many problems.')
        return 'Error: Too many problems.'
    if ('*' in problems_dict['operator']) or ('/' in problems_dict['operator']):
        #raise TypeError("Error: Operator must be '+' or '-'.")
        return "Error: Operator must be '+' or '-'."
    if (False in list(map(str.isnumeric, problems_dict['top']))) or (False in list(map(str.isnumeric, problems_dict['botton']))):
        #raise TypeError('Error: Numbers must only contain digits.')
        return 'Error: Numbers must only contain digits.'
    if (True in list(map(lambda x: len(x) > 4, problems_dict['top']))) or (True in list(map(lambda x: len(x) > 4, problems_dict['botton']))):
        #raise TypeError('Error: Numbers cannot be more than four digits.')
        return 'Error: Numbers cannot be more than four digits.'
    
    
    # segundo: agregamos los resultados y si es False(No se quiere ver) una lista tipo ['', '', '']
    if show_answers == True:
        problems_dict['results'] = answer(problems_dict)
    else:
        problems_dict['results'] = [''] * n
    
    
    # tercero: hay que acomodar los espacios    
    problems_dict['top'], problems_dict['botton'] = normalizer(problems_dict['top'], problems_dict['botton'])
    
    
    # cuarto: agregamos la operacion a botton
    problems_dict['botton'] = add_operator(problems_dict['botton'], problems_dict['operator'])
    
    
    # quinto: pegamos todo!
    problems = glue(problems_dict['top'], problems_dict['botton'], problems_dict['results'])
    
    
    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
