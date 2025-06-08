import time

"""
Calculo de interes compuesto con bucle for
Este programa calcula el interés compuesto de una inversión inicial
con una tasa de interés anual y un número de años especificado.

"""
def valorFuturoIterativo(principal, tasaInteres, periodos):
    inicio = time.time()
    valor = principal
    for _ in range(periodos):
        valor *= (1 + tasaInteres)
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
"""
def valorFuturoFormula(principal, tasaInteres, periodos):
    inicio = time.time()
    valor = principal * (1 + tasaInteres) ** periodos
    fin = time.time()
    return valor, (fin - inicio) * 1000  # Retorna el valor final y el tiempo en milisegundos