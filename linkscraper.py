import re
import csv

regex = r"<a href=\"(.*?)\"[^>]*>(.*?)-(.*?) \((.*?)\)[^>]*<"

with open('links.txt', 'r') as file:
    test_str = file.read().replace('\n', '')


matches = re.finditer(regex, test_str, re.MULTILINE)


#create an array
arr = []
arr.append(["Link", "Course Code", "Course Name", "Professor"])

for matchNum, match in enumerate(matches, start=1):
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    row = []

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print ("Group {groupNum} : {group}".format(groupNum = groupNum, group = match.group(groupNum)))
        row.append(match.group(groupNum))
        #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    row[0] = row[0].replace("&amp;","&")
    arr.append(row)

with open('courses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in arr:
        writer.writerow(row)

#########################


#import re
#re.findall(regex,line) 
#    for line in open('links.txt')