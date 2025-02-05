@echo off

cls

taskkill /F /IM calculator.exe

pyinstaller --onefile --icon=icon.ico --add-data="icon.ico;." --strip --upx-dir=upx .\calculator.pyw

start dist/calculator.exe
