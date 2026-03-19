import re
from urllib.parse import urlparse

def clean_text(text):
    return text.lower().strip()

def extract_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    return re.findall(url_pattern, text)

def is_suspicious_domain(url):
    suspicious_keywords = ['login', 'verify', 'secure', 'account', 'bank']
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    return any(word in domain for word in suspicious_keywords)