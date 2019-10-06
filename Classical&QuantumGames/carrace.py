import pygame
import time
import random

#you have to initiate this first before using pygame
pygame.init()

#Our colors
white = (255,255,255)
black  = (0,0,0)
red = (200,0,0)
green = (0,200,0)

bright_green = (0,255,0)
bright_red = (255,0,0)
#setting our screen
display_width = 800
display_height = 600

#Set up our game surface or window
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Title of our game or what we want the game to display
pygame.display.set_caption("A bit Racey")

#Create your own clock, i.e how fast we want the the game to run and how it should run
clock  = pygame.time.Clock()

#loading my sport car image
carImage = pygame.image.load("sportcar.jpg")

#Scaling my car image
car_width = 100
car_height = 100
carImage = pygame.transform.scale(carImage,(car_width,car_height))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

#Define functions of objects our car wanna avoid, this object will be inform of box
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    

#blit draws our sport car on the screen at positon x and y                               
def car(x,y):
    gameDisplay.blit(carImage, (x,y))

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

#The message we wanna display
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()
    

#What should happen if we crash
def crash():
    message_display("You crashed")

def button(msg, x,y, w,h,ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    

    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w, h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
##                
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
            
def quitgame():
    pygame.quit()
    quit()
#Defining game intro
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("Racing car",largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150,450, 100,50,green, bright_green, game_loop)
        button("END!", 550, 450, 100, 50,red, bright_red, quitgame)
        
       

        
        pygame.display.update()
        clock.tick(15)
        
                
            
    

#wHERE WE HANDLE ALL OUR EVENTS
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    #CREATING A KEY HANDLER FOR OUR GAME
    x_change = 0
    y_change = 0

    #The position x and y for our box to start
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    #how fast should they move
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dodged = 0
    #Since we are setting up a racing car, we want to set our crash to false cos we haven't crash when we started the game.
    gameExit = False

    #while crash is still false. This is our handling loop. That is keep doing doing all this things till crash = True
    while not gameExit:
        
        #Pygame.event help us to get all the events we launched in our game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #If the game is not quit then we wanna control our game
            #If a key is pressed
            if event.type == pygame.KEYDOWN:
                #if the key pressed is left arrow key
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                
            #wHAT IF WE RELEASE THE KEY, WHAT DO WE WANT TO HAPPEN? KEEP OUR NEW CHANGE
            if event.type ==pygame.KEYUP:
                #WHICH KEY IS RELEASE:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 #Dont change x again.

        #Now we want to change the our x position

        x += x_change
                    
        #Fill our screen with with white
        gameDisplay.fill(white)



        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, red)

        #We wanna keep changing our y positiobn
        thing_starty += thing_speed
        #Display our car on the screen
        car(x,y)
        things_dodged(dodged)

        #Let create a logic to break our game when it hits the wall
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5


        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x+car_width < thing_startx +thing_width:
                crash()
        
        #After running the above code, we want to update our game
        pygame.display.update()
        
        #How fast and smooth we want our frame to run
        clock.tick(60)
game_intro()
game_loop()
#Uninitiate pygame
pygame.quit()
quit()
