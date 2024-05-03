
class StudentManager:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os alunos
        self.students = []

    def add_student(self, name, logic, python, sql):
        # Calcula a média das três notas
        average = (logic + python + sql) / 3
        # Determina o status do aluno com base na média
        if average >= 7.0:
            status = "Aprovado"
        elif average >= 5.0:
            status = "De recuperação"
        else:
            status = "Reprovado"
        # Armazena as informações do aluno como uma tupla na lista de alunos
        self.students.append((name, average, status))

    def list_students(self):
        # Imprime todos os alunos com suas médias e status
        for student in self.students:
            name, average, status = student
            print(f"{name} - Média: {average:.2f} - Status: {status}")

def main():
    # Cria uma instância da classe StudentManager
    manager = StudentManager()
    # Loop principal do programa para interação do usuário
    while True:
        # Exibe o menu de opções para o usuário
        choice = input("\n1. Adicionar aluno\n2. Listar todos os alunos\n3. Sair\nEscolha uma opção: ")
        if choice == '1':
            # Solicita ao usuário as informações do aluno
            name = input("Nome do aluno: ")
            logic = float(input("Nota de Lógica: "))
            python = float(input("Nota de Python: "))
            sql = float(input("Nota de SQL: "))
            # Adiciona o aluno usando as informações fornecidas
            manager.add_student(name, logic, python, sql)
            print(f"Aluno {name} adicionado com sucesso!")
        elif choice == '2':
            # Lista todos os alunos registrados
            manager.list_students()
        elif choice == '3':
            # Encerra o programa
            print("Encerrando o programa.")
            break
        else:
            # Lida com a entrada inválida do usuário
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
