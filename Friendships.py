#Lista de Usuarios representado por um dict que contem a chave id e name
users = [
    {"id":0, "name": "Hero"},
    {"id":1, "name": "Dunn"},
    {"id":2, "name": "Sue"},
    {"id":3, "name": "Chi"},
    {"id":4, "name": "Thor"},
    {"id":5, "name": "Clive"},
    {"id":6, "name": "Hicks"},
    {"id":7, "name": "Devin"},
    {"id":8, "name": "Kate"},
    {"id":9, "name": "Klein"}
]

#lista de amizades com os respectivos ids
friendship_pairs = [(0,1), (0,2), (1,2),(1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Criar um dict com a lista de ids dos amigos, onde a chave é o id
friendships = {user["id"]:[] for user in users}
print(friendships)

#Percorrer a lista de amizades e preencher o dicionario "para cada id os seus respectivos amigos"
for i, j in friendship_pairs:
    friendships[i].append(j) #adicionando j como amigo de i
    friendships[j].append(i) #adicionando i como amigo de j

print(friendships)
#Podemos perguntar qual o numero médio de conexoes?

#Para isso é necessario saber o numero total de conexoes - Vamos criar uma função para isso
def number_of_friends(user):
    """Quantos amigos tem o user?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

print(total_connections)
print(num_users)
print(avg_connections)
