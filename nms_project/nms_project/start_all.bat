@echo off
setlocal enabledelayedexpansion

:: ============================================================================
:: NetMap AI - One-Click Project Launcher
:: ============================================================================

title NetMap AI - Intelligent Network Management System

:: Ensure working directory is the script location
cd /d "%~dp0"

:: Add common local tool paths to PATH as fallback if needed
if exist "C:\Users\sameeha\tools\jdk-17\bin" (
    set "PATH=C:\Users\sameeha\tools\jdk-17\bin;%PATH%"
)
if exist "C:\Users\sameeha\tools\maven\bin" (
    set "PATH=C:\Users\sameeha\tools\maven\bin;%PATH%"
)

cls
echo ================================================================================
echo             NETMAP AI - NETWORK TOPOLOGY & ROLE MAPPING SYSTEM                   
echo ================================================================================
echo.
echo [1/3] Verifying Java Environment...

where java >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Java was not found in PATH or standard directories!
    echo Please ensure Java 17 or 21 is installed.
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%v in ('java -version 2^>^&1') do (
    echo    %%v
    goto :java_ok
)
:java_ok

echo.
echo [2/3] Checking application package...
if not exist "target\netmap-ai-1.0.0.jar" (
    echo [INFO] JAR package not found. Building project with Maven...
    call mvn clean package -DskipTests
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Maven build failed.
        pause
        exit /b 1
    )
) else (
    echo [OK] Executable JAR verified: target\netmap-ai-1.0.0.jar
)

echo.
echo [3/3] Launching NetMap AI Server...
echo.
echo --------------------------------------------------------------------------------
echo   Application URL: http://localhost:8080
echo   Demo Login:
echo     Username: admin
echo     Password: admin123
echo --------------------------------------------------------------------------------
echo.
echo Opening browser in 5 seconds...
start "" cmd /c "timeout /t 5 /nobreak >nul && start http://localhost:8080"

echo Server is starting... (Press Ctrl+C to stop)
echo.
java -jar target\netmap-ai-1.0.0.jar

if %ERRORLEVEL% neq 0 (
    echo.
    echo [NOTE] Server terminated with exit code %ERRORLEVEL%.
    pause
)
