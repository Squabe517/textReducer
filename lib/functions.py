import openai
import tiktoken as tk
from dotenv import load_dotenv
import os
import datetime

# Reads a text file and returns the contents as a string
def readFile(textFile):
    print("reading data from file...\n")
    # Read the file in binary mode
    with open(textFile, 'rb') as file:
        byte_data = file.read()
    # Decode the bytes to string, preserving escape sequences
    text_data = byte_data.decode('unicode_escape')
    return text_data

# Splits a list into smaller lists of a given size then returns the list of lists
def split_list(long_list):
    print("splitting list...\n")
    max_len = 1000
    sublists = [long_list[i:i + max_len] for i in range(0, len(long_list), max_len)]
    return sublists

# Completely overwrites output file then writes the summary to it
def write_out_response(response):
    print("writing response to file...\n")
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    currentDT = datetime.datetime.now()
    formatted_time = currentDT.strftime("%Y-%m-%d_%H-%M-%S")  # Format without colons and periods
    filename = 'output/' + formatted_time + '.txt'
    
    with open(filename , 'w') as file:
        for string in response:
            file.write(string + '\n')  # Add a newline after each string
            
# Sends messages to chatbot and returns the responses as a list
def getSummary(splitText):
    summary = []
    for message in splitText:
        print("sending message to chatbot...(" + str(splitText.index(message)) + "/" + str(len(splitText)) + ")\n")
        myMessage = [
                {"role": "system", "content": "You are a college student who has been asked to summarize the following text:"},
                {'role': 'user', 'content': message},
        ]
        print("receiving response from chatbot...\n")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= myMessage 
        )
        summary.append(response['choices'][0]['message']['content'])
    return summary