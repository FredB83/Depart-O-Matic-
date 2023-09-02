from tkinter import Tk, Label, Entry, Frame, StringVar

from technician import secteurs, tech


def get_technicians_in_areas(area):
    return tech.get(area)


def get_area_name(area_number):
    for name, area_numbers in secteurs.items():
        if area_number in area_numbers:
            return name

    # nothing found
    return None


def on_user_input(*_):
    value = user_input.get()
    if value not in [None, ""]:
        area_name = get_area_name(int(value))
        techs = get_technicians_in_areas(area_name)

        output_text =  f"Secteur {area_name}:\n{techs}"
        output_label.config(text=output_text)


# Créer une instance de la fenêtre principale
app = Tk()
app.title("DEPARTEMENT O MATIC")
user_input = StringVar()
user_input.trace_add("write", on_user_input)


Label(app, text="Entrez le département: ").pack()
Entry(app, textvariable=user_input).pack()

output_label = Label(app, text= "")
output_label.pack()

Frame(app, width= 800, height= 800).pack()

# Lancer la boucle principale Tkinter
app.mainloop()
