# 📅 Day 002: HTTP/HTTPS Security Headers & Cookie Flags (`HttpOnly`, `Secure`, `SameSite`)

> **Phase:** Phase 1 (Linux, SSH, Nginx & Network Security) | **Time Spent:** 60 Mins  
> **Tech Stack Involved:** Nginx (`add_header`), HTTP Response Headers, Browser Cookies, Python Scanner  
> **🎓 Certification Alignment:** **ISC2 CC** (Domain 4 & 5) • **CompTIA Security+ (SY0-701)** • **APIsec Fundamentals**

👉 **အတိုချုပ် မှတ်စု (Quick Note) ဖတ်ရန်:** [DAY-002-QUICK-NOTE.md](./DAY-002-QUICK-NOTE.md)

---

## 🛠️ ဒီနေ့ လက်တွေ့ စမ်းသပ်ခဲ့သည့် Lab Files များ

1. **[header_audit.py](./header_audit.py)** — Website တစ်ခု၏ HTTP Security Headers ၅ ခုနှင့် Cookie Flags ၃ ခုကို စစ်ဆေးပေးသည့် Python Security Auditor။
2. **[clickjacking_lab.html](./clickjacking_lab.html)** — `<iframe>` သုံး၍ Clickjacking စမ်းသပ်သည့် HTML Lab (`X-Frame-Options: SAMEORIGIN` ကြောင့် `vvip9.co refused to connect` ဖြစ်ပုံကို လက်တွေ့ စမ်းသပ်ခဲ့သည်)။

---

## 🛡️ Production Nginx Fix Applied on `vvip9.co` (`VVIP9-DEV`)

`/etc/nginx/sites-available/dev-web` တွင် အောက်ပါ Security Headers များ ထည့်သွင်းပြီး Score `2/5` မှ `4/5` သို့ မြှင့်တင်ခဲ့သည်—

```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

---

## 📢 Share to the World (Blog & Video Script)

### 📝 Blog / Facebook Post Draft
> **Title:** 🛡️ Nginx မှာ စာကြောင်း ၄ ကြောင်း ထည့်ရုံနဲ့ မင်းရဲ့ Website ကို Hacker ရဲ့ Clickjacking နဲ့ SSL Strip ကနေ ကာကွယ်နည်း (Day 2/100)
>
> Website တစ်ခုမှာ HTTPS တပ်ထားရုံနဲ့ Browser ဘက်က လုံခြုံပြီလို့ ထင်တတ်ကြပါတယ်။ ဒီနေ့ Python နဲ့ ကိုယ်ပိုင် Security Header Auditor လေး ရေးပြီး ငါတို့ Server ကို စစ်ကြည့်တော့ အရေးကြီးတဲ့ Header တွေနဲ့ Cookie Flag တွေရဲ့ အလုပ်လုပ်ပုံကို လက်တွေ့ မြင်ခဲ့ရတယ်—
>
> 1. **`X-Frame-Options: SAMEORIGIN`** — Hacker က သူ့ဆိုဒ်ထဲမှာ ကိုယ့် Website ကို `<iframe>` နဲ့ ထည့်ပြီး လိမ်နှိပ်ခိုင်းတဲ့ Clickjacking ကို တားပေးတယ်။
> 2. **`X-Content-Type-Options: nosniff`** — ပုံအယောင်ဆောင်ထားတဲ့ Script တွေကို Browser က မRun အောင် တားပေးတယ်။
> 3. **`Strict-Transport-Security (HSTS)`** — Browser ကို HTTP လုံးဝမသုံးဘဲ HTTPS ပဲ အမြဲသုံးဖို့ အမိန့်ပေးတယ်။
> 4. **`Referrer-Policy`** — တခြား Link နှိပ်သွားချိန် URL အပြည့်အစုံ မပေါက်ကြားအောင် ထိန်းပေးတယ်။
>
> `#100DaysOfCybersecurity` `#DevSecOps` `#Nginx` `#Laravel` `#WebSecurity`

### 🎬 60-Second YouTube / TikTok Script
- **⚡ 00:00 – 00:08 (Hook):** *"Hacker က သူ့ရဲ့ Website အတုထဲမှာ မင်းရဲ့ Website ကို အကြည်ရောင် ထပ်တင်ပြီး User ကို လိမ်နှိပ်ခိုင်းလို့ ရတယ်ဆိုတာ သိလား? အဲ့ဒါကို Clickjacking လို့ ခေါ်တယ်!"*
- **📖 00:08 – 00:25 (Demo):** *"ဒီမှာ ကြည့်ပါဦး၊ ငါ HTML ဖိုင်တစ်ခုဆောက်ပြီး `<iframe>` နဲ့ Website ကို ထည့်ကြည့်လိုက်တယ်။ ဒါပေမဲ့ Nginx မှာ `X-Frame-Options: SAMEORIGIN` ခံထားတဲ့အတွက် Browser က `refused to connect` ဆိုပြီး ချက်ချင်း ပိတ်ချလိုက်တယ်!"*
- **💻 00:25 – 00:48 (Fix):** *"ဒီနေ့ Python နဲ့ Header Scanner တစ်ခုရေးပြီး စစ်ကြည့်တော့ `HSTS` နဲ့ `Referrer-Policy` လိုနေတာ တွေ့လို့ Nginx ထဲမှာ `add_header` ၂ ကြောင်း ထပ်ဖြည့်လိုက်တာ Security Score က 2/5 ကနေ 4/5 ချက်ချင်း တက်သွားပြီ!"*
- **🎯 00:48 – 01:00 (CTA):** *"ဒါက Day 2 of 100 Days of Cybersecurity ပါ။ မနက်ဖြန် Day 3 မှာ Hacker တွေ Hidden Subdomain တွေကို ဘယ်လိုရှာသလဲ ဆက်ပြပေးမယ်၊ Follow လုပ်ထားကြနော်!"*
