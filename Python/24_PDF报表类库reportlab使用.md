# reportlab

## 常用API

### Canvas

- canvas.Canvas(filename, pagesize)	
	- 生成一个pdf文件，可以指定页面大小格式，pagesize默认大小为A4
	- 返回一个canvas对象

- canvas_obj.drawString(x, y, content)
	- 将content写到指定坐标位置
	- 默认坐标原点在左下角

- canvas_obj.showPage() 
	- 用于产生分页

- canvas_obj.line(x1, y1, x2, y2)
	- 画一条(x1, y1) 到 (x2, y2) 的横线

- canvas_obj.setLineWidth(value)
	- 设置线段粗细

- canvas_obj.setFont(fontStyle, fontSize)
	- 设置字体样式和大小

