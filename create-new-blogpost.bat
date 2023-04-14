@echo off
set /p "path=Enter path (e.g.: blogs/3d/blender/mypost.md): "
cd anerdyplace
hugo new %path%