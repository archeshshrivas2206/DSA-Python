import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    if not engine._inLoop:  # Check if the loop is already running
        engine.say(text)
        engine.runAndWait()

def take_command():
    command = ""  # Initialize the command variable
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(f'Command received: {command}')
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        talk("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        talk("Could not request results from Google Speech Recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk(f"An error occurred: {e}")
    return command

def run_alexa():
    command = take_command()
    if command:
        print(f'Processing command: {command}')
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'date' in command:
            talk('Sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'stop' in command:
            talk('Goodbye!')
            return False  # Return False to break the loop
        else:
            talk('Please say the command again.')
    else:
        talk('Please say the command again.')
    return True  # Continue the loop

while True:
    if not run_alexa():
        break  # Exit the loop if run_alexa() returns False
