# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# inputController.py: a controller that processes inputs

from constants import *
import RPi.GPIO as GPIO
import pygame

#def quit_callback(channel):
#    InputController.should_quit = True

class InputController():
    """
    Input Controller is a controller that translates button inputs into
    actions.
    """
    # A static flag that is True iff the game should quit
    should_quit = False

    def __init__(self):
        """
        Instantiates a new input controller and sets up GPIO Pins
        """
        GPIO.setmode(GPIO.BCM)
        
        # Set up quit button
        #GPIO.setup(IN_QUIT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(IN_QUIT, GPIO.FALLING, callback=quit_callback,\
        #        bouncetime=400)

        # Set up pressure pads and back button
        for input_pin in [IN_LEFT, IN_RIGHT, IN_DOWN, IN_UP, BACK]:
            GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Set up LEDs
        self.pwm = {}
        for output_pin in OUTPUT_PINS:
            GPIO.setup(output_pin, GPIO.OUT)
            self.pwm[output_pin] = GPIO.PWM(output_pin, 100)
            self.pwm[output_pin].start(0)

        self.prev_left = False
        self.curr_left = False
        self.prev_right = False
        self.curr_right = False
        self.prev_down = False
        self.curr_down = False
        self.prev_up = False
        self.curr_up = False
        self.prev_back = False
        self.curr_back = False
        self.prev_mouse = False
        self.curr_mouse = False
        self.prev_pos = (0, 0)
        self.curr_pos = (0, 0)

        self.index = 0

    def update(self, dt):
        """
        Processes inputs from GPIO Pins
        """
        # Remember previous actions
        self.prev_left = self.curr_left
        self.prev_right = self.curr_right
        self.prev_down = self.curr_down
        self.prev_up = self.curr_up
        self.prev_back = self.curr_back
        self.prev_mouse = self.curr_mouse
        self.prev_pos = self.curr_pos

        # Read current actions
        self.curr_left = GPIO.input(IN_LEFT) == GPIO.LOW
        self.curr_right = GPIO.input(IN_RIGHT) == GPIO.LOW
        self.curr_down = GPIO.input(IN_DOWN) == GPIO.LOW
        self.curr_up = GPIO.input(IN_UP) == GPIO.LOW
        self.curr_back = GPIO.input(BACK) == GPIO.LOW
        self.curr_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                self.curr_mouse = True
            elif event.type is pygame.MOUSEBUTTONUP:
                self.curr_mouse = False
            
        if self.pressed_left():
            self.index += 1
            self.lightButton("left", COLORS[self.index % len(COLORS)])

    def terminate(self):
        for output_pin in OUTPUT_PINS:
            GPIO.output(output_pin, GPIO.LOW)
        GPIO.cleanup()
        

    def pressed_left(self):
        return self.curr_left and not self.prev_left

    def released_left(self):
        return self.prev_left and not self.curr_left

    def pressed_right(self):
        return self.curr_right and not self.prev_right

    def released_right(self):
        return self.prev_right and not self.curr_right

    def pressed_down(self):
        return self.curr_down and not self.prev_down

    def released_down(self):
        return self.prev_down and not self.curr_down

    def pressed_up(self):
        return self.curr_up and not self.prev_up

    def released_up(self):
        return self.prev_up and not self.curr_up
    
    def pressed_back(self):
        return self.curr_back and not self.prev_back

    def released_back(self):
        return self.prev_back and not self.curr_back

    def pressed_mouse(self):
        return self.curr_mouse and not self.prev_mouse

    def released_mouse(self):
        return self.prev_mouse and not self.curr_mouse

    def directionPressed(self):
        if self.pressed_left():
            return 1
        if self.pressed_down():
            return 2
        if self.pressed_up():
            return 3
        if self.pressed_right():        
            return 4

        return 0

    def lightButton(self, button, color):
        """
        """
        if button == "rim":
            print("TODO")
            print(color)
        else:
            for i in range(3):
                self.pwm[LED_BUTTONS[button][i]].ChangeDutyCycle(LED_COLORS[color][i])
