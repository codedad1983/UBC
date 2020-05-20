@echo off
pushd %~dp0
cls
title AMI Setup - IFR version 0.1
echo;
set file=%1
if not defined file (
	echo Usage: AMISetup_IFR ^<BIOS file^> && pause && exit
)

for %%i in (UEFIFind.exe UEFIExtract.exe ifrextract.exe findver.exe cecho.exe) do (
 	if not exist %%i echo !!! %%i not found !!! && pause && exit
)

set ufbl=uefifind %file% body list
set ue=uefiextract %file%

if exist _Setup rd /s /q _Setup

echo;
echo 	[AMI Setup IFR Extractor]
echo;
echo Find AMI Setup
for /f "tokens=1,2" %%a in ('%ufbl% 530079007300740065006D0020004C0061006E0067007500610067006500') do (
	set subguid=%%b
	if defined subguid (
		cecho {0B}AMI Setup in GUID %%a{#}{\n}
		cecho {0B}          SubGUID %%b{#}{\n}
		%ue% %%a -o _Setup -m body -t 18>nul
	) else (
		cecho {0B}AMI Setup in GUID %%a{#}{\n}
		%ue% %%a -o _Setup -m body -t 10>nul
))

if exist _Setup\body.bin ifrextract _Setup\body.bin _Setup\setup_extr.txt
if exist _Setup\setup_extr.txt (
	echo Find string BIOS Lock
	findver "BIOS Lock VarOffset - " 42494F53204C6F636B 45 2C 6 2 _Setup\setup_extr.txt && findver "BIOS Lock VarOffset - " 42494F53204C6F636B 45 2C 6 2 _Setup\setup_extr.txt>_Setup\BIOSLock_str.txt && echo Done!
rem	findstr /N /C:"BIOS Lock" _Setup\setup_extr.txt>_Setup\BIOSLock_str.txt && echo Done!
)
pause
exit
