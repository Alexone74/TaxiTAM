def aggiorna_categorie(contenuto):
    # Definisce le sostituzioni da fare
    sostituzioni = {
        'Normativa Regionale': 'Normativa Statale e Regionale',
        'Regolamenti': 'Regolamento e Comportamento'
    }
    
    # Applica le sostituzioni
    nuovo_contenuto = contenuto
    for vecchio, nuovo in sostituzioni.items():
        nuovo_contenuto = nuovo_contenuto.replace(vecchio + ' |', nuovo + ' |')
    
    return nuovo_contenuto

# Legge il file originale
with open('domande.txt', 'r', encoding='utf-8') as file:
    contenuto = file.read()

# Applica le modifiche
nuovo_contenuto = aggiorna_categorie(contenuto)

# Salva il file aggiornato
with open('domande.txt', 'w', encoding='utf-8') as file:
    file.write(nuovo_contenuto)

print("File domande.txt aggiornato con successo!")