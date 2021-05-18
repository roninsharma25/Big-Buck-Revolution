# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# menuController.py: a controller for the menu screen

from models.buttonModel import Button
from inputController import *
from constants import *
import pygame
import json
import operator

class DoneController():
    """
    Menu Controller is a controller that handles updating and drawing the screen
    when the player is accessing and interacting with the main menu.
    """

    EXIT_MENU = 0
    EXIT_NAME = 1
    EXIT_QUIT = 2

    def __init__(self):
        """
        Instantiates a new menu
        """
        self.logo = pygame.image.load("assets/logo.png")

        if LARGE:
            self.buttons = [
                Button("Main Menu", (640, 450)),
                Button("Enter Name", (640, 700)),
                Button("Quit", (640, 950))
            ]
        else:
            self.buttons = [
                Button("Main Menu", (210, 250)),
                Button("Enter Name", (210, 350)),
                Button("Quit", (210, 450))
            ]
        self.exitCode = -1
        self.selected = 0
        self.buttons[self.selected].setSelected(True)
        self.enterName = False
        self.nameSet = False
        self.font = pygame.font.Font(None, 40)
        self.player1Score = -1
        self.winner = 1 # Player 1 wins
    
    def start(self, score, song):
        # Load the scores and names from a file
        # {Name1: score1, name2: score2}
        self.song = song
        with open(LEADERBOARD_JSON) as f:
            self.data = json.load(f)

        # Determine the winner
        if (self.player1Score != -1): # Multiplayer
            if (self.player1Score >= score): # Player 1 won
                self.newScore = self.player1Score
                self.winner = 1
            else:
                self.newScore = score
                self.winner = 2
        else:
            self.newScore = score

        # Font object, name, score
        self.leaderboardEntries = []
        for entry in self.data[song]:
            self.leaderboardEntries.append((pygame.font.Font(None, 40), entry[0], entry[1]))
        self.leaderboardEntries = sorted(self.leaderboardEntries, key = operator.itemgetter(2), reverse = True)
        
        self.newEntryName = ["Enter Name"]
        self.newEntryIndex = 0
        self.enterName = False
        self.nameSet = False

    def update(self, input, dt):
        """
        Translates input actions into menu actions
        """
        self.exitCode = -1
        if input.pressed_back():
            InputController.should_quit = True

        if not self.enterName:
            if input.pressed_right():
                self.buttons[self.selected].setHighlighted(True)
            elif input.released_right():
                self.buttons[self.selected].setHighlighted(False)
                self.exitCode = self.selected
                if self.selected == DoneController.EXIT_NAME and not self.nameSet:
                    self.enterName = True
                    self.newEntryName = ["A"]*3
                    self.newEntryIndex = 0
            elif input.pressed_down() and not self.buttons[self.selected].highlighted:
                self.buttons[self.selected].setSelected(False)
                self.selected = min(self.selected + 1, len(self.buttons) - 1)
                self.buttons[self.selected].setSelected(True)
            elif input.pressed_up() and not self.buttons[self.selected].highlighted:
                self.buttons[self.selected].setSelected(False)
                self.selected = max(self.selected - 1, 0)
                self.buttons[self.selected].setSelected(True)
            
        # Control the letters that are displayed
        else:
            print(self.newEntryIndex)
            if self.selected == DoneController.EXIT_NAME:
                if input.pressed_up():
                    newLet = chr(ord(self.newEntryName[self.newEntryIndex]) - 1)
                    if newLet < "A":
                        newLet = "Z"
                    self.newEntryName[self.newEntryIndex] = newLet
                elif input.pressed_down():
                    newLet = chr(ord(self.newEntryName[self.newEntryIndex]) + 1)
                    if newLet > "Z":
                        newLet = "A"
                    self.newEntryName[self.newEntryIndex] = newLet
                elif input.pressed_left():
                    self.newEntryIndex -= 1
                    self.newEntryIndex = max(0, self.newEntryIndex)
                elif input.released_right():
                    self.newEntryIndex += 1
                    if self.newEntryIndex == 3:
                        self.enterName = False
                        self.nameSet = True
                        self.leaderboardEntries.append((pygame.font.Font(None, 40), "".join(self.newEntryName), self.newScore))
                        self.leaderboardEntries = sorted(self.leaderboardEntries, key = operator.itemgetter(2), reverse = True)
                        
                        # Update json
                        self.data[self.song].append(["".join(self.newEntryName), self.newScore])

                        with open(LEADERBOARD_JSON, "w") as f:
                            json.dump(self.data, f)
                        

        self.buttons[1].updateText("".join(self.newEntryName))

    def draw(self, view, dt):
        """
        Draws buttons to view
        """
        textScore = self.font.render("Score: " + str(self.newScore), True, WHITE)
        view.blit(textScore, textScore.get_rect(center = WINNER_TEXT_SCORE))

        view.blit(self.logo, self.logo.get_rect())
        for button in self.buttons:
            button.draw(view, dt)
        
        text = self.font.render("Leaderboard", True, WHITE)
        view.blit(text, text.get_rect(center= LEADERBOARD_TEXT_POS))

        count = 0
        for entry in self.leaderboardEntries:
            entryText = str(entry[1]) + ": " + str(entry[2])
            entryButton = entry[0].render(entryText, True, WHITE)
            entryRect = entryButton.get_rect(topleft = (NAME_BUTTON[0], NAME_BUTTON[1] + count))
            view.blit(entryButton, entryRect)
            count += LEADERBOARD_CHANGE

        # Display winner if multiplayer
        if (self.player1Score != -1):
            text = self.font.render("Winner: Player " + str(self.winner), True, WHITE)
            view.blit(text, text.get_rect(center = WINNER_TEXT_POS))
