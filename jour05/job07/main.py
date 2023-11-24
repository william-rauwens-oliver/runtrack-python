def arrondir_notes(notes):
    return [note if note < 38 else 40 if note == 38 else (note // 5 + 1) * 5 if (note // 5 + 1) * 5 - note < 3 else note for note in notes]

notes_eleves = [81, 75, 43, 37, 94]
notes_arrondies = arrondir_notes(notes_eleves)
print("Notes des élèves avant arrondi :", notes_eleves)
print("Notes arrondies :", notes_arrondies)