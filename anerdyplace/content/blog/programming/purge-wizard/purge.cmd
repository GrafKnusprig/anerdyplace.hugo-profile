@echo off
set /p baseFolder=< baseFolderPath.txt
echo You try to delete:
for /f "delims=" %%f in (filesToDelete.txt) do echo "%baseFolder%\%%f"
goto :choice

:choice
set /P c=Are you sure you want to continue[y/n]?
if /I "%c%" EQU "y" goto :delete
if /I "%c%" EQU "n" goto :stop

:delete
for /f "delims=" %%f in (filesToDelete.txt) do del "%baseFolder%\%%f"
echo Done.
echo Press any key to exit...
pause >nul
exit

:stop
echo You cancelled the operation.
echo Press any key to exit...
pause >nul
exit