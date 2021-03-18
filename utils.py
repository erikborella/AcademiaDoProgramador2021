from datetime import date, timedelta

"""
Recebe uma data e retorna a diferença de dias até o dia atual
"""
def calcular_diferença_dias_data_atual(data: date) -> int:
    data_hoje = date.today()
    return (data_hoje - data).days


"""
    Recebe uma string no formato dd/mm/yyyy e retorna um objeto date com a data
""" 
def converter_data_str_para_date(data_str: str) -> date:
    datas_separadas = data_str.split('/')
    return date(
        int(datas_separadas[2]), 
        int(datas_separadas[1]), 
        int(datas_separadas[0])
        )