# １．获取用户输入

temp_input = input("请输入温度：")
unit = input("请输入单位（ C 或者 F）：").upper()
#　测试输入
print(f"输入值：温度={temp_input},unit={unit}")

# 2. 将温度转换成浮点数（带异常处理）

try:
    temp = float(temp_input)
except ValueError:
    print(f"错误：温度值必须是数字。")
    exit(1) # 非0退出程序，表示异常
    
 
# 3. 实现转换逻辑

if unit == "C":
    converted = temp * 9 / 5 + 32
    target_unit = "F"
elif unit == "F":
    converted = (temp - 32) * 5 / 9
    target_unit = "C"
else:
    print("错误：单位只能输入 C 或 F")
    exit(1)
    
print(f"temp:{temp}°{unit} = {converted:.1f}°{target_unit}")

