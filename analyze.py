import re

def analyze(text):
    characters = len(text)
    words = re.findall(r"\b[a-z']+\b", text.lower())
    word_count = len(words)
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]
    return {"characters": characters, "word_count": word_count, "top10": top10}