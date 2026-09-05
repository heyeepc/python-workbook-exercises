# 基于UNIX的操作系统通常包括一个名为cat的工具，它是concatenate的缩写。把一个或多个文件名作为命令行参数提供给该工具，该工具就会显示这些文件的内容连接起来的结果。
# 文件的显示顺序与它们在命令行中显示的顺序相同。创建执行此任务的Python程序。它应该为任何不能显示的文件生成适当的错误消息，然后继续处理下一个文件。如果程序启动时没有任何命令行参数，则显示适当的错误消息。
import sys


def custom_cat():
    # 检查命令行参数：sys.argv[0] 是脚本名称，因此参数数量少于 2 说明未提供任何文件名
    if len(sys.argv) < 2:
        print("错误: 未指定任何文件。", file=sys.stderr)
        print("用法: python script.py <文件1> [文件2 ...]", file=sys.stderr)
        sys.exit(1)

    # 遍历命令行传入的所有文件名/路径
    for file_path in sys.argv[1:]:
        try:
            # 尝试打开并读取文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                print(f.read(), end="")
        except FileNotFoundError:
            print(
                f"cat: {file_path}: 没有那个文件或目录", file=sys.stderr
            )
        except IsADirectoryError:
            print(f"cat: {file_path}: 是一个目录", file=sys.stderr)
        except PermissionError:
            print(f"cat: {file_path}: 权限不够", file=sys.stderr)
        except UnicodeDecodeError:
            print(
                f"cat: {file_path}: 无法用 UTF-8 解码（可能是二进制文件）",
                file=sys.stderr,
            )
        except Exception as e:
            print(
                f"cat: {file_path}: 读取时发生未知错误 ({e})",
                file=sys.stderr,
            )


if __name__ == "__main__":
    custom_cat()
