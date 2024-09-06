def ordenamiento_seleccion(lista):
    n = len(lista)
    print(f"Lista inicial: {lista}")
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        # Intercambiar el mínimo encontrado con el elemento en la posición i
        lista[i], lista[minimo] = lista[minimo], lista[i]
        print(f"Lista después de la iteración {i + 1}: {lista}")
    return lista

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
ordenamiento_seleccion(lista)
