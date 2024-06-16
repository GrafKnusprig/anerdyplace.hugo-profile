@echo off
if [%1]==[] goto :eof
:loop
cwebp -q 80 %1 -o %~n1.webp
shift
if not [%1]==[] goto loop