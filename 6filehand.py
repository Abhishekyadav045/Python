# with open (r"C:\Users\ay407\OneDrive\Desktop\Hello Everyone.txt", "r" )as file1:
    # content=file1.read()
    # print(content)

    # content=file1.readline()
    # print(content)

    # content=file1.readlines()
    # print(content)

    # for line in file1:
    #     print(line.strip())

    # count=file1.readlines()
    # print(len(count))

    # count=0
    # for line in file1:
    #     count+=1
    # print(count)

    
with open (r"C:\Users\ay407\OneDrive\Desktop\Hello Everyone.txt", "w" )as file1:
    file1.write("Himesh,21,Banglore,\n")
    file1.write("Ankita,24,Lucknow,\n")
    file1.write("Abhishek,25,Varansi,\n")
    file1.write("Abhita,12,West bengal,\n")


# with open (r"C:\Users\ay407\OneDrive\Desktop\Hello Everyone.txt", "r" )as file1:
#      print(file1.read())

# with open (r"C:\Users\ay407\OneDrive\Desktop\Hello Everyone.txt", "a" )as file1:
#     file1.write("Karan,23,pune")

# with open (r"C:\Users\ay407\OneDrive\Desktop\Hello Everyone.txt", "r+" )as file1:
#     lines=file1.readlines()
#     lines[0]=lines[0].replace("Amit","Amit Kumar")

#     file1.seek(0)
#     file1.writelines(lines)

