import re

badword = []

def updateList():
    lists = open("list.txt","r")
    badword = []
    for words in lists:
        badword.append(words.strip().lower())
    lists.close()

def createRegex(word):
    return r''.join([rf"{char}\W*" for char in word])

def containBannedWord(sentence):
    sentence = sentence.lower()

    badwordRegex = '|'.join(createRegex(word) for word in badword)

    regex = re.compile(badwordRegex, re.IGNORECASE)
    match = regex.search(sentence)
    return match is not None

while True:
    pesan_donasi = input("Masukan pesan donasi : ")
    if containBannedWord(pesan_donasi):
        print("Pesan tidak dikirim karena mengandung kata terlarang!")
    else:
        print("Pesan berhasil dikirim!")