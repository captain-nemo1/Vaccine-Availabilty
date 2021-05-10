:loop
python %cd%\VaccineCountToTG.py
timeout /t 120 /nobreak
goto :loop
