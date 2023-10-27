import time
import platform
import cpuinfo
import math

os_version = platform.system()

print("\n\nPython CPU Benchmark (Windows, macOS(Darwin), Linux)")
print("CPU: " + cpuinfo.get_cpu_info().get("brand_raw", "Unknown"))
print("Arquitetura: " + cpuinfo.get_cpu_info().get("arch_string_raw", "Unknown"))
print("Sistema Operacional: " + str(os_version))

print("\nBenchmarking usando Fórmula de Leibniz: \n")

ITERATIONS: int = 1000000  # Quantidade de vezes que o benchmark será executado

SAMPLES: int = 10  # Quantidades de amostras para calcular a média

average_benchmark_time: float = 0
average_result: float = 0

for i in range(0, SAMPLES):
    start = time.time()
    result: float = 0

    for k in range(0, ITERATIONS):
        result += ((-1) ** k) / (2 * k + 1)

    end = time.time()
    duration = end - start
    duration = round(duration, 3)
    average_benchmark_time += duration
    average_result += 4 * result
    print("Tempo: " + str(duration) + "s")

average_benchmark_time = round(average_benchmark_time / SAMPLES, 3)
final_result: float = average_result / SAMPLES

print(f"\n'k' utilizado: {ITERATIONS}")
print(f"Média de {SAMPLES} amostras: {str(average_benchmark_time)}s")
print(f"Valor final de PI calculado: {final_result:.50f}\n\n")
