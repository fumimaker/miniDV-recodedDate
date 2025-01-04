#!/bin/bash

# ディレクトリパスを設定
DIR1="/your/path1"
DIR2="/your/path2"

# 一時ファイルを作成
DIR1_LIST=$(mktemp)
DIR2_LIST=$(mktemp)

# ディレクトリ1とディレクトリ2のaviファイルリストを取得
find "$DIR1" -maxdepth 1 -name "*.avi" -exec basename {} \; | sort > "$DIR1_LIST"
find "$DIR2" -maxdepth 1 -name "*.avi" -exec basename {} \; | sort > "$DIR2_LIST"

# 比較して差分を出力
echo "=== DIR1にあってDIR2にないファイル ==="
comm -23 "$DIR1_LIST" "$DIR2_LIST"

echo "=== DIR2にあってDIR1にないファイル ==="
comm -13 "$DIR1_LIST" "$DIR2_LIST"

# 一時ファイルを削除
rm "$DIR1_LIST" "$DIR2_LIST"
