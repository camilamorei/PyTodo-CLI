import os

def carregar_dados():
    """Lê o arquivo de texto e retorna uma lista de tarefas."""
    tarefas = []
    if os.path.exists("tarefas.txt"):
        with open("tarefas.txt", "r", encoding="utf-8") as f:
            tarefas = [linha.strip() for linha in f.readlines()]
    return tarefas

def salvar_dados(tarefas):
    """Grava a lista de tarefas atualizada no arquivo de texto."""
    with open("tarefas.txt", "w", encoding="utf-8") as f:
        for item in tarefas:
            f.write(f"{item}\n")

def menu():
    """Exibe o painel visual no terminal."""
    print("\n" + "="*30)
    print("      GESTOR DE TAREFAS      ")
    print("="*30)
    print(" [1] Visualizar tarefas")
    print(" [2] Adicionar nova")
    print(" [3] Remover concluída")
    print(" [4] Sair")
    print("="*30)

def main():
    tarefas = carregar_dados()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n📋 LISTA DE TAREFAS:")
            if not tarefas:
                print(" -> Nenhuma tarefa pendente.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f" {i}. {tarefa}")

        elif opcao == "2":
            nova = input("\n✍️  Digite a tarefa: ").strip()
            if nova:
                tarefas.append(nova)
                salvar_dados(tarefas)
                print(" ✅ Tarefa salva!")
            else:
                print(" ❌ Erro: A tarefa não pode estar vazia.")

        elif opcao == "3":
            if not tarefas:
                print("\n ⚠️ Não há nada para remover.")
                continue
            
            try:
                num = int(input("\n🗑️  Digite o número para remover: "))
                removida = tarefas.pop(num - 1)
                salvar_dados(tarefas)
                print(f" 🗑️  '{removida}' removida!")
            except (ValueError, IndexError):
                print(" ❌ Erro: Digite um número válido da lista.")

        elif opcao == "4":
            print("\n👋 Saindo... Bons estudos!")
            break
        else:
            print("\n ❌ Opção inválida! Tente de 1 a 4.")

if __name__ == "__main__":
    main()