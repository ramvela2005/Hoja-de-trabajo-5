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

# Ejecutar la simulación con diferentes cantidades de procesos
n_processes = [25, 50, 100, 150, 200]

# Ejecutar la simulación con diferentes intervalos
intervals = [1, 5, 10]

# Guardar los resultados en una lista de listas para 1 procesador
results_single_processor = []
for n in n_processes:
    for i in intervals:
        average_time, std_dev = simulate_process_time_single_processor(n, i)
        results_single_processor.append([n, i, average_time, std_dev])

# Guardar los resultados en una lista de listas para 2 procesadores
results_double_processors = []
for n in n_processes:
    for i in intervals:
        average_time, std_dev = simulate_process_time_double_processors(n, i)
        results_double_processors.append([n, i, average_time, std_dev])
        
# Crear gráficas
plt.figure(figsize=(12, 6))

# Gráfica para 1 procesador
plt.subplot(1, 2, 1)
for i in range(len(intervals)):
    plt.plot(n_processes, [result[2] for result in results_single_processor if result[1] == intervals[i]], label=f'Intervalo {intervals[i]}')
plt.xlabel('Número de procesos')
plt.ylabel('Tiempo promedio (s)')
plt.title('Tiempo promedio de ejecución con 1 procesador')
plt.legend()

# Gráfica para 2 procesadores
plt.subplot(1, 2, 2)
for i in range(len(intervals)):
    plt.plot(n_processes, [result[2] for result in results_double_processors if result[1] == intervals[i]], label=f'Intervalo {intervals[i]}')
plt.xlabel('Número de procesos')
plt.ylabel('Tiempo promedio (s)')
plt.title('Tiempo promedio de ejecución con 2 procesadores')
plt.legend()

plt.tight_layout()
plt.show()

