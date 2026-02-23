import cv2
import os

# 需要重新编码的视频
videos = [
    'B样条曲线_final.mp4',
    '圆和星型_final.mp4',
    '画笔与曲线拟合_final.mp4',
    '矩阵工具及圆角_final.mp4',
    '钢笔工具_final.mp4',
    'undoredo_final.mp4',
    '中国象棋 2026-02-21 15-24-41.mp4',
    '中国象棋 2026-02-21 15-32-47.mp4',
    '中国象棋服务器控制台 2026-02-21 15-30-45.mp4',
    '📝 LaTeX Editor.mp4'
]

def reencode_video(input_path):
    """使用H.264编码重新编码视频"""
    output_path = input_path + '.temp.mp4'
    
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"处理: {os.path.basename(input_path)}")
    print(f"  尺寸: {width}x{height}, FPS: {fps:.0f}, 帧数: {total_frames}")
    
    # 使用H.264编码 (avc1)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        # 如果avc1不支持，尝试X264
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        # 如果都不支持，使用MP4V
        print("  警告: H.264编码不支持，使用MP4V")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame)
        frame_count += 1
        
        if frame_count % 100 == 0:
            progress = (frame_count / total_frames) * 100
            print(f"  进度: {progress:.1f}%")
    
    cap.release()
    out.release()
    
    # 替换原文件
    os.remove(input_path)
    os.rename(output_path, input_path)
    
    # 检查新文件的编码
    cap = cv2.VideoCapture(input_path)
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec = chr(fourcc & 0xFF) + chr((fourcc >> 8) & 0xFF) + chr((fourcc >> 16) & 0xFF) + chr((fourcc >> 24) & 0xFF)
    cap.release()
    
    print(f"  ✓ 完成! 新编码: {codec}\n")

print("开始重新编码视频为H.264格式...\n")

for video_name in videos:
    video_path = os.path.join(r'C:\Users\mark0\web', video_name)
    
    if os.path.exists(video_path):
        try:
            reencode_video(video_path)
        except Exception as e:
            print(f"  ✗ 错误: {e}\n")
    else:
        print(f"✗ 文件不存在: {video_name}\n")

print("重新编码完成!")