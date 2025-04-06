from questions import questions,answers,options

def verify(score,answers,ans):
    for answer in answers:
        if ans.lower()==answer.lower():
            score+=1
        else:
            continue
    return score

def quiz(score):
    idx=0
    for question in questions:
        i=1
        print(f"{idx+1}. {question}")
        for option in options[idx]:
            print(f"\t{i}) {option}")
            i+=1;
        ans=input("Write your answer: ")
        score=verify(score,answers,ans)
        idx+=1
    return score