# Establece la ruta al archivo de script
$scriptPath = "macro.py"

# Activa poetry y ejecuta el script macro.py
Start-Process -NoNewWindow -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "poetry run python $scriptPath"

# Mantén la consola abierta para ver los prints
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")