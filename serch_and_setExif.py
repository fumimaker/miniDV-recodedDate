import os
import subprocess
from datetime import datetime, timedelta

def get_recorded_date(filepath):
    """MediaInfoを使用してAVIファイルのRecorded Dateを取得"""
    result = subprocess.run(["mediainfo", "--Inform=General;%Recorded_Date%", filepath],
                            capture_output=True, text=True)
    recorded_date = result.stdout.strip()
    if recorded_date:
        try:
            # JSTをUTCに変換 (9時間を減算)
            dt = datetime.strptime(recorded_date, "%Y-%m-%d %H:%M:%S.%f")  # ミリ秒対応
            dt_utc = dt - timedelta(hours=9)
            # ExifTool用フォーマットに変換
            return dt_utc.strftime("%Y:%m:%d %H:%M:%S")
        except ValueError:
            print(f"Invalid date format in {filepath}: {recorded_date}")
    return None

def write_metadata(mp4_filepath, recorded_date):
    """ExifToolを使用してMP4ファイルにメタデータを書き込む"""
    try:
        subprocess.run([
            "exiftool",
            f"-CreateDate={recorded_date}",
            f"-ModifyDate={recorded_date}",
            f"-MediaCreateDate={recorded_date}",
            f"-MediaModifyDate={recorded_date}",
            "-overwrite_original",
            mp4_filepath
        ], check=True)
        print(f"Metadata written to {mp4_filepath}")
    except subprocess.CalledProcessError as e:
        print(f"Error writing metadata to {mp4_filepath}: {e}")

def process_files_recursively(directory):
    """指定ディレクトリ以下を再帰的に探索し、AVIからMP4へのメタデータ移行を処理"""
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".avi"):
                avi_filepath = os.path.join(root, filename)
                mp4_filepath = os.path.join(root, filename.replace(".avi", ".mp4"))

                if os.path.exists(mp4_filepath):
                    recorded_date = get_recorded_date(avi_filepath)
                    if recorded_date:
                        write_metadata(mp4_filepath, recorded_date)
                    else:
                        print(f"No Recorded Date found for {avi_filepath}")
                else:
                    print(f"MP4 file not found for {avi_filepath}")


directory = "./"  # 再帰的に探索するディレクトリ
process_files_recursively(directory)
