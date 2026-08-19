import random
import json

def salvar_personagens():
    with open("personagens.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            personagens,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def carregar_personagens():
    try:
        with open("personagens.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return {}


opcoes1 = ["Iniciar", "Criar Personagem", "Tutorial", "Excluir Personagem", "Sair"]

opcoes2 = [
    "Trabalhar",
    "Trabalhos",
    "Mineração",
    "Loja",
    "Cassino",
    "Inventário",
    "Crime",
    "Fiança/Limpar Ficha",
    "Sair"
]

armazem = {
    "Picareta": {
        "preco": 10,
        "durabilidade": 10,
        "tipo": "picareta",
        "nivel": 1,
        "ganho_min": 10,
        "ganho_max": 30
    },

    "Picareta de Pedra": {
        "preco": 100,
        "durabilidade": 20,
        "tipo": "picareta",
        "nivel": 2,
        "ganho_min": 80,
        "ganho_max": 120
    },

    "Picareta de Ferro": {
        "preco": 300,
        "durabilidade": 60,
        "tipo": "picareta",
        "nivel": 3,
        "ganho_min": 150,
        "ganho_max": 210
    },

    "Picareta do Serviço Secreto": {
        "preco": 900000000,
        "durabilidade": 900,
        "tipo": "picareta",
        "nivel": 1000,
        "ganho_min": 5000000,
        "ganho_max": 900000000
    }
}

trabalhos = {
    "Gari": {
        "salario": 90,
        "chance": 90
    },

    "Caixa": {
        "salario": 95,
        "chance": 80
    },

    "Professor": {
        "salario": 115,
        "chance": 65
    },

    "Mecânico": {
        "salario": 127,
        "chance": 55
    },

    "Programador": {
        "salario": 150,
        "chance": 50
    },
 
       
    "Médico": {
        "salario": 200,
        "chance": 48
    },
    
    
    "Engenheiro": {
        "salario": 200,
        "chance": 48
    },


    "Presidente": {
        "salario": 500,
        "chance": 12
    }
}

jackpots = {
    "🍓": 300,
    "🍒": 500,
    "🍎": 700,
    "🍅": 900,
    "🌶️": 1100,
    "🍉": 1500,
    "💎": 2000
}

personagens = carregar_personagens()


def criar_personagem(personagens):
    nome = input("Por favor, escolha o nome do seu personagem: ")
    if nome in personagens:
        print("Já existe um personagem com esse nome!")
        return
    
    jogador = {
        "nome": nome,
        "dinheiro": 50,
        "xp": 0,
        "nivel": 1,
        "trabalho": None,
        "inventario": {},
        "ficha_criminal": 0
    }

    personagens[nome] = jogador
    
    salvar_personagens()
    
    return jogador


def iniciar():
    if not personagens:
        print("Nenhum personagem criado!")
        return

    while True:
        print("\n=== PERSONAGENS ===")
        
        print("0 - Cancelar")
        for numero, personagem in enumerate(personagens, start=1):
            print(f"{numero} - {personagem}")

        try:
            escolha = int(
                input(
                    f"Por favor, escolha um personagem "
                    f"(0-{len(personagens)}): "
                )
            )

        except ValueError:
            print("Opção inválida! Digite apenas números!")
            continue

        if escolha < 0 or escolha > len(personagens):
            print("Opção inválida, tente novamente.")
            continue
        if escolha == 0:
        	print("Cancelando...")
        	break

        nomes = list(personagens)

        nome_escolhido = nomes[escolha - 1]

        personagem_escolhido = personagens[nome_escolhido]

        print(f"\nVocê escolheu {nome_escolhido}!")

        menu_jogo(personagem_escolhido)

        return


def menu_jogo(personagem):
    while True:
        print(f"\n======== {personagem['nome']} ========")

        for numero, opcao in enumerate(opcoes2, start=1):
            print(f"{numero} - {opcao}")

        try:
            escolha = int(
                input(
                    f"Escolha uma opção "
                    f"(1-{len(opcoes2)}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(opcoes2):
            print("Opção inválida!")
            continue
        
        if escolha == 1:
            trabalhar(personagem)
            
        elif escolha == 2:
        	escolher_trabalho(personagem)
        	
        elif escolha == 3:
        	mineracao(personagem)
        	
        elif escolha == 4:
        	loja(personagem)
        	
        elif escolha == 5:
        	cassino(personagem)
        
        elif escolha == 6:
        	inventario(personagem)
        	
        elif escolha == 7:
        	crime(personagem)
        	
        elif escolha == 8:
        	limpar_ficha(personagem)
        
        elif escolha == 9:
        	print("Saindo...\nAté logo!")
        	break


def inventario(personagem):
    if not personagem["inventario"]:
        print(f"{personagem['nome']} está com o inventário vazio!")
        return

    print(f"\nInventário de {personagem['nome']}:")

    for item, dados in personagem["inventario"].items():

        if dados.get("tipo") == "picareta":
            durabilidade_maxima = armazem[item]["durabilidade"]

            print(
                f"{item} | Durabilidade: "
                f"{dados['durabilidade']}/{durabilidade_maxima}"
            )

        else:
            print(
                f"{item} - Quantidade: "
                f"{dados['quantidade']}"
            )
    
def loja(personagem):
    while True:
        print("\n======== LOJA ========")
        print(f"Dinheiro: R$ {personagem['dinheiro']}")

        itens = list(armazem)

        for numero, item in enumerate(itens, start=1):
            preco = armazem[item]["preco"]
            print(f"{numero} - {item} | R$ {preco}")

        print(f"{len(itens) + 1} - Sair")

        try:
            escolha = int(
                input(
                    f"Escolha um item "
                    f"(1-{len(itens) + 1}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(itens) + 1:
            print("Opção inválida!")
            continue

        if escolha == len(itens) + 1:
            break

        item_escolhido = itens[escolha - 1]
        preco = armazem[item_escolhido]["preco"]

        if item_escolhido in personagem["inventario"]:
            print(f"Você já possui {item_escolhido}!")
            continue

        if personagem["dinheiro"] >= preco:
            personagem["dinheiro"] -= preco

            personagem["inventario"][item_escolhido] = (
        armazem[item_escolhido].copy()
    )

            personagem["inventario"][item_escolhido].pop("preco")
            
            salvar_personagens()
            
            print(f"Você comprou {item_escolhido}!")

        else:
            print("Dinheiro insuficiente!")



def mineracao(personagem):
    picareta_usada = None
    maior_nivel = -1

    for item in personagem["inventario"]:
        if item in armazem:
            if armazem[item]["tipo"] == "picareta":

                nivel = armazem[item]["nivel"]

                if nivel > maior_nivel:
                    maior_nivel = nivel
                    picareta_usada = item

    if picareta_usada is None:
        print("Você precisa de uma picareta para minerar!")
        return

    chance = random.randint(1, 100)

    if chance <= 46:
        dados_picareta = armazem[picareta_usada]

        ganho = random.randint(
            dados_picareta["ganho_min"],
            dados_picareta["ganho_max"]
        )

        personagem["dinheiro"] += ganho

        if ganho <= 100:
            print(
                f"Você minerou e teve a sorte de ganhar R${ganho}!\n"
                f"Hora de gastar!!"
            )

        elif ganho <= 200:
            print(
                f"UAU! Você minerou e ganhou R${ganho}! "
                f"Será você o barão do ouro?!"
            )

        else:
            print(
                f"PARABÉNS!! VOCÊ GANHOU R${ganho}!!!!!!! "
                f"Você está cada vez mais próximo da riqueza!!!"
            )

    elif chance <= 90:
        print("Você minerou... E não conseguiu nada... Que azar.")

    else:
        print(
            "Você minerou e conseguiu uma peça de ouro de 5KG "
            "avaliada em 1 MILHÃO DE REAIS!!!\n"
            "Mas um elfo maldito estava vendo tudo e te roubou..."
        )

    personagem["inventario"][picareta_usada]["durabilidade"] -= 1

    if personagem["inventario"][picareta_usada]["durabilidade"] <= 0:
        del personagem["inventario"][picareta_usada]
        print(f"Sua {picareta_usada} quebrou!")

    salvar_personagens()
    		


def escolher_trabalho(personagem):
    while True:
        print("\n======== TRABALHOS ========")

        nomes_trabalhos = list(trabalhos)

        for numero, trabalho in enumerate(nomes_trabalhos, start=1):
            salario = trabalhos[trabalho]["salario"]
            print(f"{numero} - {trabalho} | R$ {salario}")

        print(f"{len(nomes_trabalhos) + 1} - Sair")
        
        try:
            escolha = int(
        input(
            f"Escolha um trabalho "
            f"(1-{len(nomes_trabalhos) + 1}): "
        )
    )

        except ValueError:
            print("Digite apenas números!")
            continue
        
        if escolha < 1 or escolha > len(nomes_trabalhos) + 1:
            print("Opção inválida!")
            continue
           
        if escolha == len(nomes_trabalhos) + 1:
            break
            
        trabalho_escolhido = nomes_trabalhos[escolha - 1]
        
        chance_emprego = trabalhos[trabalho_escolhido]["chance"]
        penalidade = personagem["ficha_criminal"] * 10
        chance_final = chance_emprego - penalidade
        if chance_final < 0:
            chance_final = 0
        sorteio = random.randint(1, 100)
        
        if sorteio <= chance_final:
            personagem["trabalho"] = trabalho_escolhido
            
            salvar_personagens()
            
            print(f"Parabéns! Você conseguiu o emprego de {trabalho_escolhido}!")

        else:
            print(f"Agradecemos o seu interesse na vaga de {trabalho_escolhido}. Entraremos em contato em até 5 dias úteis.")



def trabalhar(personagem):
    if not personagem["trabalho"]:
        print(
            "Você precisa de um trabalho para poder trabalhar! "
            "Hora de distribuir currículos por aí..."
        )
        return

    trabalho_atual = personagem["trabalho"]

    salario = trabalhos[trabalho_atual]["salario"]

    personagem["dinheiro"] += salario
    
    salvar_personagens()
    
    print(
        f"Você trabalhou como {trabalho_atual} "
        f"e recebeu R${salario}!"
    )


def crime(personagem):
	chance = random.randint(1, 100)
	if chance <= 34:
		ganho = random.randint(10, 700)
		personagem["dinheiro"] += ganho
		
		salvar_personagens()
		
		if ganho <= 100:
			print(f"Você roubou senhorinhas na rua e ganhou R${ganho}! Que sem coração...")
		elif ganho <= 300:
			print(f"Você subiu no crime e vendeu substâncias ilícitas. Você ganhou {ganho}!")
		elif ganho <= 600:
			print(f"Você começou a roubar bancos e ganhou {ganho}! Cuidado, nessa vida, quanto maior o degrau, maior a queda...")
		else:
			print(f"Você virou o chefão da zorra toda! Seu nome é Carl Jhonson e você tá milionário! {ganho} pila estourando no bolso!")
	elif chance <= 67:
		print("Você ia roubar uma senhoria que estava atravessando a rua, mas uma mulher começou a gritar. Você saiu correndo, tropeçou e conseguiu fugir. A única coisa que você perdeu foi sua dignidade.")
	else:
		print("Você foi pego tentando roubar. As pessoas em volta te bateram e você foi preso e perdeu tudo o que você tinha antes. Boa sorte tentando arrumar emprego!")
		personagem["dinheiro"] = 0
		personagem["ficha_criminal"] += 1
		salvar_personagens()



def limpar_ficha(personagem):
    if personagem["ficha_criminal"] == 0:
        print("Você é um cidadão honesto, não tem ficha pra limpar!")

    else:
        if personagem["dinheiro"] < 500:
            print(
                f"Tá liso dorme fi. Precisa de R$500 pra limpar a ficha, "
                f"aparentemente você só tem R${personagem['dinheiro']}"
            )

        else:
            personagem["ficha_criminal"] = 0
            personagem["dinheiro"] -= 500
            
            salvar_personagens()
            
            print("Você gastou R$500 para limpar sua ficha criminal!")
            print(
                "Agora que você tem a ficha limpa, talvez eles leiam "
                "seu currículo ao invés de só jogar fora..."
            )
	


def cassino(personagem):
    custo = 50

    if personagem["dinheiro"] < custo:
        print(
            "Pelo visto alguém tá liso e não tem "
            "R$50 pra jogar no cassino KKKKKKKKKKK"
        )
        return

    personagem["dinheiro"] -= custo

    simbolos = list(jackpots)

    slot1 = random.choice(simbolos)
    slot2 = random.choice(simbolos)
    slot3 = random.choice(simbolos)

    print(f"\n🎰 [ {slot1} ] [ {slot2} ] [ {slot3} ] 🎰")

    if slot1 == slot2 == slot3:
        premio = jackpots[slot1]
        personagem["dinheiro"] += premio
        
        salvar_personagens()
        
        if slot1 == "🍓":
            print(
                f"É, até que você é sortudinho(a)... "
                f"R${premio} na conta."
            )

        elif slot1 == "🍒":
            print(
                f"Olha só! Parabéns, nunca vi ninguém "
                f"ganhar R${premio} fácil assim!"
            )

        elif slot1 == "🍎":
            print(
                f"Três iguais?! Você só pode ser um mago "
                f"ou algo assim! +R${premio}"
            )

        elif slot1 == "🍅":
            print(
                f"UM TOMATE?! KKKKKKKKK "
                f"Seja lá como isso vale dinheiro, +R${premio}!"
            )

        elif slot1 == "🌶️":
            print(
                f"UAU! Você pode ficar sem trabalhar o resto "
                f"da semana! R${premio} entrando na conta!"
            )

        elif slot1 == "🍉":
            print(
                f"VOCÊ É MUITO SORTUDO! "
                f"Toma aí seus R${premio}!!!"
            )

        elif slot1 == "💎":
            print(
                "JAAACKPOOOOOOT HAHAHAHA!!!\n"
                "AUMENTE O VOLUME, ISSO VAI SER UM FUNERAL "
                "PARA OS VIVOS!!!\n"
                f"+R${premio}"
            )

    else:
        
        salvar_personagens()
        
        print(
            "É... parece que não foi dessa vez... "
            "Mas tenta de novo, tenho certeza que na próxima "
            "você consegue..."
        )
        
        

def excluir():
    if not personagens:
        print("Nenhum personagem criado!")
        return

    while True:
        print("\n=== PERSONAGENS ===")
        
        print("0 - Cancelar")
        for numero, nome in enumerate(personagens, start=1):
            print(f"{numero} - {nome}")

        try:
            escolha = int(
                input(
                    f"Por favor, escolha o personagem que deseja excluir "
                    f"(0-{len(personagens)}): "
                )
            )

        except ValueError:
            print("Opção inválida! Digite apenas números!")
            continue

        if escolha < 0 or escolha > len(personagens):
            print("Opção inválida, tente novamente.")
            continue
        
        if escolha == 0:
        	print("Cancelando...")
        	break
        nomes = list(personagens)

        nome_escolhido = nomes[escolha - 1]

        del personagens[nome_escolhido]

        salvar_personagens()

        print(f'Personagem "{nome_escolhido}" excluído com sucesso!')
        return
        
while True:
    print("====================")
    print("     RPG Python     ")
    print("====================")

    for numero, opcao in enumerate(opcoes1, start=1):
        print(f"{numero} - {opcao}")

    try:
        escolha = int(
            input(
                f"Por favor, escolha uma opção "
                f"(1-{len(opcoes1)}): "
            )
        )

    except ValueError:
        print("Opção inválida! Digite apenas números!")
        continue

    if escolha < 1 or escolha > len(opcoes1):
        print("Opção inválida, tente novamente.")
        continue

    if escolha == 1:
        iniciar()

    elif escolha == 2:
        criar_personagem(personagens)

    elif escolha == 3:
        print("Tutorial ainda não implementado!")
        
    elif escolha == 4:
    	excluir()

    elif escolha == len(opcoes1):
        print("Saindo...")
        break
