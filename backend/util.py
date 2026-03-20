import re

def contains_urgency(text):
    keywords = ["urgent", "immediately", "act now", "limited time", "account blocked"]
    return any(word in text.lower() for word in keywords)

def contains_suspicious_links(text):
    return "http" in text or "www" in text

def is_ip_url(url):
    return bool(re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url))

def has_special_chars(url):
    return "@" in url or "-" in url or "//" in url