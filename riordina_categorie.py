import json

# Leggi il file quiz.json
with open('quiz.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Riordina le categorie nell'ordine desiderato
data['categorie'] = [
    "Geografia",
    "Normativa Statale e Regionale",
    "Regolamento e Comportamento", 
    "Inglese",
    "Fuori Dispensa"
]

# Salva il file aggiornato
with open('quiz.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("Categorie riordinate con successo!")