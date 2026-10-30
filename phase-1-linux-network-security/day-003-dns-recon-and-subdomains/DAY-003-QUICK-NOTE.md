# 📝 Day 003 Quick Note (အတိုချုပ် မှတ်စု)

| # | သင်ခဲ့သည့် ခေါင်းစဉ် (Title) | အဓိပ္ပာယ် အတိုချုပ် (One-Line Meaning) |
| :-: | :--- | :--- |
| **1** | **Subdomain Enumeration** | Main Domain (`starchannel.tv`) ရဲ့ နောက်ကွယ်မှာ ဝှက်ထားတဲ့ Subdomain အားလုံး (`api.`, `cp.`, `web.`, `dev.`) ကို ရှာဖွေဖော်ထုတ်ခြင်း။ |
| **2** | **Certificate Transparency (CT) Logs (`crt.sh`)** | `certbot` နဲ့ SSL တင်လိုက်တိုင်း ကမ္ဘာ့ Public မှတ်တမ်းကြီးပေါ် အလိုအလျောက် ရောက်သွားလို့ Hacker တွေ Subdomain အားလုံး အလွယ်တကူ ရှာတွေ့နိုင်သည့် စနစ်။ |
| **3** | **DNS Brute-Force (Wordlist)** | အသုံးများသော Subdomain နာမည်များ (`dev`, `staging`, `admin`, `api`) ကို DNS Server တွင် တိုက်ရိုက် မေးမြန်းရှာဖွေခြင်း။ |
| **4** | **Shadow IT / Forgotten Subdomains** | Developer တွေ စမ်းသပ်ဖို့ ဆောက်ပြီး မေ့ကျန်ခဲ့တဲ့ `staging.` သို့မဟုတ် `dev.` Subdomain များ (Main site ထက် Security အားနည်းတတ်သည်)။ |
| **5** | **`APP_DEBUG=true` in Public Subdomains** | Internet ပေါ် ပွင့်နေသော Staging/Dev Subdomain တွင် `APP_DEBUG=true` မေ့ပွင့်ကျန်ခဲ့ပါက Error တက်ချိန်တွင် Source Code နှင့် Server Path များ ပေါက်ကြားခြင်း။ |
| **6** | **`APP_ENV=local` Risk** | Production/Public Server တွင် `APP_ENV=local` ထားမိပါက Horizon/Telescope လို Dashboard များ Login မလိုဘဲ အပြင်မှ ဝင်ကြည့်နိုင်သွားခြင်း။ |
| **7** | **Subdomain Hardening** | မသုံးတော့သည့် Subdomain DNS ဖျက်ခြင်း၊ Public Staging/Dev များတွင်လည်း `APP_DEBUG=false` ထားပြီး Error ကို `storage/logs/laravel.log` မှသာ ကြည့်ခြင်း။ |
