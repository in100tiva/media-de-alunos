
class Student:
    def __init__(self, name, logic, python, sql):
        self.name = name
        self.grades = {'logic': logic, 'python': python, 'sql': sql}
        self.average = self.calculate_average()
        self.status = self.determine_status()

    def calculate_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def determine_status(self):
        if self.average >= 7.0:
            return "Aprovado"
        elif self.average >= 5.0:
            return "De recuperação"
        else:
            return "Reprovado"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, logic, python, sql):
        student = Student(name, logic, python, sql)
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(f"{student.name} - Média: {student.average:.2f} - Status: {student.status}")

def main():
    manager = StudentManager()
    while True:
        choice = input("\n1. Adicionar aluno\n2. Listar todos os alunos\n3. Sair\nEscolha uma opção: ")
        if choice == '1':
            name = input("Nome do aluno: ")
            logic = float(input("Nota de Lógica: "))
            python = float(input("Nota de Python: "))
            sql = float(input("Nota de SQL: "))
            manager.add_student(name, logic, python, sql)
            print(f"Aluno {name} adicionado com sucesso!")
        elif choice == '2':
            manager.list_students()
        elif choice == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
