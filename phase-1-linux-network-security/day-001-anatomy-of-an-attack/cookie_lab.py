#!/usr/bin/env python3
"""
Day 001 Hands-On Lab: ကိုယ်တိုင် Cookie နဲ့ APP_KEY ထည့်ပြီး စမ်းသပ်ရန် Script
"""
import urllib.parse
import json
import hmac
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# =====================================================================
# 👇 အဆင့် (၁) — ဒီနေရာမှာ မင်းရဲ့ APP_KEY နဲ့ Browser ကရတဲ့ COOKIE ကို ထည့်ပါ
# =====================================================================

# 1. Server ပေါ်က .env ထဲမှာ ပါတဲ့ APP_KEY ကို ဒီမှာ ထည့်ပါ (ဥပမာ "base64:...")
MY_APP_KEY = "base64:O4maeHbGqVxQk+Trv5FXN3xVHzFC329r368j+ON5mag="

# 2. Browser (Inspect -> Application -> Cookies) ကနေ ကူးလာတဲ့ Cookie Value ကို ဒီမှာ ထည့်ပါ
MY_COOKIE = "eyJpdiI6InN6QmV0WE9Wa2xjQWdmZllJTlBQenc9PSIsInZhbHVlIjoiY3g1KzlieVBhOHVLSEVBTVNWY0NRcFFrZTlNSVJLVXNSdDdINUtiS3JwU3hjeHFhVGlpdEp5RDNmamkvVWFTZFhzL1pkT2VpNXczZWpVcmJ2TVk1SGZFSjByOEVkSGt5dkdYc3IxQ1p2Z1g3K2M2MnVIN3RrYnBvRzNwWkZGZWkiLCJtYWMiOiI2NjBiMTYyOTZhODUxMTFmMDk5MTJmNGUwNzhlNzE2NTNkMjg1ZTM1NjBhNzk0NmFkYTdkNGY1OGJlNzE4MDVkIiwidGFnIjoiIn0%3D"


# =====================================================================
# ⚙️ အောက်က Code ကတော့ Cookie ကို တစ်ဆင့်ချင်း ဖြည်ပြပေးမယ့် Engine ပါ
# =====================================================================
def run_lab():
    print("\n--- [အဆင့် ၁] Cookie ကို URL Decode + Base64 Decode လုပ်ကြည့်ခြင်း ---")
    # Browser က Cookie မှာ %3D (=) လို URL encoding ပါတတ်လို့ အရင်ဖြည်ပါတယ်
    url_decoded = urllib.parse.unquote(MY_COOKIE)
    # ပြီးမှ Base64 ဖြည်လိုက်တဲ့အခါ JSON (iv, value, mac) ထွက်လာပါတယ်
    json_str = base64.b64decode(url_decoded).decode("utf-8")
    payload = json.loads(json_str)
    print(json.dumps(payload, indent=2))

    if MY_APP_KEY == "PASTE_YOUR_APP_KEY_HERE" or not MY_APP_KEY.startswith("base64:"):
        print("\n⚠️  [သတိပေးချက်] MY_APP_KEY နေရာမှာ Server က APP_KEY (base64:...) မထည့်ရသေးပါ!")
        print("👉 cookie_lab.py ရဲ့ Line 17 မှာ MY_APP_KEY ကို ထည့်ပြီး ပြန် Run ကြည့်ပါ။\n")
        return

    print("\n--- [အဆင့် ၂] မင်းထည့်လိုက်တဲ့ APP_KEY နဲ့ MAC လက်မှတ် မှန်/မမှန် စစ်ဆေးခြင်း ---")
    key_bytes = base64.b64decode(MY_APP_KEY.replace("base64:", ""))
    expected_mac = hmac.new(
        key_bytes,
        (payload["iv"] + payload["value"]).encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    print(f"Cookie ထဲပါလာသော MAC : {payload['mac']}")
    print(f"APP_KEY နဲ့ တွက်သော MAC : {expected_mac}")

    if not hmac.compare_digest(payload["mac"], expected_mac):
        print("\n❌ MAC မတူပါ! ဆိုလိုတာက ဒီ Cookie ဟာ မင်းထည့်ထားတဲ့ APP_KEY နဲ့ ဆောက်ထားတာ မဟုတ်ပါဘူး (တခြား Project ရဲ့ APP_KEY ဖြစ်နေပါတယ်)။\n")
        return

    print("✅ MAC တစ်ထပ်တည်း တူပါတယ်! (ဒီ APP_KEY အမှန်ဖြစ်ကြောင်း သေချာသွားပြီ!)")

    print("\n--- [အဆင့် ၃] APP_KEY သုံးပြီး Cookie ထဲက 'value' ကို Decrypt (ဖြည်ချ) ခြင်း ---")
    iv_bytes = base64.b64decode(payload["iv"])
    encrypted_bytes = base64.b64decode(payload["value"])

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_bytes) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = (unpadder.update(padded_data) + unpadder.finalize()).decode("utf-8")

    print(f"🔓 ဖြည်လို့ရလာသော စာသားအစစ် (Decrypted Plaintext):\n   👉 {plaintext}")

    if "|" in plaintext:
        prefix, real_value = plaintext.split("|", 1)
        print(f"\n   📌 '|' ရှေ့က အပိုင်း (Cookie Prefix Hash) : {prefix}")
        print(f"   🔑 '|' နောက်က အပိုင်း (မင်းရဲ့ အစစ်အမှန် Session ID) : {real_value}\n")


if __name__ == "__main__":
    run_lab()
