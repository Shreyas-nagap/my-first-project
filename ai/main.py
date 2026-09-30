import win32com.client
import datetime
import webbrowser
import AppOpener
import wikipedia
import asyncio
import python_weather
import runpy
import ollama

wikipedia.set_user_agent("ShreyasProject/1.0 (contact@example.com)")
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(data):
    print(data)
    speaker.Speak(data)
    return ""

def greet():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour >= 7 and hour < 12:
        speak("GOOD MORNING")
    elif hour >= 12 and hour < 17:
        speak("GOOD AFTERNOON")
    elif hour >= 17 and hour < 19 :
        speak("GOOD EVENING")
    else:
        speak("GOOD NIGHT")

def showdate():
    month_list  = ["January", "February", "March", "April", "May", "June","July","August","September","October","November","December"]
    day = datetime.datetime.now().strftime("%d")
    month = month_list[int(datetime.datetime.now().strftime("%m"))-1]
    year = datetime.datetime.now().strftime("%Y")
    speak(f"Today date is {day} {month} {year}")

def summ(idea):
    try:
        result = wikipedia.summary(idea, sentences = 2)
        speak(result)
    except:
        speak("NO INTERNET")
async def showweather():
    try:
        async with python_weather.Client(unit= python_weather.METRIC) as client:
            weather =await client.get("Dombivli")
            speak(f" In your area Current Temperature is {weather.temperature}°C")
            speak(f"In your area Weather conditions is {weather.description}")
    except:
        speak("NO INTERNET")

def chatbot(prompt):
    client = ollama.Client()
    response = client.generate(model="llama3:8b", prompt = prompt)
    return response.response

if __name__ == "__main__":
    greet()
    speak("How may i help you")
    while True:
        prompt = input("TASK:")
        if "date" in prompt and "what" in prompt:
            showdate()

        elif "open" in prompt and "website" in prompt:
            prompt = prompt.replace("open ", "")
            prompt = prompt.replace(" website", "")
            speak(f"Opening {prompt}")
            webbrowser.open(f"https://www.{prompt}.com")

        elif "open" in prompt:
            prompt = prompt.replace("open ", "")
            speak(f"Opening {prompt}...")
            AppOpener.open(prompt, match_closest = True)

        elif "wikipedia" in prompt:
            prompt = prompt.replace(" wikipedia", "")
            summ(prompt)

        elif "search" in prompt:
            prompt = prompt.replace("search ", "")
            speak("Searching in Google...")
            webbrowser.open(f"https://www.google.com/search?q={prompt}")

        elif "weather" in prompt:
            prompt = prompt.replace("weather ", "")
            asyncio.run(showweather())

        elif "play rock paper scissor" in prompt:
            speak("Playing rock paper scissor")
            runpy.run_path(path_name="tic_tac_toe.py")

        elif "play guess the number" in prompt:
            speak("Playing Guess the number")
            runpy.run_path(path_name="guess the number/guess_the_number.py")

        elif "play guess the word" in prompt:
            speak("Playing Guess the word")
            runpy.run_path(path_name="guess the word/guess_the_word.py")

        elif "give" in prompt and "code" in prompt:
            speak("Hear is the code")
            print("Searching Results....")
            print(chatbot(prompt))
        else:
            print("Wait for Sometime....")
            speak(chatbot(prompt))