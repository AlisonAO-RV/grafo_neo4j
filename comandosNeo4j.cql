-- Listar Todos os Nós
MATCH (n) RETURN n
-- Este comando retorna todos os nós no banco de dados.

-- Listar Todos os Nós de um Tipo Específico
MATCH (p:Person) RETURN p
-- Este comando retorna todos os nós do tipo Person.

-- Encontrar um Nó pelo ID
MATCH (p:Person) WHERE p.id = 'ID_especifico' RETURN p
-- Substitua 'ID_especifico' pelo ID real da pessoa que você deseja encontrar.

-- Visualizar Relações de Amizade
MATCH (p1:Person)-[:FRIEND_OF]->(p2:Person) RETURN p1, p2
-- Este comando mostra todos os pares de pessoas que têm uma relação FRIEND_OF.

-- Visualizar a Rede de Amizades de uma Pessoa Específica
MATCH (p:Person {id: 'ID_especifico'})-[:FRIEND_OF]->(friend) RETURN p, friend
-- Substitua 'ID_especifico' pelo ID da pessoa cuja rede de amizades você deseja visualizar.

-- Contar o Número de Amigos de uma Pessoa
MATCH (p:Person {id: 'ID_especifico'})-[:FRIEND_OF]->(friend) RETURN count(friend)
-- Substitua 'ID_especifico' pelo ID da pessoa para contar quantos amigos ela tem.

-- Remover um Nó e Suas Relações
MATCH (p:Person {id: 'ID_especifico'}) DETACH DELETE p
-- Substitua 'ID_especifico' pelo ID da pessoa que você deseja remover. DETACH DELETE remove o nó e todas as suas relações.

-- Listar Nós com Relações Específicas
MATCH (p:Person)-[r:FRIEND_OF]->() RETURN p, r
-- Este comando retorna todos os nós Person que têm uma relação FRIEND_OF.

-- Encontrar Caminhos Entre Duas Pessoas
MATCH path = (p1:Person {id: 'ID1'})-[*]-(p2:Person {id: 'ID2'}) RETURN path
-- Substitua 'ID1' e 'ID2' pelos IDs das pessoas entre as quais você deseja encontrar um caminho.

-- Atualizar Propriedades de um Nó
MATCH (p:Person {id: 'ID_especifico'}) SET p.name = 'novo_nome', p.age = nova_idade RETURN p
-- Substitua 'ID_especifico', 'novo_nome' e nova_idade conforme necessário para atualizar as propriedades de uma pessoa.
