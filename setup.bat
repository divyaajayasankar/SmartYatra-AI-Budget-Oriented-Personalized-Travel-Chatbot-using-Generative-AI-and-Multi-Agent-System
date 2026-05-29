@echo off
REM Create models directory
if not exist "d:\travel_chatbot_project\backend\models" (
    mkdir "d:\travel_chatbot_project\backend\models"
    echo Directory created successfully
) else (
    echo Directory already exists
)

REM Run the Python setup script
cd /d d:\travel_chatbot_project
python quick_setup.py

pause
