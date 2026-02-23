import cv2
import os
import numpy as np

def interpolate_frames(frame1, frame2, num_frames=3):
    """
    使用线性插值在两帧之间生成中间帧
    """
    frames = []
    for i in range(1, num_frames + 1):
        alpha = i / (num_frames + 1)
        interpolated = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)
        frames.append(interpolated)
    return frames

def process_video(input_path, output_path, speed_factor=2.0, target_fps=60, scale_factor=1.5):
    """
    处理视频：加速、插帧、提高分辨率
    """
    cap = cv2.VideoCapture(input_path)
    
    # 获取原视频信息
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 计算新分辨率
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    
    print(f"处理: {os.path.basename(input_path)}")
    print(f"  原始: {original_width}x{original_height} @ {original_fps}fps, 总帧数: {total_frames}")
    print(f"  目标: {new_width}x{new_height} @ {target_fps}fps")
    
    # 读取所有帧并提高分辨率
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 使用高质量插值提高分辨率
        resized = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
        frames.append(resized)
    
    cap.release()
    
    if len(frames) < 2:
        print(f"  警告: 视频帧数不足，跳过处理")
        return
    
    print(f"  读取完成，共 {len(frames)} 帧")
    
    # 步骤1: 加速 - 按速度因子抽取帧
    speeded_frames = []
    step = int(speed_factor)
    for i in range(0, len(frames), step):
        speeded_frames.append(frames[i])
    
    print(f"  加速后帧数: {len(speeded_frames)}")
    
    # 步骤2: 插帧 - 在每两帧之间插入多帧
    interpolated_frames = []
    num_intermediate = 4  # 每两帧之间插入4帧，总帧数变为原来的5倍
    
    for i in range(len(speeded_frames) - 1):
        interpolated_frames.append(speeded_frames[i])
        # 生成中间帧
        intermediate = interpolate_frames(speeded_frames[i], speeded_frames[i + 1], num_intermediate)
        interpolated_frames.extend(intermediate)
    
    # 添加最后一帧
    interpolated_frames.append(speeded_frames[-1])
    
    print(f"  插帧后帧数: {len(interpolated_frames)}")
    
    # 步骤3: 写入输出视频
    # 使用H.264编码 (avc1)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, target_fps, (new_width, new_height))
    
    # 如果avc1失败，使用mp4v
    if not out.isOpened():
        print("  avc1编码失败，使用mp4v编码")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, target_fps, (new_width, new_height))
    
    if not out.isOpened():
        print(f"  错误: 无法创建视频写入器")
        return
    
    # 写入所有帧
    for i, frame in enumerate(interpolated_frames):
        out.write(frame)
        if (i + 1) % 100 == 0:
            print(f"    写入进度: {i + 1}/{len(interpolated_frames)}")
    
    out.release()
    print(f"  完成: {output_path}\n")

# 处理所有视频文件
video_files = [
    '钢笔工具.mp4',
    'B样条曲线.mp4',
    '画笔与曲线拟合.mp4',
    '圆和星型.mp4',
    '矩阵工具及圆角.mp4',
    'undoredo.mp4'
]

print("开始处理视频（加速 + 插帧 + 提高分辨率）...\n")

for video_file in video_files:
    input_path = os.path.join('C:\\Users\\mark0\\web', video_file)
    
    # 创建输出文件名
    name, ext = os.path.splitext(video_file)
    output_file = f"{name}_final{ext}"
    output_path = os.path.join('C:\\Users\\mark0\\web', output_file)
    
    if os.path.exists(input_path):
        try:
            process_video(
                input_path, 
                output_path, 
                speed_factor=2,      # 2倍速
                target_fps=60,       # 60fps输出
                scale_factor=1.5     # 1.5倍分辨率
            )
        except Exception as e:
            print(f"  错误: {e}\n")
    else:
        print(f"跳过: {video_file} (文件不存在)\n")

print("所有视频处理完成!")
