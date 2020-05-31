from MyQR import myqr
myqr.run(
    words='http://www.baidu.com',    # 包含信息
    picture='taylor.jpg',            # 背景图片
    colorized=True,            # 是否有颜色，如果为False则为黑白
    save_name='code.png'    # 输出文件名
)