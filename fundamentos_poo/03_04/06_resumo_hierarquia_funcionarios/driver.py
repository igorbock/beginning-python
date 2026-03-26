# Neste desafio, você implementará um sistema de hierarquia de funcionários.

# Você precisará completar os seguintes arquivos:

# person.py: Implemente a classe base Person com name, age e introduction method
# employee.py: Crie a classe Employee herdando de Person com employee_id e salary
# manager.py: Implemente a classe Manager estendendo Employee com gerenciamento de departamento
# engineer.py: Construa a classe Engineer estendendo Employee com habilidades de programação
# technical_manager.py: Crie TechnicalManager usando herança múltipla
# hierarchy_utils.py: Implemente função utilitária para exibir hierarquias de classes
# Cada arquivo contém comentários TODO detalhados que o guiam através da implementação.

from person import Person
from employee import Employee
from manager import Manager
from engineer import Engineer
from technical_manager import TechnicalManager
from hierarchy_utils import show_hierarchy

# Test your implementation - DO NOT MODIFY THIS TEST CODE
# Create instances
person = Person("John Smith", 30)
employee = Employee("Alice Johnson", 35, "E12345", 60000)
manager = Manager("Bob Williams", 45, "M54321", 85000, "Marketing")
engineer = Engineer("Carol Davis", 28, "E98765", 75000, "Python")
tech_mgr = TechnicalManager("Dave Wilson", 40, "TM24680", 90000, "R&D", "Java")

# Test basic methods
print(person.introduce())
print(employee.introduce())
print(f"Monthly pay: ${employee.calculate_paycheck():.2f}")
print(manager.manage_team())
print(engineer.code())

# Test inheritance hierarchies
print("\nHierarchy demonstrations:")
show_hierarchy(TechnicalManager)

# Test method resolution in multiple inheritance
print("\nTechnical Manager tests:")
print(tech_mgr.introduce())
print(f"Monthly pay: ${tech_mgr.calculate_paycheck():.2f}")
print(tech_mgr.manage_team())
print(tech_mgr.code())