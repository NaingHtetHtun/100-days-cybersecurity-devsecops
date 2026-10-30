# 📅 Day 003: DNS Recon & Subdomain Hunting — Hacker တွေ `dev-api` နဲ့ Hidden Staging Server တွေကို ဘယ်လို ရှာဖွေသလဲ?

> **Phase:** Phase 1 (Linux, SSH, Nginx & Network Security) | **Time Spent:** 60 Mins  
> **Tech Stack Involved:** DNS (`A`, `CNAME`), SSL Certificate Transparency (`crt.sh`), Python Recon, Laravel `.env` (`APP_DEBUG`)  
> **🎓 Certification Alignment:** **Fortinet FCF** • **CompTIA Security+ (SY0-701)** (Objective 4.1: Attack Surface & Recon) • **ISC2 CC**

👉 **အတိုချုပ် မှတ်စု (Quick Note) ဖတ်ရန်:** [DAY-003-QUICK-NOTE.md](./DAY-003-QUICK-NOTE.md)

---

## 🛠️ ဒီနေ့ လက်တွေ့ စမ်းသပ်ခဲ့သည့် Lab File

- **[subdomain_hunter.py](./subdomain_hunter.py)** — Passive Subdomain Databases (`crt.sh` / `HackerTarget`) နှင့် DNS Enumeration သုံးပြီး Domain တစ်ခု၏ နောက်ကွယ်မှ Subdomain အားလုံးနှင့် Server IP များကို ရှာဖွေပေးသည့် Python Tool။

---

## 🔍 Real-World Vulnerability Discovered During Day 003 Lab!

`subdomain_hunter.py` ဖြင့် `starchannel.tv` နှင့် `vvip9.co` တို့ကို စစ်ဆေးရာမှ တွေ့ရှိခဲ့သော `web.starchannel.tv` (`/var/www/star/staging`) နှင့် `dev-cp.vvip9.co` (`/var/www/dev/backend`) တို့တွင် အောက်ပါအတိုင်း **`APP_ENV=local` နှင့် `APP_DEBUG=true`** ပွင့်နေကြောင်း လက်တွေ့ ဖော်ထုတ်တွေ့ရှိခဲ့သည်—

```text
/var/www/star/staging/.env:APP_ENV=local
/var/www/star/staging/.env:APP_DEBUG=true

/var/www/dev/backend/.env:APP_ENV=local
/var/www/dev/backend/.env:APP_DEBUG=true
```

---

## 📢 Share to the World (Blog & Video Script)

### 📝 Blog / Facebook Post Draft
> **Title:** 🕵️‍♂️ Main Website ကို အသေအချာ လုံခြုံအောင် ပိတ်ထားပေမဲ့ `staging.` သို့မဟုတ် `dev.` Subdomain ကနေ ပေါက်သွားတဲ့အခါ! (Day 3/100)
>
> Developer တော်တော်များများက `"ငါ့ရဲ့ staging.example.com နာမည်ကို ဘယ်သူ့မှ မပြောထားတော့ Hacker မသိနိုင်ပါဘူး"` လို့ ထင်တတ်ကြပါတယ်။
>
> ဒါပေမဲ့ မင်း `certbot` နဲ့ SSL Certificate တင်လိုက်တာနဲ့ Let's Encrypt က အဲ့ဒီ Subdomain နာမည်ကို ကမ္ဘာ့ Public Certificate Transparency Log (`crt.sh`) ပေါ်မှာ တရားဝင် တင်ပေးလိုက်ပါတယ်!
>
> ဒီနေ့ Python နဲ့ Subdomain Hunter Script လေး ရေးပြီး ကိုယ့်ရဲ့ Domain တွေကို ပြန်စစ်ကြည့်တော့—
> 1. နောက်ကွယ်က `api.`, `cp.`, `web.`, `dev-cp.` Subdomain အားလုံးနဲ့ Server IP တွေ စက္ကန့်ပိုင်းအတွင်း ထွက်လာတယ်။
> 2. ပိုအရေးကြီးတာက Main site တွေမှာ `APP_DEBUG=false` ပိတ်ထားပေမဲ့ Staging နဲ့ Dev Subdomain `.env` မှာ `APP_DEBUG=true` နဲ့ `APP_ENV=local` ပွင့်ကျန်နေတာကို လက်ပူးလက်ကြပ် ရှာတွေ့ခဲ့တယ်!
>
> **🛡️ ကာကွယ်နည်း:** Internet ပေါ်ကနေ ဝင်လို့ရတဲ့ ဘယ် Server (Staging/Dev အပါအဝင်) မှာမဆို `APP_DEBUG=false` ပိတ်ထားပါ။ Error ကြည့်ချင်ရင် Server ပေါ်မှာ `tail -f storage/logs/laravel.log` နဲ့ပဲ ကြည့်ပါ!
>
> `#100DaysOfCybersecurity` `#DevSecOps` `#LaravelSecurity` `#DNS` `#BugBounty`

### 🎬 60-Second YouTube / TikTok Script
- **⚡ 00:00 – 00:08 (Hook):** *"မင်း လျှို့ဝှက်ပြီး ဆောက်ထားတဲ့ `dev.` ဒါမှမဟုတ် `staging.` Subdomain ကို Hacker တွေက ဘာလို့ ၁၀ စက္ကန့်အတွင်း အတိအကျ ရှာတွေ့သွားတာလဲ သိလား?"*
- **📖 00:08 – 00:25 (Story):** *"အဖြေကတော့ မင်း `certbot` နဲ့ Free SSL တင်လိုက်တိုင်း အဲ့ဒီ Subdomain နာမည်ဟာ ကမ္ဘာ့ Public Certificate Transparency Log ပေါ် အလိုအလျောက် ရောက်သွားလို့ပဲ! အဲ့ဒီအပြင် Python Script လေး တစ်ပုဒ်နဲ့ DNS ကို မေးလိုက်ရုံနဲ့ Subdomain အားလုံးနဲ့ Server IP တွေ အကုန် ထွက်လာတယ်!"*
- **💻 00:25 – 00:48 (Real Discovery & Fix):** *"ဒီနေ့ ငါ့ရဲ့ Domain တွေကို ကိုယ်တိုင် စစ်ကြည့်လိုက်တော့ Main Website မှာ `APP_DEBUG=false` ပိတ်ထားပေမဲ့၊ နောက်ကွယ်က `staging` နဲ့ `dev` Subdomain တွေမှာ `APP_DEBUG=true` ပွင့်ကျန်နေတာကို ရှာတွေ့ခဲ့တယ်! Internet ပေါ် ပွင့်နေတဲ့ Server တိုင်းမှာ `APP_DEBUG=false` ပိတ်ထားဖို့ လုံးဝ မမေ့ပါနဲ့!"*
- **🎯 00:48 – 01:00 (CTA):** *"ဒါက Day 3 of 100 Days of Cybersecurity ပါ။ မနက်ဖြန် Day 4 မှာ Nmap နဲ့ Server တံခါးပေါက် (Ports) တွေ စစ်နည်း ဆက်သွားမယ်၊ Follow လုပ်ထားကြနော်!"*
