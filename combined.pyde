add_library("minim")
import os, random

path = os.getcwd()
player = Minim(this)

RES_W = 1200
RES_H = 700

GROUND = 600

P_WIDTH = 100
P_HEIGHT = 160

P_HEALTH = 100

class Player:
    def __init__(self, player_num, x, y, character_name, wins_num=0):
        self.alive = True
        self.player_num = player_num
        self.char_name = character_name
        self.health = P_HEALTH
        self.x = x
        self.y = y
        self.p_height = P_HEIGHT
        self.p_width = P_WIDTH
        self.vx = 0
        self.vy = 0
        self.ground = GROUND
        self.keyLog = {'Left' : False , 'Right' : False , 'Up': False}
        self.attacking = False # to know if the player is attacking or not
        self.attack_type = {'punch': False, 'kick':False, 'special_move': False} # y = Punch, h = Kick, g = Special Move
        self.hit = False # To know if the target was hit or not
        self.wins_num = wins_num
        self.getting_hit_sound = player.loadFile(path+"/sounds/getting_hit.mp3")
        self.prev_action = 'idle'
          
        # Initial direction
        if self.player_num == 0:
            self.p_direction = 'right'
        else:
            self.p_direction = 'left'
        
        # loading Images
        self.slice = 0
        self.state = {'idle' : True, 'jump': False, 'dead': False, 'run': False, 'punch' : False, 'kick': False, 'main': False}
            # Sasuke
        if self.char_name == 'sasuke': 
            self.sasuke_idle = loadImage(path + '/assets/sasuke/sasuke_idle.png')
            self.sasuke_run = loadImage(path + '/assets/sasuke/sasuke_run.png')
            self.sasuke_punch = loadImage(path + '/assets/sasuke/sasuke_punch.png')
            self.sasuke_kick = loadImage(path + '/assets/sasuke/sasuke_kick.png')
            self.sasuke_main = loadImage(path + '/assets/sasuke/sasuke_main.png')
            self.sasuke_jump = loadImage(path + '/assets/sasuke/sasuke_jump.png')
            self.sasuke_dead = loadImage(path + '/assets/sasuke/sasuke_dead.png')
        elif self.char_name == 'spiderman':
            self.spiderman_idle = loadImage(path + '/assets/spiderman/spiderman_idle.png')
            self.spiderman_run = loadImage(path + '/assets/spiderman/spiderman_run_2.png')
            self.spiderman_punch = loadImage(path + '/assets/spiderman/spiderman_punch.png')
            self.spiderman_kick = loadImage(path + '/assets/spiderman/spiderman_kick.png')
            self.spiderman_main = loadImage(path + '/assets/spiderman/spiderman_main.png')
            self.spiderman_jump = loadImage(path + '/assets/spiderman/spiderman_jump.png')
            self.spiderman_dead = loadImage(path + '/assets/spiderman/spiderman_dead.png')
    
    def showSprite(self):
        print("this is showing sprite inside fxn")
        print(self.char_name)
        if self.char_name == 'sasuke' or self.char_name == 0:
            self.scl_factor = 3
            # Check if this character is in IDLE state
            if not self.alive:
                for i in range(10):
                    print('iii')
                image(self.sasuke_dead, self.x, self.y, 50*self.scl_factor, 16*self.scl_factor, 0, 0, 50, 16)
            elif self.state['jump']:
                if self.p_direction == 'right':
                    image(self.sasuke_jump, self.x, self.y, 35*self.scl_factor, 48*self.scl_factor, 0, 0, 35, 48) # image dimension: 35*48, 1 frame
                else:
                    image(self.sasuke_jump, self.x, self.y, 35*self.scl_factor, 48*self.scl_factor, 35, 0, 0, 48)
            elif self.state['idle']:
                if self.p_direction == 'right':
                    image(self.sasuke_idle, self.x, self.y, 48*self.scl_factor, 52*self.scl_factor, 48*self.slice, 0, 48*(self.slice+1), 52) # image dimension = 288 * 52, 6 frames
                else:
                    image(self.sasuke_idle, self.x, self.y, 48*self.scl_factor, 52*self.scl_factor, 48*(self.slice+1), 0, 48*self.slice, 52) 
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 6 == 0:
                        self.slice = 0
            elif self.state['run']:
                if self.p_direction == 'right':
                    image(self.sasuke_run, self.x, self.y, 48*self.scl_factor, 50*self.scl_factor, int(48*self.slice), 0, int(48*(self.slice+1)), 50) # image dimension = 288 * 50, 6 frames
                else:
                    image(self.sasuke_run, self.x, self.y, 48*self.scl_factor, 50*self.scl_factor, int(48*(self.slice+1)), 0, int(48*self.slice), 50)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 6 == 0:
                        self.slice = 0
            elif self.state['punch']:
                if self.p_direction == 'right':
                    image(self.sasuke_punch, self.x, self.y, 51*self.scl_factor, 50*self.scl_factor, int(51*self.slice), 0, int(51*(self.slice+1)), 50) # image dimension = 204 * 50, 4 frames
                else:
                    image(self.sasuke_punch, self.x, self.y, 51*self.scl_factor, 50*self.scl_factor, int(51*(self.slice+1)), 0, int(51*self.slice), 50)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['kick']:
                if self.p_direction == 'right':
                    image(self.sasuke_kick, self.x, self.y, 45*self.scl_factor, 50*self.scl_factor, int(45*self.slice), 0, int(45*(self.slice+1)), 50) # image dimension = 180 * 50, 4 frames
                else:
                    image(self.sasuke_kick, self.x, self.y, 45*self.scl_factor, 50*self.scl_factor, int(45*(self.slice+1)), 0, int(45*self.slice), 50)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['main']:
                if self.p_direction == 'right':
                    image(self.sasuke_main, self.x, self.y, 92*self.scl_factor, 45*self.scl_factor, int(92*self.slice), 0, int(92*(self.slice+1)), 45) # image dimension = 460 * 45, 5 frames
                else:
                    image(self.sasuke_main, self.x, self.y, 92*self.scl_factor, 45*self.scl_factor, int(92*(self.slice+1)), 0, int(92*self.slice), 45)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 5 == 0:
                        self.slice = 0
        elif self.char_name == 'spiderman':
            self.scl_factor = 4
            # Check is fthis character is in IDLE state
            if not self.alive:
                image(self.spiderman_dead, self.x, self.y, 45*self.scl_factor, 25*self.scl_factor, 0, 0,45, 25)
            elif self.state['jump']:
                if self.p_direction == 'right':
                    image(self.spiderman_jump, self.x, self.y, 29*self.scl_factor, 40*self.scl_factor, 0, 0, 29, 40) # image dimension: 29*40, 1 frame
                else:
                    image(self.spiderman_jump, self.x, self.y, 29*self.scl_factor, 40*self.scl_factor, 29, 0, 0, 40)
            elif self.state['idle']:
                if self.p_direction == 'right':
                    image(self.spiderman_idle, self.x, self.y, 44*self.scl_factor, 38*self.scl_factor, int(44*self.slice), 0, int(44*(self.slice+1)), 38) # image dimension = 176 * 38, 4 frames
                else:
                    image(self.spiderman_idle, self.x, self.y, 44*self.scl_factor, 38*self.scl_factor, int(44*(self.slice+1)), 0, int(44*self.slice), 38)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['run']:
                if self.p_direction == 'right':
                    image(self.spiderman_run, self.x, self.y, 46*self.scl_factor, 45*self.scl_factor, int(46.5*self.slice), 0, int(46.5*(self.slice+1)), 45) # image dimension = 326*45, 7 frames
                else:
                    image(self.spiderman_run, self.x, self.y, 46*self.scl_factor, 45*self.scl_factor, int(46.5*(self.slice+1)), 0, int(46.5*self.slice), 40)
                if frameCount % 8 == 0:
                    self.slice += 1
                    if self.slice % 7 == 0:
                        self.slice = 0
            elif self.state['punch']:
                if self.p_direction == 'right':
                    image(self.spiderman_punch, self.x, self.y, 46*self.scl_factor, 47*self.scl_factor, int(46*self.slice), 0, int(46*(self.slice+1)), 47) # image dimension = 138 * 47, 3 frames
                else:
                    image(self.spiderman_punch, self.x, self.y, 46*self.scl_factor, 47*self.scl_factor, int(46*(self.slice+1)), 0, int(56*self.slice), 47)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 3 == 0:
                        self.slice = 0
            elif self.state['kick']:
                if self.p_direction == 'right':
                    image(self.spiderman_kick, self.x, self.y, 45*self.scl_factor, 50*self.scl_factor, int(45*self.slice), 0, int(45*(self.slice+1)), 50) # image dimension = 135 * 50, 3 frames
                else:
                    image(self.spiderman_kick, self.x, self.y, 45*self.scl_factor, 50*self.scl_factor, int(45*(self.slice+1)), 0, int(45*self.slice), 50)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 3 == 0:
                        self.slice = 0
            elif self.state['main']:
                if self.p_direction == 'right':
                    image(self.spiderman_main, self.x, self.y, 62*self.scl_factor, 45*self.scl_factor, int(62*self.slice), 0, int(62*(self.slice+1)), 45) # image dimension = 310 * 58, 5 frames
                else:
                    image(self.spiderman_main, self.x, self.y, 62*self.scl_factor, 45*self.scl_factor, int(62*(self.slice+1)), 0, int(62*self.slice), 45)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 5 == 0:
                        self.slice = 0
        
    
    def attack(self, other_player): 
        if self.attacking == True:
            if self.attack_type['punch'] == True:
                if self.p_direction == 'right':
                    # fill(10,10,10)
                    # rect(self.x, self.y, self.p_width+20, self.p_height)
                
                    # hit_area_x = self.x+self.p_width  
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x: # checks if other player is within hit area
                    # if (-20 <= ((self.x+self.p_width) - other_player.x) <= 0) and (self.y - other_player.y <= self.p_height):
                        other_player.health -= 10
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False
                else:
                    # fill(10,10,10)
                    # rect(self.x-20, self.y, self.p_width+20, self.p_height)
                
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x: # checks if other player is within hit area 
                    # if (0 <= (self.x-(other_player.x+self.p_width)) <= 20) and (self.y - other_player.y <= self.p_height):
                        other_player.health -= 10
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False

            #elif structure to ensure just one action is executed at a time            
            elif self.attack_type['kick'] == True:
                if self.p_direction == 'right':
                    fill(10,10,100)
                    # stroke(255,100,100)
                    # rect(self.x, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x:
                        other_player.health -= 10
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False
                else:
                    # fill(10,10,10)
                    # rect(self.x-20, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x:
                        other_player.health -= 10
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False
                        
            elif self.attack_type['special_move'] == True:
                if self.p_direction == 'right':
                    # fill(10,10,10)
                    # stroke(255,100,100)
                    # rect(self.x, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x:
                        other_player.health -= 20
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False
                else:
                    # fill(10,10,10)
                    # rect(self.x-20, self.y, self.p_width+20, self.p_height)
                    # print(self.p_direction)
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x:
                        other_player.health -= 20
                        self.getting_hit_sound.rewind()
                        self.getting_hit_sound.play()
                        print('hit')
                        self.attacking = False
            if other_player.health <= 0:
                other_player.alive = False
                self.wins_num +=1 
                print("There is a winner")



    
    def movement(self):
        
        if self.y + self.p_height < self.ground:
            self.state['jump'] = True
        else:
            self.state['jump'] = False
        
        if self.attacking != True:
            # for movement in x-axis
            if self.keyLog['Left'] and not (self.x < 0) == True:
                self.vx = -5
            elif self.keyLog['Right'] and  not (self.x+self.p_width > RES_W) == True:
                self.vx = 5
            else:
                self.vx = 0
            
            # for movement in y-axis
            if self.keyLog['Up'] == True and (self.y + self.p_height == self.ground):
                self.vy = -10
            
    
    def gravity(self):
        
        if self.y + self.p_height <= GROUND:
            self.vy = self.vy + 0.3
            if self.y + self.p_height + self.vy > self.ground:
                self.vy = self.ground - (self.y + self.p_height)
        else:
            self.vy = 0
        
        
    def update(self):
        self.movement()
        self.gravity()
        
        self.x += self.vx
        self.y += self.vy
    
    def display(self, other_player):
        # print("this is checking inside the display fxn")
        self.showSprite()
        self.attack(other_player)
        self.update()
        fill(200, 60, 0)
        # rect(self.x, self.y, self.p_width, self.p_height)
        

