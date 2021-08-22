from playsound import playsound
     
def play_sound(mood):
    
    count =1
    while count < 3:
     playsound(f'//wsl$/Ubuntu/home/mohmmadnoorjebreen/project-mid/sound/music/{mood}/{mood}{count}.mp3')
     count+=1

play_sound('sad')