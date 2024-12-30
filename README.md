# greenhat <img src="https://github.com/4148/greenhat/blob/master/greenhat.png" alt="greenhat image" width="10%" height="10%"/>

# GreenHat: Simulating Git Commit History

**GreenHat** 是一个用于模拟 Git 提交记录的脚本工具，可以通过伪造指定天数内的提交记录来生成直观的 GitHub 提交图表（绿色格子）。支持设置从指定日期开始或结束的提交记录。

---

## 功能概述

- 模拟每天的多次提交记录。
- 支持自定义起始日期或结束日期。
- 自动生成提交历史并推送至远程仓库。
- 提交历史的时间戳包含本地时区信息。

---

## 平台限制

1. **操作系统**  
   - 支持 **Windows**（使用 `cmd` 和 `set` 设置环境变量）。
   - **Linux** 和 **MacOS** 用户需修改 `set` 命令为 `export`，脚本需做小幅调整。

2. **Git 环境**  
   - 必须安装 Git。
   - 当前目录必须是一个 Git 仓库，并且已配置远程仓库（运行 `git remote -v` 验证）。

3. **Python 版本**  
   - 支持 Python 3.6 及以上版本。

4. **权限**  
   - 必须有对 Git 仓库的写入权限。

---

## 使用方法

### 1. 准备环境
- 安装 Python 和 Git，并确保它们已添加到系统 PATH。
- 初始化或克隆一个 Git 仓库：
  ```bash
  git init
  git remote add origin <远程仓库URL>
  ```
  ```bash
 git clone <远程仓库URL>
  ```

### 2. 下载脚本
将代码保存为 `greenhat.py`。

### 3. 执行脚本
运行以下命令以生成提交记录：

#### 默认从今天开始，向前推 `n` 天生成提交记录
```bash
python greenhat.py 365
```

#### 指定起始日期，向前推 `n` 天生成提交记录
```bash
python greenhat.py 365 2024-01-01
```

#### 指定起始日期，向后推 `n` 天生成提交记录（需要修改代码逻辑）
如需向后推提交记录，请使用调整后的脚本（见上一节），运行如下命令：
```bash
python greenhat.py 100 2024-01-01
```

### 4. 查看生成的提交记录
使用以下命令查看提交日志：
```bash
git log --pretty=format:"%ad %s" --date=local
```

### 5. 推送至远程仓库
脚本默认会执行以下命令推送更改：
```bash
git push
```

---

## 注意事项

1. **时区问题**  
   脚本会动态检测本地时区并应用到提交记录中，请确保系统时区设置正确。

2. **文件冲突**  
   脚本生成的临时文件 `realwork.txt` 会被自动删除，请确保仓库中没有同名文件以避免冲突。

3. **安全性**  
   脚本通过 `subprocess` 调用系统命令，运行前请确保代码来源可靠，避免潜在安全风险。

4. **Git 仓库状态**  
   确保当前分支干净（无未提交的更改），以防止提交冲突。

---

## 示例

### 示例 1：默认从今天开始，生成 365 天的提交记录
运行：
```bash
python greenhat.py 365
```

输出（部分日志示例）：
```text
Processing Day 0: Sun Dec 31 12:00:00 2024 +0800
Processing Day 1: Sat Dec 30 12:00:00 2024 +0800
...
Processing Day 364: Tue Jan 01 12:00:00 2023 +0800
```

### 示例 2：从指定日期开始，生成 100 天的提交记录
运行：
```bash
python greenhat.py 100 2023-01-01
```

---

## 已知问题

1. **Windows 平台**  
   使用 `cmd` 的 `set` 命令设置环境变量，无法直接在 Linux 和 MacOS 上运行。

2. **提交频率随机性**  
   每天的提交次数是随机的（1 到 10 次），可根据需求修改 `randint` 的范围。

3. **多用户环境**  
   如果同一仓库有多人提交，伪造的记录可能会影响真实提交历史。

---

## 修改记录

- **版本 1.0**: 初始发布，支持随机生成提交记录。
- **版本 1.1**: 修复了 Windows 环境变量设置的问题，支持动态检测时区。

---

## 授权协议

本项目基于 GNU General Public License v3.0 (GPLv3) 发布，详情请参阅项目 LICENSE 文件。
