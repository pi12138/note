# 1. face_recognition包
    - 模块内容
        - face_recognition.api.batch_face_locations（images，number_of_times_to_upsample = 1，batch_size = 128 ）
            使用cnn面部检测器返回图像中人脸边界框的二维数组如果您使用的是GPU，这可以为您提供更快的结果，因为GPU可以一次处理批量图像。如果您不使用GPU，则不需要此功能。

            参数：	
            img - 图像列表（每个都是一个numpy数组）
            number_of_times_to_upsample - 对图像进行上采样以查找面部的次数。数字越大，面部越小。
            batch_size - 每个GPU处理批次中包含多少个图像。
            返回：	
            css（顶部，右侧，底部，左侧）顺序中找到的面部位置的元组列表

        - face_recognition.api.compare_faces（known_face_encodings，face_encoding_to_check，tolerance = 0.6 ）
            将面部编码列表与候选编码进行比较，以查看它们是否匹配。

            参数：	
            known_face_encodings - 已知面部编码的列表
            face_encoding_to_check - 要与列表进行比较的单面编码
            tolerance - 面部之间的距离，将其视为匹配。越低越严格。0.6是典型的最佳性能。
            返回：	
            True / False值列表，指示哪个known_face_encodings与要检查的面部编码匹配

        - face_recognition.api.face_distance（face_encodings，face_to_compare ）
            给定面部编码列表，将它们与已知的面部编码进行比较，并获得每个比较面部的欧氏距离。距离告诉您脸部的相似程度。

            参数：	
            face_encodings: - 要比较的面部编码列表
            face_to_compare - 要与之进行比较的面部编码
            返回：	
            一个numpy ndarray，每个面的距离与'faces'数组的顺序相同

        - face_recognition.api.face_encodings（face_image，known_face_locations = None，num_jitters = 1 ）
            给定图像，返回图像中每个面的128维面部编码。

            参数：	
            face_image - 包含一个或多个面的图像
            known_face_locations - 可选 - 如果您已经知道每个面的边界框。
            num_jitters - 计算编码时重新采样面的次数。更高更准确，但更慢（即100慢100倍）
            返回：	
            128维面部编码列表（图像中每个面部一个）

        - face_recognition.api.face_landmarks（face_image，face_locations = None，model ='large' ）
            给定图像，返回图像中每个面部的面部特征位置（眼睛，鼻子等）的字典

            参数：	
            face_image - 要搜索的图像
            face_locations - 可选择提供要检查的面部位置列表。
            model - 可选 - 要使用的模型。“大”（默认）或“小”，只返回5分但更快。
            返回：	
            面部特征位置（眼睛，鼻子等）的序列表

        - face_recognition.api.face_locations（img，number_of_times_to_upsample = 1，model ='hog' ）
            返回图像中人脸边界框的数组

            参数：	
            img - 一个图像（作为一个numpy数组）
            number_of_times_to_upsample - 对图像进行上采样以查找面部的次数。数字越大，面部越小。
            model - 使用哪种人脸检测模型。“hog”不太准确，但在CPU上更快。“cnn”是一种更准确的深度学习模型，它是GPU / CUDA加速（如果可用）。默认为“hog”。
            返回：	css（顶部，右侧，底部，左侧）顺序中找到的面部位置的元组列表

        - face_recognition.api.load_image_file（file，mode ='RGB' ）
            将图像文件（.jpg，.png等）加载到numpy数组中

            参数：	
            file - 要加载的图像文件名或文件对象
            mode - 将图像转换为的格式。仅支持“RGB”（8位RGB，3个通道）和“L”（黑色和白色）。
            返回：	图像内容为numpy数组
# 2. Automatically find all the faces in an image
    - 自动找到图像中的所有面孔
    - 案例见02.py
    - GPU加速查找，案例03.py

# 3.Recognize faces in images and identify who they are
    - 在图像中识别人脸，识别他们是谁
    - 案例见04.py

# 4.Identify specific facial features in a photograph
    - 识别照片中特定的面部特征
    - 案例见05.py
# 5.应用（可怕的丑陋）数字化妆
    - 案例见06.py

# 6. face_distance
    - 对比人脸差别
    - 案例见07.py

# 7. 使用网络摄像头识别实时视频中的人脸-简单/慢版本(需要安装OpenCV)
    - 案例见08.py

# 8. 使用网络摄像头识别实时视频中的人脸 - 更快的版本（需要安装OpenCV）
    - 案例见09.py

# 9. 识别图像
    - 识别图像中的人脸并且在人脸中画框，案例见test01.py
    - 识别图像中的单个人脸并且在人脸中画框并显示姓名，案例见test02.py
    - 识别图像中的所有人脸，并且在画框中显示姓名，案例见test03.py
    - 调用摄像头，识别图像中的人脸，test04.py
    - 自动放入已知图片识别图片版test05.py
    - 自动放入已知图片识别摄像头数据test06.py
    - 人脸识别课程设计 test07.py