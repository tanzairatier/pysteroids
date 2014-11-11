"#<--- --->#"
"# @author: Joe Krall #"
"# @date: 2/13/2013 #"
"# @title: Pysteroids: Asteroids in Python #"
"#<--- --->#"

import pygame,sys, random
from math import *
from pygame.locals import *
width = 520
height = 360

class Item:
    def draw(item):
        pygame.draw.circle(DISPLAYSURF, item.color, item.location, 8)
        pygame.draw.circle(DISPLAYSURF, item.edgecolor, item.location, 8, 1)
        DISPLAYSURF.blit(item.text.text, item.text.rect)

class AttackSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Attack Sphere"
        item.text = GameText("A", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (255,0,0)
        item.edgecolor = (255,255,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center

class ScoreSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Point Sphere"
        item.text = GameText("P", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (230,0,90)
        item.edgecolor = (0,200,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center
                  
class SpeedSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Speed Sphere"
        item.text = GameText("S", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (0,180,0)
        item.edgecolor = (0,0,255)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center        

class ShieldSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Shield Sphere"
        item.text = GameText("H", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (0,180,255)
        item.edgecolor = (255,255,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center

class TypeIWeaponSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Type I Weapon Sphere"
        item.text = GameText("1", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (255,0,0)
        item.edgecolor = (255,255,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center

class TypeIIWeaponSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Type II Weapon Sphere"
        item.text = GameText("2", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (0,255,255)
        item.edgecolor = (255,255,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center

class TypeIIIWeaponSphere(Item):
    def __init__(item):
        rndLoc = (int(width*random.uniform(0.15, 0.85)), int(height*random.uniform(0.15, 0.85)))
        item.type = "Type III Weapon Sphere"
        item.text = GameText("3", rndLoc[0], rndLoc[1], 16, (255,255,255))        
        item.color = (0,255,0)
        item.edgecolor = (255,255,0)
        item.location = rndLoc
        item.rect = pygame.rect.Rect(item.location[0]-8, item.location[1]-8, 16, 16)
        item.text.rect.center = item.rect.center 
        
class Enemy:
    def draw(enemy):
        enemy.paint = (max(0,250-enemy.hp),max(0,250-enemy.hp), max(0,250-enemy.hp))
        enemy.size = (enemy.hp/enemy.maxhp) * enemy.maxsize + enemy.minsize
        pygame.draw.polygon(DISPLAYSURF, enemy.paint, enemy.drawPoints)
        pygame.draw.aalines(DISPLAYSURF, enemy.edgepaint, True, enemy.drawPoints, True)
        
        for par in enemy.death_particles:   
            DISPLAYSURF.set_at((int(par[0][0]), int((par[0][1]))), (max(0,255-par[2]*2),max(0,255-par[2]*2),max(0,255-par[2]*2)))
    def fly(enemy):
        enemy.location[0] = (enemy.location[0] + enemy.velocity[0]) % width
        enemy.location[1] = (enemy.location[1] + enemy.velocity[1]) % height
        enemy.theta += 0.5
        enemy.drawPoints = []
        for i,p in enumerate(enemy.points):
            xp = p[1]*sin(radians(enemy.theta))*enemy.size + p[0]*cos(radians(enemy.theta))*enemy.size
            yp = p[1]*cos(radians(enemy.theta))*enemy.size - p[0]*sin(radians(enemy.theta))*enemy.size
            enemy.drawPoints.append( [enemy.location[0]+xp, enemy.location[1]+yp]  )
        for par in enemy.death_particles:
            par[0][0] += par[1][0]
            par[0][1] += par[1][1]
            par[2] += 1
            if par[2] >= 150:
                enemy.death_particles.remove(par); continue
        

class Asteroid(Enemy):
    def __init__(asteroid, lv, hard):
        asteroid.location = [random.randint(0,width), random.randint(0,height)]
        asteroid.size = random.randint(12,21)
        asteroid.maxsize = asteroid.size
        asteroid.minsize = 5
        #while True:
        asteroid.velocity = [min(1.0, max(-1.0, 2*0.10*(22 - asteroid.size) * random.random() - 2*0.10*(22 - asteroid.size)/2)),
                             min(1.0, max(-1.0, 2*0.10*(22 - asteroid.size) * random.random() - 2*0.10*(22 - asteroid.size)/2))]
        if abs(asteroid.velocity[0]) < 0.2:
            if asteroid.velocity[0] < 0:
                asteroid.velocity[0] = -0.2
            else:
                asteroid.velocity[0] = 0.2
        if abs(asteroid.velocity[1]) < 0.2:
            if asteroid.velocity[1] < 0:
                asteroid.velocity[1] = -0.2
            else:
                asteroid.velocity[1] = 0.2
        asteroid.hp =    hard*10 + (0.35*lv**2)*5
        asteroid.maxhp = hard*10 + (0.35*lv**2)*5
        asteroid.theta = random.randint(0,359)
        asteroid.paint = (max(0,250-asteroid.hp),max(0,250-asteroid.hp), max(0,250-asteroid.hp))
        asteroid.edgepaint = (255,0,80)
        n = random.randint(3,8)
        asteroid.points = [ [cos((i*2*pi)/n), sin((i*2*pi)/n)] for i in range(n)]
        asteroid.drawPoints = []
        for i,p in enumerate(asteroid.points):
            xp = p[1]*sin(radians(asteroid.theta))*asteroid.size + p[0]*cos(radians(asteroid.theta))*asteroid.size
            yp = p[1]*cos(radians(asteroid.theta))*asteroid.size - p[0]*sin(radians(asteroid.theta))*asteroid.size
            asteroid.drawPoints.append( [asteroid.location[0]+xp, asteroid.location[1]+yp]  )
        asteroid.death_particles = []
    def hit(asteroid):
        for i in range(int(playership.shot_power*5)):
            angle = (random.randint(0,360))
            loc = [asteroid.location[0] + (asteroid.size*cos(radians(angle))), asteroid.location[1] + (asteroid.size*sin(radians(angle)))]
            vel = [0.2 * cos(radians(angle)), 0.2 * sin(radians(angle))]
            asteroid.death_particles.append([loc, vel, 0])
class Shot:
    def __init__(shot):
        shot.location = [0.0, 0.0]
        shot.velocity = [0.0, 0.0]
    def draw(shot):

        if shot.power > 20:
            red = (255,0,0)
        elif shot.power > 15:
            red = (80,255,255)
        elif shot.power > 10:
            red = (80,255,0)
        elif shot.power > 5:
            red = (255,255,0)
        else:
            red = (255,80,0)
        blue = (255,255,255)

        if shot.power < 5:
            shift = -1
            pattern = [(0,1, red),(1,0, red),(1,2, red), (2,1, red) ]
        elif shot.power < 12:
            shift = -2
            pattern = [(2,0, red),(1,1, red),(3,1, red),(0,2, red),(4,2, red),(1,3, red),(3,3, red),(2,4, red)]
        else:
            shift = -2
            pattern = [(2,0, blue),(1,1, blue), (2,1, red ),(3,1, blue),(0,2, blue), (1,2, red ), (2,2, red ),(3,2, red ), (4,2, blue),(1,3, blue), (2,3, red ),(3,3, blue),(2,4, blue)]
        
        for p in pattern:
            DISPLAYSURF.set_at((int(shot.location[0]+p[0]+shift), int(shot.location[1]+p[1]+shift)),p[2])
    def outOfBounds(shot):
        return shot.location[0] < -20 or shot.location[1] < -20 or shot.location[0] > width+20 or shot.location[1] > height+20
    
class PlayerShip:
    def __init__(ship):
        ship.location = [width/2.0, height/2.0]
        ship.points =    [[0,10], [-140,10], [180,4], [140,10]]
        ship.rotpoints = [[0,10], [-140,10], [180,4], [140,10]]
        ship.scale = 1.0
        ship.paint = (120,120,120)
        ship.edgepaint = (0, 255, 80)
        ship.theta = 180
        ship.acceleration = [0.0, 0.0]
        ship.velocity = [0.0, 0.0]
        ship.keyflags = [False, False, False, False]
        ship.BRAKING_FORCE = 0.60
        ship.THRUST = 0.05
        ship.DRAG_FORCE = 0.98
        ship.shots = []
        ship.max_shots = 33
        ship.shot_speed = 2.0
        ship.width = 16*ship.scale
        ship.height = 16*ship.scale
        ship.thrust_flame = False
        ship.thrust_particles = []
        ship.shot_power = 2.0
        ship.lives = 3
        ship.death_particles = []
        ship.crash_position = None
        ship.invincibility = 0
        ship.ivc = 0
        ship.shot_mode = 0
        ship.shot_level = [0,-1,-1]
        ship.max_level = [3, 3, 2]
    def die(ship):
        if not(ship.location == None):
            ship.lives -= 1
            ship.crash_position = [ship.location[0], ship.location[1]]       
            ship.velocity = [0, 0]
            ship.THRUST = 0.0
            ship.thrust_particles = []
            for i in range(100):
                angle = (random.randint(0,360))
                loc = [ship.location[0] + (7.5*cos(radians(angle))), ship.location[1] + (7.5*sin(radians(angle)))]
                vel = [2.0 * cos(radians(angle)), 2.0 * sin(radians(angle))]
                ship.death_particles.append([loc, vel, 0])
            ship.location = None # invisible
            for l,lv in enumerate(ship.shot_level):
                ship.shot_level[l] = max(lv-2, -1)
            if ship.shot_mode > 0:
                if ship.shot_level[ship.shot_mode] == -1:
                    ship.shot_mode = 0
            if ship.shot_level[0] < 0: ship.shot_level[0] = 0
            
    def shoot(ship):
        if len(ship.shots) < ship.max_shots and not(ship.location == None):
            shot_modes = [["Single Shot", "Double Forward Shot", "Tri Shot", "5-Way Shot"],
                          ["Double Forward & Backwards Shot", "Quad Shot", "8-Way Shot", "32-Way Shot"],
                          ["Double Parallel Shot", "Triple Parallel Shot", "Penta Parallel Shot"]]
            ship.shot_type = shot_modes[ship.shot_mode][ship.shot_level[ship.shot_mode]]
            if ship.shot_type == "Single Shot":
                # Single Shot
                angles = [-ship.theta+90]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "Tri Shot":
                # Tri Shot
                angles = [-ship.theta+70, -ship.theta+90, -ship.theta+110]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "Quad Shot":                
                # Quad Shot
                angles = [-ship.theta+45, -ship.theta+135, -ship.theta-45, -ship.theta-135]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "8-Way Shot":
                # 8-Way Shot
                angles = [-ship.theta+da*(360/8)-180 for da in range(8)]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "5-Way Shot":
                # 5-Way Forward Shot
                angles = [-ship.theta+70, -ship.theta+90, -ship.theta+110, -ship.theta+80, -ship.theta+100]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "32-Way Shot":
                # 32-Way Shot
                angles = [-ship.theta+da*(360/32)-180 for da in range(32)]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "Double Forward Shot":
                # Double Forward Shot
                angles = [-ship.theta+75, -ship.theta+105]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "Double Forward & Backwards Shot":            
                # Double Forward & Backwards Shot
                angles = [-ship.theta+90, -ship.theta-90]
                loci = [[ship.location[0],ship.location[1]] for i in angles]
            if ship.shot_type == "Double Parallel Shot":
                # Double Parallel Shot
                angles = [-ship.theta+90, -ship.theta+90]
                loci = [[ship.location[0]+cos(radians(-ship.theta))*7,ship.location[1]+sin(radians(-ship.theta))*7], [ship.location[0]-cos(radians(-ship.theta))*7,ship.location[1]-sin(radians(-ship.theta))*7]]
            if ship.shot_type == "Triple Parallel Shot":
                # Triple Parallel Shot
                angles = [-ship.theta+90, -ship.theta+90, -ship.theta+90]
                loci = [[ship.location[0]+cos(radians(-ship.theta))*9,ship.location[1]+sin(radians(-ship.theta))*9],
                        [ship.location[0],ship.location[1]],
                        [ship.location[0]-cos(radians(-ship.theta))*9,ship.location[1]-sin(radians(-ship.theta))*9]]
            if ship.shot_type == "Penta Parallel Shot":
                # Penta Parallel Shot
                angles = [-ship.theta+90, -ship.theta+90, -ship.theta+90, -ship.theta+90, -ship.theta+90]
                loci = [[ship.location[0]+cos(radians(-ship.theta))*14,ship.location[1]+sin(radians(-ship.theta))*14],
                        [ship.location[0]+cos(radians(-ship.theta))*7,ship.location[1]+sin(radians(-ship.theta))*7],
                        [ship.location[0],ship.location[1]],
                        [ship.location[0]-cos(radians(-ship.theta))*7,ship.location[1]-sin(radians(-ship.theta))*7],
                        [ship.location[0]-cos(radians(-ship.theta))*14,ship.location[1]-sin(radians(-ship.theta))*14],]
            
            for angle,loc in zip(angles,loci):               
                new_shot = Shot()
                new_shot.power = ship.shot_power
                new_shot.location[0] = loc[0] + (7.5*cos(radians(angle)))
                new_shot.location[1] = loc[1] + (7.5*sin(radians(angle)))
                new_shot.velocity[0] = (ship.shot_speed+abs(ship.velocity[0])) * cos(radians(angle))
                new_shot.velocity[1] = (ship.shot_speed+abs(ship.velocity[1])) * sin(radians(angle))
                ship.shots.append(new_shot)
            
            
    def fly(ship):

        if not (ship.location == None):
            # Update Ship XY
            ship.location[0] = (ship.location[0] + ship.velocity[0] ) % width
            ship.location[1] = (ship.location[1] + ship.velocity[1] ) % height
        
            # Apply Dragging Force to Ship Acceleration
            ship.velocity[0] *= ship.DRAG_FORCE
            ship.velocity[1] *= ship.DRAG_FORCE

            # Fly Thrust Particles
            for par in ship.thrust_particles:
                par[0][0] += par[1][0]
                par[0][1] += par[1][1]
                par[2] += 1
                if par[2] >= 16:
                    ship.thrust_particles.remove(par); continue
                    
        # Fly Shots
        for s in ship.shots:
            s.location[0] += s.velocity[0]
            s.location[1] += s.velocity[1]
            if s.outOfBounds():
                ship.shots.remove(s); continue

        # Fly Death Particles
        for par in ship.death_particles:
            par[0][0] += par[1][0]
            par[0][1] += par[1][1]
            par[2] += 1
            if par[2] >= 175:
                ship.death_particles.remove(par); continue

        # Fly Death Particles
        if not(ship.crash_position == None):
            if len(ship.death_particles) == 0:
                ship.location = [ship.crash_position[0], ship.crash_position[1]]
                ship.THRUST = 0.05
                ship.crash_position = None
                ship.ivc = 0
                ship.invincibility = 3
                
    def collides(ship, rect):
        return not(ship.rect.right < rect.left) and not(ship.rect.bottom < rect.top) and not(ship.rect.left > rect.right) and not(ship.rect.top > rect.bottom)
    def new(ship):
        ship.shots = []
        ship.max_shots = 33
        ship.shot_speed = 2.0
        ship.width = 16*ship.scale
        ship.height = 16*ship.scale
        ship.thrust_flame = False
        ship.thrust_particles = []
        ship.shot_power = 2.0
        ship.lives = 3
        ship.death_particles = []
        ship.crash_position = None
        ship.invincibility = 0
        ship.ivc = 0
        ship.shot_mode = 0
        ship.shot_level = [0,-1,-1]
        ship.velocity = [0.0, 0.0]
        ship.location = [width/2.0, height/2.0]
        ship.THRUST = 0.05
        ship.theta = 180
        ship.keyflags = [False, False, False, False]
        
    def draw(ship):
        if not (ship.location == None):
            # bounding box for the ship
            ship.rect = pygame.rect.Rect(ship.location[0]-ship.width/2, ship.location[1]-ship.height/2, ship.width, ship.height)

            if ship.invincibility > 0:
                shipinpaint = ship.paint
                ship.ivc += 1
                nb = ship.invincibility*20
                if ship.ivc % nb < 6:
                    shipinpaint = (55,55,55)
                    shippaint = (255,255,0)
                else:
                    shippaint = ship.edgepaint
            else:
                shipinpaint = ship.paint
                shippaint = ship.edgepaint
            
            # Dealing with Ship Rotation
            for i,p in enumerate(ship.points):
                xp = p[1]*sin(radians(ship.theta+p[0]))*ship.scale
                yp = p[1]*cos(radians(ship.theta+p[0]))*ship.scale
                ship.rotpoints[i] = [ship.location[0]+xp, ship.location[1]+yp]
            pygame.draw.polygon(DISPLAYSURF, shipinpaint, ship.rotpoints)
            pygame.draw.aalines(DISPLAYSURF, shippaint, True, ship.rotpoints, True)

            # Invincibility Shield
            if ship.invincibility > 0:
                pygame.draw.circle(DISPLAYSURF, (255,255,0), (ship.rect.centerx, ship.rect.centery), 18, 1)
                                   

            # Draw Thrust Particles
            for par in ship.thrust_particles:
                if par[2] > 10:
                    red = 40 + random.randint(0,32)
                    green = par[2] + random.randint(0,32)
                elif par[2] > 5:
                    red = 80 + random.randint(0,32)
                    green = par[2] + random.randint(0,32)
                else:
                    red = 223 - par[2]*8 + random.randint(0,32)
                    green = 0 + random.randint(0,32)
                DISPLAYSURF.set_at((int(par[0][0]), int((par[0][1]))), (red,green,0))
                
        # Draw shots
        for s in ship.shots:
            s.draw()     

        # Draw Death Particles
        for par in ship.death_particles:
            DISPLAYSURF.set_at((int(par[0][0]), int((par[0][1]))), (max(0,255-par[2]*2),max(0,255-par[2]*2),max(0,255-par[2]*2)))
    
        
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()

# set up fonts
#basicFont = pygame.font.SysFont(None, 48)
basicFont = pygame.font.Font("freesansbold.ttf", 48)
DISPLAYSURF = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pysteroids')

keys =  [K_RIGHT, K_LEFT, K_DOWN, K_UP]
keys2 = [K_d,     K_a,    K_s,    K_w]
playership = PlayerShip()
enemies = []
items = []
extralife = 0
FPS = 120
fpsClock = pygame.time.Clock()


class GameText():
    def __init__(txt, string, xloc=0.5, yloc=0.5, fontSz=24, fontCl = (255,255,255)):
        txt.name = string
        txt.font_size = fontSz
        txt.font_color = fontCl
        txt.font = pygame.font.Font("freesansbold.ttf", int(txt.font_size/1.5))
        txt.text = txt.font.render(txt.name, True, txt.font_color)
        txt.rect = txt.text.get_rect()
        txt.xloc = xloc
        txt.yloc = yloc
        txt.rect.left = (DISPLAYSURF.get_rect().width - txt.rect.width) * txt.xloc
        txt.rect.top = (DISPLAYSURF.get_rect().height - txt.rect.height) * txt.yloc
    def setString(txt, string):
        txt.name = string
        txt.text = txt.font.render(txt.name, True, txt.font_color)
        txt.rect = txt.text.get_rect()
        txt.rect.left = (DISPLAYSURF.get_rect().width - txt.rect.width) * txt.xloc
        txt.rect.top = (DISPLAYSURF.get_rect().height - txt.rect.height) * txt.yloc
        
        
gameTitles = [GameText("Pysteroids", 0.50, 0.10, 48),
              GameText("Spacebar/MouseClick to Shoot.  Arrow Keys/ASWD to Fly.  Q to quit a live game.", 0.50, 0.22, 16),
              GameText("Fly into a below option to Start.", 0.50, 0.40, 24),
              GameText("Play Normal", 0.20, 0.80, 24),
              GameText("Play Hard", 0.50, 0.80, 24),
              GameText("Play Insane", 0.80, 0.80, 24),
              GameText("Ship Painter", 0.05, 0.95, 24),
              GameText("Help & About", 0.95, 0.95, 24)]

shipPainterTitles = [GameText("Back", 0.05, 0.05, 24),
                     GameText("Edge Paint", 0.30, 0.30, 24),
                     GameText("Hull Paint", 0.70, 0.30, 24),
                     GameText("Red", 0.90, 0.40, 24),
                     GameText("Green", 0.90, 0.50, 24),
                     GameText("Blue", 0.90, 0.60, 24),
                     GameText("Edge Paint", 0.30, 0.30, 24),
                     GameText("Red", 0.10, 0.40, 24),
                     GameText("Green", 0.10, 0.50, 24),
                     GameText("Blue", 0.10, 0.60, 24),
                     GameText("Fly into an RGB Color Option and Rotate to Adjust the Paint.", 0.50, 0.15, 24)]

inGameTitles = [GameText("0", 0.10, 0.02, 24), #lives
                GameText("0", 0.50, 0.02, 24), #score
                GameText("0", 0.90, 0.02, 24), #level
                GameText("Shot Type I", 0.05, 0.09, 16),
                GameText("Gun Power: " + str(playership.shot_power), 0.90, 0.09, 16)]

gameOverTitles = [GameText("Game Over!", 0.50, 0.30, 48),
                  GameText("Final Score:", 0.50, 0.50, 24),
                  GameText("Back", 0.05, 0.05)]

timerTicker = GameText("", 0.50, 0.50, 48)

helpTitles = [GameText("Pysteroids", 0.50, 0.10, 48),
              GameText("Asteroids in Python", 0.50, 0.22, 24),
               GameText("Designed and Programmed by Joe Krall, Spring 2013.", 0.50, 0.32, 16),
               GameText("How to Play: Defeat all asteroids by shooting and evading them.", 0.50, 0.42, 16),             
               GameText("Collect items to improve your ship.", 0.50, 0.62, 24),
               GameText("(A): Increase Gun Power", 0.05, 0.75, 16),
               GameText("(S): Increase Gun Speed", 0.50, 0.75, 16),
               GameText("(H): Temporary Ship Shield", 0.95, 0.75, 16),
               GameText("(1): Improve Type I", 0.05, 0.85, 16),
               GameText("(2): Improve Type II Guns", 0.50, 0.85, 16),
               GameText("(3): Improve Type III Guns", 0.95, 0.85, 16),
               GameText("(P): Gain 2500 Points", 0.50, 0.95, 16),
               GameText("Back", 0.95, 0.05, 24)]
               

firstPlay = True
mainGame = False
shipPainter = False
gameOver = False
helpWindow = False

def play_random_song(l, cur):
    while True:
        selection = random.choice(l)
        if not (selection == cur):
            break   
   
    
    current_song = selection
    try:
        pygame.mixer.music.load(selection)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.6)
        SONG_END = pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(SONG_END)
        return SONG_END
    except:
        print "Music (" + selection + ") did not load properly."
        return None
   
# Background Music
current_song = None
SONG_END = None
NEW_ROUND = None
TICKER = None
NEW_ITEM = None
ITEM_DIES = None
songs = ['FromHere.ogg', 'Deeper.ogg']
SONG_END = play_random_song(songs, current_song)


# Sounds
shot_sound = pygame.mixer.Sound('SmallExplosion8-Bit.ogg')
shot_sound.set_volume(0.2)
blown_up_sound = pygame.mixer.Sound('MediumExplosion8-Bit.ogg')
blown_up_sound.set_volume(0.2)

# Background Stars
stars = []
for i in range(150):
    x = random.randint(0,width)
    y = random.randint(0,height)
    xvel = random.uniform(-0.005, 0.005)
    yvel = random.uniform(-0.005, 0.005)
    stars.append([[x,y], [xvel, yvel], (150, 150, 150)])

clock = pygame.time.Clock()

while True:

    DISPLAYSURF.fill((0,0,0))
    # Handle Key Flags for Movement      
    for k,keyflag in enumerate(playership.keyflags):
        if keyflag:
            if k < 2: # Rotation Controls 
                playership.theta += [-1.0, 1.0][k]
            elif k == 2: # Brake
                playership.velocity[0] *= playership.BRAKING_FORCE
                playership.velocity[1] *= playership.BRAKING_FORCE
            else: # Thrust
                playership.velocity[0] = playership.velocity[0] + playership.THRUST*sin(radians(playership.theta))
                playership.velocity[1] = playership.velocity[1] + playership.THRUST*cos(radians(playership.theta))
                # Thrust Flames
                if playership.thrust_flame == False and not(playership.location == None):
                    for repeat in range(random.randint(10,20)):
                        angle = -playership.theta-90 + random.random()*30 - 15.0
                        loc = [playership.location[0]+6*cos(radians(angle)),playership.location[1]+6*sin(radians(angle))]
                        spd = random.uniform(0.1, 0.5)
                        speed = [ spd*cos(radians(angle)), spd*sin(radians(angle)) ]
                        playership.thrust_particles.append([loc, speed, 0])

    
            
    # Move & Draw the Player Ship
    playership.fly()
    playership.draw()

    # Move & Draw Enemies
    for enemy in enemies:
        enemy.fly()
        enemy.draw()

    # Draw Items
    for item in items:
        item.draw()

    # Collision Detection - Shots vs Enemies
    for enemy in enemies:
        for shot in playership.shots:
            if ((shot.location[0]-enemy.location[0])**2)+((shot.location[1]-enemy.location[1])**2) <= enemy.size**2:
                enemy.hp -= shot.power
                score += 10*difficulty
                extralife += 10*difficulty
                enemy.hit()
                if enemy.hp <= 0:
                    try:
                        enemies.remove(enemy)
                        score += 100
                        extralife += 100
                    except:
                        pass
                inGameTitles[1].setString("Score: " + str(score))
                if extralife >= 10000:
                    extralife -= 10000
                    playership.lives += 1
                    inGameTitles[0].setString("Lives: " + str(playership.lives))
                playership.shots.remove(shot)
                continue
            
    # Collision Detection - Ship vs Items
    if not(playership.location == None):
        for item in items:
            if playership.collides(item.rect):
                if item.type == "Attack Sphere":
                    playership.shot_power += 1
                    inGameTitles[4].setString("Gun Power: " + str(playership.shot_power))
                if item.type == "Point Sphere":
                    score += 2500
                    if extralife >= 10000:
                        extralife -= 10000
                        playership.lives += 1
                        inGameTitles[0].setString("Lives: " + str(playership.lives))
                    inGameTitles[1].setString("Score: " + str(score))
                if item.type == "Speed Sphere":
                    playership.shot_speed += 0.25
                if item.type == "Shield Sphere":
                    playership.invincibility += 10
                if item.type == "Type I Weapon Sphere":
                    playership.max_shots += 5
                    playership.shot_mode = 0
                    playership.shot_level[playership.shot_mode] = min(3, playership.shot_level[playership.shot_mode]+1)
                    inGameTitles[3].setString("Gun Type I:")
                if item.type == "Type II Weapon Sphere":
                    playership.max_shots += 5
                    playership.shot_mode = 1
                    playership.shot_level[playership.shot_mode] = min(3, playership.shot_level[playership.shot_mode]+1)
                    inGameTitles[3].setString("Gun Type II:")
                if item.type == "Type III Weapon Sphere":
                    playership.max_shots += 5
                    playership.shot_mode = 2
                    playership.shot_level[playership.shot_mode] = min(2, playership.shot_level[playership.shot_mode]+1)
                    inGameTitles[3].setString("Gun Type III:")
                items.remove(item); continue

    # Collision Detection - Enemies vs Enemies
    for e1 in enemies:
        for e2 in enemies:
            if not(e1 == e2):
                collision = False
                for p in e1.drawPoints:
                    if ((p[0]-e2.location[0])**2)+((p[1]-e2.location[1])**2) <= e2.size**2 and not collision:
                        A = radians(atan2(e2.location[0]-e2.location[1], e1.location[0]-e1.location[1]))
                        m1 = sqrt(e1.velocity[0]**2 + e1.velocity[1]**2)
                        m2 = sqrt(e2.velocity[0]**2 + e2.velocity[1]**2)
                        dir1 = atan2(e1.velocity[1], e1.velocity[0])
                        dir2 = atan2(e2.velocity[1], e2.velocity[0])
                        n1 = [m1*cos(dir1-A), m2*cos(dir2-A)]
                        n2 = [m2*sin(dir1-A), m2*sin(dir2-A)]
                        f1 = [((e1.size-e2.size)*n1[0]+(e2.size*2)*n1[1])/(e1.size+e2.size),((e2.size-e1.size)*n1[1]+(e2.size*2)*n1[0])/(e1.size+e2.size)]
                        f2 = [n2[0], n2[1]]
                        
                        e1.velocity[0] = cos(A)*f1[0]+cos(A+pi/2)*f1[1]
                        e1.velocity[1] = sin(A)*f1[0]+sin(A+pi/2)*f1[1]
                        e2.velocity[0] = cos(A)*f2[0]+cos(A+pi/2)*f2[1]
                        e2.velocity[1] = sin(A)*f2[0]+sin(A+pi/2)*f2[1]

                        
                        e1.location[0] +=   e1.velocity[0]
                        e1.location[1] +=   e1.velocity[1]
                        e2.location[0] +=   e2.velocity[0]
                        e2.location[1] +=   e2.velocity[1]
                        
                        collision = True

    # Collision Detection - Enemies vs Ship
    if not(playership.location == None) and playership.invincibility <= 0:
        for enemy in enemies:
            for p in enemy.drawPoints:
                if playership.rect.collidepoint(p):
                     blown_up_sound.play(0)
                     playership.die()
                     if playership.shot_mode == 0:
                         inGameTitles[3].setString("Gun Type I:")
                     elif playership.shot_mode == 1:
                         inGameTitles[3].setString("Gun Type II:")
                     elif playership.shot_mode == 2:
                         inGameTitles[3].setString("Gun Type III:")
                     inGameTitles[0].setString("Lives: " + str(playership.lives))
                     if playership.lives < 0:
                         enemies = []
                         mainGame = False
                         gameOver = True
        
            
    # Update & Draw Background Stars
    for star in stars:
        star[0][0] = (star[0][0]+star[1][0]) % width
        star[0][1] = (star[0][1]+star[1][1]) % height
        if random.random() < 0.01:
            star[2] = (255,255,255)
        else:
            star[2] = (150,150,150)
        DISPLAYSURF.set_at((int(star[0][0]), int((star[0][1]))), star[2])
    
    # First Play
    if firstPlay:
        for gameTitle in gameTitles:
            DISPLAYSURF.blit(gameTitle.text, gameTitle.rect)

            # Check collision into boxes
            if gameTitle.name == "Play Normal" and playership.collides(gameTitle.rect):
                firstPlay = False
                mainGame = True
                difficulty = 1
                level = 1
                lives = 3
                score = 0
                timer = 3
                timerTicker.setString(str(timer))
                TICKER = pygame.USEREVENT+3
                pygame.time.set_timer(TICKER, 1000)
                NEW_ROUND = pygame.USEREVENT+2
                pygame.time.set_timer(NEW_ROUND, 3000)
                inGameTitles[0].setString("Lives: " + str(lives))
                inGameTitles[1].setString("Score: " + str(score))
                inGameTitles[2].setString("Level: " + str(level))
                NEW_ITEM = pygame.USEREVENT+4
                pygame.time.set_timer(NEW_ITEM, 1000*random.randint(15,30))

                
            if gameTitle.name == "Play Hard" and playership.collides(gameTitle.rect):
                firstPlay = False
                mainGame = True
                difficulty = 2
                level = 1
                lives = 3
                score = 0
                timer = 3
                timerTicker.setString(str(timer))
                TICKER = pygame.USEREVENT+3
                pygame.time.set_timer(TICKER, 1000)
                NEW_ROUND = pygame.USEREVENT+2
                pygame.time.set_timer(NEW_ROUND, 3000)
                inGameTitles[0].setString("Lives: " + str(lives))
                inGameTitles[1].setString("Score: " + str(score))
                inGameTitles[2].setString("Level: " + str(level))
                NEW_ITEM = pygame.USEREVENT+4
                pygame.time.set_timer(NEW_ITEM, 1000*random.randint(15,30))

            if gameTitle.name == "Play Insane" and playership.collides(gameTitle.rect):
                firstPlay = False
                mainGame = True
                difficulty = 3
                level = 1
                lives = 3
                score = 0
                timer = 3
                timerTicker.setString(str(timer))
                TICKER = pygame.USEREVENT+3
                pygame.time.set_timer(TICKER, 1000)
                NEW_ROUND = pygame.USEREVENT+2
                pygame.time.set_timer(NEW_ROUND, 3000)
                inGameTitles[0].setString("Lives: " + str(lives))
                inGameTitles[1].setString("Score: " + str(score))
                inGameTitles[2].setString("Level: " + str(level))
                NEW_ITEM = pygame.USEREVENT+4
                pygame.time.set_timer(NEW_ITEM, 1000*random.randint(15,30))
                
            if gameTitle.name == "Ship Painter" and playership.collides(gameTitle.rect):
                firstPlay = False
                shipPainter = True

            if gameTitle.name == "Help & About" and playership.collides(gameTitle.rect):
                firstPlay = False
                helpWindow = True
                

    elif mainGame:
        for inGameTitle in inGameTitles:
            DISPLAYSURF.blit(inGameTitle.text, inGameTitle.rect)

        #shot type power gauges
        for i in range(playership.shot_level[playership.shot_mode]+1):
            r = Rect(inGameTitles[3].rect.right + (i+1)*22, 0.09*height, 20, 12)
            pygame.draw.rect(DISPLAYSURF, (180,180,180), r)
        for i in range(playership.max_level[playership.shot_mode]+1):
            r = Rect(inGameTitles[3].rect.right + (i+1)*22, 0.09*height, 20, 12)
            pygame.draw.rect(DISPLAYSURF, (255, 255,255), r, 1)
        
            
        if len(enemies) == 0 and NEW_ROUND == None:
            # New Level
            level += 1
            timer = 3
            timerTicker.setString(str(timer))
            TICKER = pygame.USEREVENT+3
            pygame.time.set_timer(TICKER, 1000)
            score += 1000
            extralife+= 1000
            if extralife >= 10000:
                    extralife -= 10000
                    playership.lives += 1
                    inGameTitles[0].setString("Lives: " + str(playership.lives))
            NEW_ROUND = pygame.USEREVENT+2
            pygame.time.set_timer(NEW_ROUND, 3000)
            inGameTitles[2].setString("Level: " + str(level))
            inGameTitles[1].setString("Score: " + str(score))
        if len(enemies) == 0 and not(NEW_ROUND == None):
            # Waiting on the new round
            DISPLAYSURF.blit(timerTicker.text, timerTicker.rect)
    elif shipPainter:
        for title in shipPainterTitles:
            DISPLAYSURF.blit(title.text, title.rect)

            #draw gauges for colors
            for i in range(7,10):
                pygame.draw.line(DISPLAYSURF, (255,255,255), (shipPainterTitles[8].rect.right+5, shipPainterTitles[i].rect.centery), (shipPainterTitles[8].rect.right+5+0.25*width, shipPainterTitles[i].rect.centery))
                pygame.draw.line(DISPLAYSURF, (255,255,255), (shipPainterTitles[8].rect.right+5+((playership.edgepaint[i-7]/255.0)*0.25*width),shipPainterTitles[i].rect.centery-5), (shipPainterTitles[8].rect.right+5+((playership.edgepaint[i-7]/255.0)*0.25*width),shipPainterTitles[i].rect.centery+5))
            for i in range(3,6):
                pygame.draw.line(DISPLAYSURF, (255,255,255), (shipPainterTitles[4].rect.left-5, shipPainterTitles[i].rect.centery), (shipPainterTitles[4].rect.left-5-0.25*width, shipPainterTitles[i].rect.centery))
                pygame.draw.line(DISPLAYSURF, (255,255,255), (shipPainterTitles[4].rect.left-5-width*0.25+((playership.paint[i-3]/255.0)*0.25*width),shipPainterTitles[i].rect.centery-5), (shipPainterTitles[4].rect.left-5-width*0.25+((playership.paint[i-3]/255.0)*0.25*width),shipPainterTitles[i].rect.centery+5))

            if playership.keyflags[0]:
                add = -1
            elif playership.keyflags[1]:
                add = 1
            else:
                add = 0
            if title.name == "Red" and title.xloc == 0.90 and playership.collides(title.rect): #hull red
               playership.paint = ((playership.paint[0]+add) % 255, playership.paint[1], playership.paint[2])
            if title.name == "Green" and title.xloc == 0.90 and playership.collides(title.rect): #hull green
                playership.paint = (playership.paint[0], (playership.paint[1]+add)%255, playership.paint[2])
            if title.name == "Blue" and title.xloc == 0.90 and playership.collides(title.rect): #hull blue
                playership.paint = (playership.paint[0], playership.paint[1], (playership.paint[2]+add)%255)
            if title.name == "Red" and title.xloc == 0.10 and playership.collides(title.rect): #hull red
                playership.edgepaint = ((playership.edgepaint[0]+add) % 255, playership.edgepaint[1], playership.edgepaint[2])
            if title.name == "Green" and title.xloc == 0.10 and playership.collides(title.rect): #hull green
                playership.edgepaint = (playership.edgepaint[0], (playership.edgepaint[1]+add)%255, playership.edgepaint[2])
            if title.name == "Blue" and title.xloc == 0.10 and playership.collides(title.rect): #hull blue
                playership.edgepaint = (playership.edgepaint[0], playership.edgepaint[1], (playership.edgepaint[2]+add)%255)

            shotPaintHandler = False
            if title.name == "Back" and playership.collides(title.rect):
                shipPainter = False
                firstPlay = True
                
    elif helpWindow:
        # Help & About Window
        for title in helpTitles:
            DISPLAYSURF.blit(title.text, title.rect)

            if title.name == "Back" and playership.collides(title.rect):
                helpWindow = False
                firstPlay = True
            
    elif gameOver:
        # Game Over Window
        gameOverTitles[1].setString("Final Score: " + str(score))
        for title in gameOverTitles:
            DISPLAYSURF.blit(title.text, title.rect)

            if title.name == "Back" and playership.collides(title.rect):
                gameOver = False
                firstPlay = True
                extralife = 0
                playership.new()
                
    pygame.display.flip()
    
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Catch New Round Event
        if event.type == NEW_ROUND and mainGame:
            NEW_ROUND = None
            playership.invincibility += 3
            enemies = [Asteroid(level, difficulty) for i in range(2*(difficulty) + (max(1, level/2)))]
                

        if event.type == TICKER:
            timer -= 1
            timerTicker.setString(str(timer))
            TICKER = pygame.USEREVENT+3
            pygame.time.set_timer(TICKER, 1000)
            if playership.invincibility > 0:
                playership.invincibility -= 1

        # Catch Item Event
        if event.type == NEW_ITEM and mainGame:
            itemtypes = [AttackSphere, SpeedSphere, ScoreSphere, ShieldSphere, TypeIWeaponSphere, TypeIIWeaponSphere, TypeIIIWeaponSphere]
            items.append(random.choice(itemtypes)())
            ITEM_DIES = pygame.USEREVENT+5
            pygame.time.set_timer(ITEM_DIES, 7000)
            NEW_ITEM = pygame.USEREVENT+4
            pygame.time.set_timer(NEW_ITEM, 1000*random.randint(15,30))

        # Catch Item Removal Event
        if event.type == ITEM_DIES:
            items = []
            
        # Catch Song End Event
        if event.type == SONG_END:
            play_random_song(songs, current_song)
            
        # Handle Key Input for Arrow Keys
        if event.type == KEYDOWN:
            for k,key,keyflag in zip(range(4),keys,playership.keyflags):
                if event.key == key:
                    playership.keyflags[k] = True
            for k,key,keyflag in zip(range(4),keys2,playership.keyflags):
                if event.key == key:
                    playership.keyflags[k] = True
            if event.key == K_SPACE:
                shot_sound.play(0)
                playership.shoot()
            if event.key == K_q:
                enemies = []
                items = []
                score = 0
                level = 0
                extralife = 0
                playership.new()
                firstPlay = True
                shipPainter = False
                gameOver = False
                mainGame = False
                helpWindow = False
            if event.key == K_p:
                play_random_song(songs, current_song)
                    
        if event.type == KEYUP:
            for k,key,keyflag in zip(range(4),keys,playership.keyflags):
                if event.key == key:
                    playership.keyflags[k] = False
            for k,key,keyflag in zip(range(4),keys2,playership.keyflags):
                if event.key == key:
                    playership.keyflags[k] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shot_sound.play(0)
                playership.shoot()
        
        
        
    fpsClock.tick(FPS)
