import time
import pyperclip


def remove_newlines(s):
    print('#' * 100)
    print(repr(s))
    revised_s = s.replace('\r\n', ' ')
    print('^' * 100)
    print(revised_s)
    return revised_s


last_clipboard_content = pyperclip.paste()  # 获取当前剪贴板的内容

while True:
    clipboard_content = pyperclip.paste()  # 获取当前剪贴板的内容
    if clipboard_content != last_clipboard_content:  # 如果剪贴板的内容发生了变化
        new_content = remove_newlines(clipboard_content)  # 删除换行符
        pyperclip.copy(new_content)  # 将修改后的内容放回剪贴板
        last_clipboard_content = new_content  # 更新最后一次获取的剪贴板内容
    time.sleep(0.1)  # 每0.1秒检查一次剪贴板的内容
