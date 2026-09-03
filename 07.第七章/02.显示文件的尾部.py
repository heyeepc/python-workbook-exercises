# 基于 UNIX的操作系统通常还包括一个名为tail的工具。把文件名提供为命令行参数，该工具显示文件的后10行。
# 编写一个提供相同行为的Python程序。如果用户请求的文件不存在，或者省略了命令行参数，则显示适当的错误消息。
import sys
from collections import deque

try:
    # 获取命令行参数传入的文件名
    filename = sys.argv[1]

    # maxlen=10 会自动只保留最新的 10 行，旧的行会被自动丢弃
    with open(filename, 'r', encoding='utf-8') as f:
        last_lines = deque(f, maxlen=10)

    # 循环输出最后 10 行
    for line in last_lines:
        print(line, end='')

except IndexError:
    print("错误：请提供文件名。用法: python tail.py <filename>", file=sys.stderr)
except FileNotFoundError:
    print(f"错误：文件 '{sys.argv[1]}' 不存在。", file=sys.stderr)
except Exception as e:
    print(f"发生错误：{e}", file=sys.stderr)
