from flask import Flask, make_response

app = Flask(__name__)

@app.route('/download')
def download_csv():
    # Replace this with your actual data retrieval or generation logic
    csv_list = ['all', 'my', 'data', 'goes', 'here']  # Example data
    
    # Convert list to comma-separated string
    csv_string = ','.join(csv_list)
    
    response = make_response(csv_string)
    response.headers['Content-Disposition'] = 'attachment; filename=myCSV.csv'
    return response

if __name__ == '__main__':
    app.run(debug=True)