class Game:
    def __init__(self):
        self.player1 = Player(0, 200, 200, 'sasuke')
        self.player2 = Player(1, 750, 200, 'spiderman')
        self.play_ongoing = False
        self.end_round = False
        self.end_game = False
        self.current_round = 1
        self.time_left = 60
        self.bg_music = player.loadFile(path +"/sounds/background.mp3")
        self.bg_music.loop()
        self.bg_img = loadImage(path+"/assets/background.png")
    
    def distance(self, first, second):
        return ((first.x - second.x)**2 + (first.y - second.y)**2)**0.5

    def timer(self):

        textSize(50)
        text_time = str(self.time_left)
        fill(0,0,0)
        text(text_time, 580, 55)
        # print(self.play_ongoing)
        if self.play_ongoing:
            elapsed_time = millis()
            # print("this is elapsed time", elapsed_time)
            if self.time_left >0 :
                self.time_left = 60 - elapsed_time // 1000 
    
    def display(self):
        image(self.bg_img, 0,0, RES_W, RES_H)
        # Display players
        self.player1.display(self.player2)
        self.player2.display(self.player1)
        
        # For Time tracker
        self.timer() 
        
        # This is for health-bar
        for i in range(2):
            if i == 0:
                noStroke()
                fill(230,230,230)
                rect(20, 30, 300, 20)
                fill(200, 10, 10)
                rect(20,30, 300*(float(game.player1.health) / float(P_HEALTH)), 20)
                # print("kian")
            else:
                noStroke()
                fill(230,230,230)
                rect(880, 30, 300, 20)
                fill(200, 10, 10)
                rect(880,30, 300*(float(game.player2.health)/ float(P_HEALTH)), 20)
        
        # For Ground
        fill(100,100,0)
        rect(0, GROUND, RES_W, RES_H)
        
        #For Rounds
        
        for i in range(self.player1.wins_num):
            fill(100,255,100)
            circle(30+20*i,60,20)
            
        for i in range(self.player1.wins_num, 2):
            fill(210, 210, 210)
            circle(30+20*i,60,20)

        for i in range(self.player2.wins_num):
            fill(100,255,100)
            circle(890+20*i,60,20)
            
        for i in range(self.player2.wins_num, 2):
            fill(210, 210, 210)
            circle(890+20*i,60,20)
    

        
        #
        if self.player1.alive == False or self.player2.alive == False :
            self.end_round = True
            self.current_round += 1
            
            self.player1.alive = True
            self.player1 = Player(0, 200, 200, 'sasuke', self.player1.wins_num)
            self.player2 = Player(1, 750, 200, 'spiderman', self.player2.wins_num)
            self.player1.alive = True
            
        if self.current_round == 6:
            self.end_game = True  
        
        

