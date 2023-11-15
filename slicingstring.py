
def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '",phrase,"'", sep = "")
    character = int(input("Character to start with?[Enter number]"))
    character2 = int(input("Character to end with?[Enter number]"))+1
    print ("Your substring is '",phrase[character:character2],"'", sep="")
                          

main()
