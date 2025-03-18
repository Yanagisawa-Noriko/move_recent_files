import os
import shutil
import datetime
import sys

current_dir = os.getcwd()
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
new_folder = os.path.join(current_dir, f"NewFiles_{timestamp}")

now = datetime.datetime.now()
files_moved = 0

# 実行中の .exe ファイルのパス（.py の場合は __file__）
exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
exe_name = os.path.basename(exe_path)

for file in os.listdir(current_dir):
    file_path = os.path.join(current_dir, file)

    if os.path.isfile(file_path) and file != exe_name:  # .exe 自身を除外
        file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if (now - file_time).total_seconds() <= 86400:
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            shutil.move(file_path, new_folder)
            files_moved += 1

if files_moved > 0:
    print(f"{files_moved} 個のファイルを {new_folder} に移動しました。")
else:
    print("24時間以内に作成されたファイルはありません。")
