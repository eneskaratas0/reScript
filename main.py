import re

def extract_ipv4(text):
    octet = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    octet_ipv4 = rf"{octet}(?:\.{octet}){{3}}"
    ip_matches = re.findall(octet_ipv4, text)
    return ip_matches

def extract_md5(text):
    octet_md5 = r"\b[0-9a-fA-F]{32}\b"
    md5_matches = re.findall(octet_md5, text)
    return md5_matches

def extract_sha256(text):
    octet_sha256 = r"\b[0-9a-fA-F]{64}\b"
    sha256_matches = re.findall(octet_sha256, text)
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