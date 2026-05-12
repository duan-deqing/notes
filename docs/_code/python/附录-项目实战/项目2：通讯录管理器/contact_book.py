import os
import json

FILENAME = 'contacts.json'

# 加载
def load_contacts():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("通讯录文件损坏，将重建。")
    return {}

# 保存
def save_contacts(contacts):
    with open(FILENAME, 'w', encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

# 添加
def add_contact(contacts):
    name = input("姓名: ").strip()
    if not name:
        print("姓名不能为空")
        return
    phone = input("电话: ").strip()
    email = input("邮箱: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"已添加联系人: {name}")

# 查找
def find_contact(contacts):
    name = input("要查找的姓名: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"姓名: {name}, 电话: {info['phone']}, 邮箱: {info['email']}")
    else:
        print(f"未找到联系人: {name}")
# 删除
def delete_contact(contacts):
    name = input("要删除的姓名: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"已删除联系人: {name}")
    else:
        print(f"未找到联系人: {name}")
# 显示
def show_all(contacts):
    if not contacts:
        print("通讯录为空")
        return
    print("\n所有联系人:")
    for name, info in contacts.items():
        print(f"  {name}: 电话 {info['phone']}, 邮箱 {info['email']}")

# main
def main():
    contacts = load_contacts()
    while True:
        print("\n===Contacts====")
        print("1. 添加联系人")
        print("2. 查找联系人")
        print("3. 删除联系人")
        print("4. 显示全部")
        print("5. 退出")
        choice = input("请选择（1-5）:").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            find_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            show_all(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("已保存！")
            break
        else:
            print("无效选择，请重新输入！")
        
if __name__ == "__main__":
    main()