def ordenamiento_insercion(lista):
    n = len(lista)
    print(f"Lista inicial: {lista}")
    
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave
        print(f"Lista después de la iteración {i}: {lista}")
    
    return lista

# Ejemplo de uso
lista = [4, 3, 2, 10, 12, 1, 5]
ordenamiento_insercion(lista)
