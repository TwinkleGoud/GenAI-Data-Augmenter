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
- OpenAI GPT-mini-4o
- HTML/CSS


## Screenshots


## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/TwinkleGoud/GenAI-Data-Augmenter.git

# 2. Navigate into the project directory
cd GenAI-Data-Augmenter

# 3. Install required Python packages
pip install -r requirements.txt

# 4. Install required Python packages
Add your OpenAI Key in app.py

# 5. Run the Flask app
python app.py
