# Disciplina: Introdução a Programação

# Componentes: Letícia Gabriela, Cecília, Mariana, Tyfany, Ana Beatriz.

# Lista para armazenar os pacientes
pacientes = []

def menu():
    """Exibe o menu e executa a opção escolhida pelo usuário."""
    while True:  # Mantém o menu rodando até que o usuário escolha sair.
        print("\n MENU ")
        print("1. Cadastrar Paciente")
        print("2. Consultar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Apagar Paciente")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")  # Usuário escolhe uma opção.
        
        # Verifica qual opção foi escolhida e chama a função correspondente.
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            apagar()
        elif opcao == "5":
            print("Saindo do programa...")
            break  # Encerra o loop e finaliza o programa.
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar():
    """Cadastra um novo paciente na lista."""
    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    
    paciente = [nome, idade, telefone]  # Cria uma lista com os dados do paciente.
    pacientes.append(paciente)  # Adiciona o paciente à lista principal.
    print("Paciente cadastrado com sucesso!")

def consultar():
    """Exibe a lista de pacientes cadastrados."""
    if len(pacientes) > 0:  # Verifica se há pacientes cadastrados.
        print("\n Lista de Pacientes ")
        for i in range(len(pacientes)):  # Percorre a lista de pacientes.
            p = pacientes[i]  # Obtém os dados do paciente na posição i.
            print(f"{i+1}. Nome: {p[0]}, Idade: {p[1]}, Telefone: {p[2]}")  
            # Mostra os dados do paciente formatados corretamente.
    else:
        print("Nenhum paciente cadastrado.")

def atualizar():
    """Atualiza os dados de um paciente existente."""
    consultar()  # Exibe a lista para que o usuário veja os pacientes.
    
    if len(pacientes) == 0:  # Se não houver pacientes, sai da função.
        return
    
    i = int(input("Digite o número do paciente a ser atualizado: ")) - 1  
    # O usuário escolhe o número do paciente na lista, mas precisamos subtrair 1
    # pois os índices da lista começam em 0.

    if 0 <= i < len(pacientes):  # Verifica se o número inserido é válido.
        nome = input("Novo nome: ")
        idade = input("Nova idade: ")
        telefone = input("Novo telefone: ")
        
        pacientes[i] = [nome, idade, telefone]  # Atualiza os dados do paciente.
        print("Paciente atualizado com sucesso!")
    else:
        print("Número inválido. Paciente não encontrado.")

def apagar():
    """Remove um paciente da lista sem usar pop()."""
    consultar()  # Exibe a lista para que o usuário veja os pacientes.
    
    if len(pacientes) == 0:  # Se não houver pacientes, sai da função.
        return
    
    i = int(input("Digite o número do paciente a ser removido: ")) - 1  
    # O usuário escolhe o número do paciente na lista, mas precisamos subtrair 1
    # para obter o índice correto.

    if 0 <= i < len(pacientes):  # Verifica se o índice é válido.
        pacientes[i] = []  # Esvazia os dados do paciente, mas deixa um espaço vazio na lista.
        print("Paciente removido!")
    else:
        print("Número inválido. Paciente não encontrado.")

menu()  # Inicia o programa.