import sys
from datetime import date, timedelta, datetime
from random import randint
import subprocess

# 动态获取指定日期的格式化日期字符串，包含本地时区
def get_date_string(n, startdate):
    d = startdate - timedelta(days=n)
    # 动态获取本地时区
    local_timezone = datetime.now().astimezone().strftime("%z")
    rtn = d.strftime(f"%a %b %d %X %Y {local_timezone}")
    return rtn

# 主程序
def main(argv):
    if len(argv) < 1 or len(argv) > 2:
        print("Error: Bad input.")
        sys.exit(1)

    # 获取输入参数
    n = int(argv[0])  # 天数
    if len(argv) == 1:
        startdate = date.today()
    if len(argv) == 2:
        startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))

    i = 0
    while i <= n:
        # 获取当前日期
        curdate = get_date_string(i, startdate)
        # 随机生成当天的提交次数
        num_commits = randint(1, 10)

        for commit in range(num_commits):
            # 生成一个文件，并添加到 git
            subprocess.call(f"echo {curdate}{randint(0, 1000000)} > realwork.txt", shell=True)
            subprocess.call("git add realwork.txt", shell=True)

            # 设置 GIT_AUTHOR_DATE 和 GIT_COMMITTER_DATE 并提交
            subprocess.call(
                f'set GIT_AUTHOR_DATE="{curdate}" && set GIT_COMMITTER_DATE="{curdate}" && git commit -m "update"',
                shell=True,
            )

        print(f"Processing Day {i}: {curdate}")  # 调试输出
        i += 1

    # 删除临时文件并推送
    subprocess.call("git rm realwork.txt", shell=True)
    subprocess.call("git commit -m 'delete'", shell=True)
    subprocess.call("git push", shell=True)

if __name__ == "__main__":
    main(sys.argv[1:])
