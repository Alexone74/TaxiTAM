def correggi_riga(riga):
    # Separa la riga nei suoi componenti
    parti = [p.strip() for p in riga.split('|')]
    if len(parti) != 6:
        return riga

    # Corregge gli apostrofi
    for i in range(len(parti)):
        parti[i] = parti[i].replace("'", "'")
        
    # Rimuove spazi doppi
    for i in range(len(parti)):
        parti[i] = ' '.join(parti[i].split())

    # Rimuove spazi extra prima dei segni di punteggiatura
    parti[1] = parti[1].replace(" ,", ",")
    parti[1] = parti[1].replace(" :", ":")
    parti[1] = parti[1].replace(" ?", "?")

    # Aggiunge spazio dopo la virgola se non presente
    parti[1] = parti[1].replace(",", ", ").replace("  ", " ")

    return " | ".join(parti)

# Legge il file originale
with open('domande.txt', 'r', encoding='utf-8') as file:
    linee = file.readlines()

# Corregge ogni riga e salva nel nuovo file
with open('domande_corretto.txt', 'w', encoding='utf-8') as file:
    for riga in linee:
        riga_corretta = correggi_riga(riga.strip())
        file.write(riga_corretta + '\n')

print("File corretto creato con successo!")