with open("pythonwiki.txt", "r") as f:
    for line in f.read().split("\n")[::2]:
        print(line)