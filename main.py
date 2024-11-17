import random
import webbrowser
import datetime
import time
import user_config
import smtplib, ssl
import pyttsx3
import pyautogui
import wikipedia
import pywhatkit as pwk
from transformers import pipeline
import requests
from huggingface_hub import InferenceClient
import speech_recognition as sr
import chainlit as cl 
from getpass import getpass
import os
import json
from plyer import notification
from youtubesearchpython import VideosSearch


import logging
logging.basicConfig(level=logging.CRITICAL)  # Only show critical errors



os.environ['HUGGINGFACEHUB_API_TOKEN'] = user_config.JOI_Hugging_Face

repo_id = "microsoft/DialoGPT-medium"


# Create an inference client with the chosen model
llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
)




# Creating pyttsx3 Object and Tuning my AI Voice
engine = pyttsx3.init()
engine.setProperty('rate', 170)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


        # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language = 'en-in')
            print("You Said.............." + content)
        except Exception as e:
            print("Please Try Again...")

        return content

# request = command()
# print(request)


def speak(audioToSay):
    engine.say(audioToSay)
    engine.runAndWait()

# audioToSay = "You Look Lonely, I can Fix That!"
# speak(audioToSay)




def main_process():

     # Month names dictionary
    month_names = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }



    while True:
        request = command().lower()
        print(f"User Command: {request}")  # Debug: Check the command input

        #PHASE 1

        #Hello 
        if request.startswith("hello"):
            speak("Welcome, How can I Help You!")




        #Play Music
        elif "play music" in request:
            # Extract the search query
            search_query = request.replace("play music", "").strip()

            # If no specific query is provided, play a random preset song
            if not search_query:
                speak("Playing a random song.")
                random_song = random.choice([
                    "https://www.youtube.com/watch?v=CRnCzZ6vqtQ",
                    "https://www.youtube.com/watch?v=EiAMmYbr3vA",
                    "https://www.youtube.com/watch?v=_r-nPqWGG6c"
                ])
                webbrowser.open(random_song)
                continue

            try:
                # Search for the query on YouTube
                speak(f"Searching YouTube for {search_query}")
                videos_search = VideosSearch(search_query, limit=1)
                result = videos_search.result()["result"]

                # If a result is found, play the first video
                if result:
                    top_result_url = result[0]["link"]
                    speak(f"Playing {result[0]['title']} on YouTube.")
                    webbrowser.open(top_result_url)
                else:
                    speak("Sorry, I couldn't find anything for your request.")

            except Exception as e:
                # Handle errors gracefully
                print(f"Error: {e}")
                speak("Sorry, there was an error searching YouTube.")




        #Time Functionality
        elif any(phrase in request for phrase in ["say the time", "what's the time now", "current time"]):
            time_now = datetime.datetime.now().strftime("%H:%M")
            speak("Current Time is : " + str(time_now))




        #Date Functionality
        elif any(phrase in request for phrase in ["say the date", "what's the date today", "today's date"]):
            current_date = datetime.datetime.now()
            day = current_date.strftime("%d")
            month = current_date.strftime("%m")
            month_name = month_names[month]
            speak(f"Today's Date is: {day} {month_name}")





        #Adding a Task
        elif "add a task" in request:
            # Remove the trigger phrase and get the task
            todo = request.replace("add a task", "").strip()  # Remove phrase and clean up extra spaces

            if todo:  # Ensure there is a task to add
                speak("Adding Task: " + todo)
                with open("todo.txt", "a") as file:
                    file.write(todo + "\n")  # Add newline after each task
            else:
                speak("I didn't understand the task. Please try again.")




        #Read Tasks
        elif any(phrase in request for phrase in ["read my task", "read my tasks", "what's in my to do"]):
            try:
                with open("todo.txt", "r") as file:
                    todos = file.read().strip()  # Read and clean up the file content
                    if todos:
                        speak("Your tasks are: " + todos.replace("\n", ", "))  # Replace newlines with commas for better readability
                    else:
                        speak("Your task list is empty.")
            except FileNotFoundError:
                speak("You don't have any tasks yet.")







        #Deleting a Task
        elif "delete task" in request:
            # Extract the task to be deleted
            task_to_delete = request.replace("delete task", "").strip()  # Clean up the command

            if task_to_delete:
                try:
                    with open("todo.txt", "r") as file:
                        tasks = file.readlines()  # Read all lines

                    # Filter out the task to delete
                    updated_tasks = [task for task in tasks if task.strip() != task_to_delete]

                    if len(updated_tasks) < len(tasks):  # Task was found and deleted
                        with open("todo.txt", "w") as file:
                            file.writelines(updated_tasks)  # Write the updated tasks back to the file
                        speak(f"Task '{task_to_delete}' has been deleted.")
                    else:
                        speak(f"Task '{task_to_delete}' not found in your list.")
                except FileNotFoundError:
                    speak("You don't have any tasks yet.")


                

        #Showing Todos in Notification
        elif "show work" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()  # Read tasks and strip extra spaces

                if tasks:  # Check if there are tasks
                    notification.notify(
                        title="Today's Work",
                        message=tasks,
                        timeout=10  # Notification duration in seconds
                    )
                    speak("I have displayed today's work in a notification.")
                else:
                    speak("Your task list is empty.")
            except FileNotFoundError:
                speak("You don't have any tasks yet.")





        #Opening Website in PC
        elif "open youtube" in request: 
            webbrowser.open("www.youtube.com")
            speak(result)

        #Opening Website in PC
        elif "open instagram" in request: 
            webbrowser.open("www.instagram.com")
            speak(result)


        #Opening any Software in PC
        elif "open" in request: 
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            # pyautogui.sleep(2)
            pyautogui.press("enter")






        #Taking Screenshot
        elif any(phrase in request for phrase in ["take screenshot", "take a screenshot", "capture screen"]):
            img = pyautogui.screenshot()

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
            # Save the screenshot to a file (you can specify a path as well)
            img.save(f"screenshot_{timestamp}.png")
            
            # Notify the user
            speak("Screenshot taken and saved successfully.")




        
        #PHASE 2

        #Implementing Wikipedia Functionality

        elif "wikipedia" in request: 
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)


        elif "search google" in request: 
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q=" + request)




        elif "send whatsapp" in request: 
            # Remove the phrase "send whatsapp" from the request to get the actual message
            request = request.replace("send whatsapp", "").strip()

            # Send the message instantly using pywhatkit
            pwk.sendwhatmsg_instantly("+917666217289", request)

            # Wait a couple of seconds for the message to appear in the WhatsApp Web text field
            time.sleep(2)

            # Simulate pressing the 'Enter' key to send the message
            pyautogui.press("enter")

            speak("Message sent Successfully!")



        #Error coming due to 2FA I think

        # elif "send email" in request:
        #     # pwk.send_mail("nishank.kose77@gmail.com", user_config.gmail_password, "Test Mail", "This is a test email", "nishank.kose77@gmail.com")
            
        #     speak("Email sent Successfully!")

        # elif "send email" in request:
        #     s = smtplib.SMTP('smtp@gmail.com', 587)
        #     s.starttls()
        #     s.login("nishank.kose77@gmail.com", user_config.gmail_password)   
        #     message = """
        #     This is the Message

        #     Thank you for always being there
        #     """
        #     speak("Email sent Successfully!")
        #     s.sendmail("nishank.kose77@gmail.com", "nishank.kose77@gmail.com", message)
        #     s.quit()
        #     speak("Email sent!")

        


        #Nothing is Free

        # #Using AI - Hugging Face Transformers Library

        # # Load GPT-J model for text generation
        # elif "tell me" in request:

        #     prompt = request.replace("tell me", "").strip()

        #     # Generate text
        #     generated_text = generator(prompt, max_length=100, num_return_sequences=1)

        #     #Get the generated Text
        #     response = generated_text[0]['generated_text']

        #     # Print the generated text
        #     print(response)
            
        #     speak(response)


        #This also not working
        # elif "tell me" in request:
        #     promptSaid = request.replace("tell me", "").strip()
        #     fullResponse = openai.Completion.create(
        #         model="text-davinci-003",  # You can also use GPT-4 if available
        #         prompt=promptSaid,
        #         max_tokens=100
        #     )

        #     response = fullResponse.choices[0].text.strip()
        #     print(response)
        #     speak(response)


        # else:
        #     print("Wait!!")

        elif "tell me" in request:

            # Remove "tell me" and clean the input
            prompt = request.replace("tell me", "").strip()

            try:
                # Make the API call for text generation
                response = llm_client.post(
                    json={
                        "inputs": prompt,  # Use the rest of the input after "tell me"
                        "parameters": {
                            "max_new_tokens": 400,  # Limit the length of the response
                            "temperature": 0.7,     # Allow for natural responses
                        },
                        "task": "text-generation",
                    }
                )

                # Decode and get the generated text
                generated_text = json.loads(response.decode())[0]["generated_text"].strip()

                # Truncate to the first sentence for conciseness (if applicable)
                if '.' in generated_text:
                    generated_text = generated_text.split('.')[0] + '.'

                # Handle cases where the output might be empty or non-meaningful
                if not generated_text:
                    generated_text = "Sorry, I couldn't process your request."

            except Exception as e:
                # Handle any errors gracefully
                print(f"Error: {e}")
                generated_text = "Sorry, I couldn't process your request."

            # Print and speak the generated text
            print(generated_text)
            speak(generated_text)



        elif "stop" in request.lower():
            speak("Goodbye!")
            break  # Exit the loop and stop the assistant



main_process()
