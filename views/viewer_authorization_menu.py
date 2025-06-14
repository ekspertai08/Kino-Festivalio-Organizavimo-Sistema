import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import services.actions_with_viewers as vie_act
import views.viewer_menu as vm






def viewer_authorization_menu():
    while True:
        print(f"""{Fore.CYAN}
Žiūrovo autorizacijos meniu.
1. Prisijungti jau esamam žiūrovui.
2. Sukurti naują žiūrovą.
0. Grįžti į vartotojo tipo meniu.""")
        user_input = input("Įveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            if vie_act.empty_viewer_list_check():
                viewer_name = input("Įveskite žiūrovo vardą: ")
                viewers_list = vie_act.open_viewers_list_file()
                for i in viewers_list:
                    if i.name == viewer_name:
                        print(f"{Fore.GREEN}Prisijungta sėkmingai.")
                        upd = vm.viewer_menu(i)
                        vie_act.save_updated_viewer(upd)
                        break
                else:
                    print(f"{Fore.RED}Tokio žiūrovo nėra.")
            else:
                print(f"{Fore.RED}Šiuo metu registruotų žiūrovų nėra.")
        elif user_input == "2":
            new = vie_act.create_viewer_object()
            if vie_act.empty_viewer_list_check():
                vie_act.exist_viewer_check(new)
            else:
                vie_act.save_viewer_to_list(new)
        elif user_input == "0":
            break
        else:
            print(f"{Fore.RED}Tokio pasirinkimo nėra. Bandykite dar kartą.")
            


