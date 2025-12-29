# import gspread
# from google.oauth2.service_account import Credentials
# from flask import Flask, request, jsonify
# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# SCOPES = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive"
# ]

# creds = Credentials.from_service_account_file(
#     "service_account.json",
#     scopes=SCOPES
# )

# client = gspread.authorize(creds)

# # 🔴 PASTE YOUR GOOGLE SHEET URL HERE
# sheet = client.open_by_url(
#     "https://docs.google.com/spreadsheets/d/1aJ_wTICQisUdGX-pSv3v49ITp__z0aWCUKfX4iP_egE/edit?gid=0#gid=0"
# ).sheet1


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/submit", methods=["POST"])
# def submit():
#     data = request.json

#     row = [
#         data["Name"],
#         data["Id"],
#         data["Gmail_id"],
#         data["idno"],
#         data["asset_Type"],
#         data["configuration"],
#         data["Ram"],
#         data["Doamin"],
#         data["AV"],
#         data["FC"],
#         data["win_ver"]
#     ]

#     sheet.append_row(row)
#     return jsonify({"status": "success"})



# if __name__ == "__main__":
#     app.run(debug=True)



import json
import os
from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Read service account JSON from environment variable
SERVICE_ACCOUNT_JSON = os.environ.get("SERVICE_ACCOUNT_JSON")
creds_dict = json.loads(SERVICE_ACCOUNT_JSON)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open("Asset_Inventory").sheet1

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    sheet.append_row(list(data.values()))
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
