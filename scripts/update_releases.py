#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys, urllib.request
from pathlib import Path

DOWNLOAD = Path(__file__).resolve().parents[1] / "download.md"
UA = "xhj-release-updater/1.0"

PROJECTS = {
    "clash-verge-rev/clash-verge-rev": [
        r"Clash[ .]Verge[_-].*?_x64-setup\.exe$",
        r"Clash[ .]Verge[_-].*?_x64_fixed_webview2-setup\.exe$",
        r"Clash[ .]Verge[_-].*?_aarch64\.dmg$",
        r"Clash[ .]Verge[_-].*?_x64\.dmg$",
    ],
    "chen08209/FlClash": [
        r"FlClash-.*-android-arm64-v8a\.apk$",
        r"FlClash-.*-android-armeabi-v7a\.apk$",
        r"FlClash-.*-android-x86_64\.apk$",
    ],
    "2dust/v2rayN": [
        r"v2rayN-windows-64\.zip$",
    ],
    "MetaCubeX/ClashMetaForAndroid": [
        r"cmfa-.*-meta-arm64-v8a-release\.apk$",
        r"cmfa-.*-meta-armeabi-v7a-release\.apk$",
        r"cmfa-.*-meta-universal-release\.apk$",
    ],
}

def latest(repo: str) -> dict:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/releases/latest",
        headers={"Accept":"application/vnd.github+json", "User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def choose_assets(rel: dict, patterns: list[str]) -> dict[str,str]:
    assets = rel.get("assets", [])
    out = {}
    for pat in patterns:
        rx = re.compile(pat, re.I)
        hit = next((a for a in assets if rx.search(a.get("name", ""))), None)
        if hit:
            out[pat] = hit["browser_download_url"]
    return out

def direct_and_proxy_replace(text: str, repo: str, new_urls: dict[str,str]) -> tuple[str,int]:
    count=0
    # Replace old GitHub release URLs for this repo by matching asset family/name pattern.
    for pat, new in new_urls.items():
        asset_name = new.rsplit('/',1)[-1]
        # derive a stable asset-family regex from the configured pattern
        old_url_rx = re.compile(rf"https://github\.com/{re.escape(repo)}/releases/download/[^/]+/[^\s\"')>]+", re.I)
        candidates = list(old_url_rx.finditer(text))
        for m in reversed(candidates):
            old=m.group(0)
            old_asset=old.rsplit('/',1)[-1]
            if re.search(pat, old_asset, re.I):
                text=text[:m.start()]+new+text[m.end():]
                count+=1
        # proxy forms are automatically updated because the embedded direct URL is also matched above.
    return text,count

def main() -> int:
    text=DOWNLOAD.read_text(encoding="utf-8")
    total=0
    summary=[]
    for repo, patterns in PROJECTS.items():
        rel=latest(repo)
        tag=rel.get("tag_name", "?")
        selected=choose_assets(rel, patterns)
        missing=[p for p in patterns if p not in selected]
        if missing:
            print(f"WARN {repo} {tag}: missing {len(missing)} expected asset(s)", file=sys.stderr)
        text,n=direct_and_proxy_replace(text,repo,selected)
        total+=n
        summary.append(f"{repo}: {tag} ({len(selected)}/{len(patterns)} assets)")
    DOWNLOAD.write_text(text,encoding="utf-8")
    print("\n".join(summary))
    print(f"URLs replaced: {total}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
