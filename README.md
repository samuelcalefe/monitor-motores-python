# Monitoramento de Motores Industriais - v1.0.0
## Data/Hora da leitura: 26/11/2026 10:22:44

[ **NORMAL** ] MTR-01 _(Estamparia)_ | **Temp**: 68.4 C | **Corr**: 14.2 A | **Vib**: 2.1 mm/s | **RPM**: 1750

[ **CRÍTICO** ] MTR-02 _(Usinagem)_ | **Temp**: 84.7 C | **Corr**: 19.3 A | **Vib**: 5.2 mm/s | **RPM**: 1690
* **Alerta**: Superaquecimento _(84.7 C)_
* **Alerta**: Sobrecorrente _(19.3 A)_
* **Alerta**: Vibracao elevada _(5.2 mm/s)_

[ **ATENCAO** ] MTR-03 _(Bobinagem)_ | **Temp**: 76.3 C | **Corr**: 17.8 A | **Vib**: 4.7mm/s | **RPM**: 1520
* **Alerta**: Vibracao elevada _(4.7 mm/s)_

[ **NORMAL** ] MTR-04 _(Pintura)_ | **Temp**: 61.0 C | **Corr**: 11.5 A | **Vib**: 1.8 mm/s | **RPM**: 1780

---

### **Resumo:**
1. :thermometer: Temperatura Media: *72.58 C*
2. :light_bulb: Corrente Media: *15.7 A*
3. :high_voltage: Potencia Total: *31.5 KW*

---

### **Código:**
-[] Funcionando
-[] Possui erros

```
Trecho 1
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
```

> Quer descobrir como digitar emojis também? 
> Acesse esse S[repositório](https://github.com/ikatyang/emoji-cheat-sheet)!