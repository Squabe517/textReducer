import openai
import tiktoken as tk
from dotenv import load_dotenv
import os

# GET API KEY FROM .ENV FILE
load_dotenv()
api_key = os.environ.get("API_KEY")

# SET OPENAI API KEY
openai.api_key = api_key


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
    with open('output.txt', 'w') as file:
        pass  # File is emptied by opening it in write mode

    with open('output.txt', 'w') as file:
        for string in summary:
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


# Read the file in binary mode
text_data = readFile('text.txt')

# Encode the text and see how many tokens it contains
encoding = tk.encoding_for_model('gpt-3.5-turbo')
tokenizedText = encoding.encode(text_data)

# Split the text into smaller chunks, then decode it
splitText = split_list(tokenizedText)
for i in range(len(splitText)):
  splitText[i] = encoding.decode(splitText[i])

summary = getSummary(splitText)
# Send messages to chatbot, then append responses to list

write_out_response(summary)