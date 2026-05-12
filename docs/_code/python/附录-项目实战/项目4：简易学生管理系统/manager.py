# manager.py
import csv
import os
from models import Student

FILENAME = "students.csv"

class StudentManager:
    def __init__(self):
        self.students = []  # 存放 Student 对象的列表

    def load_from_file(self):
        if not os.path.exists(FILENAME):
            return
        with open(FILENAME, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:  # 简单校验
                    sid, name, score_str = row
                    try:
                        score = float(score_str)
                    except ValueError:
                        score = 0.0
                    self.students.append(Student(sid, name, score))

    def save_to_file(self):
        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for stu in self.students:
                writer.writerow([stu.student_id, stu.name, stu.score])

    def add_student(self, sid, name, score):
        # 检查学号唯一性
        if any(s.student_id == sid for s in self.students):
            raise ValueError(f"学号 {sid} 已存在")
        stu = Student(sid, name, score)
        self.students.append(stu)

    def remove_student(self, sid):
        for i, stu in enumerate(self.students):
            if stu.student_id == sid:
                del self.students[i]
                return True
        return False

    def show_all(self):
        if not self.students:
            print("（无学生数据）")
            return
        for stu in self.students:
            print(stu)

    def sort_by_score(self, reverse=False):
        self.students.sort(key=lambda s: s.score, reverse=reverse)

    def find_student(self, sid):
        for stu in self.students:
            if stu.student_id == sid:
                return stu
        return None