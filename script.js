// 页面加载动画
document.addEventListener('DOMContentLoaded', function() {
    // 代码查看器标签切换
    const codeViewers = document.querySelectorAll('.code-viewer');
    codeViewers.forEach(viewer => {
        const tabs = viewer.querySelectorAll('.code-tab');
        const panels = viewer.querySelectorAll('.code-panel');
        
        tabs.forEach(tab => {
            tab.addEventListener('click', function() {
                const targetId = this.getAttribute('data-target');
                
                // 切换标签状态
                tabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                
                // 切换面板
                panels.forEach(p => p.classList.remove('active'));
                const targetPanel = viewer.querySelector('#' + targetId);
                if (targetPanel) {
                    targetPanel.classList.add('active');
                }
            });
        });
    });

    

    // 为每个项目卡片添加延迟动画
    const projectSections = document.querySelectorAll('.project-section');
    
    projectSections.forEach((section, index) => {
        section.style.animationDelay = `${index * 0.1}s`;
    });

    // 时间轴点击跳转
    const timelineNodes = document.querySelectorAll('.timeline-node');
    timelineNodes.forEach(node => {
        node.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 滚动时高亮当前时间轴节点
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                timelineNodes.forEach(node => {
                    node.classList.remove('active');
                    if (node.getAttribute('data-target') === '#' + id) {
                        node.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    projectSections.forEach(section => {
        observer.observe(section);
    });

    // 视频懒加载优化
    const videos = document.querySelectorAll('video');
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const video = entry.target;
                // 预加载视频元数据
                video.load();
                videoObserver.unobserve(video);
            }
        });
    }, {
        rootMargin: '50px'
    });

    videos.forEach(video => {
        videoObserver.observe(video);
    });

    // 添加平滑滚动效果
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 卡片悬停效果增强
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });

    // 视频展示切换
    const videoTabs = document.querySelectorAll('.video-tab');
    const videoItems = document.querySelectorAll('.video-item');
    
    // 预加载所有视频 - 设置为auto以预加载更多数据
    videoItems.forEach(item => {
        const video = item.querySelector('video');
        if (video) {
            video.preload = 'auto';
            video.load();
        }
    });
    
    videoTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const targetId = this.getAttribute('data-video');
            
            // 切换标签
            videoTabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            
            // 先处理所有视频的暂停和隐藏
            videoItems.forEach(item => {
                const video = item.querySelector('video');
                if (item.id !== targetId) {
                    item.classList.remove('active');
                    if (video) {
                        video.pause();
                    }
                }
            });
            
            // 再处理目标视频的显示和播放
            const targetItem = document.getElementById(targetId);
            if (targetItem) {
                targetItem.classList.add('active');
                const video = targetItem.querySelector('video');
                if (video) {
                    video.currentTime = 0;
                    // 使用requestAnimationFrame确保DOM更新后再播放
                    requestAnimationFrame(() => {
                        const playPromise = video.play();
                        if (playPromise !== undefined) {
                            playPromise.catch(() => {
                                // 如果自动播放失败，添加canplay监听器
                                const canPlayHandler = () => {
                                    video.play().catch(() => {});
                                    video.removeEventListener('canplay', canPlayHandler);
                                };
                                video.addEventListener('canplay', canPlayHandler);
                            });
                        }
                    });
                }
            }
        });
    });
});

// 返回顶部按钮
const backToTopButton = document.getElementById('backToTop');

window.addEventListener('scroll', function() {
    if (window.pageYOffset > 300) {
        backToTopButton.classList.add('show');
    } else {
        backToTopButton.classList.remove('show');
    }
});

backToTopButton.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// 训练图表已使用静态图片，无需动态加载
