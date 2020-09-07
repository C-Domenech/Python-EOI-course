import webbrowser


def data_input(full_birthdate, name):
    split_birthdate = full_birthdate.split('/')
    return what_pokemon_are_you(day=split_birthdate[0], month=split_birthdate[1], name=name)


def what_pokemon_are_you(day, month, name):
    f_step = int(day) * int(month)
    s_step = f_step * len(name)
    t_step = s_step // 2
    while t_step > 718:
        t_step = t_step // 2

    url = "https://www.pokemon.com/es/pokedex/{}".format(t_step)
    webbrowser.open_new_tab(url)
