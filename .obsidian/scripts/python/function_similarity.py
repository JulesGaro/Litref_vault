def calculate_jaccard_similarity(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    similarity = intersection / union
    return similarity

def similar_name(str1, str2, threshold=0.7):
    str1 = str1.replace("′", "'")
    str1 = str1.replace(":", " -")
    if str1[-1] == ".":
        str1 = str1[:-1]
    if str2[-1] == ".":
        str2 = str2[:-1]
    str2 = str2.replace("′", "'")
    str2 = str2.replace(":", " -")
    similarity = calculate_jaccard_similarity(str1, str2)
    
    return similarity >= threshold

def same_name(str1, str2):
    str1 = str1.replace("′", "'")
    str1 = str1.replace(":", " -")
    if str1[-1] == ".":
        str1 = str1[:-1]
    if str2[-1] == ".":
        str2 = str2[:-1]
    str2 = str2.replace("′", "'")
    str2 = str2.replace(":", " -")
    
    return str1 == str2