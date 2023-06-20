from random import choice, randint

# Remplacer "ascii_letters" par choice(cip) si vous le voulez
#cip = ["ascii_lowercase","ascii_uppercase","ascii_letters"]


def gen(l,mi):
    """
    l: longeur minimume caractère
    mi: longeur minimume de nombre de caractère du groupe b
    """

    text = f"""
        "cipher": "ascii_letters",
        "substitue with": "configs/all.db",
        "cipher punctuation": "true",
        "cipher space": true,
        "cipher accent": "true",
        "cipher digits": "true",
        "len_caractere": [{l},{randint(l+1,15)}],
        "len_carac_special": [3,{l-1}],
        "nombre_cle": [50,{randint(51,90)}],
        "mini": {mi},
        "maxi": {randint(mi+100,999)},
        "rolling":{randint(100,999999)}
    """

    return "{\n"+text+"\n}"


def get_random_setting():
    f = open("configs/setting.json", "w")
    f.write(gen(5,100))
    f.close()
