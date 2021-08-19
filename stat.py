import csv
from typing import Counter

# reads the file and makes a list of the data
with open('MMM project/height_weight.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

# deletes the first row as there is name given
fileData.pop(0)

# new variable for the data as an array
newData = []

# as long is the file data, it iterates and sets the number as the first index
for i in range(len(fileData)):
    number = fileData[i][1]
    newData.append(float(number))

data = Counter(newData)

modeRange = {
    '75-85': 0,
    '85-95': 0,
    '95-105': 0,
    '105-115': 0,
    '115-125': 0,
    '125-135': 0,
    '135-145': 0,
    '145-155': 0,
    '155-165': 0,
    '165-175': 0
}

# n is the number of terms in the data
n = len(newData)
# then the new data is sorted, in ascending or descending
newData.sort()
total = 0

# as the file is read, the total increases
for x in newData:
    total += x

# then the mean is calculated
mean = total / n

# checks if the number of terms are even or odd
# accordingly calculates the median
if n % 2 == 0:
    median1 = float(newData[n // 2])
    median2 = float(newData[(n // 2) - 1])

    median = (median1 + median2) // 2
else:
    median = newData[n // 2]

for height, occurence in data.items():
    if 75 < float(height) < 85:
        modeRange['75-85'] += occurence
    
    elif 85 < float(height) < 95:
        modeRange['85-95'] += occurence
    
    elif 95 < float(height) < 105:
        modeRange['95-105'] += occurence

    elif 105 < float(height) < 115:
        modeRange['105-115'] += occurence

    elif 115 < float(height) < 125:
        modeRange['115-125'] += occurence

    elif 125 < float(height) < 135:
        modeRange['125-135'] += occurence

    elif 135 < float(height) < 145:
        modeRange['135-145'] += occurence

    elif 145 < float(height) < 155:
        modeRange['145-155'] += occurence
    
    elif 155 < float(height) < 165:
        modeRange['155-165'] += occurence

    elif 165 < float(height) < 175:
        modeRange['165-175'] += occurence

mode_Range, modeOccurence = 0, 0

for range, occurence in modeRange.items():
    if occurence < modeOccurence:
        mode_Range, modeOccurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence

mode = float((mode_Range[0] + mode_Range[1]) / 2)

print('Mean of the data is: ', mean)
print('Median of the data is: ', median)
print('Mode of the data is: ', mode)