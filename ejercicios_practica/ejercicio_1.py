# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    if numero_1 > numero_2:
        valor_max = numero_1        
    else:
        valor_max = numero_2
    return(valor_max)
    
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    valor_max = imprimir_mayor(2, 10)
    print("El numero mayor es:", valor_max)

    print("terminamos")