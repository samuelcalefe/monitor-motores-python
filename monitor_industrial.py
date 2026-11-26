# trecho 1
from datetime import datetime

SISTEMA_NOME = "Monitoramento de Motores Industriais"
VERSAO = "1.0.0"

LIMITES = {
    "temperatura_max": 80.0,
    "corrente_max": 18.5,
    "vibracao_max": 4.5,
    "rpm_min": 1400,
    "rpm_max": 1800,
}

LEITURAS_MOTORES = [
    {"id": "MTR-01", "setor": "Estamparia", "temperatura": 68.4, "corrente": 14.2, "vibracao": 2.1, "rpm": 1750, "potencia_kw": 7.5},
    {"id": "MTR-02", "setor": "Usinagem", "temperatura": 84.7, "corrente": 19.3, "vibracao": 5.2, "rpm": 1690, "potencia_kw": 11.0},
    {"id": "MTR-03", "setor": "Bobinagem", "temperatura": 76.2, "corrente": 17.8, "vibracao": 4.7, "rpm": 1520, "potencia_kw": 5.5},
    {"id": "MTR-04", "setor": "Pintura", "temperatura": 61.0, "corrente": 11.5, "vibracao": 1.8, "rpm": 1780, "potencia_kw": 7.5},
]

# trecho 2
def validar_leitura(motor):
    campos_obrigatorios = ["id", "setor", "temperatura", "corrente", "vibracao", "rpm", "potencia_kw"]
    for campo in campos_obrigatorios:
        if campo not in motor or motor[campo] is None:
            return False
    if motor["temperatura"] < 0 or motor["corrente"] < 0 or motor["vibracao"] < 0 or motor["rpm"] < 0:
        return False
    return True


def obter_leituras_validas(lista_motores):
    return [m for m in lista_motores if validar_leitura(m)]

# trecho 3
def analisar_alertas(motor):
    alertas = []
    if motor["temperatura"] > LIMITES["temperatura_max"]:
        alertas.append(f"Superaquecimento ({motor['temperatura']:.1f} C)")
    if motor["corrente"] > LIMITES["corrente_max"]:
        alertas.append(f"Sobrecorrente ({motor['corrente']:.1f} A)")
    if motor["vibracao"] > LIMITES["vibracao_max"]:
        alertas.append(f"Vibracao elevada ({motor['vibracao']:.1f} mm/s)")
    if motor["rpm"] < LIMITES["rpm_min"] or motor["rpm"] > LIMITES["rpm_max"]:
        alertas.append(f"Rotacao fora da faixa ({motor['rpm']} RPM)")

    if len(alertas) == 0:
        status = "NORMAL"
    elif len(alertas) == 1:
        status = "ATENCAO"
    else:
        status = "CRITICO"

    return status, alertasS