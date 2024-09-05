# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
with open('dados.json', 'r') as file:
    dados = json.load(file)

valores_positivos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(valores_positivos)
maior_valor = max(valores_positivos)
media_mensal = sum(valores_positivos) / len(valores_positivos)
acima_media = len([valor for valor in valores_positivos if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:,.2f}")
print(f"Número de dias com faturamento acima da média: {acima_media}")