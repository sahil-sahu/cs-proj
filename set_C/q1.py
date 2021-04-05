def replace(file, word1, word2):
    f = open(file, 'r')
    data = f.read()
    data = data.replace(word1, word2)
    f.close()
    f = open(file, 'w')
    f.write(data)
    f.close()


replace('file.txt', 'that', 'this')
