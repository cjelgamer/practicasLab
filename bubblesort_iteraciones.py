def ordenamiento_burbuja(lista):
    n = len(lista)
    iteraciones = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteraciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return iteraciones

# Pruebas
lista_peor_caso = [9, 6, 5, 5, 2, 1]  # Lista en orden descendente
lista_mejor_caso = [1, 2, 5, 5, 6, 9]  # Lista ya ordenada
lista_caso_general = [5, 2, 9, 1, 5, 6]  # Lista desordenada

iteraciones_peor_caso = ordenamiento_burbuja(lista_peor_caso.copy())
iteraciones_mejor_caso = ordenamiento_burbuja(lista_mejor_caso.copy())
iteraciones_caso_general = ordenamiento_burbuja(lista_caso_general.copy())

print(f"Iteraciones en el peor caso: {iteraciones_peor_caso}")
print(f"Iteraciones en el mejor caso: {iteraciones_mejor_caso}")
print(f"Iteraciones en un caso general: {iteraciones_caso_general}")
