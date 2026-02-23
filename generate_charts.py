import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置深色主题样式
plt.style.use('dark_background')

# 读取训练数据
with open('training_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"加载数据: {len(data['batches'])} 个数据点")

# 采样数据（每10个点取1个，减少图片大小）
sample_rate = 10
sampled_batches = data['batches'][::sample_rate]
sampled_losses = data['losses'][::sample_rate]
sampled_avg_losses = data['avgLosses'][::sample_rate]
sampled_lrs = data['learningRates'][::sample_rate]

# 创建图表1: Loss曲线
fig1, ax1 = plt.subplots(figsize=(12, 6), facecolor='#0f172a')
ax1.set_facecolor('#1e293b')

ax1.plot(sampled_batches, sampled_losses, label='当前Loss', color='#6366f1', linewidth=2, alpha=0.8)
ax1.plot(sampled_batches, sampled_avg_losses, label='平均Loss', color='#8b5cf6', linewidth=2, alpha=0.8)
ax1.fill_between(sampled_batches, sampled_losses, alpha=0.1, color='#6366f1')
ax1.fill_between(sampled_batches, sampled_avg_losses, alpha=0.1, color='#8b5cf6')

ax1.set_xlabel('Batch编号', color='#cbd5e1', fontsize=12)
ax1.set_ylabel('Loss值', color='#cbd5e1', fontsize=12)
ax1.set_title('训练Loss曲线', color='#f1f5f9', fontsize=16, fontweight='bold', pad=20)
ax1.legend(loc='upper right', facecolor='#1e293b', edgecolor='#334155', labelcolor='#cbd5e1')
ax1.grid(True, alpha=0.2, color='#334155')
ax1.tick_params(colors='#94a3b8')

# 设置x轴标签数量
ax1.xaxis.set_major_locator(plt.MaxNLocator(10))

plt.tight_layout()
plt.savefig('loss_chart.png', dpi=150, bbox_inches='tight', facecolor='#0f172a', edgecolor='none')
print("Loss图表已保存: loss_chart.png")
plt.close()

# 创建图表2: 学习率曲线
fig2, ax2 = plt.subplots(figsize=(12, 6), facecolor='#0f172a')
ax2.set_facecolor('#1e293b')

ax2.plot(sampled_batches, sampled_lrs, label='学习率', color='#ec4899', linewidth=2, alpha=0.8)
ax2.fill_between(sampled_batches, sampled_lrs, alpha=0.2, color='#ec4899')

ax2.set_xlabel('Batch编号', color='#cbd5e1', fontsize=12)
ax2.set_ylabel('学习率', color='#cbd5e1', fontsize=12)
ax2.set_title('学习率变化曲线', color='#f1f5f9', fontsize=16, fontweight='bold', pad=20)
ax2.legend(loc='upper right', facecolor='#1e293b', edgecolor='#334155', labelcolor='#cbd5e1')
ax2.grid(True, alpha=0.2, color='#334155')
ax2.tick_params(colors='#94a3b8')

# 设置y轴为科学计数法
ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# 设置x轴标签数量
ax2.xaxis.set_major_locator(plt.MaxNLocator(10))

plt.tight_layout()
plt.savefig('lr_chart.png', dpi=150, bbox_inches='tight', facecolor='#0f172a', edgecolor='none')
print("学习率图表已保存: lr_chart.png")
plt.close()

# 计算统计信息
initial_loss = data['losses'][0]
final_loss = data['losses'][-1]
loss_reduction = ((initial_loss - final_loss) / initial_loss * 100) if initial_loss > 0 else 0
unique_epochs = sorted(set(data['epochs']))

print(f"\n训练统计:")
print(f"  训练轮数: {len(unique_epochs)} epochs ({unique_epochs[0]}-{unique_epochs[-1]})")
print(f"  总批次数: {len(data['batches'])}")
print(f"  初始Loss: {initial_loss:.4f}")
print(f"  最终Loss: {final_loss:.4f}")
print(f"  Loss降低: {loss_reduction:.2f}%")
print("\n图表生成完成！")



