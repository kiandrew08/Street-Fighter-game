add_library("minim")
import os, random, time

path = os.getcwd()
player = Minim(this)

RES_W = 1200
RES_H = 700

GROUND = 600

P_WIDTH = 100
P_HEIGHT = 210

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
        # self.action_allowed = True
        self.attacking = False # to know if the player is attacking or not
        self.attack_type = {'punch': False, 'kick':False, 'special_move': False} # y = Punch, h = Kick, g = Special Move
        self.hit = False # To know if the target was hit or not
        self.wins_num = wins_num
        self.getting_hit_sound = player.loadFile(path+"/sounds/getting_hit.mp3")
        self.prev_action = 'idle'
        self.winner = False
          
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
            self.sasuke_img = loadImage(path + '/assets/sasuke/sasuke.png')
        elif self.char_name == 'naruto':
            self.naruto_img = loadImage(path + '/assets/naruto/naruto.png')
    
    def showSprite(self):
        if self.char_name == 'naruto':
            if self.state['jump']:
                    if self.p_direction == 'right':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*6, int(83.75*13), 100*7, int(83.75*14))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*7, int(83.75*13), 100*6, int(83.75*14))
            elif self.state['idle']:
                    if self.p_direction == 'right':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*self.slice, int(83.75*0), 100*(self.slice+1), int(83.75*1))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+1), int(83.75*0), 100*(self.slice), int(83.75*1))
                    if frameCount % 10 == 0:
                        self.slice += 1
                        if self.slice % 4 == 0:
                            self.slice = 0
            elif self.state['run']:
                    if self.p_direction == 'right':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+4), int(83.75*0), 100*(self.slice+4+1), int(83.75*1))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+4+1), int(83.75*0), 100*(self.slice+4), int(83.75*1))
                    if frameCount % 10 == 0:
                        self.slice += 1
                        if self.slice % 6 == 0:
                            self.slice = 0
            elif self.state['punch']:
                    if self.p_direction == 'right':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice), int(83.75*9), 100*(self.slice+1), int(83.75*10))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+1), int(83.75*9), 100*(self.slice), int(83.75*10))
                    if frameCount % 10 == 0:
                        self.slice += 1
                        if self.slice % 4 == 0:
                            self.slice = 0
            elif self.state['kick']:
                    if self.p_direction == 'right':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+6), int(83.75*8), 100*(self.slice+6+1), int(83.75*9))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+6+1), int(83.75*8), 100*(self.slice+6), int(83.75*9))
                    if frameCount % 10 == 0:
                        self.slice += 1
                        if self.slice % 4 == 0:
                            self.slice = 0
            elif self.state['main']:
                    if self.p_direction == 'main':
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice), int(83.75*11), 100*(self.slice+1), int(83.75*12))
                    else:
                        image(self.naruto_img, self.x, self.y, 300, 3*int(83.75), 100*(self.slice+1), int(83.75*11), 100*(self.slice), int(83.75*12))
                    if frameCount % 10 == 0:
                        self.slice += 1
                        if self.slice % 3 == 0:
                            self.slice = 0
                
        elif self.char_name == 'sasuke':
            if self.state['jump']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*9, 1*85, 109*10, 2*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*10, 1*85, 109*9, 2*85)
            elif self.state['idle']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*self.slice, 0*85, 109*(self.slice+1), 1*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+1), 0*85, 109*self.slice, 1*85)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['run']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+4), 0*85, 109*(self.slice+4+1), 1*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+4+1), 0*85, 109*(self.slice+4), 1*85)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['punch']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice), 8*85, 109*(self.slice+1), 9*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+1), 8*85, 109*(self.slice), 9*85)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['kick']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+3), 12*85, 109*(self.slice+3+1), 13*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+3+1), 12*85, 109*(self.slice+3), 13*85)
                if frameCount % 10 == 0:
                    self.slice += 1
                    if self.slice % 4 == 0:
                        self.slice = 0
            elif self.state['main']:
                if self.p_direction == 'right':
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+5), 8*85, 109*(self.slice+5+1), 9*85)
                else:
                    image(self.sasuke_img, self.x, self.y, 327, 255, 109*(self.slice+5+1), 8*85, 109*(self.slice+5), 9*85)
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
                        self.attacking = False
            if other_player.health <= 0:
                other_player.alive = False
                self.winner = True
                self.wins_num +=1 
                print("There is a winner")



    
    def movement(self, other_player):
        
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
        
        
    def update(self, other_player):
        self.movement(other_player)
        self.gravity()
        
        self.x += self.vx
        self.y += self.vy
    
    def display(self, other_player):
        self.showSprite()
        self.attack(other_player)
        self.update(other_player)
        

