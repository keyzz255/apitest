from flask import Flask, jsonify
import requests

app = Flask(__name__)

# 🔹 API Bank (Validasi Rekening)
API_BANK_URL = "https://cek-nomor-rekening-bank-indonesia1.p.rapidapi.com/cekRekening"
API_BANK_HEADERS = {
    "x-rapidapi-key": "347c3d28d8msh5b5bbb8fcfdf9eap1b3295jsn7f44586c582f",
    "x-rapidapi-host": "cek-nomor-rekening-bank-indonesia1.p.rapidapi.com"
}

# 🔹 API E-Wallet (Validasi DANA, OVO, ShopeePay, dll)
API_EWALLET_URL = "https://check-id-ovo-gopay-shopee-linkaja-dana.p.rapidapi.com"
API_EWALLET_HEADERS = {
    "x-rapidapi-key": "347c3d28d8msh5b5bbb8fcfdf9eap1b3295jsn7f44586c582f",
    "x-rapidapi-host": "check-id-ovo-gopay-shopee-linkaja-dana.p.rapidapi.com"
}

@app.route("/")
def home():
    return "API is running!", 200

@app.route("/cek_rekening/<kode_bank>/<no_rekening>")
def cek_rekening(kode_bank, no_rekening):
    """🔹 Endpoint untuk cek rekening bank"""
    params = {"kodeBank": kode_bank, "noRekening": no_rekening}
    try:
        response = requests.get(API_BANK_URL, headers=API_BANK_HEADERS, params=params)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/cek_ewallet/<ewallet>/<nomor>")
def cek_ewallet(ewallet, nomor):
    """🔹 Endpoint untuk cek e-Wallet"""
    endpoint = f"/cek_ewallet/{nomor}/{ewallet}"
    try:
        response = requests.get(API_EWALLET_URL + endpoint, headers=API_EWALLET_HEADERS)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
