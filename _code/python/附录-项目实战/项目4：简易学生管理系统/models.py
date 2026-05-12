# models.py
class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"[{self.student_id}] {self.name} - {self.score}分"