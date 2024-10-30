@echo off

pyinstaller --onefile --icon=icon.ico --add-data="icon.ico;." .\calculator.pyw

start dist/calculator.exe