def setup():
    size(RES_W, RES_H)

def draw():
    background(200,255,198)
    # image(
    if game.end_game == False:
        game.display()

game = Game()

### This is for Key Presses for Player 1 and Player 2:

def keyPressed():
    game.play_ongoing = True
    
    # For Player 1
    
    if keyCode == LEFT:
        game.player1.keyLog['Left'] = True
        game.player1.p_direction = 'left'
        
        # Setting the player's state to run and canceling idle
        game.player1.state['run'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'left':
            game.player1.slice = 0
            game.player1.prev_action = 'left'
    elif keyCode == RIGHT:
        game.player1.keyLog['Right'] = True
        game.player1.p_direction = 'right'
        
        # Setting the player's state to run and canceling idle
        game.player1.state['run'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'right':
            game.player1.slice = 0
            game.player1.prev_action = 'right'
    elif keyCode == UP:
        game.player1.keyLog['Up'] = True
    
    if key == 'p' or key =='P':
        game.player1.attacking = True
        game.player1.attack_type['punch'] = True
        
        # Setting the player's state to kick and canceling idle
        game.player1.state['punch'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'punch':
            game.player1.slice = 0
            game.player1.prev_action = 'punch'
        
    elif key == 'k' or key =='K':
        game.player1.attacking = True
        game.player1.attack_type['kick'] = True
        
        # Setting the player's state to kick and canceling idle
        game.player1.state['kick'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'kick':
            game.player1.slice = 0
            game.player1.prev_action = 'kick'
        
    elif key == 'm' or key =='M':
        game.player1.attacking = True
        game.player1.attack_type['special_move'] = True
        
        # Setting the player's state to main and canceling idle
        game.player1.state['main'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'main':
            game.player1.slice = 0
            game.player1.prev_action = 'main'
        
        
        
    # For Player 2
    
    if key == 'a' or key == 'A':
        game.player2.keyLog['Left'] = True
        game.player2.p_direction = 'left'
        
        # Setting the player's state to run and canceling idle
        game.player2.state['run'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'left':
            game.player2.slice = 0
            game.player2.prev_action = 'left'
    elif key == 'd' or key == 'D':
        game.player2.keyLog['Right'] = True
        game.player2.p_direction = 'right'
        
        # Setting the player's state to run and canceling idle
        game.player2.state['run'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'right':
            game.player2.slice = 0
            game.player2.prev_action = 'right'
    elif key == 'w' or key == 'W':
        game.player2.keyLog['Up'] = True
        
    # if key == 'r' or key == 'R':
    #     game.player2.attacking = True
    #     game.player2.attack_type[1] = True
        
    if key == 'r' or key =='R':
        game.player2.attacking = True
        game.player2.attack_type['punch'] = True
        
        # Setting the player's state to run and canceling idle
        game.player2.state['punch'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'punch':
            game.player2.slice = 0
            game.player2.prev_action = 'punch'
        
    elif key == 'q' or key =='Q':
        game.player2.attacking = True
        game.player2.attack_type['kick'] = True
        
        # Setting the player's state to run and canceling idle
        game.player2.state['kick'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'kick':
            game.player2.slice = 0
            game.player2.prev_action = 'kick'
        
    elif key == 'x' or key =='X':
        game.player2.attacking = True
        game.player2.attack_type['special_move'] = True
        
        # Setting the player's state to run and canceling idle
        game.player2.state['main'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'main':
            game.player2.slice = 0
            game.player2.prev_action = 'main'
        
        
    
    
def keyReleased():
    
    #for Player1
    
    if keyCode == LEFT:
        game.player1.keyLog['Left'] = False
        
        # Reversing run and idle state
        game.player1.state['run'] = False
        game.player1.state['idle'] = True
    elif keyCode == RIGHT:
        game.player1.keyLog['Right'] = False
        
        # Reversing run and idle state
        game.player1.state['run'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
    elif keyCode == UP:
        game.player1.keyLog['Up'] = False
    
    if key == 'p' or key == 'P':
        game.player1.attacking = False
        game.player1.attack_type['punch'] = False
        
        # Reversing punch and idle state
        game.player1.state['punch'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    if key == 'k' or key =='K':
        game.player1.attacking = False
        game.player1.attack_type['kick'] = False
        
        # Reversing kick and idle state
        game.player1.state['kick'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    if key == 'm' or key =='M':
        game.player1.attacking = False
        game.player1.attack_type['special_move'] = False
        
        # Reversing main and idle state
        game.player1.state['main'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    
    #For player 2, (w, a, d to move), (r-punch, q-kick, x-main)
    
    if key == 'a' or key == 'A':
        game.player2.keyLog['Left'] = False
        # Reversing run and idle state
        game.player2.state['run'] = False
        game.player2.state['idle'] = True
    elif key == 'd' or key == 'D':
        game.player2.keyLog['Right'] = False
        # Reversing run and idle state
        game.player2.state['run'] = False
        game.player2.state['idle'] = True
    elif key == 'w' or key == 'W':
        game.player2.keyLog['Up'] = False
        
    if key == 'r' or key == 'R':
        game.player2.attacking = False
        game.player2.attack_type['punch'] = False
        
        # Reversing punch and idle state
        game.player2.state['punch'] = False
        game.player2.state['idle'] = True
        
    elif key == 'q' or key =='Q':
        game.player2.attacking = False
        game.player2.attack_type['kick'] = False
        
        # Reversing kick and idle state
        game.player2.state['kick'] = False
        game.player2.state['idle'] = True
        
    elif key == 'x' or key =='X':
        game.player2.attacking = False
        game.player2.attack_type['special_move'] = False
        
        # Reversing main and idle state
        game.player2.state['main'] = False
        game.player2.state['idle'] = True
