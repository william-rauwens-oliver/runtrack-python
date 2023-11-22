def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un nombre entier positif de minutes.")
        return
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        print("{} minutes.".format(minutes))
    elif heures == 1 and minutes_restantes == 0:
        print("{} heure.".format(heures))
    elif heures == 1:
        print("{} heure et {} minute{}.".format(heures, minutes_restantes, 's' if minutes_restantes != 1 else ""))
    elif minutes_restantes == 0:
        print("{} heures.".format(heures))
    else:
        print("{} heures et {} minute{}.".format(heures, minutes_restantes, 's' if minutes_restantes != 1 else "")) # "!" sert à ajouter un s au mots "minute" en vérifiant si il est différent de 1.

time_to_text(160)
time_to_text(85)
time_to_text(35)
time_to_text(0)
time_to_text(-20)