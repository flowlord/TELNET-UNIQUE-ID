import subprocess


def init():
    subprocess.run('get_info_cmd.bat', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
init()


def geolocalisation():
    return  open("network.txt", "r").read()


def get_user_entry():
    return  open("user_entry.txt", "r").read()


def get_more_info():
    
    data_file = open("result.txt","r", encoding="utf-8").readlines()
    data_file = data_file[0:32]

    new_file = open("result.txt","w", encoding="utf-8")

    #on enlève les lignes inutiles
    n_lst = [25,27,28,11,12]
    c = 0

    for e in data_file:
        if c not in n_lst:
            new_file.write(e)
        c = c+1
    
    new_file.close()
    return open("result.txt", "r").read()





