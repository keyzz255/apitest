from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7242900315:AAEAa695JhocGlIskgv6RGI3JMdnydDDjk8"

API_BANK_URL = "https://cek-nomor-rekening-bank-indonesia1.p.rapidapi.com/cekRekening"
API_EWALLET_URL = "https://check-id-ovo-gopay-shopee-linkaja-dana.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-key": "347c3d28d8msh5b5bbb8fcfdf9eap1b3295jsn7f44586c582f",
    "x-rapidapi-host": "check-id-ovo-gopay-shopee-linkaja-dana.p.rapidapi.com"
}

@app.route("/cek-rekening", methods=["POST"])
def cek_rekening():
    data = request.json
    kode_bank = data.get("kode_bank")
    nomor_rekening = data.get("nomor_rekening")
    response = requests.get(API_BANK_URL, headers=HEADERS, params={"kodeBank": kode_bank, "noRekening": nomor_rekening})
    return jsonify(response.json())

@app.route("/cek-ewallet", methods=["POST"])
def cek_ewallet():
    data = request.json
    ewallet = data.get("ewallet")
    nomor_hp = data.get("nomor_hp")
    response = requests.get(f"{API_EWALLET_URL}/cek_ewallet/{nomor_hp}/{ewallet}", headers=HEADERS)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
