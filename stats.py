def num_words(string):
    temp=string.split()
    num=len(temp)
    return num

def char_count(input):
    chars={}
    for char in input:
        lower=char.lower()
        if "a" <= lower <= "z":
            if lower in chars:
                chars[lower]+=1
            else:
                chars[lower]=1
    return chars

def sort_on(items):
    return items["num"]

def pairs(dict):
    result=[]
    char=""
    num=0
    for key, value in dict.items():
        temp={"char": "","num": 0}
        char = key
        num = value
        temp["char"]=char
        temp["num"]=num
        result.append(temp)
    result.sort(reverse=True, key=sort_on)
    return result
        