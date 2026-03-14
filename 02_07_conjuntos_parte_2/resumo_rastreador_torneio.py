# Em um torneio de jogos competitivos, os jogadores participam de diferentes partidas. 
# Sua tarefa é analisar a participação dos jogadores em três partidas usando conjuntos Python.

# Serão fornecidos três conjuntos de jogadores:

# match1: Jogadores que participaram da Partida 1
# match2: Jogadores que participaram da Partida 2
# match3: Jogadores que participaram da Partida 3
# Sua tarefa é:

# Encontrar jogadores que participaram de todas as três partidas
# Identificar jogadores que participaram de exatamente duas partidas
# Determinar jogadores que participaram de apenas uma partida
# Contar o número total de jogadores únicos no torneio
# Encontrar jogadores que participaram da Partida 1, mas não da Partida 2 ou Partida 3
# Imprima os resultados no seguinte formato:

# Use sorted(list(set_name)) para exibir os jogadores em ordem alfabética
# Imprima o formato de saída exato mostrado no exemplo
# Entrada de Exemplo:
# {"Alice", "Bob", "Charlie", "Diana"}
# {"Charlie", "Diana", "Eve", "Frank"}
# {"Alice", "Diana", "Frank", "George"}
# Saída de Exemplo:
# Players in all matches: ['Diana']
# Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
# Players in only one match: ['Bob', 'Eve', 'George']
# Total unique players: 7
# Players in Match 1 only: ['Bob']

match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
players_in_all_matches = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
players_in_two_matches = (
    (match1 & match2) | (match1 & match3) | (match2 & match3)
) - players_in_all_matches

# 3. Find players who participated in only one match
players_in_one_match = (
    (match1 - match2 - match3)
    | (match2 - match1 - match3)
    | (match3 - match1 - match2)
)

# 4. Count total unique players
total_unique_players = len(match1 | match2 | match3)

# 5. Find players in Match 1 only
players_in_match1_only = match1 - match2 - match3

# Print results in the specified format
print("Players in all matches:", sorted(list(players_in_all_matches)))
print("Players in exactly two matches:", sorted(list(players_in_two_matches)))
print("Players in only one match:", sorted(list(players_in_one_match)))
print("Total unique players:", total_unique_players)
print("Players in Match 1 only:", sorted(list(players_in_match1_only)))