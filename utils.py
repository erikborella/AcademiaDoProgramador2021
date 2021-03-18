from datetime import date, timedelta

"""
Recebe uma data e retorna a diferença de dias até o dia atual
"""
def calcular_diferença_dias_data_atual(data: date) -> int:
    data_hoje = date.today()
    return (data_hoje - data).days