class Game:
    def __init__(self):
        self.player1 = Player(0, 200, 200, 'sasuke')
        self.player2 = Player(1, 750, 200, 'naruto')
        self.play_ongoing = False
        self.end_round = False
        self.end_game = False
        self.current_round = 1
        self.current_round_winner = 0
        self.time_in_frames = 60 * 61 # 60 frames * 61 seconds, 61 seconds just to give allowance
        self.time_left = 60
        self.bg_music = player.loadFile(path +"/sounds/background.mp3")
        self.round_win = False
        self.counter = 0
        self.beginning = True
        self.instructions_img = loadImage(path+ '/assets/instructions.png')
        self.bg_music.loop()
        self.bg_img = loadImage(path+"/assets/background.png")
        self.player_1_round = loadImage(path+'/assets/player_1_round.png')
        self.player_1_game = loadImage(path+'/assets/player_1_game.png')
        self.player_2_round = loadImage(path+'/assets/player_2_round.png')
        self.player_2_game = loadImage(path+'/assets/player_2_game.png')

    def new_timer(self):
        if self.time_in_frames >= 0:
            self.time_left = self.time_in_frames // 60
            self.time_in_frames -= 1
            
            
        textSize(50)
        text_time = str(self.time_left)
        fill(0,0,0)
        text(text_time, 580, 55)
    

    
    def display_instructions(self):
        image(self.instructions_img, 0, 0)
    
    def display_round_win(self):
        print(self.player1.winner)
        print(self.player2.winner)
        self.counter += 1
        if self.player1.winner:
            image(self.player_1_round, 0, 0)
        elif self.player2.winner:
            image(self.player_2_round, 0, 0)
        
        if self.counter % 180 == 0:
            self.counter = 0
            self.round_win = False
            self.player1.winner = False
            self.player1.alive = True
            self.player2.winner = False
            self.player2.alive = True
            
    
    def display(self):
        image(self.bg_img, 0, 0)
        
        self.player1.display(self.player2)
        self.player2.display(self.player1)
        
        
        # For Time tracker
        self.new_timer() 
        
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
    

        if self.player1.alive == False or self.player2.alive == False :
            self.end_round = True
            self.current_round += 1
            
            if self.player1.alive == False:
                self.current_round_winner = 2
            else: 
                self.current_round_winner = 1
        
            self.player1 = Player(0, 200, 200, 'sasuke', self.player1.wins_num)
            self.player2 = Player(1, 750, 200, 'naruto', self.player2.wins_num)
            if self.current_round_winner == 1:
                self.player1.winner = True
                print('kkkkk')
            else:
                self.player2.winner = True
                print('kjljkljkl')
            
            self.round_win = True
            
        if self.current_round == 4 or self.player1.wins_num == 2 or self.player2.wins_num == 2:
            self.end_game = True  
        
        

def setup():
    size(RES_W, RES_H)

def draw():
    background(200,255,198)
    if game.beginning == True:
        game.display_instructions()
        
    elif game.end_game == False:
        if game.round_win == False:
            game.display()
        else:
            game.time_in_frames = 60*61
            game.display_round_win()
    else:
        if game.player1.wins_num == 2:
            image(game.player_1_game, 0, 0)
        elif game.player2.wins_num == 2:
            image(game.player_2_game, 0, 0)        
    

game = Game()

### This is for Key Presses for Player 1 and Player 2:

