from quiz_logic import quiz    

def main():
    print("<===Welcome to the Quiz===>\n")
    print("Disclaimer:\nDouble check the spelling of the answer before you enter\n")
    name=input("Enter your name player: ")
    score=0
    print(f"Score of {name} is {score}")
    score=quiz(score)
    print("Congratulations!!")
    print(f"Score of {name} is {score}")
    return 0;

if __name__ == "__main__":
    main()