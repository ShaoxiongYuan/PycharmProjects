import random

count = 0
for i in range(3):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = int(input(f"{num1}+{num2}=?"))
    # if result == num1 + num2:
    #     count += 10
    # else:
    #     count -= 5
    count += 10 if result == num1 + num2 else -5
    """
    到0不往下扣分
    """
    # if count < 0:
    #     count = 0
if count > 0:
    print(f"恭喜你得了{count}分！")
else:
    print("继续努力...")
