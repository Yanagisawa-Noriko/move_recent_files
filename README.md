# move_recent_files
24時間以内に作成されたファイルを1つのフォルダにまとめる機能

# 使い方
- 使用したいディレクトリ内にファイルを配置
- pythonがインストールされていればダブルクリックで起動
- 24時間以内に作成されたファイルを1つのフォルダにまとめる

# 作成理由
- 記録のためのスクリーンショットが増えすぎるため
- まとめて一括廃棄を手軽にするため

# .exe の作り方
1. Python をインストールする（未インストールの場合）
2. コマンドプロンプトで以下を実行
```
 pip install pyinstaller
``` 
4. `.exe`を作成する方法
- `pyinstaller move_recent_files.spec`を実行
6. `dist/move_recent_files.exe` が作成される
