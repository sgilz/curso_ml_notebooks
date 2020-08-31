# this script was made to reduce the length of our dataset since its huge size
# the output file named "train_sample.csv" is the one with we are working,
# this one represents a 10% sample of significant data from the main dataset

lines_per_week = int(input("Insert lines per week: "))

in_file = open("train.csv", "r")
out_file = open("train_sample.csv", "w")

# categorizing lines per week
weeks = dict()
for line in in_file.readlines():
    key = line[0]
    if (key in weeks):
        if (len(weeks[key]) < lines_per_week):
            weeks[key].append(line)
    else:
        weeks[key] = [line]

in_file.close()

for i,j in weeks.items():
    print(i , len(j))
    for line in j:
        out_file.write(line)
del(weeks)
out_file.close()
