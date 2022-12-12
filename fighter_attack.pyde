RES_W = 1200
RES_H = 700

GROUND = 600

P_width = 100
P_HEIGHT = 250

P_HEALTH = 100

class Player:
    def __init__(self, player_num, x, y ):
        self.alive = True
        self.player_num = player_num
        self.health = P_HEALTH
        self.x = x
        self.y = y
        self.p_height = P_HEIGHT
        self.p_width = P_width
        self.vx = 0
        self.vy = 0
        self.ground = GROUND
        self.keyLog = {'Left' : False , 'Right' : False , 'Up': False}
        self.attacking = False # to know if the player is attacking or not
        self.attack_type = {'punch': False, 'kick':False, 'special_move': False} # y = Punch, h = Kick, g = Special Move
        self.hit = False # To know if the target was hit or not
        # Initial direction
        if self.player_num == 0:
            self.p_direction = 'right'
        else:
            self.p_direction = 'left'
    
    def attack(self, other_player): 
        if self.attacking == True:
            if self.attack_type['punch'] == True:
                if self.p_direction == 'right':
                    fill(10,10,10)
                    rect(self.x, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    # hit_area_x = self.x+self.p_width  
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x: # checks if other player is within hit area
                    # if (-20 <= ((self.x+self.p_width) - other_player.x) <= 0) and (self.y - other_player.y <= self.p_height):
                        other_player.health -= 10
                        print('hit')
                        self.attacking = False
                else:
                    fill(10,10,10)
                    rect(self.x-20, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x: # checks if other player is within hit area 
                    # if (0 <= (self.x-(other_player.x+self.p_width)) <= 20) and (self.y - other_player.y <= self.p_height):
                        other_player.health -= 10
                        print('hit')
                        self.attacking = False

            #elif structure to ensure just one action is executed at a time            
            elif self.attack_type['kick'] == True:
                if self.p_direction == 'right':
                    fill(10,10,100)
                    stroke(255,100,100)
                    rect(self.x, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x:
                        other_player.health -= 10
                        print('hit')
                        self.attacking = False
                else:
                    fill(10,10,10)
                    rect(self.x-20, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x:
                        other_player.health -= 10
                        print('hit')
                        self.attacking = False
                        
            elif self.attack_type['special_move'] == True:
                if self.p_direction == 'right':
                    fill(10,10,10)
                    stroke(255,100,100)
                    rect(self.x, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (other_player.x+other_player.p_width) - (self.x+self.p_width + 20) <= other_player.p_width and self.x < other_player.x:
                        other_player.health -= 20
                        print('hit')
                        self.attacking = False
                else:
                    fill(10,10,10)
                    rect(self.x-20, self.y, self.p_width+20, self.p_height)
                    print(self.p_direction)
                    if (self.x - 20)  - (other_player.x) <= other_player.p_width and self.x > other_player.x:
                        other_player.health -= 20
                        print('hit')
                        self.attacking = False
            if self.health <= 0 or other_player.health <= 0:
                self.alive = False



    
    def movement(self):
        
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
        self.attack(other_player)
        self.update()
        fill(200, 60, 0)
        rect(self.x, self.y, self.p_width, self.p_height)
        

class Game:
    def __init__(self):
        self.player1 = Player(0, 200, 200)
        self.player2 = Player(1, 750, 200)
    
    def distance(self, first, second):
        return ((first.x - second.x)**2 + (first.y - second.y)**2)**0.5
    
    def display(self):
        
        # Display players
        self.player1.display(self.player2)
        self.player2.display(self.player1)
        
        # 
        
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
        
        
        

def setup():
    size(RES_W, RES_H)

def draw():
    background(255,255,255)
    if game.player1.alive == True and game.player2.alive == True:
        game.display()

game = Game()

### This is for Key Presses for Player 1 and Player 2:

def keyPressed():
    # For Player 1
    
    if keyCode == LEFT:
        game.player1.keyLog['Left'] = True
        game.player1.p_direction = 'left'
    elif keyCode == RIGHT:
        game.player1.keyLog['Right'] = True
        game.player1.p_direction = 'right'
    elif keyCode == UP:
        game.player1.keyLog['Up'] = True
    
    if key == 'p' or key =='P':
        game.player1.attacking = True
        game.player1.attack_type['punch'] = True
        
    elif key == 'k' or key =='K':
        game.player1.attacking = True
        game.player1.attack_type['kick'] = True
        
    elif key == 'm' or key =='M':
        game.player1.attacking = True
        game.player1.attack_type['special_move'] = True
        
        
        
    # For Player 2
    
    if key == 'a' or key == 'A':
        game.player2.keyLog['Left'] = True
        game.player2.p_direction = 'left'
    elif key == 'd' or key == 'D':
        game.player2.keyLog['Right'] = True
        game.player2.p_direction = 'right'
    elif key == 'w' or key == 'W':
        game.player2.keyLog['Up'] = True
        
    # if key == 'r' or key == 'R':
    #     game.player2.attacking = True
    #     game.player2.attack_type[1] = True
        
    if key == 'y' or key =='Y':
        game.player2.attacking = True
        game.player2.attack_type['punch'] = True
        
    elif key == 'h' or key =='H':
        game.player2.attacking = True
        game.player2.attack_type['kick'] = True
        
    elif key == 'g' or key =='G':
        game.player2.attacking = True
        game.player2.attack_type['special_move'] = True
        
        
    
    
def keyReleased():
    
    #for Player1
    
    if keyCode == LEFT:
        game.player1.keyLog['Left'] = False
    elif keyCode == RIGHT:
        game.player1.keyLog['Right'] = False
    elif keyCode == UP:
        game.player1.keyLog['Up'] = False
    
    if key == 'p' or key == 'P':
        game.player1.attacking = False
        game.player1.attack_type['punch'] = False
        
    if key == 'k' or key =='K':
        game.player1.attacking = False
        game.player1.attack_type['kick'] = False
        
    if key == 'm' or key =='M':
        game.player1.attacking = False
        game.player1.attack_type['special_move'] = False
        
    
    #For player 2
    
    if key == 'a' or key == 'A':
        game.player2.keyLog['Left'] = False
    elif key == 'd' or key == 'D':
        game.player2.keyLog['Right'] = False
    elif key == 'w' or key == 'W':
        game.player2.keyLog['Up'] = False
    
    # if key == 'r' or key == 'R':
    #     game.player2.attacking = False
    #     game.player2.attack_type[1] = False
        
    if key == 'y' or key == 'Y':
        game.player2.attacking = False
        game.player2.attack_type['punch'] = False
        
    elif key == 'h' or key =='H':
        game.player2.attacking = False
        game.player2.attack_type['kick'] = False
        
    elif key == 'g' or key =='G':
        game.player2.attacking = False
        game.player2.attack_type['special_move'] = False
        
        
