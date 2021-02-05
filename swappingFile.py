def swapFiles():
    file1 = input("Enter the file which you want to change: ")
    file2 = input("Enter the file which you want to take the text from: ")
    data_A = open(file1, "r")
    file1text = data_A.readlines()

    data_B = open(file2, "r")
    file2text = data_B.readlines()

    file1Change = open(file1, "w")
    change = file1Change.writelines(file2text)

    file2Change = open(file2, "w")
    change1 = file2Change.writelines(file1text)

    print("The original text that has been replaced is below: ")
    print(file2text)


swapFiles()