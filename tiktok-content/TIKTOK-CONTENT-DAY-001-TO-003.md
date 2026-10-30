# 🎬 TikTok Content Pack: Days 001 – 003 (100 Days of Cybersecurity & DevSecOps)

> 💡 **အသုံးပြုပုံ:**  
> Day တစ်ခုချင်းစီအတွက် **TikTok Photo Mode (Carousel Slide ၃ ပုံ)** တင်ရန် ပုံ (၃) ပုံစီနှင့် **Copy-Paste တန်းတင်နိုင်သော မြန်မာလို Caption + Voiceover Script + Hashtags** အပြည့်အစုံကို စုစည်းပေးထားပါသည်။
> - **AI Visual Infographic ပုံ (၉) ပုံ:** `tiktok-content/day-001/`, `day-002/`, `day-003/` ဖိုဒါများထဲတွင် တိုက်ရိုက် ယူသုံးနိုင်ပါသည်။
> - **မြန်မာစာ + Terminal Code ပါသော Slide ပုံ (၉) ပုံ လိုချင်ပါက:** `brave-tiktok-slide-exporter.html` ကို မင်းရဲ့ **Brave Browser** ဖြင့် ဖွင့်ပြီး `Download 1080x1920 PNG` ခလုတ်နှိပ်ကာ တစ်ပုံချင်း ဒေါင်းယူနိုင်ပါသည်!

---

## 🔥 DAY 001: Hacker တွေ Server တစ်လုံးကို မဖောက်ခင် ပထမဆုံး ဘာလုပ်သလဲ? (Recon & Info Disclosure)

### 🖼️ အသုံးပြုမည့် ပုံ (၃) ပုံ (`tiktok-content/day-001/`)
1. **ပုံ (၁) — `day1-slide1-recon.png`:** Hacker က `curl -I` တစ်ကြောင်းတည်းနဲ့ Server ရဲ့ Nginx Version အတိအကျ (`nginx/1.26.3`) ကို လှမ်းထောက်လှမ်းနေပုံ (Red Team Attack)
2. **ပုံ (၂) — `day1-slide2-cookie-encryption.png`:** Laravel Session Cookie ကို Base64 ဖြည်ကြည့်ပေမယ့် `AES-256-CBC` + `HMAC-SHA256` သော့ခတ်ထားလို့ `APP_KEY` မရှိဘဲ ပြင်မရပုံ (Under the Hood)
3. **ပုံ (၃) — `day1-slide3-nginx-defense.png`:** Nginx မှာ `server_tokens off;` တစ်ကြောင်းတည်းထည့်ပြီး Version Number ကို အပြီးတိုင် ဖျောက်ပစ်ပုံ (Blue Team Fix)

---

### 📋 TikTok Post Caption (Copy ကူးပြီး တန်းတင်ရန်)

```text
🛡️ 100 Days of Cybersecurity & DevSecOps — Day 1/100 🚀

Hacker တစ်ယောက်က မင်းရဲ့ Website သို့မဟုတ် Server ကို စတိုက်ခိုက်တော့မယ်ဆိုရင် ပထမဆုံး ဘာလုပ်တယ်ထင်လဲ? 🤔

အဖြေကတော့ "Reconnaissance (ထောက်လှမ်းခြင်း)" ပါပဲ!

🔴 1. The Attack (ပုံ - ၁)
Terminal ကနေ `curl -I https://yourwebsite.com` ဆိုပြီး ရိုးရိုးလေး လှမ်းမေးလိုက်ရုံနဲ့ Server က `Server: nginx/1.26.3 (Ubuntu)` ဆိုပြီး သူသုံးထားတဲ့ OS နဲ့ Version အတိအကျကို ပြန်ပြောပြနေတတ်ပါတယ်။
ဒါကို "Banner Grabbing / Information Disclosure" လို့ ခေါ်ပါတယ်။ Hacker က Version အတိအကျ သိသွားရင် အဲ့ဒီ Version မှာရှိတဲ့ CVE ဟာကွက်အတိုင်း အလွယ်တကူ တိုက်ခိုက်နိုင်သွားပါပြီ!

🔐 2. Laravel Cookie Under the Hood (ပုံ - ၂)
Response Header ထဲမှာ ပါလာတဲ့ Laravel Session Cookie ကို Base64 ဖြည်ကြည့်လိုက်ရင် `iv`, `value`, `mac` ဆိုပြီး ၃ ပိုင်း တွေ့ရပါတယ်။
Laravel က Cookie ကို `AES-256-CBC` နဲ့ Encrypt လုပ်ထားသလို `HMAC-SHA256` နဲ့ တံဆိပ်ခတ်ထားလို့ Server ပေါ်က `.env` ထဲက `APP_KEY` မပေါက်ကြားသရွေ့ Hacker က Cookie ကို လုံးဝ ပြင်လို့/ဖတ်လို့ မရပါဘူး! (ဒါကြောင့် APP_KEY ကို အသက်လို ကာကွယ်ပါ!)

