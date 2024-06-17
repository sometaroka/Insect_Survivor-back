#!/bin/bash

# サンプルデータのリスト
words=("apple" "banana" "cherry" "date" "elderberry" "fig" "grape" "honeydew" "kiwi" "lemon")

# APIエンドポイントのURL
url="http://localhost:8000/api/words/"

# 単語をAPIに送信
for word in "${words[@]}"; do
  curl -X POST "$url" -d "{\"word\": \"$word\"}" -H "Content-Type: application/json"
  echo "Sent word: $word"
done

echo "All words sent!"
