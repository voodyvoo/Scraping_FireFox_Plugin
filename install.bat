@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\NativeMessagingHosts\app /d C:\praktWebExt\app.json
pause
