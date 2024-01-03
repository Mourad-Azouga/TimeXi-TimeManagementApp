from header import room
from tabulate import tabulate

# initalize les jours w les creneaux
emploi = {
    'Lundi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
              ('5:00 PM', '6:45 PM')],
    'Mardi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
              ('5:00 PM', '6:45 PM')],
    'Mercredi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
                 ('5:00 PM', '6:45 PM')],
    'Jeudi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
              ('5:00 PM', '6:45 PM')],
    'Vendredi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
                 ('5:00 PM', '6:45 PM')],
    'Samedi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'),
               ('5:00 PM', '6:45 PM')]
}
materiaux = "Datashow;Micro"
# 3amar les objects salles w amphis
amphi1 = room(1, 1, "Amphi1", emploi, materiaux, 115)
amphi2 = room(1, 2, "Amphi2", emploi, materiaux, 115)
amphi3 = room(1, 3, "Amphi3", emploi, materiaux, 115)
amphi4 = room(1, 4, "Amphi4", emploi, materiaux, 115)
amphi5 = room(1, 5, "Amphi5", emploi, materiaux, 300)
amphi6 = room(1, 6, "Amphi6", emploi, materiaux, 400)
amphis = [amphi1, amphi2, amphi3, amphi4, amphi5, amphi6]

