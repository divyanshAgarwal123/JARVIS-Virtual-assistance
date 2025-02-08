import pyttsx3
import datetime
import pywhatkit
import wikipedia
import speech_recognition as sr
import webbrowser
from googlesearch import search

# Initialize pyttsx3 engine for speech synthesis
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Set speech rate
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Set voice to female


# Function to make the assistant speak
def speak(text):
	engine.say(text)
	engine.runAndWait()


# Greeting function
def greet():
	hour = int(datetime.datetime.now().hour)
	if hour < 12:
		speak("Good morning, Sir")
	elif hour < 18:
		speak("Good afternoon, Sir")
	else:
		speak("Good evening, Sir")


# Function to recognize speech
def recognize_speech():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source, duration=0.2)
		print("Listening...")
		try:
			audio = recognizer.listen(source, timeout=5)
			query = recognizer.recognize_google(audio)
			return query.lower()
		except sr.UnknownValueError:
			speak("Sorry, I couldn't understand. Please repeat.")
			return "none"
		except sr.RequestError:
			speak("Speech recognition service is unavailable.")
			return "none"
		except Exception as e:
			print(f"Error: {e}")
			return "none"


# Function to perform a Google search
def google_search():
	speak("What do you want to search for?")
	search_query = recognize_speech()

	if search_query == "none":
		return

	speak("Searching on Google...")
	for result in search(search_query, num=1, stop=1, pause=2):
		speak(f"Here's what I found: {result}")
		print(result)
		webbrowser.open(result)  # Open URL in the browser


# Function to get Wikipedia information
def wikipedia_search(command):
	speak("Searching Wikipedia...")
	command = command.replace("wikipedia", "").strip()
	try:
		results = wikipedia.summary(command, sentences=2)
		speak("According to Wikipedia...")
		print(results)
		speak(results)
	except wikipedia.exceptions.DisambiguationError as e:
		speak(f"There are multiple results for {command}. Please be more specific.")
	except wikipedia.exceptions.PageError:
		speak("Sorry, I couldn't find anything on Wikipedia.")
	except Exception as e:
		speak("An error occurred while searching Wikipedia.")


# Function to perform Google search through pywhatkit
def pywhatkit_search(command):
	speak("Processing your search...")
	pywhatkit.search(command)


# Main function
def main_code():
	greet()
	speak("How can I assist you today?")

	while True:
		query = recognize_speech()
		print(f"User said: {query}")

		if "jarvis" in query:
			speak("Yes, Sir.")
			command = query.replace("jarvis", "").strip()

			while True:
				if "introduce" in command:
					speak("Hello world! I am Jarvis, an AI assistant made by Divyansh.")
					speak("I am here to make your interaction with your system more convenient.")
				elif "wikipedia" in command:
					wikipedia_search(command)
				elif "search" in command:
					pywhatkit_search(command)
				elif "google" in command:
					google_search()
				elif "shutdown" in command:
					speak("Goodbye, Sir. Have a great day!")
					exit()
				else:
					speak("Sorry, I didn't understand that.")
					break
				command = recognize_speech()

		elif "shutdown" in query:
			speak("Disconnecting Jarvis... Goodbye, Sir!")
			break


if __name__ == "__main__":
	main_code()
