import pygame, os, time

lyrics = [ 
    {
        "text":"I'm going under and this time I fear there's no one to save me",
        "duration":08.614
    },
    {
        "text":"This all or nothing really got a way of driving me crazy",
        "duration":17.316
    },
    {
        "text":"I need somebody to heal",
        "duration":24.349
    },
    {
        "text":"Somebody to know",
        "duration":26.967
    },
    {
        "text":"Somebody to have",
        "duration":28.777
    },
    {
        "text":"Somebody to hold",
        "duration":31.233
    },
    {
        "text":"It's easy to say",
        "duration":33.810
    },
    {
        "text":"But it's never the same",
        "duration":35.656
    },
    {
        "text":"I guess I kinda liked the way you numbed all the pain",
        "duration":37.860
    },
    {
        "text":"Now the day bleeds",
        "duration":42.048
    },
    {
        "text":"Into nightfall",
        "duration":43.876
    },
    {
        "text":"And you're not here",
        "duration":46.282
    },
    {
        "text":"To get me through it all",
        "duration":48.337
    },
    {
        "text":"I let my guard down",
        "duration":50.795
    },
    {
        "text":"And then you pulled the rug",
        "duration":53.097
    },
    {
        "text":"I was getting kinda used to being someone you loved",
        "duration":55.059
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