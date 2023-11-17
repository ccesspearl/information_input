import tkinter as tk
from art import *
import pyttsx3

def display_welcome_message():
    window = tk.Tk()
    window.title("Information Input")
    window.configure(bg="#1F354B")  
   
    def get_user_input():
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        
        gathered_info = f"\nThank you for sharing your information! We're glad to have you in our system. \n Here's the data you provided in our system:\n\nNAME: {name}\nAGE: {age}\nADDRESS: {address}\n\n🔐 Your data has been safely recorded. 🔐"
        info_display.config( text=gathered_info, font=("Courier", 12, "bold"), fg="cyan", relief="raised", padx=20, pady=20)

        window.update()

        engine = pyttsx3.init()
        engine.say(gathered_info)
        engine.runAndWait()
        
    label = tk.Label(window, text=text2art("Welcome to the System"), fg="yellow", font=("Courier", 12, "bold"), bg="#1F354B")
    label.pack()

    window.update()

    engine = pyttsx3.init()
    engine.say("Welcome to the System")
    engine.runAndWait()

    text = "Welcome Aboard!🚀 We're thrilled to have you.✨ We'd like to know your personal details.🔎"
    info_display = tk.Label(window, text="", font=("Courier", 10, "bold"), bg="#1F354B", fg="white")

    window.update()
    
    engine = pyttsx3.init()
    engine.say("Welcome Aboard! We're thrilled to have you. We'd like to know your personal details. We'll present you a set of question and type your answer in the message box below. Thank you.")
    engine.runAndWait()

    top_border = f"\u2554{'\u2550' * (len(text) + 5)}\u2557"
    bottom_border = f"\u255a{'\u2550' * (len(text) + 5)}\u255d"

    top_label = tk.Label(window, text=top_border, fg="#08FF88", bg="#1F354B", font=("Courier", 12, "bold"))
    top_label.pack()
    message_label = tk.Label(window, text=f"\u2551 {text} \u2551", bg="#1F354B", fg="#08FF88", font=("Courier", 12, "bold"))
    message_label.pack()
    bottom_label = tk.Label(window, text=bottom_border, fg="#08FF88", bg="#1F354B", font=("Courier", 12, "bold"))
    bottom_label.pack()

    name_label = tk.Label(window, text="What's your name?", fg="#5CE1E6", bg="#1F354B", font=("Courier", 12, "bold") )
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    age_label = tk.Label(window, text="How old are you?", fg="#F6B972", bg="#1F354B", font=("Courier", 12, "bold"))
    age_label.pack()
    age_entry = tk.Entry(window)
    age_entry.pack()

    address_label = tk.Label(window, text="Where do you live? Give your address.", fg="#FF7046", bg="#1F354B", font=("Courier", 12, "bold"))
    address_label.pack()
    address_entry = tk.Entry(window)
    address_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=get_user_input)
    submit_button.pack()

    info_display.pack()

    window.mainloop()

display_welcome_message()
