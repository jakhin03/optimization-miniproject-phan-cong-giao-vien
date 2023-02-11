#!/usr/bin/python3

import sys
from collections import defaultdict

def input(filename):
    with open(filename) as f:
        lines = f.readlines()
        [T, N, M] = [int(x) for x in lines[0].split()]
        class_subjects = [list(map(lambda x: int(x)-1,line.replace("0","").split())) for line in lines[1:1+N]]
        teacher_subjects = [list(map(lambda x: int(x)-1,line.replace("0","").split())) for line in lines[1+N:1+N+T]]
        subject_duration = [int(d) for d in lines[T + N + 1].split()]
    return T, N, M, class_subjects, teacher_subjects, subject_duration

def schedule(T,N,M,class_subjects, teacher_subjects, subject_duration):
    schedule = defaultdict(lambda x: (0,0,0,0))
    teachers_available = [(teacher, list(map(lambda x: [x,-1],subject))) for teacher,subject in enumerate(teacher_subjects)]

    # Sử dụng thuật toán greedy để tìm ra giáo viên phù hợp nhất cho mỗi lớp-môn theo thứ tự ưu tiên của môn đã biết của giáo viên và số lớp môn đã phân cho giáo viên đó.
    # Sắp xếp lớp-môn theo số tiết học giảm dần để tránh trường hợp phân công giáo viên cho môn dài hơn mà không còn thời gian.
    classes = [(i,[(k,subject_duration[k]) for k in j]) for i,j in enumerate(class_subjects)]
    classes.sort(key = lambda c: sum([x[1] for x in c[1]]),reverse=True)

    # Xếp thời khóa biểu cho lớp-môn đầu tiên vào các ngày và tiết trống trước tiên trong tuần.
    for i,c in classes:
        print(c)
        period = 0
        for sub, duration in c:
            status = False
            for teacher,subject_available in teachers_available: 
                if ([sub,-1] in subject_available) and check(period,subject_available):
                    status = True
            if status:
                schedule.append(i,sub,period,teacher)
                #add period vao status available cua giao vien
                teachers_available[teacher][teachers_available[teacher].index([sub,-1])] = period
                period += duration
    def check():
        # Khi phân công lớp-môn tiếp theo, kiểm tra xem lớp-môn đó có thể được phân công vào các ngày và tiết trống còn lại mà không gây chồng lấp với các lớp-môn đã phân công trước đó.
        
    
    # Nếu không tìm thấy thời khóa biểu phù hợp, hãy tìm một lớp-môn đã phân công và thay đổi thời khóa biểu của nó để tạo ra thời khóa biểu trống cho lớp-môn mới.
    



def main():
    T, N, M, class_subjects, teacher_subjects, subject_duration = input("data.txt")
    schedule(T,N,M,class_subjects, teacher_subjects, subject_duration)


if __name__ == "__main__":
    main()