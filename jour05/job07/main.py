def arrondir_notes(notes):
    return [note if note < 40 else ((note + 4) // 5) * 5 for note in notes]

# Exemple d'utilisation :
notes = [83, 42, 78, 39, 91]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)
