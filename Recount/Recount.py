from collections import Counter
votes = []
while True:
    name = input()
    if name == "***":
        break
    else:
        votes.append(name)
votecount = Counter(votes)
votenum = []
for key in votecount:
    votenum.append(votecount[key])
votenum = sorted(votenum, reverse=True)
if votenum[0] == votenum[1]:
    print("Runoff!")
else:
    win = votenum[0]
    for each in votecount:
        if votecount[each] == win:
            print(each)
