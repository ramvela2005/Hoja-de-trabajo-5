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
# Función que simula el tiempo de ejecución de un proceso con 2 procesadores
def simulate_process_time_double_processors(n_processes, interval):
    # Generar un número aleatorio para el tiempo de ejecución de cada proceso
    process_times = np.abs(np.random.normal(0, 1, n_processes))  # Ensure non-negative process times
    
    # Dividir los procesos entre los procesadores
    processes_per_processor = n_processes // 2
    
    # Calcular el tiempo total de ejecución para cada procesador
    total_times_per_processor = [np.sum(process_times[i:i+processes_per_processor]) for i in range(0, n_processes, processes_per_processor)]
    
    # Calcular el tiempo total de ejecución para ambos procesadores
    total_time = max(total_times_per_processor)
    
    # Calcular el promedio de tiempo de ejecución
    average_time = total_time / n_processes
    
    # Calcular la desviación estándar
    std_dev = np.std(process_times)
    
    # Retornar los resultados
    return average_time, std_dev
