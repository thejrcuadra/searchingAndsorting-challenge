import csv

def main():
    with open("Resources\\students_complete.csv") as file:
        raw = csv.reader(file)
        data = list(raw)

    print("Original Dataset:\n")
    for print1 in data[:6]:
        print(print1)

    selSort = selectionSort(data)
    print("\nDataset Sorted (Math Score, Desc.):\n")
    for print2 in selSort[:6]:
        print(print2)

    insSort = insertionSort(data)
    print("\nDataset Sorted (Reading Score, Asc.):\n")
    for print3 in insSort[:6]:
        print(print3)

    print("\nEnter the Student ID # to find student's scores: ")
    id = int(input(" >"))
    linSearch = linearSearch(data, id)
    print(f"\nStudent ID ({id}) Scores:\n")
    if linSearch == 0:
        print("['Not found']")
    else:
        print(data[0])
        print(linSearch)

    print("\nEnter a Reading Score to find a student that got that score: \n")
    readingScore = int(input(" >"))
    binSearchIndex = binarySearch(insSort, readingScore)
    print(f"Reading Score Searched ({readingScore}):\n")
    if binSearchIndex == 0:
        print("['Record with reading score not found']")
    else:
        print(insSort[0])
        print(insSort[binSearchIndex])

    statisticsReading(data)
    statisticsMath(data)

def selectionSort(data):
    for x in range(1, len(data)):
        maxIndex = x

        for y in range(x + 1, len(data)):
            if data[y][6] > data[maxIndex][6]:
                maxIndex = y

        data[x], data[maxIndex] = data[maxIndex], data[x]

    return data

def insertionSort(data):
    for i in range(2, len(data)):
        key = data[i]
        j = i-1
        while j >= 1 and key[5] < data[j][5]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    
    return data

def linearSearch(data, id):
    for i in range(1, len(data)):
        if data[i][0] == str(id):
            return data[i]
    
    return 0

def binarySearch(data, score):
    min = 1
    max = len(data) - 1 
    mid = 0

    while min <= max:
        mid = (min + max) // 2

        if int(data[mid][5]) == score:
            return mid
        else:
            if int(data[mid][5]) < score:
                min = mid + 1
            else:
                max = mid - 1

    return 0

def statisticsReading(data):
    counter9thGrade = 0
    counter10thGrade = 0
    counter11thGrade = 0
    counter12thGrade = 0

    sum9th = 0
    sum10th = 0
    sum11th = 0
    sum12th = 0

    avg9th = 0
    avg10th = 0
    avg11th = 0
    avg12th = 0

    seventyPlus9th = 0
    seventyPlus10th = 0
    seventyPlus11th = 0
    seventyPlus12th = 0

    passingAvg9th = 0
    passingAvg10th = 0
    passingAvg11th = 0
    passingAvg12th = 0

    for x in range(1, len(data)):
        if data[x][3] == "9th":
            sum9th += int(data[x][5])
            counter9thGrade += 1
            if int(data[x][5]) >= 70:
                seventyPlus9th += 1
            
        elif data[x][3] == "10th":
            sum10th += int(data[x][5])
            counter10thGrade += 1
            if int(data[x][5]) >= 70:
                seventyPlus10th += 1

        elif data[x][3] == "11th":
            sum11th += int(data[x][5])
            counter11thGrade += 1
            if int(data[x][5]) >= 70:
                seventyPlus11th += 1

        elif data[x][3] == "12th":
            sum12th += int(data[x][5])
            counter12thGrade += 1
            if int(data[x][5]) >= 70:
                seventyPlus12th += 1

    avg9th = sum9th / counter9thGrade
    avg10th = sum10th / counter10thGrade
    avg11th = sum11th / counter11thGrade
    avg12th = sum12th / counter12thGrade

    passingAvg9th = seventyPlus9th / counter9thGrade * 100
    passingAvg10th = seventyPlus10th / counter10thGrade * 100
    passingAvg11th = seventyPlus11th / counter11thGrade * 100
    passingAvg12th = seventyPlus12th / counter12thGrade * 100

    print("\nAverage Reading Scores per Grade:\n")
    print("9th Grade:")
    print(f"\tAverage Grade: {round(avg9th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg9th, 2)}%")
    print("10th Grade:")
    print(f"\tAverage Grade: {round(avg10th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg10th, 2)}%")
    print("11th Grade:")
    print(f"\tAverage Grade: {round(avg11th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg11th, 2)}%")
    print("12th Grade:")
    print(f"\tAverage Grade: {round(avg12th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg12th, 2)}%")

def statisticsMath(data):
    counter9thGrade = 0
    counter10thGrade = 0
    counter11thGrade = 0
    counter12thGrade = 0

    sum9th = 0
    sum10th = 0
    sum11th = 0
    sum12th = 0

    avg9th = 0
    avg10th = 0
    avg11th = 0
    avg12th = 0

    seventyPlus9th = 0
    seventyPlus10th = 0
    seventyPlus11th = 0
    seventyPlus12th = 0

    passingAvg9th = 0
    passingAvg10th = 0
    passingAvg11th = 0
    passingAvg12th = 0

    for x in range(1, len(data)):
        if data[x][3] == "9th":
            sum9th += int(data[x][6])
            counter9thGrade += 1
            if int(data[x][6]) >= 70:
                seventyPlus9th += 1
            
        elif data[x][3] == "10th":
            sum10th += int(data[x][6])
            counter10thGrade += 1
            if int(data[x][6]) >= 70:
                seventyPlus10th += 1

        elif data[x][3] == "11th":
            sum11th += int(data[x][6])
            counter11thGrade += 1
            if int(data[x][6]) >= 70:
                seventyPlus11th += 1

        elif data[x][3] == "12th":
            sum12th += int(data[x][6])
            counter12thGrade += 1
            if int(data[x][6]) >= 70:
                seventyPlus12th += 1

    avg9th = sum9th / counter9thGrade
    avg10th = sum10th / counter10thGrade
    avg11th = sum11th / counter11thGrade
    avg12th = sum12th / counter12thGrade

    passingAvg9th = seventyPlus9th / counter9thGrade * 100
    passingAvg10th = seventyPlus10th / counter10thGrade * 100
    passingAvg11th = seventyPlus11th / counter11thGrade * 100
    passingAvg12th = seventyPlus12th / counter12thGrade * 100

    print("\nAverage Math Scores per Grade:\n")
    print("9th Grade:")
    print(f"\tAverage Grade: {round(avg9th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg9th, 2)}%")
    print("10th Grade:")
    print(f"\tAverage Grade: {round(avg10th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg10th, 2)}%")
    print("11th Grade:")
    print(f"\tAverage Grade: {round(avg11th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg11th, 2)}%")
    print("12th Grade:")
    print(f"\tAverage Grade: {round(avg12th, 2)}")
    print(f"\tPassing Percentage: {round(passingAvg12th, 2)}%")

if __name__ == "__main__":
    main()