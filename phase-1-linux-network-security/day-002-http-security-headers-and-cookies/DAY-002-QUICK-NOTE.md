# 📝 Day 002 Quick Note (အတိုချုပ် မှတ်စု)

| # | သင်ခဲ့သည့် ခေါင်းစဉ် (Title) | အဓိပ္ပာယ် အတိုချုပ် (One-Line Meaning) |
| :-: | :--- | :--- |
| **1** | **Clickjacking Attack** | Hacker က သူ့ရဲ့ Website အတုထဲမှာ ကိုယ့် Website ကို `<iframe>` နဲ့ အကြည်ရောင် ထပ်တင်ပြီး User ကို မသိဘဲ ခလုတ်နှိပ်မိအောင် လှည့်စားခြင်း။ |
| **2** | **`X-Frame-Options: SAMEORIGIN`** | ကိုယ့် Domain မဟုတ်တဲ့ တခြား Website တွေက ကိုယ့် Site ကို `<iframe>` ထဲ ထည့်သုံးလို့ မရအောင် (`refused to connect`) ပိတ်ပေးသည့် Header။ |
| **3** | **MIME Sniffing & `nosniff`** | `X-Content-Type-Options: nosniff` သုံး၍ ပုံ (`.jpg`) အယောင်ဆောင်ထားသော Script ဖိုင်များကို Browser က အလိုအလျောက် မRun မိအောင် တားဆီးခြင်း။ |
| **4** | **HSTS (`Strict-Transport-Security`)** | Browser ကို နောင်တစ်ချိန် `http://` ရိုးရိုးဖြင့် လုံးဝမချိတ်ဘဲ `https://` ဖြင့်သာ အမြဲချိတ်ဆက်ရန် အမိန့်ပေးသည့် Header။ |
| **5** | **`Referrer-Policy`** | ကိုယ့် Website မှ ပြင်ပ Link တစ်ခုသို့ နှိပ်သွားချိန်တွင် URL အပြည့်အစုံ (Path/Query parameters) သူများဆီ မပေါက်ကြားအောင် ထိန်းချုပ်သည့် Header။ |
| **6** | **`Content-Security-Policy (CSP)`** | Website ပေါ်တွင် ခွင့်ပြုထားသော Domain များမှလွဲ၍ ပြင်ပ Hacker JavaScript များ မRun နိုင်အောင် ကန့်သတ်သည့် Header (XSS ကာကွယ်ရေး)။ |
| **7** | **`HttpOnly` Cookie Flag** | Browser ၏ JavaScript (`document.cookie`) မှ Session Cookie ကို ဖတ်ရှု/ခိုးယူ၍ မရအောင် ပိတ်ပေးသည့် Flag (`XSRF-TOKEN` တွင်မူ Axios ဖတ်ရန် မထည့်ထားပါ)။ |
| **8** | **`Secure` Cookie Flag** | Cookie ကို လုံခြုံသော `HTTPS` Connection ဖြင့်သာ ပို့ဆောင်စေပြီး ရိုးရိုး `HTTP` ဖြင့် လုံးဝ မပို့စေသည့် Flag။ |
| **9** | **`SameSite=Lax` / `Strict`** | ပြင်ပ Hacker Website မှ ကိုယ့် Server ဆီသို့ လှည့်စားပြီး Request ပို့သည့်အခါ (CSRF Attack) Session Cookie မပါသွားအောင် တားဆီးပေးသည့် Flag။ |
