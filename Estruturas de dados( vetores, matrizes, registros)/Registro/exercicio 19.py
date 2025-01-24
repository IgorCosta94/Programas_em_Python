from dataclasses import dataclass
@dataclass
class pesquisa:
    idade: int
    frequencia: int
    avaliacao: int
    melhoria: str

result = [0] * 10

cont_18 = 0
cont_65 = 0
cont_70 = 0

cont_E = 0
cont_B = 0
cont_M = 0

for w in range(10):
    idade = int(input("Qual a idade: "))
    frequencia = int(input("Qual a frequencia de visita ao shopping (1 - diária, 2 - semanal, 3 - eventual): "))
    avaliacao = int(input("Qual sua avaliação do shopping (1 - Excelente, 2 - Boa, 3 - Precisa Melhorar):  "))

    if avaliacao == 3:
        melhoria = input("Qual sua sugestão de melhoria? ")
        result[w] = pesquisa(idade, frequencia, avaliacao, melhoria )
    else:
        result[w] = pesquisa(idade, frequencia, avaliacao,'')


for w in range(10):

    if result[w].idade < 18:
        cont_18 += 1
    elif result[w].idade >= 18 and result[w].idade <= 65:
        cont_65 += 1
    elif result[w].idade > 65:
        cont_70 += 1

    if result[w].avaliacao == 1:
        cont_E += 1
    elif result[w].avaliacao == 2:
        cont_B += 1
    elif result[w].avaliacao == 3:
        cont_M += 1

porcentagem_18 = (cont_18 * 100) / 10
porcentagem_65 = (cont_65 * 100) / 10
porcentagem_70 = (cont_70 * 100) / 10

porcentagem_E = (cont_E * 100) / 10
porcentagem_B = (cont_B * 100) / 10
porcentagem_M = (cont_M * 100) / 10

print()

print("  ==================================================\n"
      "|| Porcentagem dos entrevistados por faixa etária   ||\n"
     f"|| Menores de 18 anos:             {porcentagem_18}             ||\n"
     f"|| Maiores de 18 anos até 65 anos: {porcentagem_65}             ||\n"
     f"|| Maiores de 65 anos:             {porcentagem_70}             ||\n"
      "  ==================================================\n")

print()

print("  =========================================\n"
      "|| Porcentagem das avaliações              ||\n"
     f"|| Excelentes:             {porcentagem_E}            ||\n"
     f"|| Boa:                    {porcentagem_B}            ||\n"
     f"|| Precisa melhorar:       {porcentagem_M}            ||\n"
      "  =========================================\n")

print()

print("  ========================================================\n"
      "||        Listagem com sugestões de melhorias             ||")
for w in range(10):
    if result[w].frequencia == 1:
        print(f"||  Sugestão de melhoria: {result[w].melhoria}\n"
              f"||  Idade:                {result[w].idade}\n"
              f"||  Frequencia:           {result[w].frequencia}\n")
    elif result[w].frequencia == 2:
        print(f"||  Sugestão de melhoria: {result[w].melhoria}\n"
              f"||  Idade:                {result[w].idade}\n"
              f"||  Frequencia:           {result[w].frequencia}\n")
    elif result[w].frequencia == 3:
        print(f"||  Sugestão de melhoria: {result[w].melhoria}\n"
              f"||  Idade:                {result[w].idade}\n"
              f"||  Frequencia:           {result[w].frequencia}")
print("  =========================================================")

