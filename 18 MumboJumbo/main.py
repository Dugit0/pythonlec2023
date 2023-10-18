def lang_to_alf(lang):
    alf = set()
    for word in lang:
        alf |= set(word)
    return alf

arr = []
while (s := input()):
    arr.append(s)
first_lang = arr[::2]
second_lang = arr[1::2]

vaw = {word[0] for word in arr}
first_cons = lang_to_alf(first_lang) - vaw
second_cons = lang_to_alf(second_lang) - vaw

if len(first_cons) > len(second_cons):
    print("Mumbo")
else:
    print("Jumbo")



