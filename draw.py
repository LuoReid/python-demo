from PIL import Image, ImageDraw

# 创建 400x400 白色背景图像
img = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(img)

# 画直线
draw.line((50, 50, 350, 50), fill="red", width=5)

# 画矩形
draw.rectangle((50, 100, 200, 200), outline="blue", width=3)

# 画椭圆
draw.ellipse((250, 100, 350, 200), outline="green", width=3)

# 画多边形（三角形）
draw.polygon([(100, 300), (50, 350), (150, 350)], outline="purple", fill="yellow")

# 显示图像
# img.show()
img.save("./output.jpg")
