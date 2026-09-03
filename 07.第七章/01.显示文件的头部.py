# 基于UNIX的操作系统通常包括一个名为head的工具。把文件名提供为命令行参数，该工具显示文件的前10行。编写一个提供相同行为的Python程序。如果用户请求的文件不存在，或者省略了命令行参数，则显示适当的错误消息。

import sys

try:
    file_path = sys.argv[1]

    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 10:
                break
            print(line, end='')

except IndexError:
    print("错误：请提供文件名")
except FileNotFoundError:
    print("错误：文件不存在")
```
