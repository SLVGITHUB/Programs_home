@echo off
chcp 1251 >nul
title Конвертер WAV в MP3

:check_ffmpeg
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo FFmpeg не найден!
    echo.
    echo Скачайте FFmpeg с https://ffmpeg.org/download.html
    echo и добавьте в PATH или положите ffmpeg.exe в папку с батником
    pause
    exit /b
)

:check_file
if "%~1"=="" (
    echo Перетащите WAV файл на этот файл!
    pause
    exit /b
)

set "input=%~1"
set "filename=%~n1"
set "output=%~dp1\%filename%.mp3"

echo.
echo ========================================
echo Файл: %filename%.wav
echo Сохраняем как: %filename%.mp3
echo Параметры: 256 kbps, 44.1кГц, стерео
echo ========================================
echo.

ffmpeg -i "%input%" -codec:a libmp3lame -b:a 256k -ar 44100 -ac 2 -vn "%output%" -y -loglevel error -stats

if %errorlevel%==0 (
    echo.
    echo [OK] Конвертация завершена!
    echo Размер файла: 
    for %%A in ("%output%") do echo %%~zA байт
) else (
    echo.
    echo [ОШИБКА] Не удалось конвертировать файл!
)

echo.
pause