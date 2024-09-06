import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

# Clase principal para la aplicación de ordenamiento
class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualización de Algoritmos de Ordenamiento")
        self.root.geometry("1200x600")  # Tamaño ajustado

        # Crear el frame para los controles
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)

        # Botones y controles
        self.generate_button = tk.Button(self.control_frame, text="Generar Datos", command=self.prompt_data)
        self.generate_button.grid(row=0, column=0, padx=10, pady=5)

        self.sort_button = tk.Button(self.control_frame, text="Ordenar todos", command=self.sort_all_algorithms)
        self.sort_button.grid(row=0, column=1, padx=10, pady=5)

        # Crear tres gráficos, uno para cada algoritmo
        self.bubble_frame = tk.Frame(self.root)
        self.bubble_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.selection_frame = tk.Frame(self.root)
        self.selection_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.insertion_frame = tk.Frame(self.root)
        self.insertion_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Etiquetas para mostrar el tiempo
        self.bubble_time_label = tk.Label(self.bubble_frame, text="Burbuja: Tiempo no calculado")
        self.bubble_time_label.pack(pady=5)

        self.selection_time_label = tk.Label(self.selection_frame, text="Selección: Tiempo no calculado")
        self.selection_time_label.pack(pady=5)

        self.insertion_time_label = tk.Label(self.insertion_frame, text="Inserción: Tiempo no calculado")
        self.insertion_time_label.pack(pady=5)

        # Crear gráficos de matplotlib con tamaño reducido
        self.fig_bubble, self.ax_bubble = plt.subplots(figsize=(3.5, 3))  # Tamaño ajustado
        self.canvas_bubble = FigureCanvasTkAgg(self.fig_bubble, master=self.bubble_frame)
        self.canvas_bubble.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.fig_selection, self.ax_selection = plt.subplots(figsize=(3.5, 3))  # Tamaño ajustado
        self.canvas_selection = FigureCanvasTkAgg(self.fig_selection, master=self.selection_frame)
        self.canvas_selection.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.fig_insertion, self.ax_insertion = plt.subplots(figsize=(3.5, 3))  # Tamaño ajustado
        self.canvas_insertion = FigureCanvasTkAgg(self.fig_insertion, master=self.insertion_frame)
        self.canvas_insertion.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.data = []
        self.sorted_data = []

    # Pedir datos al usuario
    def prompt_data(self):
        data_input = simpledialog.askstring("Entrada de Datos", "Ingrese los números separados por comas:")
        if data_input:
            try:
                self.data = [int(x.strip()) for x in data_input.split(',')]
                self.update_plot(self.ax_bubble, self.data)
                self.update_plot(self.ax_selection, self.data)
                self.update_plot(self.ax_insertion, self.data)
            except ValueError:
                tk.messagebox.showerror("Error", "Por favor, ingrese solo números enteros separados por comas.")

    # Actualizar el gráfico con los datos
    def update_plot(self, ax, data, colors=None):
        ax.clear()
        if colors is None:
            colors = ['blue'] * len(data)
        ax.bar(range(len(data)), data, color=colors)
        ax.figure.canvas.draw()

    # Ejecutar todos los algoritmos simultáneamente
    def sort_all_algorithms(self):
        self.sorted_data = self.data.copy()

        # Crear hilos para cada algoritmo
        bubble_thread = threading.Thread(target=self.bubble_sort)
        selection_thread = threading.Thread(target=self.selection_sort)
        insertion_thread = threading.Thread(target=self.insertion_sort)

        # Iniciar los hilos
        bubble_thread.start()
        selection_thread.start()
        insertion_thread.start()

    # Algoritmo de burbuja
    def bubble_sort(self):
        data = self.sorted_data.copy()
        n = len(data)
        start_time = time.time()
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                self.update_plot(self.ax_bubble, data, ['red' if x == j or x == j+1 else 'blue' for x in range(n)])
                time.sleep(0.05)  # Pausa para visualizar
        end_time = time.time()
        bubble_time = round(end_time - start_time, 2)
        self.bubble_time_label.config(text=f"Burbuja: {bubble_time}s")

    # Algoritmo de selección
    def selection_sort(self):
        data = self.sorted_data.copy()
        n = len(data)
        start_time = time.time()
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.update_plot(self.ax_selection, data, ['red' if x == min_idx or x == i else 'blue' for x in range(n)])
            time.sleep(0.1)
        end_time = time.time()
        selection_time = round(end_time - start_time, 2)
        self.selection_time_label.config(text=f"Selección: {selection_time}s")

    # Algoritmo de inserción
    def insertion_sort(self):
        data = self.sorted_data.copy()
        n = len(data)
        start_time = time.time()
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.update_plot(self.ax_insertion, data, ['red' if x == i or x == j+1 else 'blue' for x in range(n)])
            time.sleep(0.1)
        end_time = time.time()
        insertion_time = round(end_time - start_time, 2)
        self.insertion_time_label.config(text=f"Inserción: {insertion_time}s")

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
