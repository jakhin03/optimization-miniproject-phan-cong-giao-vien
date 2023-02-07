# optimization-miniproject-topic23

## Problem:
  • Có T giáo viên 1,2,..., T cần được phân công dạy các môn học cho các lớp. Có M môn học 1, 2, ..., M
  • Có N lớp học 1, 2,..., N. Mỗi lớp học có 1 danh sách các môn học (lấy từ 1, 2, ..., M). Mỗi lớp học gắn với 1 môn được gọi là lớp-môn
  • Mỗi môn học có số tiết là d(m)
  • Mỗi giáo viên t có danh sách các môn mà giáo viên đó có thể dạy
  • Mỗi buổi học được chia thành 5 tiết
  • Cần xây dựng kế hoạch phân công giáo viên cũng như thời khóa biểu (ngày/tiết bắt đầu) cho mỗi lớp-môn thỏa mãn:
    • Các lớp-môn của cùng lớp thì không được xếp thời khóa biểu chồng lấp lên nhau
    • Các lớp-môn được phân công cho cùng giáo viên cũng không được xếp thời khóa biểu chồng lấp lên nhau
  • Mặc định 1 tuần có 5 ngày và 1 ngày có 2 buổi học
