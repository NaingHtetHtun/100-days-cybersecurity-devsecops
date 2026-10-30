#!/usr/bin/env python3
"""
Day 002 Hands-On Lab: HTTP Security Headers & Cookie Flags Auditor
မင်းကိုယ်တိုင် TARGET_URL ကို ပြောင်းပြီး စမ်းသပ်နိုင်သည့် Security Scanner
"""
import urllib.request
import ssl

# =====================================================================
# 👇 ဒီနေရာမှာ မင်း စစ်ကြည့်ချင်တဲ့ Website URL ကို ပြောင်းထည့်ပြီး စမ်းကြည့်ပါ
# =====================================================================
TARGET_URL = "https://citywizz.com"


def audit_site(url: str):
    print("=" * 75)
    print(f"🔍 Auditing Security Headers & Cookies for: {url}")
    print("=" * 75)

    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Day002-Security-Auditor/1.0"})

    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        headers = {k.lower(): v for k, v in resp.headers.items()}
        cookies = resp.headers.get_all("Set-Cookie") or []

    # 1. Security Headers စစ်ဆေးခြင်း
    security_checks = [
        (
            "x-frame-options",
            "Clickjacking ကာကွယ်ရေး (iframe ထဲ ထည့်ခိုးနှိပ်ခိုင်းခြင်းမှ ကာကွယ်သည်)",
            "add_header X-Frame-Options \"SAMEORIGIN\" always;",
        ),
        (
            "x-content-type-options",
            "MIME Sniffing ကာကွယ်ရေး (.jpg အယောင်ဆောင်ထားသော JS/HTML ကို Browser က မRun အောင် တားသည်)",
            "add_header X-Content-Type-Options \"nosniff\" always;",
        ),
        (
            "strict-transport-security",
            "HSTS (Browser ကို HTTP လုံးဝမသုံးဘဲ HTTPS အမြဲသုံးရန် အမိန့်ပေးသည်)",
            "add_header Strict-Transport-Security \"max-age=31536000; includeSubDomains\" always;",
        ),
        (
            "referrer-policy",
            "Referrer Policy (အခြား Link နှိပ်သွားချိန် URL အပြည့်အစုံ မပေါက်ကြားအောင် ထိန်းချုပ်သည်)",
            "add_header Referrer-Policy \"strict-origin-when-cross-origin\" always;",
        ),
        (
            "content-security-policy",
            "CSP (XSS ဖြစ်လျှင်တောင် ပြင်ပ Hacker Script များ မRun နိုင်အောင် ပိတ်ဆို့သည်)",
            "add_header Content-Security-Policy \"default-src 'self' ...\";",
        ),
    ]

    print("\n📌 [1] HTTP SECURITY HEADERS စစ်ဆေးချက် —")
    score = 0
    for header_key, desc, fix in security_checks:
        if header_key in headers:
            score += 1
            print(f"  ✅ {header_key.upper()} : ရှိပါသည် -> {headers[header_key]}")
            print(f"     💡 အဓိပ္ပာယ်: {desc}\n")
        else:
            print(f"  ❌ {header_key.upper()} : ပျောက်ဆုံးနေပါသည်! (MISSING)")
            print(f"     ⚠️ အန္တရာယ် : {desc}")
            print(f"     🛠️ Nginx Fix: {fix}\n")

    print(f"📊 Header Security Score: {score}/{len(security_checks)}\n")

    # 2. Cookie Security Flags စစ်ဆေးခြင်း
    print("📌 [2] COOKIE SECURITY FLAGS (HttpOnly, Secure, SameSite) စစ်ဆေးချက် —")
    if not cookies:
        print("  ℹ️ Set-Cookie မတွေ့ပါ။")
    for c in cookies:
        cname = c.split("=", 1)[0]
        c_lower = c.lower()
        has_httponly = "httponly" in c_lower
        has_secure = "secure" in c_lower
        has_samesite = "samesite=" in c_lower

        print(f"  🍪 Cookie Name: [{cname}]")
        print(f"     • HttpOnly : {'✅ ပါသည် (JS document.cookie မှ ခိုးယူ၍မရပါ)' if has_httponly else '⚠️ မပါပါ (JS မှ ဖတ်နိုင်သည်)'}")
        print(f"     • Secure   : {'✅ ပါသည် (HTTPS ဖြင့်သာ ပို့ဆောင်မည်)' if has_secure else '❌ မပါပါ (HTTP မှ ပေါက်ကြားနိုင်သည်!)'}")
        print(f"     • SameSite : {'✅ ပါသည် (CSRF တိုက်ခိုက်မှုမှ ကာကွယ်သည်)' if has_samesite else '❌ မပါပါ'}")
        print()


if __name__ == "__main__":
    audit_site(TARGET_URL)
