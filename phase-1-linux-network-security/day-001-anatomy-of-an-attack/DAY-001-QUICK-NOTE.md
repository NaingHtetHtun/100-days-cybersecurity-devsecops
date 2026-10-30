# 📝 Day 001 Quick Note (အတိုချုပ် မှတ်စု)

| # | သင်ခဲ့သည့် ခေါင်းစဉ် (Title) | အဓိပ္ပာယ် အတိုချုပ် (One-Line Meaning) |
| :-: | :--- | :--- |
| **1** | **Reconnaissance (Recon)** | Hacker က Website တစ်ခုကို မဖောက်ခင် Server နဲ့ Tech Stack အချက်အလက်တွေကို အရင် စုံစမ်းထောက်လှမ်းခြင်း။ |
| **2** | **Banner Grabbing (`curl -sI`)** | HTTP Response Header တောင်းကြည့်ပြီး Server OS နဲ့ Version (`nginx/1.24.0 (Ubuntu)`) ကို ဖော်ထုတ်ခြင်း။ |
| **3** | **Information Disclosure** | မလိုအပ်ဘဲ Server Version, Framework, သို့မဟုတ် `.env` အချက်အလက်များ အပြင်သို့ ပေါက်ကြားနေခြင်း။ |
| **4** | **`server_tokens off;`** | Nginx ရဲ့ Version နဲ့ OS အမည်ကို Header မှာ မပေါ်အောင် (`Server: nginx` သာပြအောင်) ပိတ်သည့် Setting။ |
| **5** | **Dotfiles Protection (`/.env`, `/.git`)** | Nginx တွင် `location ~ /\.(?!well-known).* { deny all; }` သုံး၍ `.` ဖြင့်စသော အရေးကြီးဖိုင်များကို `403` ဖြင့် ပိတ်ဆို့ခြင်း။ |
| **6** | **Laravel Cookie (`eyJpdiI6...`)** | Base64 ဖြည်လိုက်လျှင် `iv` (Random တန်ဖိုး), `value` (Encrypted စာသား), `mac` (HMAC လက်မှတ်) ပါဝင်သော JSON ဖွဲ့စည်းပုံ။ |
| **7** | **`APP_KEY` & `MAC` Verification** | Cookie ထဲက `value` ကို `APP_KEY` မသိဘဲ ပြင်လိုက်ပါက `mac` လက်မှတ် မကိုက်ညီတော့သဖြင့် Laravel က ပယ်ချသည့် စနစ်။ |
| **8** | **`SESSION_DRIVER=database` / `file`** | Cookie ထဲတွင် User Data တိုက်ရိုက်မသိမ်းဘဲ အက္ခရာ အလုံး ၄၀ ပါသော Random **Session ID** သာ သိမ်းသည့် လုံခြုံသော စနစ်။ |
| **9** | **Session Hijacking** | User ရဲ့ Login ဝင်ပြီးသား Session Cookie ကို ခိုးယူပြီး Password မလိုဘဲ အခြား Browser မှ အကောင့်ထဲ တိုက်ရိုက်ဝင်ရောက်ခြင်း။ |
| **10** | **`HttpOnly` Cookie Flag** | Browser ရဲ့ JavaScript (`document.cookie`) ကနေ Session Cookie ကို ဖတ်လို့/ခိုးလို့ မရအောင် ကာကွယ်ပေးသော အမှန်ခြစ် (Flag)။ |
| **11** | **`try_files` Bot Drain & `return 444;`** | Bot က မရှိသည့် `/wp-login.php` လာခေါ်ချိန် `/index.php` (Laravel) ဆီ မရောက်စေဘဲ Nginx မှ `444` ဖြင့် ချက်ချင်း ဖြတ်ချခြင်း။ |
