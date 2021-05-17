# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# game.py: the main entrypoint for the game

from constants import *
from controllers import *
from controllers.inputController import InputController
from controllers.menuController import MenuController
from controllers.gameController import GameController
from controllers.selectController import SelectController
from controllers.difficultyController import DifficultyController
from controllers.editController import EditController
from controllers.doneController import DoneController
import RPi.GPIO as GPIO
import pygame
import time
import os

class Game():
    """
    The game that this script starts
    """
    def __init__(self):
        # Initialize view
        os.putenv("SDL_MOUSEDEV", "/dev/input/touchscreen")
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(NAME)
        self.view = pygame.display.set_mode(SIZE)
        self.state = STATE_MENU
        
        # Initialize controllers
        self.inputController = InputController()
        self.menuController = MenuController()
        self.gameController = GameController()
        self.selectController = SelectController()
        self.difficultyController = DifficultyController()
        self.editController = EditController()
        self.doneController = DoneController()

    def run(self):
        prev = time.time()
        curr = time.time()
        while not InputController.should_quit:

            # Time increments
            time.sleep(1/FPS)
            prev = curr
            curr = time.time()
            dt = curr - prev

            # Game updates then draws
            self.update(dt)
            self.draw(dt)

        self.terminate()

    def update(self, dt):
        # Process inputs
        self.inputController.update(dt)

        # Update appropriate controller based on state and change state if necessary
        if self.state == STATE_MENU:
            self.updateStateMenu(dt)
        if self.state == STATE_SELECTSCREEN:
            self.selectController.should_exit = False
            self.updateStateSelectScreen(dt)
        if self.state == STATE_SINGLEPLAYER:
            self.updateStateSingleplayer(dt)
        if self.state = STATE_DIFFICULTY:
            self.updateStateDifficulty(dt)
        if self.state == STATE_EDITOR:
            self.updateStateEditor(dt)
        if self.state == STATE_DONE:
            self.updateStateDone(dt)

    def draw(self, dt):
        # Clear the screen
        self.view.fill(BLACK)

        # Draw appropriate controller based on state
        if self.state == STATE_MENU:
            self.menuController.draw(self.view, dt)
        if self.state == STATE_SINGLEPLAYER:
            self.gameController.draw(self.view, dt)
        if self.state == STATE_SELECTSCREEN:
            self.selectController.draw(self.view, dt)
        if self.state == STATE_DIFFICULTY:
            self.difficultyController.draw(self.view, dt)
        if self.state == STATE_EDITOR:
            self.editController.draw(self.view, dt)
        if self.state == STATE_DONE:
            self.doneController.draw(self.view, dt)

        # Finalize changes
        pygame.display.flip()

    def terminate(self):
        self.inputController.terminate()

    def updateStateMenu(self, dt):
        self.menuController.update(self.inputController, dt)
        #if self.menuController.exitCode == MenuController.EXIT_SINGLEPLAYER:
        #    self.state = STATE_SELECTSCREEN
        #elif self.menuController.exitCode == MenuController.EXIT_LEVELEDITOR:
            #self.state = STATE_EDITOR
            #self.editController.start()
        if self.menuController.exitCode != -1:
            self.state = STATE_SELECTSCREEN
            self.selectController.start(self.menuController.exitCode == EXIT_LEVELEDITOR)

    def updateStateSingleplayer(self, dt):
        self.gameController.update(self.inputController, dt)
        if self.gameController.should_exit:
            self.state = STATE_MENU
        elif self.gameController.done:
            self.state = STATE_DONE
            self.doneController.start(self.gameController.score)
    
    def updateStateSelectScreen(self, dt):
        self.selectController.update(self.inputController, dt)
        if self.selectController.should_exit:
            self.state = STATE_MENU
            self.selectController.exitCode = -1
            self.selectController.flag = False
        elif self.selectController.exitCode != -1:
            #self.state = STATE_SINGLEPLAYER
            #self.gameController.start(self.selectController.exitCode)
            self.difficultyController.start(self.selectController.exitCode)
            self.state = STATE_DIFFICULTY
    
    def updateStateDifficulty(self, dt):
        self.difficultyController.update(self.inputController, dt)
        if self.difficultyController.should_exit:
            self.state = STATE_SELECT_SCREEN
            self.difficultyController.exitCode = -1
            self.difficultyController.flag = False
        elif self.difficultyController.exitCode != -1:
            if self.selectController.levelSelect:
                self.state = STATE_EDITOR
                self.editController.start(self.difficultController.song, self.difficultyController.exitCode == 0)
            else:
                self.state = STATE_SINGLEPLAYER
                self.gameController.start(self.difficultyController.song, self.difficultyController.exitCode == 0)

    def updateStateEditor(self, dt):
        self.editController.update(self.inputController, dt)
        if self.editController.done:
            #self.state = STATE_MENU
            self.state = STATE_SINGLEPLAYER
            self.gameController.start(self.editController.index, self.editController.bbb, (True, self.editController.newLevel))
    
    def updateStateDone(self, dt):
        self.doneController.update(self.inputController, dt)
        if self.doneController.exitCode == DoneController.EXIT_MENU:
            self.state = STATE_MENU
        elif self.doneController.exitCode == DoneController.EXIT_QUIT:
            InputController.should_quit = True


if __name__ == "__main__":
    game = Game()
    game.run()

