import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import requests
import sys
import pyautogui
import os
import time
import webbrowser
from datetime import datetime
from subprocess import call
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from PIL import ImageDraw
from tkinter import*
from PIL import Image

# Initialize speech recognition and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            return command
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")
    elif hour >= 12 and hour < 17:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("Ready to comply. What can I do for you?")

def open_game_file():
    call(["python", "flappy.py"])

def run_alexa():

    command = take_command()
    if command:
        if "stop listening" in command:
            stop_listening()
    if command is None:
        talk('Sorry, I did not understand that. Please try again.')
        return
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'close youtube' in command:
        talk("Closing YouTube")
        os.system('taskkill /im chrome.exe')
    elif 'open youtube' in command:
        talk("What would you like to watch?")
        qrry = take_command()
        pywhatkit.playonyt(qrry)
    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'open google' in command:
        talk("opening google")
        talk("What should I search?")
        qry = take_command()
        webbrowser.open(f"https://www.google.com/search?q={qry}")
    elif 'close google' in command:
        talk("Closing Google")
        os.system('taskkill /im chrome.exe')
    elif 'joke' in command:
        talk("the joke is")
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        talk('Goodbye')
        sys.exit()
    elif 'exit' in command or 'go to sleep' in command:
        talk("Alright then, I am switching off.")
        sys.exit()
    elif 'take screenshot' in command:
        talk("Taking screenshot. Please wait...")
        region = (100, 100, 500, 400)
        img = pyautogui.screenshot(region=region)
        img.save("region_screenshot.png")
        talk("Screenshot saved as screenshot.png")
    elif 'wish me' in command:
        wishMe()
    elif 'open notepad' in command:
        talk('Opening notepad')
        os.system("notepad.exe")
    elif 'close notepad' in command:
        talk("Closing notepad")
        os.system('taskkill /im notepad.exe')
    elif "open command prompt" in command:
        talk("Opening command prompt")
        os.system("start cmd")
    elif 'close notepad' in command:
        talk("Closing notepad")
        os.system('taskkill /im cmd.exe')
    elif 'drag visual studio to the right' in command:
        talk("Dragging VS Code to right")
        pyautogui.moveTo(46, 31, 2)
        pyautogui.dragRel(1857, 31, 2)
    elif "scroll down" in command:
        talk("Scrolling down")
        pyautogui.scroll(1000)
    elif 'date' in command:
        talk("The current date is")
        current_date = datetime.now().strftime("%A,%d %B %Y")
        talk(current_date)
    elif 'who are you' in command:
        talk("My name is Radhika. I am your personal assistant. I can do everything my creator programmed me to do.")
    elif 'who created you' in command:
        talk("I was created using Python programming language in Visual Studio Code.")
    elif 'volume up' in command:
        talk("raising volume")
        for _ in range(15):
            pyautogui.press("volumeup")
    elif 'game' in command:
        talk("Playing bird game")
        open_game_file()
    elif 'close game ' in command:
        talk("stoping the game")
        window.destroy()
    elif 'volume down' in command:
        ("making volume up")
        for _ in range(15):
            pyautogui.press("volumedown")
    elif 'mute' in command:
        pyautogui.press("volumemute")
    elif 'calculator' in command:
        talk('Opening calculator')
        os.system("calc.exe")
    elif 'calendar' in command:
        talk("Opening calendar")
        os.system("start outlookcal:")
    elif 'camera' in command:
        talk("Opening camera")
        os.system("start microsoft.windows.camera:")
    elif "refresh" in command:
        talk("Refreshing system")
        pyautogui.moveTo(1551, 551, 2)
        pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        pyautogui.moveTo(1620, 667, 1)
        pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        talk("System refreshed")
    else:
        talk('Please say the command again.')

def start_listening():
    talk("i am listening to you,how can i help you")
    # Start listening when the button is clicked
    run_alexa()

def stop_listening():
    """Function to stop the application."""
    talk("Stopping the application. Goodbye!")
    window.destroy()  # Closes the Tkinter window and stops the application

def create_circular_image(image_path, size):
    """Create a circular version of the given image."""
    img = Image.open("micro.png").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    circular_img = Image.new("RGBA", (size, size))
    circular_img.paste(img, (0, 0), mask)
    return circular_img


def fade_in(canvas, image_id, step=5, delay=50):
    """Create a fade-in effect for the image on canvas."""
    current_opacity = 0
    while current_opacity < 1:
        current_opacity += 0.05  # Increase opacity
        # Modify the image transparency using after and update the canvas
        canvas.itemconfig(image_id, stipple=f"gray{int(current_opacity * 100)}")
        window.after(delay)  # Wait for a short time
        window.update()



def create_rounded_button(parent, text, command, width=15, height=2, color="white", fg="black"):
    """Create a button with rounded corners."""
    # Create a regular Button widget and apply styling to give it rounded corners
    button = Button(parent, text=text, command=command, width=width, height=height, bg=color, fg=fg, relief="flat")
    button.place(relx=0.5, rely=0.5, anchor="center")  # Adjust the position as needed
    return button



# Set up the GUI
window = tk.Tk()
window.title("Radhika - Voice Assistant")
window.configure(bg="black")

# Make the window full-screen
window.attributes("-fullscreen", True)

# Create a circular image
circular_image = create_circular_image("micro.png", 300)  # Replace "logo.png" with your image file
circular_image_tk = ImageTk.PhotoImage(circular_image)

# Create a canvas to display the image
canvas = tk.Canvas(window, width=400, height=400, bg="black", bd=0, highlightthickness=0)
canvas.place(relx=0.5, rely=0.3, anchor="center")  # Center the canvas

# Add the circular image to the canvas
image_id = canvas.create_image(200, 200, image=circular_image_tk)




# Create Start Listening button with rounded corners
start_button = create_rounded_button(window, "Start Listening", start_listening, color="yellow", fg="black")

# Create Stop Running button with rounded corners
stop_button = create_rounded_button(window, "Stop Running", stop_listening, color="red", fg="black")

# Place buttons next to each other horizontally
start_button.place(relx=0.4, rely=0.7, anchor="center")
stop_button.place(relx=0.6, rely=0.7, anchor="center")

# Function to make the image vibrate
def vibrate_image(canvas, image_id, offset=10, count=10, step=1):
    """Make the image vibrate by moving it back and forth."""
    if count > 0:
        canvas.move(image_id, step, 0)  # Move right by 'step'
        canvas.after(50, vibrate_image, canvas, image_id, offset, count - 1, -step)  # Move back in the opposite direction after a short delay
    else:
        canvas.after(50, vibrate_image, canvas, image_id, offset, count, step)  # Repeat vibration


# Start the vibration effect immediately
window.after(500, lambda: vibrate_image(canvas, image_id, step=10, count=10))  # Vibrate for 10 cycles



# Start the tkinter event loop
window.mainloop()