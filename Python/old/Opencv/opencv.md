# 1.图像基本知识
    - 1、图像是什么：
        - 图像是客观对象的一种相似性的、生动性的描述或写真，是人类社会活动中最常用的信息载体。或者说图像是客观对象的一种表示，它包含了被描述对象的有关信息。     

    - 2、图像基本属性有哪些：
        - 通道数目、高与宽、像素数据、图像类型

# 2.基本函数
    - 读取图片：imread(filename[, flags]) -> retval
    - 打开一个win窗口：namedWindow(winname[, flags]) -> None
    - 显示图片：imshow(winname, mat) -> None
    - 保存图片：imwrite(filename, img[, params]) -> retval
    - 等待： waitKey([, delay]) -> retval
    - 关闭win窗口：destroyWindow(winname) -> None
        - 关闭所有win窗口：destroyAllWindows() -> None
    - 案例见test03.py

    - 打开摄像头：VideoCapture(0),#打开0号摄像头，捕捉该摄像头实时信息，参数0代表摄像头的编号有多个摄像头的情况下，可用编号打开摄像头。
    - 打开视频：VideoCapture(videoname),若是加载视频，则将参数改为视频路径，cv.VideoCapture加载视频是没有声音的，OpenCV只对视频的每一帧进行分析
    - 读取摄像头(视频)内容：
        - read(...) method of cv2.VideoCapture instance
          read([, image]) -> retval, image
    - 案例见test04.py