🔵 3. The 1-Line Fix (ပုံ - ၃)
ကိုယ့် Server ရဲ့ Nginx Version ကို Hacker မမြင်ရအောင် `/etc/nginx/nginx.conf` ထဲမှာ ဒီတစ်ကြောင်းလေးပဲ ထည့်ပေးရုံပါပဲ—
👉 `server_tokens off;`

Nginx ကို reload လုပ်ပြီး ပြန်စစ်ကြည့်လိုက်ရင် Version နံပါတ် လုံးဝ ပျောက်သွားပြီး `Server: nginx` လို့ပဲ ထွက်ပါတော့တယ်! ✅

မနက်ဖြန် Day 2 မှာ Browser Security Headers တွေနဲ့ Cookie Flags (`HttpOnly`, `Secure`, `SameSite`) အကြောင်း လက်တွေ့ ဆက်စမ်းပြပါမယ်။ Follow လုပ်ထားကြနော် သားကြီးတို့! 🔥

#cybersecurity #devsecops #webdeveloper #laravel #nginx #linux #myanmartech #100daysofcybersecurity #ethicalhacking #codingmyanmar
```

---

### 🎙️ Voiceover Script (အသံသွင်းချင်သူများအတွက် စက္ကန့် ၄၀ စာ)
> *"100 Days of Cybersecurity Day 1 မှ ကြိုဆိုပါတယ် သားကြီးတို့! Hacker တစ်ယောက်က Server တစ်လုံးကို မဖောက်ခင် ပထမဆုံး ဘာလုပ်သလဲ သိလား? Terminal ကနေ `curl -I` ဆိုတဲ့ Command လေး တစ်ကြောင်းနဲ့ Server ရဲ့ Response Header ကို လှမ်းကြည့်တာပါ။ အဲ့ဒီမှာ Server အများစုက `nginx/1.26.3 Ubuntu` ဆိုပြီး ကိုယ်သုံးထားတဲ့ Version အတိအကျကို သွားပြောပြမိနေတတ်ပါတယ်။ ဒါကို ပိတ်ချင်ရင်တော့ `/etc/nginx/nginx.conf` ထဲမှာ `server_tokens off;` ဆိုတဲ့ စာကြောင်းလေး တစ်ကြောင်းပဲ ထည့်ပြီး Nginx reload လုပ်လိုက်ပါ။ Version နံပါတ် လုံးဝ ပျောက်သွားပါလိမ့်မယ်! Day 2 မှာ ဘာဆက်လုပ်မလဲ သိချင်ရင် Follow လုပ်ထားလိုက်တော့နော်!"*

---
---

## 🔥 DAY 002: Website ကို iframe ထဲ ထည့်ပြီး ခိုးနှိပ်ခိုင်းတဲ့ Clickjacking နဲ့ Cookie လုံခြုံရေး!

### 🖼️ အသုံးပြုမည့် ပုံ (၃) ပုံ (`tiktok-content/day-002/`)
1. **ပုံ (၁) — `day2-slide1-clickjacking.png`:** Hacker က အပြင်မှာ "iPhone မဲပေါက်သည်" ခလုတ်ပြထားပြီး နောက်ကွယ်မှာ အကြည်ရောင် (`opacity: 0`) `<iframe>` နဲ့ Admin/Bank ခလုတ်ကို ထပ်ထားသည့် Clickjacking Attack
2. **ပုံ (၂) — `day2-slide2-security-headers.png`:** Website တစ်ခုတိုင်း မဖြစ်မနေ တပ်ဆင်ထားရမည့် HTTP Security Header ဒိုင်း (၅) ချပ် (`X-Frame-Options`, `HSTS`, `nosniff`, `Referrer-Policy`, `CSP`)
3. **ပုံ (၃) — `day2-slide3-cookie-flags.png`:** Login Session Cookie ကို XSS နဲ့ CSRF ရန်မှ ကာကွယ်ပေးသည့် သော့ (၃) ချောင်း (`HttpOnly`, `Secure`, `SameSite=Lax`)

---

### 📋 TikTok Post Caption (Copy ကူးပြီး တန်းတင်ရန်)

```text
🛡️ 100 Days of Cybersecurity & DevSecOps — Day 2/100 🚀

