# GenAI Data Augmentor

A simple web app built with Flask and OpenAI API that takes a CSV file and generates synthetic data rows using Generative AI.

## Features

- Upload CSV files
- Specify:
  - Number of rows to generate
  - Primary key column
  - Unique key columns (e.g., email, phone)
- Augmented CSV file returned as download

## Technologies Used

- Python
- Flask
- OpenAI GPT-4o
- HTML/CSS


## Screenshots


## Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/genai-data-augmentor.git
cd genai-data-augmentor
pip install -r requirements.txt
python app.py
