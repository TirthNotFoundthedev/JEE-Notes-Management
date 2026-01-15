@echo off
echo Running map generator...
python generate_map.py
if %errorlevel% neq 0 (
    echo Error generating map. Exiting.
    pause
    exit /b %errorlevel%
)

echo.
echo Adding changes to git...
git add .

echo.
set /p commit_msg="Enter commit message (or press Enter for 'Update notes'): "
if "%commit_msg%"=="" set commit_msg=Update notes

echo Committing with message: "%commit_msg%"...
git commit -m "%commit_msg%"

echo.
echo Pushing to GitHub...
git push

echo.
echo Done!
pause