မင်းရဲ့ Website က HTTPS (အစိမ်းရောင် သော့ခလောက်လေး) ပါနေရုံနဲ့ လုံခြုံပြီလို့ ထင်နေလား? 😱
HTTP Security Headers တွေ မပါရင် Hacker က User ရဲ့ Browser ကို အလွယ်တကူ လှည့်စားလို့ရပါတယ်!

🔴 1. Clickjacking Attack ဆိုတာ ဘာလဲ? (ပုံ - ၁)
Hacker က "iPhone ကံစမ်းမဲ နှိပ်ရန်" ဆိုတဲ့ အတု Page တစ်ခု ဆောက်ပြီး အပေါ်မှာ မင်းရဲ့ Website သို့မဟုတ် Admin Panel ကို အကြည်ရောင် (`opacity: 0`) `<iframe>` နဲ့ ထပ်ထားလိုက်ပါတယ်။
User က ဆုမဲခလုတ်ကို နှိပ်လိုက်ပေမယ့် တကယ်တမ်း နောက်ကွယ်က မင်းရဲ့ Website ထဲက "Delete Account" သို့မဟုတ် "Confirm Transfer" ခလုတ်ကို နှိပ်မိသွားတာမျိုးပါ!

🔵 2. မဖြစ်မနေ တပ်ဆင်ရမည့် Security Header ဒိုင်း (၅) ချပ် (ပုံ - ၂)
ကိုယ့်ရဲ့ Production Server (Nginx) ကို Python Audit Script နဲ့ စစ်ဆေးပြီး ဒီ Header တွေ ထည့်သွင်းခဲ့ပါတယ်—
✅ `X-Frame-Options: SAMEORIGIN` -> သူများ ဆိုဒ်က ကိုယ့်ဆိုဒ်ကို iframe ထဲ ထည့်မရအောင် ပိတ်သည် (Clickjacking ကာကွယ်သည်)
✅ `X-Content-Type-Options: nosniff` -> ပုံ (.jpg) အယောင်ဆောင်ထားတဲ့ Hacker JS/HTML ဖိုင်တွေကို Browser က မRun အောင် တားသည်
✅ `Strict-Transport-Security (HSTS)` -> Browser ကို HTTP လုံးဝမသုံးဘဲ HTTPS အမြဲသုံးရန် အမိန့်ပေးသည်
✅ `Referrer-Policy` -> Link နှိပ်သွားချိန် URL အပြည့်အစုံ မပေါက်ကြားအောင် ထိန်းသည်
✅ `Content-Security-Policy (CSP)` -> XSS script များ မRun နိုင်အောင် ကာကွယ်သည်

🍪 3. Cookie Security Flags ၃ ခု (ပုံ - ၃)
User Login ဝင်ထားတဲ့ Session Cookie မှာ ဒီ Flag ၃ ခု ပါ/မပါ အမြဲစစ်ပါ—
🔒 `HttpOnly` -> JavaScript (`document.cookie`) ကနေ Cookie ခိုးယူ၍ လုံးဝမရအောင် ပိတ်သည်
🔒 `Secure` -> HTTPS လိုင်းပေါ်ကသာ Cookie ပို့ဆောင်မည်
🔒 `SameSite=Lax` -> တခြား ဆိုဒ်ကနေ လှမ်းတိုက်ခိုက်တဲ့ CSRF Attack ကို ကာကွယ်သည်

ကိုယ့် Website မှာရော ဒီ Header တွေ ပါပြီလား? Day 3 မှာ Hacker တွေ နောက်ကွယ်က ဝှက်ထားတဲ့ `dev` နဲ့ `staging` Subdomain တွေကို ဘယ်လို ရှာဖွေဖောက်ထွင်းသလဲ ဆက်ပြပေးပါမယ်! 🔥

