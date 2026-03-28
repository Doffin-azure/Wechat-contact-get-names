import pyautogui
import pyperclip
import time
import keyboard

def get_wechat_contacts():
    """从微信窗口自动获取联系人名字"""
    contacts = []

    print("请先点击第一个联系人，然后将鼠标移动到右上角名字显示区域")
    print("按Enter开始记录鼠标位置...")
    input()

    # 记录右上角名字区域的位置
    print("3秒后记录鼠标位置...")
    time.sleep(3)
    name_x, name_y = pyautogui.position()
    print(f"已记录名字区域位置: ({name_x}, {name_y})")

    print("\n现在将鼠标移动到联系人列表区域")
    print("按Enter继续...")
    input()

    print("3秒后记录联系人列表位置...")
    time.sleep(3)
    list_x, list_y = pyautogui.position()
    print(f"已记录列表位置: ({list_x}, {list_y})")

    print("\n现在将鼠标移动到下一个联系人的位置")
    print("按Enter继续...")
    input()

    print("3秒后记录下一个联系人位置...")
    time.sleep(3)
    next_x, next_y = pyautogui.position()
    offset_y = next_y - list_y
    print(f"已记录移动偏移: Y轴 {offset_y} 像素")

    print("\n开始获取联系人，按ESC键停止\n")
    time.sleep(2)

    stop_flag = {'stop': False}

    def on_esc():
        stop_flag['stop'] = True
        print("\n检测到ESC，准备停止...")

    keyboard.on_press_key('esc', lambda _: on_esc())

    try:
        while not stop_flag['stop']:
            pyautogui.click(name_x, name_y)
            time.sleep(0.1)

            # 连续点击4次选中文本
            pyautogui.click(name_x, name_y, clicks=3)
            time.sleep(0.2)

            # 复制
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.2)

            name = pyperclip.paste().strip()

            if name and name not in contacts:
                contacts.append(name)
                print(f"已获取: {name} (共{len(contacts)}个)")

            # 点击回联系人列表
            pyautogui.click(list_x, list_y)
            time.sleep(0.2)

            # 移动到下一个联系人位置
            scroll_amount= offset_y
            pyautogui.scroll(-scroll_amount)
            pyautogui.click(list_x, list_y)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n获取完成！")

    # 保存到文件
    with open('contacts.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(contacts))

    print(f"已保存{len(contacts)}个联系人到 contacts.txt")
    return contacts

if __name__ == '__main__':
    get_wechat_contacts()
