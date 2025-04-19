def get_num_words(text):
    words = text.split()
    num_of_words = len(words)
    return num_of_words

def get_num_chars(text):
    text = text.lower()
    char_records = {}

    for char in text:
        if char in char_records:
            char_records[char] += 1
        else:
            char_records[char] = 1
    return char_records

def sort_dict(d):
    sorted_chars = []

    for char, count in d.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "count": count})
    
    sorted_chars.sort(key=lambda item: item["count"], reverse=True)
    return sorted_chars