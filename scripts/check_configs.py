#!/usr/bin/env python3
import urllib.request
import os

WHITELIST_SOURCE_URLS = {
    "WHITE-CIDR-RU-all.txt":     "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-all.txt",
    "WHITE-CIDR-RU-checked.txt": "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-checked.txt",
    "WHITE-SNI-RU-all.txt":      "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-SNI-RU-all.txt",
}

OUTPUT_DIR = "configs"


def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  [WARN] Could not fetch {url}: {e}")
        return ""


def main():
    print("=== Whitelist Updater ===\n")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Downloading whitelists...")
    for filename, url in WHITELIST_SOURCE_URLS.items():
        print(f"  Fetching {filename} ...")
        raw = fetch_url(url)
        if raw:
            with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
                f.write(raw)
            lines = len([l for l in raw.splitlines() if l.strip()])
            print(f"    Saved {lines} lines.")
        else:
            print(f"    [WARN] Failed to download {filename}")

    print("\nDone.")


if __name__ == "__main__":
    main()
