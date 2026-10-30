#!/usr/bin/env python3
"""
Day 003 Hands-On Lab: Subdomain Hunter (Certificate Transparency + DNS Resolver)
မင်းကိုယ်တိုင် TARGET_DOMAIN ကို ပြောင်းပြီး နောက်ကွယ်က Subdomain အားလုံးကို ရှာဖွေနိုင်သည့် Tool
"""
import json
import socket
import urllib.request

# =====================================================================
# 👇 ဒီနေရာမှာ မင်း ရှာချင်တဲ့ Main Domain ကို ထည့်ပါ (ဥပမာ "vvip9.co" သို့မဟုတ် "starchannel.tv")
# =====================================================================
TARGET_DOMAIN = "kbzpay.com"

# အသုံးများသော Subdomain နာမည်များ (DNS Brute-Force အတွက်)
COMMON_SUBDOMAINS = [
    "www", "api", "cp", "admin", "dev", "dev-api", "dev-cp",
    "staging", "web", "test", "beta", "mail", "portal", "smartprofile"
]


def fetch_crt_sh(domain: str) -> set[str]:
    """Method 1: Passive Recon (HackerTarget + crt.sh Certificate Transparency Logs) မှ Subdomain အားလုံးကို ဆွဲထုတ်ခြင်း"""
    found = set()
    print(f"\n🔎 [Method 1] Checking Passive Subdomain Databases (HackerTarget & crt.sh) for *.{domain} ...")

    # 1A: HackerTarget Passive DNS / CT API (Fast & Reliable)
    ht_url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    try:
        req = urllib.request.Request(ht_url, headers={"User-Agent": "Day003-Subdomain-Hunter/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            lines = resp.read().decode("utf-8").splitlines()
            for line in lines:
                if "," in line and not line.startswith("error"):
                    host = line.split(",", 1)[0].strip().lower()
                    if host.endswith(domain):
                        found.add(host)
    except Exception:
        pass

    # 1B: crt.sh Certificate Transparency API
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Day003-Subdomain-Hunter/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for entry in data:
                names = entry.get("name_value", "").split("\n")
                for n in names:
                    n = n.strip().lower().lstrip("*.")
                    if n.endswith(domain):
                        found.add(n)
    except Exception:
        pass

    print(f"   ✅ Passive Databases မှ Subdomain ({len(found)}) ခု ရှာတွေ့ခဲ့ပါသည်!")
    return found


def brute_force_dns(domain: str) -> set[str]:
    """Method 2: အသုံးများသော Subdomain နာမည်များကို DNS တွင် တိုက်ရိုက် မေးမြန်းရှာဖွေခြင်း"""
    print(f"\n🔎 [Method 2] Running DNS Enumeration on common subdomain names for *.{domain} ...")
    found = {domain}
    for sub in COMMON_SUBDOMAINS:
        fqdn = f"{sub}.{domain}"
        try:
            socket.gethostbyname(fqdn)
            found.add(fqdn)
        except socket.gaierror:
            pass
    return found


def resolve_and_display(subdomains: set[str]):
    print("\n" + "=" * 78)
    print(f"🎯 ရှာတွေ့သမျှ SUBDOMAINS နှင့် နောက်ကွယ်မှ SERVER IP ADDRESSES ({len(subdomains)} found)")
    print("=" * 78)
    print(f"{'SUBDOMAIN':<32} | {'STATUS':<12} | {'SERVER IP(s)'}")
    print("-" * 78)

    for sub in sorted(subdomains):
        try:
            _, _, ips = socket.gethostbyname_ex(sub)
            ip_str = ", ".join(ips)
            print(f"{sub:<32} | {'🟢 ACTIVE':<11} | {ip_str}")
        except socket.gaierror:
            print(f"{sub:<32} | {'⚪ NO DNS':<11} | (DNS record ဖျက်ထားသည် သို့မဟုတ် မရှိတော့ပါ)")
    print("=" * 78 + "\n")


if __name__ == "__main__":
    all_subs = fetch_crt_sh(TARGET_DOMAIN) | brute_force_dns(TARGET_DOMAIN)
    resolve_and_display(all_subs)
