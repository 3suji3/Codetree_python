N = int(input())

student_score_list = [list(map(int, input().split())) for _ in range((N))]

res_scs = 0

for i in range(N):
    student_sum = student_score_list[i][0] + student_score_list[i][1] + student_score_list[i][2] + student_score_list[i][3]
    if student_sum / 4 >= 60:
        print('pass')
        res_scs += 1
    else:
        print('fail')
    
print(res_scs)
