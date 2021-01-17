lphavit1 =["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и",
            "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с",
            "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]

alphavit2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Enter key")
key = int(input())
print("Enter word")
word = input()
end = ""

for x in range(len(word)):
    for i in range(len(alphavit1)):
        if alphavit1[i] == word[x]:
            end += alphavit1[i + key]

for x in range(len(word)):
    for i in range(len(alphavit2)):
        if alphavit2[i] == word[x]:
            end += alphavit2[i + key]

print(end)