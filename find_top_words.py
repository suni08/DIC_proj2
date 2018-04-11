import collections

List = open("out.txt").readlines()

counter = collections.Counter()

for line in List:
    k, v = line.strip().split("\t", 2)

    counter[k] += int(v)

Most = counter.most_common(50)

words =[]
freq = []

for line in Most:
	words.append(line[0])
	freq.append(line[1])

with open('output.txt', "w") as ou:
    for i in range(len(words)):
        ou.write(words[i])
        ou.write("\t")
        ou.write(str(freq[i]))
        ou.write("\n")
