# Therapy Note Polisher

Therapy Note Polisher is a simple Streamlit app that converts raw therapist notes into well-structured SOAP notes using the OpenAI API.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file based on `.env.example` and add your OpenAI API key:

```bash
cp .env.example .env
# edit .env and set OPENAI_API_KEY
```

## Running the Application

After setting up the environment variables, start the Streamlit app with:

```bash
streamlit run app.py
```
