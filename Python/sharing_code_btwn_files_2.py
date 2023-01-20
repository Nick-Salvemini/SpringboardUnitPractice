from sharing_code_btwn_files import get_rand_month, get_rand_year
# could also use v , but then you would need to write sharing_code_btwn_files.get_rand_month()
# import sharing_code_btwn_files


def make_person(name, fav_color):
    return {
        'name': name,
        'fav_color': fav_color,
        'birth_year': get_rand_year(),
        'birth_month': get_rand_month()
    }