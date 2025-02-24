import models.viewer_class as vc
import os
import pickle

def create_viewer_object():
    name = input("Įveskite žiūrovo vardą: ")
    return vc.Viewer(name)

def open_viewers_list_file():
    if os.path.exists("data/viewers_list.pickle"):
        with open("data/viewers_list.pickle", "rb") as file:
            return pickle.load(file)
    else:
        return False

def save_viewer_to_list(viewer):
    if open_viewers_list_file():
        viewers_list = open_viewers_list_file()
        viewers_list.append(viewer)
        with open("data/viewers_list.pickle", "wb") as file:
            pickle.dump(viewers_list, file)
    else:
        with open("data/viewers_list.pickle", "wb") as file:
            viewers_list = []
            viewers_list.append(viewer)
            pickle.dump(viewers_list, file)

def empty_viewer_list_check():
    viewers_list = open_viewers_list_file()
    if viewers_list != False and len(viewers_list) > 0:
        return True
    else:
        return False
    
def exist_viewer_check(viewer_object):
    viewer_list = open_viewers_list_file()
    for i in viewer_list:
        if i.name == viewer_object.name:
            print("Toks žiūrovas jau egzistuoja.")
            return        
    save_viewer_to_list(viewer_object)
    print("Naujas žiūrovas sukurtas, galite prisijungti.")


def save_updated_viewer(new):
    if open_viewers_list_file():
        viewers_list = open_viewers_list_file()
        for num, viewer in enumerate(viewers_list):
            if viewer.name == new.name:
                viewers_list[num] = new
        with open("data/viewers_list.pickle", "wb") as file:
            pickle.dump(viewers_list, file)
    else:
        with open("data/viewers_list.pickle", "wb") as file:
            viewers_list = []
            viewers_list.append(new)
            pickle.dump(viewers_list, file)

# def update_viewer_list_after_screening_delete(old_name):
#     viewer_list = open_viewers_list_file()
#     if viewer_list != False:
#         if len(viewer_list)>0:
#             for num,i in enumerate(viewer_list):
#                 if len(i.tickets)>0:
#                     for a in i.tickets:
#                         a.




# def update_screening_list_after_movie_delete(old_name):
#     screening_list = open_sceenings_list_file()
#     if screening_list != False:
#         if len(screening_list)>0:
#             for num,i in enumerate(screening_list):
#                 if i.screening_movie != None:
#                     if i.screening_movie.name == old_name:
#                         number = num
#                         screening_list[number].screening_movie = None
#                         save_updated_screening_list(screening_list)

# def update_screening_list_after_movie_update(old_name, updated_movie):
#     screening_list = open_sceenings_list_file()
#     if screening_list != False:
#         if len(screening_list)>0:
#             for num,i in enumerate(screening_list):
#                 if i.screening_movie != None:
#                     if i.screening_movie.name == old_name:
#                         number = num
#                         screening_list[number].screening_movie = updated_movie
#                         save_updated_screening_list(screening_list)