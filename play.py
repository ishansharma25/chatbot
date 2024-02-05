from importlib.resources import path
from re import L
from tkinter import *
import pygame
import random
import os
from chat import get_response, bot_name, feel, get_mood

pygame.mixer.init()
os.add_dll_directory("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#FFF"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root = Tk()
root.configure(width=670, height=670, background=BG_GRAY)
root.title("Chat")
root.resizable(width=False, height=False)


# head label
head_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR,
                   text="Welcome", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)


# tiny divider
line = Label(root, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)


# text widget
text_widget = Text(root, width=20, height=2, bg="yellow",
                   fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

# scroll bar
scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)

# bottom label #change from here
bottom_label = Label(root, bg=BG_GRAY, height=70)
bottom_label.place(relwidth=1, rely=0.6)

# message entry box
msg_entry = Entry(bottom_label, bg="white", fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)


global pa
global listsong


def get_input():
    input = msg_entry.get().strip()
    return input


def send():
    input = get_input()
    send = "You- " + input
    res = bot_name + "- " + get_response(input)
    address = feel(get_mood(input))
    global pa
    pa=address
    text_widget.insert(END, "\n" + send)
    text_widget.insert(END, "\n" + res)
    msg_entry.delete(0, END)

def play():
    global listsong
    song=listsong
    song=song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def add_song():
    global listsong
    file = os.listdir(pa)
    songplay = random.choice(file)
    path=f"{pa}{songplay}"
    listsong=path
    song_box.insert(END, path)

def add_more():
    global listsong
    file = os.listdir(pa)
    for i in file:
        path=f"{pa}{i}"
        listsong=path
        song_box.insert(END, listsong)
    pygame.mixer.music.load(listsong)

global paused
paused=False

def pause(is_pause):

    global paused
    paused=is_pause
    if(paused ):
        pygame.mixer.music.unpause()
        paused=False
    else:

        pygame.mixer.music.pause()
        paused=True

def stop():
    pygame.mixer.music.stop()

def clear():
    song_box.delete(0,END)
    pygame.mixer.music.stop()

# delete one song
def delete():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def game():
    pygame.init()


    # Colors
    blue = (0, 126, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)

    # Creating window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    # Game Title
    pygame.display.set_caption("Snake Game")
    pygame.display.update()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])


    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

    # Game Loop
    def gameloop():
        # Game specific variables
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1

        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        score = 0
        init_velocity = 5
        snake_size = 30
        fps = 60
        while not exit_game:
            if game_over:
                gameWindow.fill(blue)
                text_screen("Game Over! Press Enter To Continue", red, 100, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                    score +=1
                    food_x = random.randint(20, screen_width / 2)
                    food_y = random.randint(20, screen_height / 2)
                    snk_length +=5

                gameWindow.fill(blue)
                text_screen("Score: " + str(score * 10), red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list)>snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True

                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    game_over = True
                plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        pygame.mixer.init()
    gameloop()

send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=send)
send_button.place(relx=0.77, rely=0.008, relheight=0.05, relwidth=0.22)


# tiny divider
down_lable = Label(root, width=450, bg=BG_GRAY)
down_lable.place(relwidth=1, rely=0.71, relheight=0.012)

song_box = Listbox(root, width=20, height=2,
                   bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
song_box.place(relheight=0.11, relwidth=1, rely=0.72)

# control button

#previous song
clear_button = Button(bottom_label, text="Clear",
                     font=FONT_BOLD, width=15, bg=BG_GRAY,command=clear)
clear_button.place(relx=0.01, rely=0.145, relheight=0.042, relwidth=0.15)

#all song
addmore_button = Button(bottom_label, text="add more",
                     font=FONT_BOLD, width=15, bg=BG_GRAY,command=add_more)
addmore_button.place(relx=0.17, rely=0.145, relheight=0.042, relwidth=0.15)

#play button
play_button = Button(bottom_label, text="Play",
                     font=FONT_BOLD, width=15, bg=BG_GRAY, command=play)
play_button.place(relx=0.33, rely=0.145, relheight=0.042, relwidth=0.15)

#pause button
pause_button = Button(bottom_label, text="Pause",
                      font=FONT_BOLD, width=15, bg=BG_GRAY,command=lambda: pause(paused))
pause_button.place(relx=0.49, rely=0.145, relheight=0.042, relwidth=0.15)


#stop button
stop_button = Button(bottom_label, text="stop",
                     font=FONT_BOLD, width=15, bg=BG_GRAY,command=stop)
stop_button.place(relx=0.65, rely=0.145, relheight=0.042, relwidth=0.15)

#add song
add_button = Button(bottom_label, text="Add",
                    font=FONT_BOLD, width=15, bg=BG_GRAY,command=add_song)
add_button.place(relx=0.81, rely=0.145, relheight=0.042, relwidth=0.15)

#add all
delete_button = Button(bottom_label, text="delete",
                      font=FONT_BOLD, width=15, bg=BG_GRAY,command=delete)
delete_button.place(relx=0.33, rely=0.2, relheight=0.042, relwidth=0.15)
#
#Clear song box
game_button = Button(bottom_label, text="Game",
                      font=FONT_BOLD, width=15, bg=BG_GRAY,command=game)
game_button.place(relx=0.49, rely=0.2, relheight=0.042, relwidth=0.15)

root.mainloop()
