import random
import os
import ast
bot_name="Sam"
#Normal talk

with open("D:\New folder\Progams\python\emotion\data.txt",encoding='utf-8') as fi:
    greeting={}
    for i in fi:
        (k, v) = i.split("/")
        greeting[k.strip()] = v.strip()
#print(greeting)


#Goobye talk
with open("D:\New folder\Progams\python\emotion\goodbye.txt",encoding='utf-8') as fi:
    bye={}
    for i in fi:
        (k, v) = i.split("/")
        bye[k.strip()] = v.strip()

#funny talk
with open("D:\New folder\Progams\python\emotion\happy.txt",encoding='utf-8') as fi:
    fun={}
    for i in fi:
        (k, v) = i.split("/")
        fun[k.strip()] = v.strip()

#sad talk
with open("D:\New folder\Progams\python\emotion\saddness.txt",encoding='utf-8') as fi:
    sad={}
    for i in fi:
        (k, v) = i.split("/")
        sad[k.strip()] = v.strip()

with open("D:\New folder\Progams\python\emotion\stressness.txt",encoding='utf-8') as fi:
    stress={}
    for i in fi:
        (k, v) = i.split("/")
        stress[k.strip()] = v.strip()

with open("D:\New folder\Progams\python\emotion\\angry.txt",encoding='utf-8') as fi:
    ang={}
    for i in fi:
        (k, v) = i.split("/")
        ang[k.strip()] = v.strip()

with open("D:\New folder\Progams\python\emotion\default.txt",encoding='utf-8') as fi:
    default=fi.read().splitlines()


mood=""
#Loop for conservation
def get_response(send):
    single_output=-1
    for i in greeting.keys():
        single_output = 0
        if (send.lower() == i.lower() and single_output == 0):
            return(greeting[i])
        else:
            continue

    for i in ang.keys():
        single_output = 0
        if (send.lower() == i.lower() and single_output == 0):
            return(ang[i])
        else:
            continue

    for i in fun.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            return(fun[i])
        else:
            continue

    for i in bye.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            single_output = 1
            return(bye[i])
        else:
            continue

    for i in sad.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            return(sad[i])
        else:
            continue

    for i in stress.keys():
        single_output = 0
        if (send.lower() == i.lower() and single_output == 0):
            return (stress[i])
        else:
            continue
    
    return(random.choice(default))
   

def get_mood(send):
    single_output=-1
    for i in greeting.keys():
        single_output = 0
        if (send.lower() == i.lower() and single_output == 0):
            mood="neutral"
            feel(mood)
            return(mood)
        else:
            continue

    for i in fun.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            mood="funny"
            return(mood)
        else:
            continue

    for i in bye.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            single_output = 1
            mood="bye"
            feel(mood)
            return(mood)
        else:
            continue

    for i in sad.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            mood="sad"
            feel(mood)
            return(mood)
        else:
            continue

    for i in ang.keys():
        single_output=0
        if (send.lower() == i.lower() and single_output == 0):
            mood="angry"
            feel(mood)
            return(mood)
        else:
            continue

    for i in stress.keys():
        single_output = 0
        if (send.lower() == i.lower() and single_output == 0):
            mood="stress"
            feel(mood)
            return (mood)
        else:
            continue
    
    return("neutral")

def feel(h):
    music_dir=""
    if(h=="neutral"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\musicdata\\"
        return music_dir
    elif(h=="funny"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\happy\\"
        return music_dir
    elif(h=="bye"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\htata\\"
        return music_dir
    elif(h=="sad"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\sad\\"
        return music_dir 
    elif(h=="stress"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\stress\\"
        return music_dir
    elif(h=="angry"):
        music_dir = "C:\\Users\ishan\Desktop\Progams\python\\angry\\"
        return music_dir
        