#cybersecurity #devsecops #websecurity #laravel #nginx #clickjacking #infosec #myanmartech #100daysofcybersecurity #webdeveloper
```

---

### 🎙️ Voiceover Script (အသံသွင်းချင်သူများအတွက် စက္ကန့် ၄၅ စာ)
> *"100 Days of Cybersecurity Day 2 ပါ သားကြီးတို့! Website မှာ HTTPS သော့ခလောက်လေး ပါရုံနဲ့ လုံခြုံပြီလို့ မထင်လိုက်ပါနဲ့။ တကယ်လို့ မင်းရဲ့ Server မှာ `X-Frame-Options` header မပါရင် Hacker က မင်းရဲ့ Website ကို အကြည်ရောင် iframe ထဲ ထည့်ပြီး User တွေကို မသိဘဲ ခလုတ်မှားနှိပ်မိအောင် လှည့်စားတဲ့ Clickjacking တိုက်ခိုက်မှု လုပ်လို့ရပါတယ်။ ဒါကြောင့် ဒီနေ့မှာ Python script တစ်ခု ရေးပြီး ကိုယ့် Server ရဲ့ Security Header ၅ ခုနဲ့ Cookie Flags တွေဖြစ်တဲ့ `HttpOnly`, `Secure`, `SameSite` တွေကို စစ်ဆေးပြင်ဆင်ခဲ့ပါတယ်။ Nginx မှာ `Strict-Transport-Security` နဲ့ `X-Frame-Options` ထည့်လိုက်တာနဲ့ Browser က အလိုအလျောက် ကာကွယ်ပေးသွားပါပြီ။ မနက်ဖြန် Day 3 က အရမ်းမိုက်မယ်၊ နောက်ကွယ်က Subdomain တွေ ဘယ်လိုရှာသလဲ ဆက်ကြည့်ရအောင်!"*

---
---

## 🔥 DAY 003: Main Website ကို အသေပိတ်ထားပေမယ့် `dev` နဲ့ `staging` Subdomain ကနေ ပေါက်သွားတဲ့အခါ! (`APP_DEBUG=true` အန္တရာယ်)

### 🖼️ အသုံးပြုမည့် ပုံ (၃) ပုံ (`tiktok-content/day-003/`)
1. **ပုံ (၁) — `day3-slide1-subdomain-recon.png`:** Main Domain (`website.com`) ကို အခိုင်အမာ ကာကွယ်ထားပေမယ့် Hacker က SSL Transparency Log (`crt.sh`) နဲ့ DNS Recon သုံးပြီး နောက်ကွယ်က `dev-api.`, `dev-cp.`, `staging.` တို့ကို ရှာတွေ့သွားပုံ
2. **ပုံ (၂) — `day3-slide2-app-debug-leak.png`:** Public ပွင့်နေသော Dev/Staging Subdomain မှာ `APP_ENV=local` နဲ့ `APP_DEBUG=true` မေ့ကျန်ခဲ့လို့ Error တက်ချိန် Server File Path (`/var/www/...`) တွေနဲ့ `/docs/api` (API Docs) တစ်ခုလုံး Login မလိုဘဲ ပွင့်နေပုံ
3. **ပုံ (၃) — `day3-slide3-production-fix.png`:** Server ပေါ်က `.env` မှာ `APP_ENV=production` နဲ့ `APP_DEBUG=false` ပိတ်ပြီး `/docs/api` ကို `403 Forbidden` ဖြစ်အောင် ကာကွယ်လိုက်ပုံ

---

### 📋 TikTok Post Caption (Copy ကူးပြီး တန်းတင်ရန်)

```text
🛡️ 100 Days of Cybersecurity & DevSecOps — Day 3/100 🚀

Main Website (`www.example.com`) ကို လုံခြုံရေး အပြည့်ပိတ်ထားပေမယ့် ကုမ္ပဏီတော်တော်များများ ဘာလို့ Hack ခံနေရသေးလဲ သိလား? 🤯

အဖြေကတော့ Developer တွေ စမ်းသပ်ဖို့ ဆောက်ထားပြီး မေ့ကျန်ခဲ့တဲ့ `dev.`, `staging.`, `dev-api.` ဆိုတဲ့ **Subdomains (Shadow IT)** တွေကြောင့်ပါပဲ!

🔴 1. Hacker တွေ Hidden Subdomain ကို ဘယ်လိုရှာသလဲ? (ပုံ - ၁)
မင်းက `dev-api.yourwebsite.com` ကို ဘယ်သူ့မှ မပြောဘဲ ဝှက်ထားတယ် ဆိုပေမယ့်...
`certbot` နဲ့ HTTPS SSL တင်လိုက်တဲ့ စက္ကန့်မှာတင် အဲ့ဒီ Subdomain နာမည်က ကမ္ဘာ့ Public **Certificate Transparency (CT) Logs (`crt.sh`)** ပေါ်ကို အလိုအလျောက် ရောက်သွားပါတယ်!
ဒါ့အပြင် DNS Enumeration script နဲ့ စက္ကန့်ပိုင်းအတွင်း အနောက်က Subdomain အားလုံးနဲ့ Server IP တွေကို ရှာတွေ့နိုင်ပါတယ်။

