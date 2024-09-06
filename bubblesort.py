def ordenamiento_burbuja(lista):
    n = len(lista)
    iteraciones = 0
    print(f"Lista inicial: {lista}")
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteraciones += 1
            print(f"Iteración {iteraciones}: Comparando {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"Intercambio: {lista}")
    
    print(f"Lista ordenada: {lista}")
    print(f"Total de iteraciones: {iteraciones}")
    return lista

# Ejemplo de uso
lista = [5, 2, 9, 1, 5, 6]
ordenamiento_burbuja(lista)
