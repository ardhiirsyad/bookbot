def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_counts(text):
    text = text.lower()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sort_characters(counts):
    sorted_list = [
        {"char": char, "num": num}
        for char, num in counts.items()
        if char.isalpha()
    ]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
