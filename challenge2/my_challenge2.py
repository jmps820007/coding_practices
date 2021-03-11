#####題目#####
# 寫一個function來印出誰的成績是第二高，
# 如果高過一個人分數都是第二高，請把人名一行一行印出來

# function的參數:
#     students : 一個二維清單，例如[['Jerry', 88], ['Justin', 84], ['Tom', 90],
#     ['Akriti', 92], ['Harsh', 90]]

# function的回傳:
#     不須回傳

# 期望的執行結果:

# 例如 有個清單是 students = [['Jerry', 88], ['Justin', 84], ['Tom', 90],
# ['Akriti', 92], ['Harsh', 90]]
# sencond_highest(students) 的執行結果要印出:
#     Tom
#     Harsh
#########################################################

def second_highest(students):
    #####快寫法######
    grades = [s[1] for s in students] # 只把成績拿出來
    #####普通寫法#####
    # grades = []
    # for s in students:
    #     grades.append(s[1])
    # print(grades)
    grades = sorted(grades, reverse=True) # 將分數由高到低排列
    second = grades[1]
    # print(second)

    #####快寫法#####
    second_high_students = [s[0] for s in students if s[1] == second]
    #####普通寫法#####
    # second_high_students = []
    # for s in students:
    #     if s[1] == second:
    #         second_high_students.append(s[0])
    # print(second_high_students)
    for student in second_high_students:
        print(student)


students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] 
second_highest(students)


