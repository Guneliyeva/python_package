def samitleri_al(text):
    samitler = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    list = []
    
    text = text.split(" ")
    for word in text:
        for letter in word:
            if letter in samitler:
                if list.count(letter) == 0:
                    list.append(letter)
    return list