def keyPressed():
    game.play_ongoing = True
    
    # For Player 1
    
    if key == 'a' or key == 'A':
        # game.player1.action_allowed = False
        game.player1.keyLog['Left'] = True
        game.player1.p_direction = 'left'
        
        # Setting the player's state to run and canceling idle
        game.player1.state['run'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'left':
            game.player1.slice = 0
            game.player1.prev_action = 'left'
    elif key == 'd' or key == 'D':
        # game.player1.action_allowed = False
        game.player1.keyLog['Right'] = True
        game.player1.p_direction = 'right'
        
        # Setting the player's state to run and canceling idle
        game.player1.state['run'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'right':
            game.player1.slice = 0
            game.player1.prev_action = 'right'
    elif key == 'w' or key == 'W':
        # game.player1.action_allowed = False
        game.player1.keyLog['Up'] = True
    
    if key == 't' or key =='T':
        # game.player1.action_allowed = False
        game.player1.attacking = True
        game.player1.attack_type['punch'] = True
        
        # Setting the player's state to kick and canceling idle
        game.player1.state['punch'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'punch':
            game.player1.slice = 0
            game.player1.prev_action = 'punch'
        
    elif key == 'f' or key =='F':
        # game.player1.action_allowed = False
        game.player1.attacking = True
        game.player1.attack_type['kick'] = True
        
        # Setting the player's state to kick and canceling idle
        game.player1.state['kick'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'kick':
            game.player1.slice = 0
            game.player1.prev_action = 'kick'
        
    elif key == 'c' or key =='C':
        # game.player1.action_allowed = False
        game.player1.attacking = True
        game.player1.attack_type['special_move'] = True
        
        # Setting the player's state to main and canceling idle
        game.player1.state['main'] = True
        game.player1.state['idle'] = False
        
        if game.player1.prev_action != 'main':
            game.player1.slice = 0
            game.player1.prev_action = 'main'
        
        
        
    # For Player 2
    
    if keyCode == LEFT:
        game.player2.keyLog['Left'] = True
        game.player2.p_direction = 'left'
        
        # Setting the player's state to run and canceling idle
        game.player2.state['run'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'left':
            game.player2.slice = 0
            game.player2.prev_action = 'left'
    elif keyCode == RIGHT:
        game.player2.keyLog['Right'] = True
        game.player2.p_direction = 'right'
        
        # Setting the player's state to run and canceling idle
        game.player2.state['run'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'right':
            game.player2.slice = 0
            game.player2.prev_action = 'right'
    elif keyCode == UP:
        game.player2.keyLog['Up'] = True
        
    # if key == 'r' or key == 'R':
    #     game.player2.attacking = True
    #     game.player2.attack_type[1] = True
        
    if key == 'p' or key =='P':
        game.player2.attacking = True
        game.player2.attack_type['punch'] = True
        
        # Setting the player's state to run and canceling idle
        game.player2.state['punch'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'punch':
            game.player2.slice = 0
            game.player2.prev_action = 'punch'
        
    elif key == 'k' or key =='K':
        game.player2.attacking = True
        game.player2.attack_type['kick'] = True
        
        # Setting the player's state to run and canceling idle
        game.player2.state['kick'] = True
        game.player2.state['idle'] = False
        
        if game.player2.prev_action != 'kick':
            game.player2.slice = 0
            game.player2.prev_action = 'kick'
        
    elif key == 'm' or key =='M':
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
    
    if key == 'a' or key == 'A':
        game.player1.keyLog['Left'] = False
        
        # Reversing run and idle state
        game.player1.state['run'] = False
        game.player1.state['idle'] = True
    elif key == 'd' or key == 'D':
        game.player1.keyLog['Right'] = False
        
        # Reversing run and idle state
        game.player1.state['run'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
    elif key == 'w' or key == 'W':
        game.player1.keyLog['Up'] = False
    
    if key == 't' or key == 'T':
        game.player1.attacking = False
        game.player1.attack_type['punch'] = False
        
        # Reversing punch and idle state
        game.player1.state['punch'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    if key == 'f' or key =='F':
        game.player1.attacking = False
        game.player1.attack_type['kick'] = False
        
        # Reversing kick and idle state
        game.player1.state['kick'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    if key == 'c' or key =='C':
        game.player1.attacking = False
        game.player1.attack_type['special_move'] = False
        
        # Reversing main and idle state
        game.player1.state['main'] = False
        game.player1.state['idle'] = True
        game.player1.slice = 0
        
    
    #For player 2, (w, a, d to move), (r-punch, q-kick, x-main)
    
    if keyCode == LEFT:
        game.player2.keyLog['Left'] = False
        # Reversing run and idle state
        game.player2.state['run'] = False
        game.player2.state['idle'] = True
    elif keyCode == RIGHT:
        game.player2.keyLog['Right'] = False
        # Reversing run and idle state
        game.player2.state['run'] = False
        game.player2.state['idle'] = True
    elif keyCode == UP:
        game.player2.keyLog['Up'] = False
        
    if key == 'p' or key == 'P':
        game.player2.attacking = False
        game.player2.attack_type['punch'] = False
        
        # Reversing punch and idle state
        game.player2.state['punch'] = False
        game.player2.state['idle'] = True
        
    elif key == 'k' or key =='K':
        game.player2.attacking = False
        game.player2.attack_type['kick'] = False
        
        # Reversing kick and idle state
        game.player2.state['kick'] = False
        game.player2.state['idle'] = True
        
    elif key == 'm' or key =='M':
        game.player2.attacking = False
        game.player2.attack_type['special_move'] = False
        
        # Reversing main and idle state
        game.player2.state['main'] = False
        game.player2.state['idle'] = True

def mouseClicked():
    if game.beginning:
        game.beginning = False
    if game.end_game == True:
        global game
        game = Game()
    
