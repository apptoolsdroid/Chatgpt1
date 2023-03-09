# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# import chatgptgpt
import tkinter as tk
from chatgpt import *
import openai
# from revChatGPT.revChatGPT import Chatbot
#Creating the application window
win = tk.Tk()
win.title("ChatGPT Demo")
win.geometry("800x800")

print('PyCharm')

#Creating the model
gpt = Conversation() #model_id="3456"

#Creating the text widget
text_box=tk.Text(win, height=40, width=90, relief=tk.SUNKEN)
text_box.config(state=tk.DISABLED)
text_box.grid(row=0, column=0, padx=5, pady=5)

#Creating the user input box
user_input = tk.Entry(win, width=30)
user_input.grid(row=1, column=0, columnspan=1, padx=5, pady=5)

openai.api_key = ""

# Set up the model and prompt
model_engine = "text-davinci-003"


#Creating the submit button
def submit():
    #fetching the user input
    user_text = user_input.get()

    #generating the response
    response = gpt.stream(user_text)#gpt.get_response(user_text)

    #updating the text box
    text_box.config(state=tk.NORMAL)
    text_box.insert(tk.END, "\nYou: "+user_text)

    prompt = user_text#"Hello, how are you today?"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(response)
    text_box.insert(tk.END, "\nBot: " + response)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
submit_button = tk.Button(win, text='Submit', command=submit)
submit_button.grid(row=3, column=0)

win.mainloop()