salle_A_nums = [
    room(2, {i + 1}, f"Salle A-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_B_nums = [
    room(2, {i + 1}, f"Salle B-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_E_nums = [
    room(2, {i + 1}, f"Salle E-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_F_nums = [
    room(2, {i + 1}, f"Salle F-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]
salles = [salle_A_nums, salle_B_nums, salle_E_nums, salle_F_nums]


# ---------------------------------------------------------------------------------------------------------------------------------------#
#                                                           RESERVATION METHODS
# ---------------------------------------------------------------------------------------------------------------------------------------#

def make_res(type, section, num):
    """Make a reservation and add it to the system"""
    room_instance = None

    if type == 1:
        # Amphi
        room_instance = amphis[num - 1]
    elif type == 2:
        # Class
        room_instance = salles[{'A': 0, 'B': 1, 'E': 2, 'F': 3}[section]][num - 1]
    else:
        print("Invalid room type")
        return

    # Display the current timetable

    # Get user input for day and timeslot
    day = input("Enter the day of the reservation: ")
    timeslot = input("Enter the timeslot of the reservation: ")

    # Check if the entered day and timeslot are valid in emploi
    if day not in emploi or timeslot not in [slot[0] for slot in emploi[day]]:
        print("Invalid day or timeslot. Please enter a valid day and timeslot.")
        return

    # Attempt to make the reservation
    success = room_instance.make_reser(day, timeslot)

    if success:
        print("Reservation successful!")

        # Display reservation details
        print(
            f"You have reserved {room_instance.name} ({'Amphi' if type == 1 else 'Salle'} {section}{num}) on {day} at {timeslot}.")
    else:
        print("Reservation failed. The slot is already reserved.")

def remove_res(type, section, num):

    room_instance = None
    if type == 1:
        # Amphi
        room_instance = amphis[num - 1]
    elif type == 2:
        # Class
        room_instance = salles[{'A': 0, 'B': 1, 'E': 2, 'F': 3}[section]][num - 1]

    # Implement the removal logic based on your requirements
    day = input("Enter the day for the reservation to be removed: ")
    timeslot = input("Enter the timeslot for the reservation to be removed: ")

    if room_instance.remove_reser(day, timeslot):
        print("Reservation removed successfully!")
    else:
        print("No reservation found for the specified day and timeslot.")


def modif_res(type, section, num):

    room_instance = None
    if type == 1:
        # Amphi
        room_instance = amphis[num - 1]
    elif type == 2:
        # Class
        room_instance = salles[{'A': 0, 'B': 1, 'E': 2, 'F': 3}[section]][num - 1]
    else:
        print("Invalid room type")
        return

    day = input("Enter the current day of the reservation: ")
    timeslot = input("Enter the current tiameslot of the reservation: ")

    # Check if the reservation exists
    if day not in emploi or timeslot not in [slot[0] for slot in emploi[day]]:
        print("Invalid day or timeslot. Please enter a valid day and timeslot.")
        return


    # Get user input for the new day and timeslot
    new_day = input("Enter the new day of the reservation: ")
    new_timeslot = input("Enter the new timeslot of the reservation: ")

    # Check if the new day and timeslot are valid
    if new_day not in emploi or new_timeslot not in [slot[0] for slot in emploi[new_day]]:
        print("Invalid day or timeslot. Please enter a valid day and timeslot.")
        return

    # Attempt to modify the reservation
    success = room_instance.modify_reservation(day, timeslot, new_day, new_timeslot)

    if success:
        print("Reservation modified successfully!")
        print(
            f"The reservation has been moved from {day} at {timeslot} to {new_day} at {new_timeslot}.")
    else:
        print("Reservation modification failed. The new slot is already reserved.")

# ---------------------------------------------------------------------------------------------------------------------------------------#
#                                                          NAVIGATION METHODS
# ---------------------------------------------------------------------------------------------------------------------------------------#


def navigator_amphi():
    """The first base for the amphis, where we'll have the menu"""

    type = 1
    amphi_numero = int(input("Vous avez choisi les amphis!\nSVP de choisir le numero d'amphi (1 - 6): "))
    if amphi_numero < 1 or amphi_numero > 6:
        print("Erreur de saisie!")
        return
    print("Vous avez choisi amphi {}\nL'emploi du temps present de cet amphi:\n".format(amphi_numero))
    # Create the amphi instance
    amphi_instance = amphis[amphi_numero - 1]

    # Display the timetable using the class method
    amphi_instance.display_timetable()

    choix = int(input(
        "Menu:\n___\n(1) Faire une reservation\n(2) Annule une reservation\n(3) Modifier une reservation \n(4) Retour au menu principal\n"))
    if choix == 1:
        make_res(type, 0, amphi_numero)
    elif choix == 2:
        remove_res(type, 0, amphi_numero)
    elif choix == 3:
        modif_res(type, 0, amphi_numero)
    elif choix == 4:
        print("Retour..\n")
        return
    else:
        print("Erreur saisir!\n")
        return


def navigator_salles():
    """The first base for the salles, where we'll have the menu, it should also test the input before doing anything"""

    type = 2
    salle_section = input("Vous avez choisi les salles!\nSVP de choisir le section du salle (A-B-E-F)\n")
    if salle_section not in {'A', 'B', 'E', 'F'}:
        print("Erreur saisie!\n")
        return
    salle_numero = int(
        input("Vous avez choisi les salles de section {}, SVP de choisir le numero de salle: ".format(salle_section)))
    if salle_numero < 1 or salle_numero > 15:
        print("Erreur de saisie!")
        return
    print(
        "Vous avez choisi la salle {}{}\nL'emploi du temps present de cet amphi:\n".format(salle_section, salle_numero))

    # Create the salle instance
    salle_instance = salles[{'A': 0, 'B': 1, 'E': 2, 'F': 3}[salle_section]][salle_numero - 1]

    # Display the timetable using the class method
    salle_instance.display_timetable()
    choix = int(input(
        "Menu:\n___\n(1) Faire une reservation\n(2) Annule une reservation\n(3) Modifier une reservation \n(4) Retour au menu principal\n"))
    if choix == 1:
        make_res(type, salle_section, salle_numero)
    elif choix == 2:
        remove_res(type, salle_section, salle_numero)
    elif choix == 3:
        modif_res(type, salle_section, salle_numero)
    elif choix == 4:
        print("Retour..\n")
        return
    else:
        print("Erreur saisir!\n")
        return


if __name__ == '__main__':
    print("Bienvenu au system gestion TIMEXI\n")
    while True:
        choix = int(input("\nMenu Principal\n___\n(1)Les Amphis\n(2)Les Salles\n(3)To be made\n(4)Quitter\n"))
        match choix:
            case 1:
                navigator_amphi()
            case 2:
                navigator_salles()
            case 3:
                print("")
            case 4:
                print("Au revoir")
                break