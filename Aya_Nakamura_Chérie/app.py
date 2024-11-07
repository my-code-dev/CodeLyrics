import pygame, os, time

lyrics = [ 
    {
        "text":"[Instru] ...",
        "duration":09.043
    },
    {
        "text":"J'me promenais tranquille",
        "duration":22.594
    },
    {
        "text":"Et puis j'ai croisé, lui",
        "duration":25.249
    },
    {
        "text":"Il m'a fait la cour, oui",
        "duration":27.983
    },
    {
        "text":"Garçon m'a fait la cour, oui",
        "duration":30.767
    },
    {
        "text":"J'me mets en valeur que pour un putain d'mec (sheesh)",
        "duration":33.607
    },
    {
        "text":"D'après mes ex, j'suis une putain d'meuf (yeah)",
        "duration":36.495
    },
    {
        "text":"Y a pas d'issue d'secours (oh non)",
        "duration":39.103
    },
    {
        "text":"C'est la seule solution (yeah)",
        "duration":41.762
    },
    {
        "text":"Igo, pardon (pardon)",
        "duration":44.586
    },
    {
        "text":"C'est dans tes bras que tu veux que j'm'endorme",
        "duration":45.820
    },
    {
        "text":"Attention, c'est dangereux, attention",
        "duration":50.094
    },
    {
        "text":"Mais moi c'est la puissance, la tentation",
        "duration":55.623
    },
    {
        "text":"Chéri, attention (a-a-a-attention)",
        "duration":58.821
    },
    {
        "text":"Mais moi c'est la puissance, la tentation",
        "duration":61.250
    },
    {
        "text":"Chéri, attention (attention)",
        "duration":64.225
    }
]


def main():
    pygame.mixer.init()
    os.system("clear")
    pygame.mixer.music.load("songs.mp3")
    pygame.mixer.music.play()
    last_time = 0   
    for l in lyrics:
        time_to_wait = l['duration'] - last_time
        last_time = l['duration']
        time.sleep(time_to_wait)
        print(l['text'])
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.quit()
    
if __name__ == "__main__":
    main()