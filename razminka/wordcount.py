def chastota(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    
    words = text.split()
    res = {}
    for w in words:
        res[w] = res.get(w, 0) + 1
    return res