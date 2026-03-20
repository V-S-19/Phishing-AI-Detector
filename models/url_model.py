def dummy_url_check(url):
    suspicious_words = ["login", "verify", "update", "bank", "secure"]

    if "@" in url:
        return "Suspicious URL"

    for word in suspicious_words:
        if word in url.lower():
            return "Suspicious URL"

    return "Safe URL"