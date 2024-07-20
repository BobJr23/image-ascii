import time
import os
from asciimatics.screen import Screen
from blessings import Terminal
import pygame
import sys

# Initialize colorama to make ANSI escape sequences work on Windows
file_path = "ascii/sunset.txt"
frame_delay = 1 / 30  # Delay between frames in seconds
term = Terminal()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_ascii_blessings(file_path):
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into frames using 'p' as the delimiter
    frames = content.split('p')

    with term.fullscreen():
        print(term.clear)
        for frame in frames:  # Assuming `frames` is a list of frame strings
            print(term.move(0, 0) + frame)
            time.sleep(frame_delay)  # Control frame rate


def display_ascii_pygame(frames):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    running = True
    current_frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        frame_text = font.render(frames[current_frame], True, (0, 0, 0))
        screen.blit(frame_text, (10, 10))
        pygame.display.flip()

        current_frame = (current_frame + 1) % len(frames)
        clock.tick(1 / frame_delay)

    pygame.quit()


# Function to read frames from the file and display them
def display_ascii_video():
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into frames using 'p' as the delimiter
    frames = content.split('p')

    # Display each frame
    for frame in frames:
        clear_screen()  # Clear the screen for the first frame
        print(frame)  # Move cursor to top left and print the frame
        time.sleep(frame_delay)  # Wait for the specified delay


def play_video(screen):
    screen.clear()
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into frames using 'p' as the delimiter
    frames = content.split('p')

    for frame in frames:  # Assuming `frames` is a list of frame strings

        screen.print_at(frame, 0, 0, )
        screen.refresh()
        time.sleep(frame_delay)  # Control frame rate


# Screen.wrapper(play_video)
display_ascii_video()
# Path to the ASCII frames file

# Display the ASCII video
#
# display_ascii_video(file_path)
