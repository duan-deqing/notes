# 4. 封装成函数
def convert_temperature(temp, unit):
    if unit == 'C':
        return temp * 9 / 5 + 32, 'F'
    elif unit == 'F':
        return (temp - 32) * 5 / 9, 'C'
    else:
        raise ValueError("单位必须为 C 或 F")
    
if __name__ == "__main__":
    print("======温度转换器======")
    while True:
        cmd = input("请输入温度或 q 退出: ").strip()
        if cmd.lower() == 'q':
            break
        unit = input("单位 C/F: ").strip().upper()
        try:
            temp = float(cmd)
            new_temp, new_unit = convert_temperature(temp, unit)
            print(f"{temp:.1f}°{unit} = {new_temp:.1f}°{new_unit}")
        except ValueError as e:
            print(f"错误：{e}")