# main.py
from manager import StudentManager

def main():
    mgr = StudentManager()
    mgr.load_from_file()
    while True:
        print("\n===== 学生管理系统 =====")
        print("1. 添加学生")
        print("2. 显示所有")
        print("3. 按成绩排序显示")
        print("4. 删除学生")
        print("5. 查找学生")
        print("6. 退出")
        choice = input("选择: ").strip()
        try:
            if choice == '1':
                sid = input("学号: ").strip()
                name = input("姓名: ").strip()
                score = float(input("成绩: "))
                mgr.add_student(sid, name, score)
                print("添加成功。")
            elif choice == '2':
                mgr.show_all()
            elif choice == '3':
                mgr.sort_by_score(reverse=True)
                print("按成绩降序：")
                mgr.show_all()
            elif choice == '4':
                sid = input("要删除的学号: ").strip()
                if mgr.remove_student(sid):
                    print("删除成功。")
                else:
                    print("未找到该学号。")
            elif choice == '5':
                sid = input("查找学号: ").strip()
                stu = mgr.find_student(sid)
                if stu:
                    print(stu)
                else:
                    print("未找到。")
            elif choice == '6':
                mgr.save_to_file()
                print("数据已保存，再见！")
                break
            else:
                print("无效选择。")
        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()