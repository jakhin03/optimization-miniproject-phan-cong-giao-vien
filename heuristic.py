"""
• Có T giáo viên 1,2,..., T cần được phân công dạy các môn học cho các lớp. Có M môn học 1, 2, ..., M
• Có N lớp học 1, 2,..., N. Mỗi lớp học có 1 danh sách các môn học (lấy từ 1, 2, ..., M). Mỗi lớp học gắn với 1 môn được gọi là lớp-môn
• Mỗi môn học có số tiết là d(m)
• Mỗi giáo viên t có danh sách các môn mà giáo viên đó có thể dạy
• Mỗi buổi học được chia thành 5 tiết
• Cần xây dựng kế hoạch phân công giáo viên cũng như thời khóa biểu (ngày/tiết bắt đầu) cho mỗi lớp-môn thỏa mãn:
    • Các lớp-môn của cùng lớp thì không được xếp thời khóa biểu chồng lấp lên nhau
    • Các lớp-môn được phân công cho cùng giáo viên cũng không được xếp thời khóa biểu chồng lấp lên nhau
• Mặc định 1 tuần có 5 ngày và 1 ngày có 2 buổi học


• Input:
    • Dòng 1: T (số giáo viên), N (số lớp), M (số môn)
    • Dòng i+1 (i= 1,..., N): ghi danh sách các môn mà lớp i cần phải học (kết thúc bởi 0)
    • Dòng thứ t + N + 1 (t = 1,2,.., T): ghi danh sách các môn mà giáo viên t có thể dạy (kết thúc bởi 0)
    • Dòng thứ N + T + 2: ghi d(m) là số tiết của môn m (m = 1,..., M)
"""
"""
• Notation:
    • G(c) is the set of subjects that teacher c has
    • Z/Sub_Cla is dictionary containing (subject - class)
   
• Variables:
    • X(m,g,t) = 1 if subject m ∈ Z is taught by teacher g ∈ {1,2,...,T} at shift t ∈ {1,2,...,50} else 0
• Constraints:
    • (for each g ∈ t (for each t ∈ 50)) Sum(X(m,g,t)) = {0,1} for m ∈ Z


    • (for each m ∈ Z (for each t ∈ 50)) Sum(X(m,g,t)) = {0,1} for g ∈ T
   
    • Sum(X(m,g,t)) = d(m) for m ∈ Z, g ∈ {1,2,...,T}, t ∈ {1,2,...,50}
"""


import sys
def new_input():
T,N,M = map(int, input().split())
	for _ in range(T):
		
def input(filename):
    with open(filename) as f:
        lines = f.readlines()
        [T, N, M] = [int(x) for x in lines[0].split()]
        for _ in range(N):
            class_subjects = [int(x) for x in lines[_ + 1].split()][0:-2]
        for _ in range(T):
            teacher_subjects = [int(x) for x in lines[_ + N + 1].split()][0:-2]
        subject_duration = [int(x) for x in lines[T + N + 1].split()]
    return T, N, M, class_subjects, teacher_subjects, subject_duration
T, N, M, class_subjects, teacher_subjects, subject_duration = input("data.txt")
print(T, N, M, class_subjects, teacher_subjects, subject_duration)


from collections import defaultdict


def schedule(T,N,M,class_subjects, teacher_subjects, subject_duration):
	
	schedule = defaultdict(lambda: (0,0,0,0))
	available = [[False] for i in range(


classes = [i, sub for i, sub in enumerate(class_subjects)]
	classes.sort(key = lambda x:x[1], reverse = True)


	teachers = [i, t for i,t in enumerate(teachers)]


	subject = [i, d for i,d in enumerate(duration)]
	
	for i,sub in subjects:
		for j,class in classes:
			for k,teacher  in teachers:
				if (sub in teacher) and (available[i][k])