⚠️ 2. အကြီးမားဆုံး အမှား — Public Dev Server မှာ `APP_DEBUG=true` ပွင့်နေခြင်း! (ပုံ - ၂)
ဒီနေ့ ကိုယ်ပိုင် Server တွေကို Subdomain Hunter Python Script နဲ့ ပြန်စစ်ကြည့်တဲ့အခါ Main site တွေက လုံခြုံပေမယ့် Staging နဲ့ Dev Subdomain မှာ `APP_ENV=local` နဲ့ `APP_DEBUG=true` ပွင့်နေတာကို လက်ပူးလက်ကြပ် မိခဲ့ပါတယ်!
ဘာအန္တရာယ်ရှိလဲဆိုတော့—
❌ Error တမင်ဖြစ်အောင် `curl -X POST` နဲ့ ထိုးလိုက်တာနဲ့ Server ရဲ့ Folder Path အတိအကျ (`/var/www/...`) နဲ့ Code Stacktrace အကုန် ပြန်ပေါ်လာတယ်!
❌ `APP_ENV=local` ဖြစ်နေတဲ့အတွက် `/docs/api` (API Documentation) ကြီးတစ်ခုလုံးက Login လုံးဝမလိုဘဲ အပြင်လူတိုင်း ဝင်ကြည့်လို့ ရနေတယ်!

🔵 3. The Blue Team Fix (ပုံ - ၃)
Internet ပေါ်ကနေ လှမ်းဝင်လို့ရတဲ့ ဘယ် Server မဆို (Staging/Dev ဖြစ်ပါစေ) `.env` မှာ မဖြစ်မနေ ဒီလို ပိတ်ရပါမယ်—
✅ `APP_ENV=production`
✅ `APP_DEBUG=false`
✅ `php artisan config:clear`

ပိတ်ပြီး ပြန်စမ်းလိုက်တဲ့အခါ Stacktrace လည်း လုံးဝ မပေါ်တော့သလို `/docs/api` ကလည်း `403 Forbidden` နဲ့ လုံခြုံသွားပါပြီ! (Error ကြည့်ချင်ရင် SSH ကနေ `tail -f storage/logs/laravel.log` နဲ့ပဲ ကြည့်ပါ!)

မင်းတို့ရဲ့ Staging / Dev Server တွေမှာရော `APP_DEBUG=true` ပွင့်နေသေးလား? အခုပဲ စစ်ကြည့်လိုက်တော့နော်! 🔥

#cybersecurity #devsecops #laravel #php #subdomain #bugbounty #linuxserver #myanmartech #100daysofcybersecurity #webdeveloper
```

---

### 🎙️ Voiceover Script (အသံသွင်းချင်သူများအတွက် စက္ကန့် ၅၀ စာ)
> *"100 Days of Cybersecurity Day 3 ပါ သားကြီးတို့! Main Website ကြီးကို လုံခြုံရေး အထပ်ထပ် ပိတ်ထားပေမယ့် ဘာလို့ Server တွေ ပေါက်နေသေးလဲ သိလား? Developer တွေ စမ်းဖို့ ဆောက်ထားတဲ့ `dev` တို့ `staging` တို့လို Subdomain တွေကြောင့်ပါ! Certbot နဲ့ SSL တင်လိုက်တာနဲ့ Subdomain နာမည်က Public Certificate Log ပေါ် အလိုအလျောက် ရောက်သွားသလို DNS Brute-Force နဲ့လည်း စက္ကန့်ပိုင်းအတွင်း ရှာလို့ရပါတယ်။ ဒီနေ့ ကိုယ့်ရဲ့ Subdomain တွေကို ကိုယ်တိုင် ရေးထားတဲ့ Python Script နဲ့ ပြန်စစ်ကြည့်တော့ Dev Subdomain တစ်ခုမှာ `APP_ENV=local` နဲ့ `APP_DEBUG=true` ပွင့်ကျန်နေတာကို သွားတွေ့ပါတယ်။ အဲ့ဒါကြောင့် Error ဖြစ်အောင် လှမ်းထိုးလိုက်တာနဲ့ Server ထဲက File Path တွေ အကုန်ပေါ်နေသလို `/docs/api` ကလည်း Login မလိုဘဲ ပွင့်နေခဲ့ပါတယ်။ ချက်ချင်းပဲ `APP_ENV=production` နဲ့ `APP_DEBUG=false` ပြောင်းပိတ်လိုက်မှ `403 Forbidden` ဖြစ်ပြီး လုံခြုံသွားပါတယ်။ မင်းတို့ရဲ့ Dev Server တွေကိုလည်း အခုပဲ စစ်ကြည့်လိုက်ဦးနော်!"*
