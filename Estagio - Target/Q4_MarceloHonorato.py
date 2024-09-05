# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sum([sp,rj,mg,es,outros])

percent_sp = (sp/total)*100
percent_rj = (rj/total)*100
percent_mg = (mg/total)*100
percent_es = (es/total)*100
percent_outros = (outros/total)*100

print(f"Percentual de representacao de faturamento de Sao Paulo: {percent_sp:.2f}% do valor total mensal da distribuidora")
print(f"Percentual de representacao de faturamento de Rio de Janeiro: {percent_rj:.2f}% do valor total mensal da distribuidora")
print(f"Percentual de representacao de faturamento de Minas Gerais: {percent_mg:.2f}% do valor total mensal da distribuidora")
print(f"Percentual de representacao de faturamento de Espirito Santo: {percent_es:.2f}% do valor total mensal da distribuidora")
print(f"Percentual de representacao de faturamento dos outros estados Brasileiros: {percent_outros:.2f}% do valor total mensal da distribuidora")

