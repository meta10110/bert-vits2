@echo off
chcp 65001

echo 请将音频脚本放入[input]文件夹

echo 正在切割

python ./audio-slicer.py  --input input --output output 15

echo 切割完成！请查看output文件夹！

pause
