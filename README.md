# reScript

A small Python script that uses the `re` module to extract IPv4 addresses, MD5 hashes, and SHA256 hashes from a text file.

## Features

- **IPv4 extraction** — matches four dot-separated groups of 1-3 digits (`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`). This is a lightweight pattern and does not validate the 0-255 range per octet, so strings like `999.999.999.999` are also matched.
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

The script prints three lists to stdout: matched IPv4 addresses, MD5 hashes, and SHA256 hashes, in that order.

## Example

Given a `dosya.txt` containing:

```
Connection from 192.168.1.1
MD5: 5d41402abc4b2a76b9719d911017c592
SHA256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

Running `python main.py` outputs:

```
['192.168.1.1']
['5d41402abc4b2a76b9719d911017c592']
['2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824']
```

## Project structure

- [main.py](main.py) — contains `extract_ipv4`, `extract_md5`, and `extract_sha256`, plus the script entry point that reads `dosya.txt` and prints the results.
- [dosya.txt](dosya.txt) — sample input file used for testing.
