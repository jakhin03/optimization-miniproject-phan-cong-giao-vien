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
    schedule = []
    teachers_non_available = [[teacher, list(map(lambda x: [x,[]],subject))] for teacher,subject in enumerate(teacher_subjects)] #format each element: [teacher,[subject 1,[shift begin, shift end],[subject 2,[shift begin, shift end], ...]]]

    # Sử dụng thuật toán greedy để tìm ra giáo viên phù hợp nhất cho mỗi lớp-môn theo thứ tự ưu tiên của môn đã biết của giáo viên và số lớp môn đã phân cho giáo viên đó.
    # Sắp xếp lớp-môn theo số tiết của một môn phải học giảm dần để tránh trường hợp phân công giáo viên cho môn dài hơn mà không còn thời gian.
    classes = [(i,[(k,subject_duration[k]) for k in j]) for i,j in enumerate(class_subjects)] #format each element(class) [(class,[(subject 1, duration of subject 1), (subject 2, duration of subject 2), ...])]
    classes.sort(key = lambda c: sum([x[1] for x in c[1]]),reverse=True)

    teacher_done = None
    subject_index_done = None
    subject_index = None

    print(classes)
    # Xếp thời khóa biểu cho lớp-môn đầu tiên vào các ngày và tiết trống trước tiên trong tuần.
    for i,c in classes:
        shift = 0
        for sub, duration in c:
            status = False
            for teacher,subject_non_available in teachers_non_available: 
                print(sub)
                subject_index = find_index(subject_non_available,sub)
                if subject_index:
                    print(f"class {i} sub {sub} list {subject_non_available} index {subject_index} shift {shift}")
                    if (shift not in range(i,j) for i,j in subject_non_available[subject_index][1]):# Khi phân công lớp-môn tiếp theo, kiểm tra xem lớp-môn đó có thể được phân công vào các ngày và tiết trống còn lại mà không gây chồng lấp với các lớp-môn đã phân công trước đó.
                        subject_index_done = subject_index
                        teacher_done = teacher
                        status = True
                        break
            if status:
                schedule.append((i,sub,shift,teacher_done))
                teachers_non_available[teacher_done][1][subject_index_done][1].append((shift,shift+duration))
                shift += duration
        

    
    # Nếu không tìm thấy thời khóa biểu phù hợp, hãy tìm một lớp-môn đã phân công và thay đổi thời khóa biểu của nó để tạo ra thời khóa biểu trống cho lớp-môn mới.
    return schedule



def main():
    T, N, M, class_subjects, teacher_subjects, subject_duration = input_("data.txt")
    time_table = schedule(T,N,M,class_subjects, teacher_subjects, subject_duration)
    time_table.sort(key = lambda x:(x[0],x[1]))
    [print(f"Class {x+1} subject {y+1} shift {u+1} teacher {v+1}") for (x,y,u,v) in time_table]

if __name__ == "__main__":
    main()