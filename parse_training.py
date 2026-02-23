import re
import json

def parse_training_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    data = {
        'epochs': [],
        'batches': [],
        'losses': [],
        'avgLosses': [],
        'learningRates': [],
        'epochMarkers': []
    }
    
    # 提取epoch标记
    epoch_pattern = r'Epoch (\d+)/20'
    current_epoch = None
    batch_index = 0
    
    # 提取batch和loss信息
    batch_pattern = r'Batch (\d+)/16000, Loss: ([\d.]+), Avg: ([\d.]+), LR: ([\d.e-]+)'
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # 检查epoch标记
        epoch_match = re.search(epoch_pattern, line)
        if epoch_match:
            new_epoch = int(epoch_match.group(1))
            if new_epoch != current_epoch:
                current_epoch = new_epoch
                data['epochMarkers'].append({
                    'epoch': current_epoch,
                    'batchIndex': batch_index
                })
        
        # 提取batch数据
        batch_match = re.search(batch_pattern, line)
        if batch_match:
            batch_num = int(batch_match.group(1))
            loss = float(batch_match.group(2))
            avg_loss = float(batch_match.group(3))
            lr = float(batch_match.group(4))
            
            data['batches'].append(batch_index)
            data['losses'].append(loss)
            data['avgLosses'].append(avg_loss)
            data['learningRates'].append(lr)
            data['epochs'].append(current_epoch if current_epoch else 0)
            batch_index += 1
    
    return data

if __name__ == '__main__':
    data = parse_training_data('training_output.txt')
    
    # 保存为JSON文件
    with open('training_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"解析完成！")
    print(f"总batch数: {len(data['batches'])}")
    print(f"Epoch数: {len(set(data['epochs']))}")
    print(f"数据已保存到 training_data.json")


