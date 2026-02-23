@echo off
chcp 1251 >nul
title Конвертер MP3 в WAV

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
    echo Перетащите MP3 файл на этот файл!
    pause
    exit /b
)

set "input=%~1"
set "filename=%~n1"
set "output=%~dp1\%filename%.wav"

echo.
echo ========================================
echo Файл: %filename%.mp3
echo Сохраняем как: %filename%.wav
echo Параметры: 44.1кГц, 16 бит, моно
echo ========================================
echo.

ffmpeg -i "%input%" -acodec pcm_s16le -ac 1 -ar 44100 -vn "%output%" -y -loglevel error -stats

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