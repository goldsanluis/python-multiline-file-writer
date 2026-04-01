def write_mylife():
    # 1. Open mylife.txt in write mode
    myFile = open("mylife.txt", "w")

    # 2. Loop forever
    while True:
        # 2.1 Ask user to enter a line
        line = input("Enter line: ")
        # 2.2 Write that line to the file
        myFile.write(line + "\n")

        # 2.3 Ask if there are more lines
        more = input("Are there more lines y/n? ")
        # 2.4 If answer is 'n', stop the loop
        if more == "n":
            break

    # 3. Close the file
    myFile.close()

# 4. Call the function
write_mylife()
