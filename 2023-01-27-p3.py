# Moo Operations
# http://usaco.org/index.php?page=viewproblem&cpid=1265

# These are all possible combinations of the three letters. the value of each
# key represents the amount of "moves" needed to get to string "MOO". 100 means 
# it's impossible to move to "MOO"
combination = {
    "OOO": 1,
    "OOM": 2,
    "OMO": 100,
    "OMM": 100,
    "MOO": 0,
    "MOM": 1,
    "MMO": 100,
    "MMM": 100
}

wordCount = int(input())
words = []
for i in range(wordCount):
    s = input()
    words.append(s)


for word in words:
    # edge case
    if (len(word) < 3):
        print(-1)
        continue
    
    # for each character we keep track of how many "moves" it has to make in
    # order to move to "MOO". 
    score = [100] * len(word)
    for i in range(0, len(word) - 2):
        pre = word[i:i + 3]
        score[i] = combination[pre]
    
    # In the end we calculate a) the score of the char in that position, and 
    # b) how expensive it is to remove the prefixes and postfixes.
    answer = 100
    for i in range(len(score)):
        answer = min(answer, score[i] + len(word) - 3)
    
    if (answer == 100):
        print(-1)
    else:
        print(answer)
        
    # tbh this code is rather sloppy and could be done better (especially the 
    # 100 score part but hey it works so i'm not complaining ¯\_(ツ)_/¯) 