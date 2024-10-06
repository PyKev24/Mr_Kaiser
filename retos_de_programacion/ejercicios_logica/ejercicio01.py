# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:19:25 2024

@author: Kevin

Retos de programación - Ejercicios de Lógica 

Ejercicio 1: El famoso Fizz-Buzz

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

for i in range(1, 100+1):
    if (i % 3 == 0) and (i % 5 == 0):
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
