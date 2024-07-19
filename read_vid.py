import time
import os
from asciimatics.screen import Screen

# Initialize colorama to make ANSI escape sequences work on Windows
file_path = "ascii/sunset.txt"

frame_delay = 1 / 30  # Delay between frames in seconds


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
