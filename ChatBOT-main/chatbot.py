import nltk
from nltk.chat.util import Chat , reflections
QA = [
    [
        r"1",
        ["  COLLEGE IS IN VASAI "]

    ],
    [
        r"2",

        [
         "  THERE ARE MANY MANY COMPANIES SOME OF THEM ARE "
         "\n --TCS ,\n --WIPRO , MANY MORE  "]
    ],
    [
        r"3",
        [" MOST POPULAR SPORTS ARE  \n FOOTBALL \n CHESS  \n CARROM  \n CRICKET  \n MANY MORE "]

    ],
    [
        r"4",
        ["  YES THERE ARE STUDENT DEVELOPMENT PROGRAMS ORAGINISED BY COLLEGE "
         "IN WHICH THERE ARE THOUGHT HANDS-ON LABORATAROY PRACTICE "]
    ],
    [
        r"5",
        ["  SIMPLE AND EFFECTIVE "]
    ],
    [
        r"6",
        [" COMPUTER SCIENCE \n DATA SCIENCE \n ARTIFICIAL INTELLEGENCE \n CIVIL \n MECHANICAL " ]
    ]
]
def chat():
    print("WELCOME TO VIDYAVARDINI'S COLLEGE OF ENGINEERING")
    print("HOW CAN I HELP YOU !!!!!!")
    print("")
    print("     1 : WHERE IS THE COLLEGE LOCATED ? ")
    print("     2 : WHICH ARE THE COMPANIES PROVIDING INTERSHIP IN THE COLLEGE ? ")
    print("     3 : WHICH ARE THE SPORTS PLAYED IN COLLEGE ? ")
    print("     4 : IS THERE ANY STUDENT DEVELOPMENT PROGRAMS  ? ")
    print("     5 : HOW ARE IS COLLEGE CARRICULUM ? ")
    print("     6 : COURSES OFFERDED BY COLLEGE ? ")
    chat = Chat(QA, reflections)
    chat.converse()
if __name__ == "__main__":
    chat()
