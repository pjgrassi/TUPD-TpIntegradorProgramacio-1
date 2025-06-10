import time

"""
Calculo de interes compuesto con bucle for
Este programa calcula el interés compuesto de una inversión inicial
con una tasa de interés anual y un número de años especificado.

La T(n) = 1 + 2n, donde n es el número de periodos.
Por lo tanto podemos decir que tiene una T(n) = O(n), es decir, lineal, lo que nos indica que el tiempo de ejecución aumenta linealmente con el número de periodos.
"""
def valorFuturoIterativo(principal, tasaInteres, periodos):
    inicio = time.time()
    valor = principal # 1 operación de asignación de valores
    for _ in range(periodos):
        valor *= (1 + tasaInteres) # 2 operación sumatoria y multiplicación
    fin = time.time()
    return valor, (fin - inicio) * 1000  # Retorna el valor final y el tiempo en milisegundos

"""
Calculo de interes compuesto con formula cerrada
VF = P * (1 + r)^n
Donde los valores son:
P = Capital inicial
r = Tasa de interes anual
n = Numero de periodos (años)
VF = Valor futuro de la inversion
La T(n) = 3, es decir, constante, lo que nos indica que el tiempo de ejecución no depende del número de periodos.
Por lo tanto podemos decir que tiene una T(n) = O(1), es decir, constante.
"""
def valorFuturoFormula(principal, tasaInteres, periodos):
    inicio = time.time()
    valor = principal * (1 + tasaInteres) ** periodos # 3 operaciones: 1 de multiplicación, 1 de suma y 1 de potencia
    fin = time.time()
    return valor, (fin - inicio) * 1000  # Retorna el valor final y el tiempo en milisegundos