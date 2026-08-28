# reScript

A small Python script that uses the `re` module to extract IPv4 addresses, MD5 hashes, and SHA256 hashes from a text file.

## Features

- **IPv4 extraction** — matches four dot-separated octets, each validated to be in the 0-255 range (e.g. `25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9]`), so out-of-range strings like `999.999.999.999` are correctly rejected.
- **MD5 extraction** — matches standalone 32-character hexadecimal strings (`\b[0-9a-fA-F]{32}\b`).
- **SHA256 extraction** — matches standalone 64-character hexadecimal strings (`\b[0-9a-fA-F]{64}\b`).

Word boundaries (`\b`) around the hash patterns ensure only complete, exact-length hex sequences are matched — a fixed-length pattern without `\b` could otherwise match part of a longer hex string.

## Requirements

- Python 3 (no external dependencies — only the standard library `re` module is used)

## Usage

Place the text you want to scan in `dosya.txt` (in the same directory as `main.py`), then run:

```bash
python main.py
```

The script writes the extracted IOCs (indicators of compromise) to `iocs.json` in the same directory, deduplicated per list while preserving first-seen order.

## Example

`dosya.txt` includes a longer sample "incident report" with repeated IPs and hashes, plus deliberate edge cases (an out-of-range IP, and 31/33/40-character hex strings that should not be mistaken for MD5/SHA256).

Running `python main.py` against it produces an `iocs.json` file:

```json
{
  "ip": [
    "192.168.1.1",
    "10.0.0.254",
    "45.33.12.90",
    "172.16.0.1",
    "8.8.8.8",
    "203.0.113.45"
  ],
  "hash": {
    "md5": [
      "5d41402abc4b2a76b9719d911017c592",
      "7d793037a0760186574b0282f2f435e7",
      "f3f0c6e992b7562598d9865b6fe8b3a6"
    ],
    "sha256": [
      "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
      "486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7",
      "2f293f67aa33f2ce247b28d6fb2fef2623cfde731f96b3d7f84ae74e9e192bdd"
    ]
  }
}
```

Note that repeated IPs/hashes (e.g. `172.16.0.1`, the `invoice.exe` hash pair) appear only once, and the invalid/edge-case values in `dosya.txt` are correctly excluded.

## Project structure

- [main.py](main.py) — contains `extract_ipv4`, `extract_md5`, `extract_sha256`, and `dedupe`, plus the script entry point that reads `dosya.txt` and writes `iocs.json`.
- [dosya.txt](dosya.txt) — sample input file used for testing.
- `iocs.json` — generated output file (git-ignored, created when the script runs).
