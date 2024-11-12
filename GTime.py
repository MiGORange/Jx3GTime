from datetime import datetime
import pytz
from colorama import Fore, Style, init

# 初始化 colorama
init(autoreset=True)


def get_current_time():
    # 获取当前时间并设置时区为'Asia/Shanghai' (东八区)
    shanghai_tz = pytz.timezone("Asia/Shanghai")
    current_time = datetime.now(shanghai_tz).strftime("%H:%M:%S")
    return current_time


def get_direction_string(current_time):
    hour = int(current_time.split(":")[0])  # 获取当前小时
    # 时间段数组
    time_segments = [
        {"hour": 1, "value": "东-9,南-0,西-1,"},
        {"hour": 5, "value": "南-0,西-1,北-4,"},
        {"hour": 11, "value": "东-9,西-1,北-4,"},
        {"hour": 17, "value": "东-9,南-0,北-4,"},
        {"hour": 23, "value": "东-9,南-0,西-1,"},
    ]

    # 查找匹配的时间段字符串
    segment_value = ""
    for segment in reversed(time_segments):
        if hour >= segment["hour"]:
            segment_value = segment["value"]
            break

    # D列和E列的时间-方向数据
    time_to_direction = {
        "00:00:00": "北-9",
        "00:15:00": "北-0",
        "00:30:00": "北-1",
        "00:45:00": "北-2",
        "01:00:00": "北-3",
        "01:15:00": "北-4",
        "01:30:00": "北-4",
        "01:45:00": "北-4",
        "02:00:00": "北-4",
        "02:15:00": "北-4",
        "02:30:00": "北-4",
        "02:45:00": "北-4",
        "03:00:00": "北-3",
        "03:15:00": "北-2",
        "03:30:00": "北-1",
        "03:45:00": "北-0",
        "04:00:00": "北-9",
        "04:15:00": "北-8",
        "04:30:00": "北-7",
        "04:45:00": "北-6",
        "05:00:00": "东-0",
        "05:15:00": "东-1",
        "05:30:00": "东-2",
        "05:45:00": "东-3",
        "06:00:00": "东-4",
        "06:15:00": "东-5",
        "06:30:00": "东-6",
        "06:45:00": "东-7",
        "07:00:00": "东-8",
        "07:15:00": "东-9",
        "07:30:00": "东-9",
        "07:45:00": "东-9",
        "08:00:00": "东-9",
        "08:15:00": "东-9",
        "08:30:00": "东-9",
        "08:45:00": "东-9",
        "09:00:00": "东-8",
        "09:15:00": "东-7",
        "09:30:00": "东-6",
        "09:45:00": "东-5",
        "10:00:00": "东-4",
        "10:15:00": "东-3",
        "10:30:00": "东-2",
        "10:45:00": "东-1",
        "11:00:00": "南-1",
        "11:15:00": "南-2",
        "11:30:00": "南-3",
        "11:45:00": "南-4",
        "12:00:00": "南-5",
        "12:15:00": "南-6",
        "12:30:00": "南-7",
        "12:45:00": "南-8",
        "13:00:00": "南-0",
        "13:15:00": "南-0",
        "13:30:00": "南-0",
        "13:45:00": "南-0",
        "14:00:00": "南-0",
        "14:15:00": "南-0",
        "14:30:00": "南-0",
        "14:45:00": "南-0",
        "15:00:00": "南-9",
        "15:15:00": "南-8",
        "15:30:00": "南-7",
        "15:45:00": "南-6",
        "16:00:00": "南-5",
        "16:15:00": "南-4",
        "16:30:00": "南-3",
        "16:45:00": "南-2",
        "17:00:00": "西-2",
        "17:15:00": "西-3",
        "17:30:00": "西-4",
        "17:45:00": "西-5",
        "18:00:00": "西-6",
        "18:15:00": "西-7",
        "18:30:00": "西-8",
        "18:45:00": "西-9",
        "19:00:00": "西-1",
        "19:15:00": "西-1",
        "19:30:00": "西-1",
        "19:45:00": "西-1",
        "20:00:00": "西-1",
        "20:15:00": "西-1",
        "20:30:00": "西-1",
        "20:45:00": "西-1",
        "21:00:00": "西-0",
        "21:15:00": "西-9",
        "21:30:00": "西-8",
        "21:45:00": "西-7",
        "22:00:00": "西-6",
        "22:15:00": "西-5",
        "22:30:00": "西-4",
        "22:45:00": "西-3",
        "23:00:00": "北-5",
        "23:15:00": "北-6",
        "23:30:00": "北-7",
        "23:45:00": "北-8",
    }

    # 按时间顺序查找 direction
    direction_keys = sorted(time_to_direction.keys())
    direction = ""
    for key in direction_keys:
        if current_time >= key:
            direction = time_to_direction[key]
        else:
            break
    return f"{segment_value}{direction}"


def confirm_time():
    current_time = get_current_time()
    step = [00, 15, 30, 45]
    hour = current_time.split(":")[0]
    minute = int(current_time.split(":")[1])
    notice = ""
    for i in step:
        if minute < i and i - minute == 1:
            notice = f"，距离下一时间段({hour}:{i}:00)已不足一分钟"
            break
    print("----------------------")
    print(Fore.YELLOW + f"当前时间(UTC/GMT+08:00)为：{current_time}{notice}")
    print(Fore.YELLOW + Style.DIM + "按 Enter 键确认，按其他键手动输入当前时间")

    user_input = input()
    if user_input == "":
        print(Fore.GREEN + f"已确认时间:{current_time}")
        return current_time
    else:
        # 检查输入时间格式
        try:
            # 尝试将用户输入的时间转换为小时:分钟:秒格式
            datetime.strptime(user_input, "%H:%M:%S")
            print(Fore.GREEN + f"你输入的时间是：{user_input}")
            return user_input
        except ValueError:
            print(Fore.RED + "格式错误，请按照类似01:02:59的格式书写")
            return confirm_time()


# 主逻辑
while True:
    current_time = confirm_time()
    direction = get_direction_string(current_time)
    print(" -------------------")
    print("|" + Fore.CYAN + Style.BRIGHT + direction + Style.RESET_ALL + "|")
    print(" -------------------")

    step = [00, 15, 30, 45]
    hour = current_time.split(":")[0]
    minute = int(current_time.split(":")[1])
    for i in step:
        if minute < i and i - minute == 1:
            notice = f"{hour}:{i}:00后："
            direction = get_direction_string(f"{hour}:{i}:00")
            print(Fore.CYAN + Style.DIM + f"({notice}{direction})")
            break
    print(Fore.YELLOW + Style.DIM + "按Enter重新获取当前时间")
    input()  # 等待用户按 Enter 键继续
