from fileinput import filename
from flask import Flask, request, json
from flask_cors import CORS
import textract
import os
from werkzeug.utils import secure_filename
from dateutil import parser
import datefinder

# Initializing app
app = Flask(__name__)

# Enabling CORS
CORS(app)

# Setting all documents to go to contracts
app.config["UPLOAD_FOLDER"]= "contracts"


## Receiving documents and retrieving the data from the PDF
@app.route("/", methods=["GET", "POST"])
def HelloWorld():
    
    data = request.files.getlist("file[]")
    print(data)
    response = []

    for f in data:

        print(f.filename)

        fileName = secure_filename(f.filename)

        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], fileName))
    
        pdfData = textract.process("/Users/gabrielmachado/Documents/Development/harbour-contract-dates-backend/contracts/" + str(fileName), encoding='utf-8', method='pdfminer')
    
        matches = datefinder.find_dates(str(pdfData), strict=True)

        
        for match in matches:
            res = {"filename": fileName, "data": str(match), "url": "file:///Users/gabrielmachado/Documents/Development/harbour-contract-dates-backend/contracts/"}
            print(res)
            response.append(res)
        
        
        jsonifiedAnswer = app.response_class(
            response=json.dumps(response),
            status=200,
            mimetype='application/json'
        )
    return jsonifiedAnswer


# PIP Server
if __name__ == "__main__":
    app.run(debug=True)

