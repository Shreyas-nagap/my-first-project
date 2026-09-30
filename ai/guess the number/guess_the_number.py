import random
from main import speak

number = random.randint(1,1000)
running = True
while running:
    user_input = int(input("Enter any number:"))

    if user_input < number:
        speak("The number is smaller")
    elif user_input > number:
        speak("The number is greater")
    else:
        speak("you found it")
        running = False