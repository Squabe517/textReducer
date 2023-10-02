# Text Summarizer using GPT-3.5 Turbo

This script reads a long text from a file, splits it into manageable chunks, and uses the OpenAI GPT-3.5 Turbo model to generate a summary. The summarized text is then written to an output file.

## Prerequisites

- Python 3.x
- OpenAI Python package
- Tiktoken Python package
- python-dotenv package

You can install the necessary Python packages using pip:

```bash
pip install openai tiktoken python-dotenv
```

## Environment Variables

Create a `.env` file in your project directory and add your OpenAI API key:

```env
API_KEY=your_openai_api_key_here
```

## Usage

1. Place the text you want to summarize in a file called `input.txt` in the project directory.
2. Run the script:

```bash
python reducer.py
```

3. The summarized text will be written to an output folder created in the same directory, named by the time it was created.

## How It Works

1. **Read Text**: The `readFile` function reads the text from `text.txt`.
2. **Tokenize and Split**: Tiktoken is used to tokenize the text and split it into smaller chunks.
3. **Generate Summary**: Each chunk is sent to GPT-3.5 Turbo to generate a summary.
4. **Write Summary**: The `write_out_response` function writes the summary to the output directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.