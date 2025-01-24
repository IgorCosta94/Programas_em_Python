def dia_da_semana(dia):
    switch = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    return switch.get(dia, "Dia inválido")  # Retorna "Dia inválido" se o valor não estiver no dicionário

# Exemplo de uso
print(dia_da_semana(3))  # Saída: Terça-feira
print(dia_da_semana(8))  # Saída: Dia inválido
