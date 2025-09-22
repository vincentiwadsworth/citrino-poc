@echo off
echo ========================================
echo INICIANDO DEMO CITRINO PARA REUNION
echo ========================================
echo.

cd /d "C:\Users\nicol\OneDrive\Documentos\trabajo\citrino\citrino"

echo 1. Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no encontrado
    pause
    exit /b 1
)

echo.
echo 2. Verificando API en puerto 5000...
timeout /t 2 /nobreak > nul

echo 3. Iniciando servidor API (en segundo plano)...
start /B python api/server.py
timeout /t 5 /nobreak > nul

echo.
echo 4. Iniciando demo de Streamlit...
echo    Espere a que aparezca la URL...
echo.

python -m streamlit run demo_stable.py --server.headless true --server.port 8501

echo.
echo Demo finalizada.
pause