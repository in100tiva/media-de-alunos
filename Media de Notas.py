
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, logic, python, sql):
        average = self.calculate_average(logic, python, sql)
        status = self.determine_status(average)
        self.students.append({
            "name": name,
            "grades": {"logic": logic, "python": python, "sql": sql},
            "average": average,
            "status": status
        })

    def calculate_average(self, logic, python, sql):
        return (logic + python + sql) / 3

    def determine_status(self, average):
        if average >= 7.0:
            return "Aprovado"
        elif average >= 5.0:
            return "De recuperação"
        else:
            return "Reprovado"

    def list_students(self):
        return self.students

def main():
    manager = StudentManager()
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Listar todos os alunos")
        print("3. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            name = input("Nome do aluno: ")
            logic = float(input("Nota de Lógica: "))
            python = float(input("Nota de Python: "))
            sql = float(input("Nota de SQL: "))
            manager.add_student(name, logic, python, sql)
            print(f"Aluno {name} adicionado com sucesso!")
        elif choice == '2':
            students = manager.list_students()
            if students:
                print("\nLista de Alunos:")
                for student in students:
                    print(f"{student['name']} - Média: {student['average']:.2f} - Status: {student['status']}")
            else:
                print("Nenhum aluno registrado.")
        elif choice == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
