from neo4j import GraphDatabase
import uuid

uri = "neo4j://localhost:7687"  # ou o endereço do seu Docker container
username = "neo4j"
password = "redesocial"

driver = GraphDatabase.driver(uri, auth=(username, password))


def menu():
    while True:
        print("\nMenu da Rede Social")
        print("1. Adicionar nova pessoa")
        print("2. Listar todas as pessoas")
        print("3. Adicionar relação de amizade")
        print("4. Visualizar rede de amizades de uma pessoa")
        print("5. Remover pessoa")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome: ")
            age = input("Digite a idade: ")
            location = input("Digite a localização: ")
            add_person(name, age, location)
        elif choice == '2':
            list_people()
        elif choice == '3':
            person_id1 = input("Digite o ID da primeira pessoa: ")
            person_id2 = input("Digite o ID da segunda pessoa: ")
            add_friendship(person_id1, person_id2)
        elif choice == '4':
            person_id = input("Digite o ID da pessoa: ")
            view_friends(person_id)
        elif choice == '5':
            person_id = input("Digite o ID da pessoa a ser removida: ")
            remove_person(person_id)
        elif choice == '6':
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


def add_person(name, age, location):
    unique_id = str(uuid.uuid4())  # Gera um UUID em Python
    with driver.session() as session:
        session.run("CREATE (p:Person {id: $id, name: $name, age: $age, location: $location})",
                    id=unique_id, name=name, age=age, location=location)


def list_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.id, p.name")
        for record in result:
            print(f"ID: {record['p.id']}, Nome: {record['p.name']}")


def add_friendship(person_id1, person_id2):
    with driver.session() as session:
        session.run("MATCH (p1:Person {id: $id1}), (p2:Person {id: $id2}) "
                    "CREATE (p1)-[:FRIEND_OF]->(p2)",
                    id1=person_id1, id2=person_id2)


def view_friends(person_id):
    with driver.session() as session:
        result = session.run("MATCH (p:Person)-[:FRIEND_OF]->(friend) WHERE p.id = $id "
                             "RETURN friend", id=person_id)
        for record in result:
            print(record["friend"])


def remove_person(person_id):
    with driver.session() as session:
        session.run("MATCH (p:Person) WHERE p.id = $id DELETE p", id=person_id)


menu()
