import os
import subprocess
import re
from datetime import datetime


def get_recorded_date(filepath):
    try:
        # MediaInfoコマンドを実行して情報を取得
        result = subprocess.run(["mediainfo", filepath], capture_output=True, text=True)
        output = result.stdout

        # "Recorded date" を正規表現で抽出
        match = re.search(r"Recorded date\s+:\s+(.+)", output)
        if match:
            return match.group(1).strip()  # 日付文字列を返す
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return None


def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".avi"):  # AVIファイルを対象
            file_path = os.path.join(directory, filename)
            recorded_date = get_recorded_date(file_path)

            if recorded_date:
                try:
                    # 日時フォーマットの整形
                    parsed_date = datetime.strptime(recorded_date, "%Y-%m-%d %H:%M:%S.%f")
                    new_filename = parsed_date.strftime("%Y-%m-%d-%H%M%S") + ".avi"
                    new_file_path = os.path.join(directory, new_filename)

                    # ファイル名を変更
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                except ValueError as e:
                    print(f"Error parsing date for {filename}: {recorded_date} ({e})")
            else:
                print(f"No 'Recorded date' found for {filename}")


directory = "./"  # 対象ディレクトリのパスを指定
rename_files(directory)
