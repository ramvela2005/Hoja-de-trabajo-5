import numpy as np
import matplotlib.pyplot as plt

# Función que simula el tiempo de ejecución de un proceso con 1 procesador
def simulate_process_time_single_processor(n_processes, interval):
    # Generar un número aleatorio para el tiempo de ejecución de cada proceso
    process_times = np.abs(np.random.normal(0, 1, n_processes))  # Ensure non-negative process times
    
    # Sumar los tiempos de ejecución de todos los procesos
    total_time = np.sum(process_times)
    
    # Calcular el promedio de tiempo de ejecución
    average_time = total_time / n_processes
    
    # Calcular la desviación estándar
    std_dev = np.std(process_times)
    
    # Retornar los resultados
    return average_time, std_dev

