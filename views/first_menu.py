import views.coordinator_authorization as ca
import views.viewer_menu as vm

def first_menu():
    while True:
        print("""
Kino Festivalių Organizavimo Sistema
    Vartotojo tipo meniu.
              
    Pasirinkite vartotojo tipą:
    1. Organizatorius.
    2. Žiūrovas.
    0. Išjungti programą.
""")
        user_input = input("Įveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            ca.coordinator_authorization()
        elif user_input == "2":
            vm.viewer_menu()
        elif user_input == "0":
            exit()
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
