"""
需求场景:电脑文件夹杂乱无章
解决方案：一键整理,很适用小白练手
"""
import os
import shutil

formats = {
    "音频": [".mp3", ".wav"],
    "视频": [".mp4", ".avi", ".mov"],
    "图片": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".jfif"],
    "文档": [".txt", ".pdf", ".doc", ".docx", ".md"],
    "程序": [".exe", ".msi"],
    "压缩": [".zip", ".rar"],
    "linux压缩": [".gz", ".deb", ".sh", ".whl", ".AppImage"],
    "浏览器扩展": [".crx", ".xpi"]
}

os.chdir('./items')

for f in os.listdir():
    ext = os.path.splitext(f)[-1]

    for d, exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(f, "{0}/{1}".format(d, f))

print("整理完成")
