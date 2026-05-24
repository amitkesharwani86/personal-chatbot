import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from openai import OpenAI # ai

engine = pyttsx3.init()
print("Hi, I am here to help you. Say 'Aryan' to wake me up.")
engine.say("Hi, I am here to help you. Say 'Aryan' to wake me up.")
engine.runAndWait()

# ai
client = OpenAI(
    api_key="",
    base_url="https://api.groq.com/openai/v1"
)
ai_pre_message = "you are my ai assistant and your name is aryan and reply according answer only output dont repete that who are you untill ask and input : "
# Initialize Recognizer
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Helps with noise
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()  # Convert speech to lowercase text
            print(f"You: {text}") # only for tset
            if "aryan" in text:
                print("Yes sir")
                engine.say("Yes sir")
                engine.runAndWait()

                # Now listen for commands after wake word
                while True:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source)
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        print(f"You said: {command}")
                        # engine.say(f"You said {command}")
                        # engine.runAndWait()

                        # ai
                        ai_work = True

                        if "terminate yourself" in command:
                            ai_work = False
                            print("Terminating...")
                            engine.say("You asked me to terminate. Have a good day, sir.")
                            engine.runAndWait()
                            exit()

                        elif "goodbye" in command or "thank you" in command:
                            ai_work = False
                            print("Goodbye sir!")
                            engine.say("Goodbye sir! when ever you need just call me")
                            engine.runAndWait()
                            break  # Exit listening mode, return to wake word detection

                        if "open google" in command:
                            ai_work = False
                            print("Opening Google...")
                            webbrowser.open("https://google.com")
                            print("https://google.com")
                            engine.say("Opening google")
                            engine.runAndWait()

                        if "open youtube" in command:
                            ai_work = False
                            print("Opening youtube...")
                            webbrowser.open("https://youtube.com")
                            print("https://youtube.com")
                            engine.say("Opening youtube")
                            engine.runAndWait()   
                            
                        if "open whatsapp" in command:
                            ai_work = False
                            print("Opening whatsapp...")
                            os.startfile(r"C:\Users\Lenovo\Desktop\WhatsApp.lnk")
                            print(r"C:\Users\Lenovo\Desktop\WhatsApp.lnk")
                            engine.say("Opening whatsapp")
                            engine.runAndWait() 

                        if ai_work:
                            response = client.chat.completions.create(
                                    model="llama-3.3-70b-versatile",
                                    messages=[
                                            {"role": "user", "content": ai_pre_message + command}
                                        ]
                            )
                            print("AI output:  ", response.choices[0].message.content)
                            engine.say(response.choices[0].message.content)
                            engine.runAndWait() 


                    except sr.UnknownValueError:
                        print("Sorry, I couldn't understand what you said.")
                        engine.say("Sorry, I couldn't understand what you said.")
                        engine.runAndWait()

                    except sr.RequestError:
                        print("Error with the API request.")
                        engine.say("There was an error connecting to the speech recognition service.")
                        engine.runAndWait()

        except sr.UnknownValueError:
            pass  # Ignore and keep listening

        except sr.RequestError:
            print("Error with the API request.")
            engine.say("There was an error connecting to the speech recognition service.")
            engine.runAndWait()