# WeChat 联系人名称导出

一个针对桌面微信界面的 Python 脚本。它使用鼠标和键盘操作读取联系人列表中可复制的名称，并将名称写入当前目录的 `contacts.txt`。

## 使用

打开你的微信联系人列表，保持窗口的大小和位置不变。在终端运行：

```powershell
python -m pip install pyautogui pyperclip keyboard
python wechat_contacts.py
```

按终端提示将鼠标放到对应位置。脚本依赖窗口布局和剪贴板，微信界面改版、缩放或窗口移动后可能需要重新定位。导出文件可能包含个人信息，请在本机处理。
