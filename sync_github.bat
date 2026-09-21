@echo off
echo =========================================================
echo   🎓 REPO KULIAH SISTEM INFORMASI - AUTO SYNC GITHUB
echo   Mahasiswa: Lukman Hakim (byomanisme) - UNPAM
echo =========================================================
echo.
git add .
set /p commit_msg="Masukkan pesan commit (tekan Enter untuk default): "
if "%commit_msg%"=="" set commit_msg="Update bahan kuliah & tugas: %date% %time%"
git commit -m "%commit_msg%"
echo.
echo Mengunggah perubahan ke GitHub...
git push origin main
echo.
echo =========================================================
echo   🎉 SINKRONISASI BERHASIL! DOKUMEN TERSIMPAN AMAN DI CLOUD
echo =========================================================
pause
