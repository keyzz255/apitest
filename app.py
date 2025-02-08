from flask import Flask, request, jsonify
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

# 🔹 Endpoint untuk mengecek rekening bank
@app.route("/cek-rekening", methods=["GET"])
def cek_rekening():
    kode_bank = request.args.get("kodeBank")
    nomor_rekening = request.args.get("noRekening")

    if not kode_bank or not nomor_rekening:
        return jsonify({"error": "Kode bank dan nomor rekening harus diisi"}), 400

    response = requests.get(API_BANK_URL, headers=API_BANK_HEADERS, params={
        "kodeBank": kode_bank,
        "noRekening": nomor_rekening
    })

    return jsonify(response.json()), response.status_code

# 🔹 Endpoint untuk mengecek e-wallet
@app.route("/cek-ewallet", methods=["GET"])
def cek_ewallet():
    nomor_hp = request.args.get("nomorHP")
    ewallet = request.args.get("ewallet")

    if not nomor_hp or not ewallet:
        return jsonify({"error": "Nomor HP dan e-wallet harus diisi"}), 400

    response = requests.get(f"{API_EWALLET_URL}/cek_ewallet/{nomor_hp}/{ewallet}", headers=API_EWALLET_HEADERS)

    return jsonify(response.json()), response.status_code

# 🔹 Menjalankan server Flask
if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
