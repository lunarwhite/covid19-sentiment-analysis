# covid19-sentiment-data-analysis

![GitHub Repo stars](https://img.shields.io/github/stars/lunarwhite/covid-social-analysis?color=orange)
![GitHub watchers](https://img.shields.io/github/watchers/lunarwhite/covid-social-analysis?color=yellow)
![GitHub forks](https://img.shields.io/github/forks/lunarwhite/covid-social-analysis?color=green)
![GitHub top language](https://img.shields.io/github/languages/top/lunarwhite/covid-social-analysis)
![GitHub License](https://img.shields.io/github/license/lunarwhite/covid-social-analysis)

ML-based analysis of social media user attentiveness of COVID-19. || 基于机器学习的疫情背景下微博文本情感分析与可视化

```
├───res
│   ├───input
│   │   ├───comment # 评论数据
│   │   ├───dict # 词典
│   │   ├───hot # 热词
│   │   ├───SOPMI
│   │   ├───stage # 不同阶段微博数据
│   │   └───topic # 微博数据
│   └───output
│       ├───clustering
│       │   ├───cluster-num # 聚类数
│       │   ├───image1 # 聚类分析饼图
│       │   └───image2 # 聚类数
│       ├───comment-txt # 评论数据-txt
│       ├───emotion-dict
│       │   └───image # 情感对比图
│       ├───hot
│       ├───multi-emotion
│       │   └───image # 多维情感分析图
│       └───topic-txt # 微博数据-txt
└───src
    ├───01crawling # 爬取数据
    ├───02preprocessing # 预处理
    ├───03analysis #分析
    │   ├───clustering # 聚类
    │   ├───emotion-dict # 情感词典
    │   └───multi-emotion # 多维情感
    └───04visualization # 可视化
        ├───clustering
        ├───emotion-dict
        └───multi-emotion
```

## 1 Overview

- 手动爬取疫情背景下微博文本与评论，进行情感分析
- 分别尝试聚类、情感词典和多维度情感分析
- 主要工具包版本为Python 3.6.10、scikit-learn 0.24.2

## 2 Setup

- 克隆repo：`git clone https://github.com/lunarwhite/covid-social-analysis.git`
- 更新pip：`pip3 install --upgrade pip`
- 为项目创建虚拟环境：`conda create --name <env_name> python=3.6`
- 激活env：`conda activate <env_name>`
- 安装python库依赖：`pip3 install -r requirements.txt`

## 3 Workflow

- 数据获取
  - 爬取微博文本
  - 爬取微博评论
- 数据预处理
  - 数据清洗
  - 去停用词
  - jieba分词
  - textRank关键词分析
- 分析-情感词典
  - SO-PMI新词发现
  - 心态词典扩展
  - 心态值计算
- 分析-聚类
  - K-means聚类
  - DBSCAN聚类
  - 层次聚类
- 分析-多维度分析
  - 多维心态词典
  - 多维情感分析
- 可视化
  - pyecharts
  - matplotlib
