import services.actions_with_screenings as scr_act




def ticket_reservation_menu (viewer):
    print("""
Bilietų reservavimo meniu.
          
Galimi filmų seansai:
""")
    scr_act.show_screenings_list()
    scr_list = scr_act.open_sceenings_list_file()
    while True:
        try:
            print("\nNorėdami nutraukti bilietų rezervaciją įveskite: 0")
            user_input = input("Norėdami tęsti, įveskite norimo seanso numerį: ")
            user_input = int(user_input)
            if user_input == 0:
                return viewer
            elif user_input > 0 and user_input <= len(scr_list):
                if scr_list[user_input-1].avialable_seats > 0:
                    scr_list[user_input-1].avialable_seats -= 1
                    scr_act.save_updated_screening_list(scr_list)
                    viewer.add_tickets(scr_list[user_input-1])
                    print("Bilietas rezervuotas.")
                    return viewer
                else:
                    print("Šiame seanse vietų nebėra.")
            else: 
                print("Tokio numerio seanso nėra. Bandykite dar kartą.")
        except ValueError:
            print("Įvestis galima tik sveikais skaičiais. Bandykite dar kartą.")
    
    
