lst = str(input())
with open(lst, "r") as file:
        #file.readline("test.txt")
        print(file.readline(lst), end="")