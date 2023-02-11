"""
• Có T giáo viên 1,2,..., T cần được phân công dạy các môn học cho các lớp. Có M môn học 1, 2, ..., M
• Có N lớp học 1, 2,..., N. Mỗi lớp học có 1 danh sách các môn học (lấy từ 1, 2, ..., M). Mỗi lớp học gắn với 1 môn được gọi là lớp-môn
• Mỗi môn học có số tiết là d(m)
• Mỗi giáo viên t có danh sách các môn mà giáo viên đó có thể dạy
• Mỗi buổi học được chia thành 5 tiết
• Cần xây dựng kế hoạch phân công giáo viên cũng như thời khóa biểu (ngày/tiết bắt đầu) cho mỗi lớp-môn thỏa mãn:
    • Các lớp-môn của cùng lớp thì không được xếp thời khóa biểu chồng lấp lên nhau
    • Các lớp-môn được phân công cho cùng giáo viên cũng không được xếp thời khóa biểu chồng lấp lên nhau


• Input:
    • Dòng 1: T (số giáo viên), N (số lớp), M (số môn)
    • Dòng i+1 (i= 1,..., N): ghi danh sách các môn mà lớp i cần phải học (kết thúc bởi 0)
    • Dòng thứ t + N + 1 (t = 1,2,.., T): ghi danh sách các môn mà giáo viên t có thể dạy (kết thúc bởi 0)
    • Dòng thứ N + T + 2: ghi d(m) là số tiết của môn m (m = 1,..., M)
"""

import sys

def input_(filename):
    with open(filename) as f:
        lines = f.readlines()
        [T, N, M] = [int(x) for x in lines[0].split()]
        class_subjects = [list(map(lambda x: int(x)-1,line.replace("0","").split())) for line in lines[1:1+N]]
        teacher_subjects = [list(map(lambda x: int(x)-1,line.replace("0","").split())) for line in lines[1+N:1+N+T]]
        subject_duration = [int(d) for d in lines[T + N + 1].split()]
    return T, N, M, class_subjects, teacher_subjects, subject_duration

def find_index(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list))
    return False

def schedule(T,N,M,class_subjects, teacher_subjects, subject_duration):
    def can_teach(teacher, course):
        return course in teachers[teacher]

    schedule = []
    teachers_available = [[teacher, list(map(lambda x: [x,0],subject))] for teacher,subject in enumerate(teacher_subjects)]

    # Sử dụng thuật toán greedy để tìm ra giáo viên phù hợp nhất cho mỗi lớp-môn theo thứ tự ưu tiên của môn đã biết của giáo viên và số lớp môn đã phân cho giáo viên đó.
    # Sắp xếp lớp-môn theo số tiết của một môn phải học giảm dần để tránh trường hợp phân công giáo viên cho môn dài hơn mà không còn thời gian.
    classes = [(i,[(k,subject_duration[k]) for k in j]) for i,j in enumerate(class_subjects)]
    classes.sort(key = lambda c: sum([x[1] for x in c[1]]),reverse=True)

    teacher_done = None
    subject_index_done = None
    subject_index = None

    # Xếp thời khóa biểu cho lớp-môn đầu tiên vào các ngày và tiết trống trước tiên trong tuần.
    for i,c in classes:
        shift = 0
        for sub, duration in c:
            status = False
            for teacher,subject_available in teachers_available: 
                subject_index = find_index(subject_available,sub)
                if subject_index:
                    if (subject_available[subject_index][1] <= shift):# Khi phân công lớp-môn tiếp theo, kiểm tra xem lớp-môn đó có thể được phân công vào các ngày và tiết trống còn lại mà không gây chồng lấp với các lớp-môn đã phân công trước đó.
                        subject_index_done = subject_index
                        teacher_done = teacher
                        status = True
                        break
            if status:
                schedule.append((i,sub,shift,teacher_done))
                #add shift vao status available cua giao vien
                teachers_available[teacher_done][1][subject_index_done][1] += duration
                shift += duration
        

    
    # Nếu không tìm thấy thời khóa biểu phù hợp, hãy tìm một lớp-môn đã phân công và thay đổi thời khóa biểu của nó để tạo ra thời khóa biểu trống cho lớp-môn mới.
    return schedule



def main():
    T, N, M, class_subjects, teacher_subjects, subject_duration = input_("data.txt")
    time_table = schedule(T,N,M,class_subjects, teacher_subjects, subject_duration)
    for x,y,u,v in time_table:
        print(f"Class {x+1} subject {y+1} shift {u+1} teacher {v+1}")

if __name__ == "__main__":
    main()