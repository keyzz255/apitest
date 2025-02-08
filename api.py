from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://ngopi-bro.web.app"}})

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

# ✅ Endpoint untuk Cek Rekening Bank
@app.route("/cek_rekening/<kode_bank>/<nomor_rekening>", methods=["GET"])
def cek_rekening(kode_bank, nomor_rekening):
    try:
        params = {"kodeBank": kode_bank, "noRekening": nomor_rekening}
        response = requests.get(API_BANK_URL, headers=API_BANK_HEADERS, params=params)
        data = response.json()

        if response.status_code == 200 and "data" in data and "nama" in data["data"]:
            return jsonify({
                "success": True,
                "nama_pemilik": data["data"]["nama"],
                "kode_bank": kode_bank,
                "nomor_rekening": nomor_rekening
            })
        else:
            return jsonify({"success": False, "message": "Rekening tidak ditemukan"}), 404

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# ✅ Endpoint untuk Cek E-Wallet (DIPERBAIKI)
@app.route("/cek_ewallet/<nomor_hp>/<ewallet>", methods=["GET"])
def cek_ewallet(nomor_hp, ewallet):
    try:
        url = f"{API_EWALLET_URL}/cek_ewallet/{nomor_hp}/{ewallet}"
        response = requests.get(url, headers=API_EWALLET_HEADERS)
        data = response.json()

        if response.status_code == 200 and "data" in data:
            return jsonify({
                "success": True,
                "nama_pemilik": data["data"]["name"],
                "ewallet": ewallet,
                "nomor_hp": nomor_hp
            })
        else:
            return jsonify({"success": False, "message": "E-Wallet tidak ditemukan"}), 404

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# ✅ Endpoint Home
@app.route("/")
def home():
    return "API is running!", 200

# 🔥 Jalankan Server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
