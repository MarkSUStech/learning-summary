// 解析训练数据并提取关键信息
function parseTrainingData(text) {
    const data = {
        epochs: [],
        batches: [],
        losses: [],
        avgLosses: [],
        learningRates: []
    };

    // 提取epoch信息
    const epochRegex = /Epoch (\d+)\/20/g;
    let epochMatch;
    let currentEpoch = null;
    let epochStartIndex = 0;

    // 提取batch和loss信息
    const batchRegex = /Batch (\d+)\/16000, Loss: ([\d.]+), Avg: ([\d.]+), LR: ([\d.e-]+)/g;
    let match;
    let batchIndex = 0;

    while ((match = batchRegex.exec(text)) !== null) {
        const batch = parseInt(match[1]);
        const loss = parseFloat(match[2]);
        const avgLoss = parseFloat(match[3]);
        const lr = parseFloat(match[4]);

        // 检查是否进入新的epoch
        const epochCheck = epochRegex.exec(text);
        if (epochCheck && parseInt(epochCheck[1]) !== currentEpoch) {
            currentEpoch = parseInt(epochCheck[1]);
            epochRegex.lastIndex = 0; // 重置
        }

        data.batches.push(batchIndex++);
        data.losses.push(loss);
        data.avgLosses.push(avgLoss);
        data.learningRates.push(lr);
        
        if (currentEpoch !== null) {
            data.epochs.push(currentEpoch);
        }
    }

    return data;
}

// 从文件加载数据（需要先读取文件内容）
async function loadTrainingData() {
    try {
        const response = await fetch('training_output.txt');
        const text = await response.text();
        return parseTrainingData(text);
    } catch (error) {
        console.error('加载训练数据失败:', error);
        return null;
    }
}

