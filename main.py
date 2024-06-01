import pandas as pd
import random

# Load the Excel file
file_path = './table.xlsx'  # Replace with the correct file path
df = pd.read_excel(file_path, sheet_name='action')

# Função para verificar a resposta do usuário
def check_answer(user_input, rightRes, A, B, C, D):
    if user_input.lower() == 'a' and A == rightRes:
        print("\033[92mParabéns, você acertou!\033[0m")  # Texto verde
        return 1
    elif user_input.lower() == 'b' and B == rightRes:
        print("\033[92mParabéns, você acertou!\033[0m")  # Texto verde
        return 1
    elif user_input.lower() == 'c' and C == rightRes:
        print("\033[92mParabéns, você acertou!\033[0m")  # Texto verde
        return 1
    elif user_input.lower() == 'd' and D == rightRes:
        print("\033[92mParabéns, você acertou!\033[0m")  # Texto verde
        return 1
    else:
        print(f"\033[91mInfelizmente você errou. A resposta certa era: {rightRes}\033[0m")  # Texto vermelho
        return 0

corrects = 0
wrongs = 0

while True:
    quest = []
    questType = int
    questNumber = random.randint(0, 22)
    type_choice = random.choice(["problem", "implementation"])  # escolha aleatória de tipo
    rightRes = []
    res1 = []
    res2 = []
    res3 = []

    if type_choice == "problem":
        questType = 2  # coluna do problema
    else:
        questType = 4  # coluna da implementação

    questNumber = random.randint(0, 22)

    if type_choice == "problem":
        quest = f"Esse padrão enfrenta o seguinte problema: " + df.iloc[questNumber, questType] + ". Também está ligado ao seguinte princípio SOLID: " + df.iloc[questNumber, 5]
    else:
        quest = f"Esse padrão é implementado da seguinte maneira: " + df.iloc[questNumber, questType] + ". Também está ligado ao seguinte princípio SOLID: " + df.iloc[questNumber, 5]

    # Criando a resposta correta
    rightRes = df.iloc[questNumber, 0] + f'. Tipo ' + df.iloc[questNumber, 1]

    # Criando set de resposta, adicionando a resposta correta, crinando respostas falsas e embaralhando a lista de respostas
    responses = set()
    responses.add(rightRes)

    while len(responses) < 4:
        random_index = random.randint(0, 22)
        random_res = df.iloc[random_index, 0] + f'. Tipo ' + df.iloc[random_index, 1]
        if random_res != rightRes and random_res not in responses:
            responses.add(random_res)

    responses = list(responses)
    random.shuffle(responses)

    A, B, C, D = responses

    # Fazendo a pergunta
    print("\n")
    print(quest)
    print("\n Escolha a resposta correta: \n")
    print("A)", A)
    print("B)", B)
    print("C)", C)
    print("D)", D)

    # Salvando a resposta
    user_input = input("Digite a letra da sua resposta (A, B, C, D): ")

    # Verificando a resposta do usuário e atualizando contadoresb
    count = check_answer(user_input, rightRes, A, B, C, D)

    # Atualizando contadores de acertos/erros
    if count > 0:
        corrects = corrects + 1
    else:
        wrongs = wrongs + 1

    # Perguntar se deseja continuar
    continuar = input("Deseja continuar estudando? (S/N): ")
    if continuar.lower() == 'n':
        print(f"Você teve {corrects} acerto(s) e {wrongs} erro(s). Obrigado por estudar! Até mais!")
        break
