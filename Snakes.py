import pygame
from pygame.locals import *
import time
import random

size = 10

class SoundEffect:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("woosh.wav")

    def play(self):
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        

class Food:
    def __init__(self, parent_screen):
        self.food = pygame.image.load("Untitled.png")
        self.parent_screen = parent_screen
        self.x = 100
        self.y = 100

    def drawfood(self):
       self.parent_screen.blit(self.food, (self.x, self.y))
       pygame.display.flip()

    def move(self):
        self.x = size * random.randint(1, 70)
        self.y = size * random.randint(1, 50)
       
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.snake = pygame.image.load("Untitled.png")
        self.x = [size] * length
        self.y = [size] * length
        self.direction = "right"
        self.length = length

    def increaseLength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()
    def move_left(self):
        if self.direction != "right":
            self.direction = "left"
    def move_right(self):
        if self.direction != "left":
            self.direction = "right"
    def move_up(self):
        if self.direction != "down":
            self.direction = "up"
    def move_down(self):
        if self.direction != "up":
            self.direction = "down"
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]


        if self.direction == "right":
            self.x[0] += size
        if self.direction == "left":
            self.x[0] -= size
        if self.direction == "up":
            self.y[0] -= size
        if self.direction == "down":
            self.y[0] += size
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.dis = pygame.display.set_mode((800, 600))
        self.dis.fill((0, 0, 0))
        self.snake = Snake(self.dis, 3)
        self.snake.draw()
        self.food = Food(self.dis)
        self.food.drawfood()
        self.sound = SoundEffect()

    def expansion(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def run(self):
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                       self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    game_over = True
            self.snake.walk()
            self.food.drawfood()
            if self.expansion(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
                self.food.move()
                self.snake.increaseLength()
                self.sound.play()
            for i in range(2, self.snake.length):
                if self.expansion(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i],):
                    game_over = True
                    exit()
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game()
    game.run()