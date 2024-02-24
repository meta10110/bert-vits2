chcp 65001
@echo off


:input_project_name
set /p project_name=请输入在Data文件夹目录下，你的训练项目文件夹名称：

rem 构建完整的日志目录路径
set logdir=.\Data\%project_name%\models

rem 检查路径是否存在
if not exist "%logdir%" (
    echo 没有找到路径：%logdir%
    echo 请确保输入的训练项目名称与路径匹配
    goto input_project_name
)

echo 正在启动Tensorboard...
echo 请访问该网址进入Tensorboard:

.\workenv\python.exe -m tensorboard.main --logdir=%logdir%

pause
