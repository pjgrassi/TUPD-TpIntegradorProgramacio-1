from interesCompuesto import valorFuturoFormula
"""
Ejemplo de uso:
Para simular el análisis de el algoritmo, generamos una lista con valores aleatorios.
Los datos de la inversion se asemejaran a una inversión de el plazo establecido.
El resultado serán el valor final de la inversión y el tiempo que tardó en calcularlo, para cada iteración.
"""
valoresIniciales = [642226.93, 760322.26, 104757.69, 399684.60, 395746.39, 740615.86, 959015.46, 854345.91, 725954.37, 165218.05]  # Valores iniciales de ejemplo

for i in (valoresIniciales):
    principal = i  # Inversión inicial de la lista
    tasaInteres = 0.75   # Tasa de interés fija del 75%
    periodos = 30 # Periodos fijos de 30 años

    # Calcular el valor futuro
    valorFinal, tiempo = valorFuturoFormula(principal, tasaInteres, periodos)

    # Mostrar resultados
    print(f"{tasaInteres * 100};{periodos};{principal:.2f};{valorFinal:.2f};{tiempo}")
    

