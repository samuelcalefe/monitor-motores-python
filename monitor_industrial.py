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

    return status, alertas

# trecho 4
def calcular_estatisticas(motores):
    total = len(motores)
    if total == 0:
        return {}

    temp_media = sum(m["temperatura"] for m in motores) / total
    corrente_media = sum(m["corrente"] for m in motores) / total
    potencia_total = sum(m["potencia_kw"] for m in motores)
    maior_temp = max(motores, key=lambda m: m["temperatura"])

    return {
        "total_motores": total,
        "temperatura_media": round(temp_media, 2),
        "corrente_media": round(corrente_media, 2),
        "potencia_total_kw": round(potencia_total, 2),
        "motor_mais_quente": maior_temp["id"],
    }

# trecho 5
def exibir_painel(motores):
    print("=" * 64)
    print(f"{SISTEMA_NOME} - v{VERSAO}")
    print(f"Data/Hora da leitura: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 64)

    for motor in motores:
        status, alertas = analisar_alertas(motor)
        print(
            f"[{status:<7}] {motor['id']} ({motor['setor']}) | "
            f"Temp: {motor['temperatura']} C | Corr: {motor['corrente']} A | "
            f"Vib: {motor['vibracao']} mm/s | RPM: {motor['rpm']}"
        )
        for alerta in alertas:
            print(f"  -> Alerta: {alerta}")

    stats = calcular_estatisticas(motores)
    print("-" * 64)
    print(
        f"Resumo: {stats['total_motores']} motores | "
        f"Temp. media: {stats['temperatura_media']} C | "
        f"Corr. media: {stats['corrente_media']} A | "
        f"Potencia total: {stats['potencia_total_kw']} kW | "
        f"Maior temp.: {stats['motor_mais_quente']}"
    )
    print("=" * 64)


if __name__ == "__main__":
    motores_validos = obter_leituras_validas(LEITURAS_MOTORES)
    exibir_painel(motores_validos)