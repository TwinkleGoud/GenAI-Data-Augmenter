import pandas as pd
import io
import json
from openai import OpenAI
from flask import Flask, render_template, request, send_file

client = OpenAI(api_key='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')

app = Flask(__name__)

def clean(dict_variable):
    return next(iter(dict_variable.values()))

def create_file(df_csv, rows, pk_key=None, uk_key=None):
    prompt = (
        "You are a data augmentation assistant.\n\n"
        f"I have a dataset with the following schema:\n{df_csv.to_dict('records')}\n\n"
        f"Please generate {rows} realistic and diverse synthetic rows that match the column structure and data types of this dataset.\n"
    )

    if pk_key:
        prompt += f'- Ensure the primary key column "{pk_key}" is unique for each new row.\n'
    if uk_key:
        prompt += f'- Ensure the following columns are unique across all rows (existing and new): {uk_key}\n'
    prompt += (
        "- Do not copy rows directly from the input. Generate plausible new data based on the patterns.\n\n"
        f"Here is a sample of the original data:\n{df_csv}\n"
        "Return the output in JSON Format"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
    except Exception as e:
        print("OpenAI API error:", e)
        return df_csv

    synthetic_rows = clean(json.loads(response.choices[0].message.content))
    df_new = pd.DataFrame(synthetic_rows)
    df_final = pd.concat([df_csv, df_new], ignore_index=True)

    return df_final

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No File Uploaded", 400

        file = request.files['file']
        rows_count = request.form.get('rowsCount', 10)
        pk_key = request.form.get('primaryKey', None)
        uk_key = request.form.get('uniqueKeys', None)
        output_filename = request.form.get('output_filename', None)

        if file.filename == '':
            return "No file selected", 400

        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            print(df)
            df_augmented = create_file(df, rows_count, pk_key=pk_key, uk_key=uk_key)

            output = io.BytesIO()
            df_augmented.to_csv(output, index=False)
            output.seek(0)

            return send_file(output, mimetype='text/csv', as_attachment=True, download_name = file.filename + '_augmented.csv')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)