import re

def extract_ipv4(text):
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ip_matches = re.findall(ip_pattern, text)
    return ip_matches

def extract_md5(text):
    md5_pattern = r"\b[0-9a-fA-F]{32}\b"
    md5_matches = re.findall(md5_pattern, text)
    return md5_matches

def extract_sha256(text):
    sha256_pattern = r"\b[0-9a-fA-F]{64}\b"
    sha256_matches = re.findall(sha256_pattern, text)
    return sha256_matches


if __name__ == "__main__":
    with open("dosya.txt", "r", encoding="utf-8") as f:
        content = f.read()
        ipv4_matches = extract_ipv4(content)
        md5_matches = extract_md5(content)
        sha256_matches = extract_sha256(content)
        print(ipv4_matches)
        print(md5_matches)
        print(sha256_matches)