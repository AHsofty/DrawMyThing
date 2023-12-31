import pygame
from Pen import Pen
import GlobalVariables
from EventHandler import EventHandler
from BoardDraw import Board
from ClientDir import Client

pygame.init()

# Sets up the scene
screen = pygame.display.set_mode((1100, 600))
BGCOLOR = (255, 255, 255)
screen.fill(BGCOLOR)
pygame.display.flip()

# Creates a client
client = Client.Client(screen)

# Sets up variables
pen = Pen(screen)
is_pressed = False
running = True
is_turn_to_draw = True
event_handler = EventHandler(screen, client)

client.assign_event_handler(event_handler)

# Draws the board
board = Board(screen)
board.draw_stage()

while GlobalVariables.running:
    event_handler.handle_events()

pygame.quit()
