# UBC
UBC is an UEFI BIOS Configurator based on GRUB2 with setup_var

# Warning
Most laptop manufactures lock down their BIOSes very securely with RSA signing nowadays. This bypasses the dillema of finding a bypass to flash a modified BIOS and instead modifies the NVRAM registers instead.

USE WITH CAUTION AND ENSURE YOU HAVE EXAMINED YOU ARE ACCESSING RIGHT SETUP VARIABLE OR YOU WILL RISK BRICKING YOUR COMPUTER!!! I AM NOT RESPONSIBLE IF ANYTHING HAPPENS TO YOUR COMPUTER, INCLUDING BUT NOT LIMITED TO: SPONTANEOUS COMBUSTION, IMPLOSION, THERMONUCLEAR MELTDOWN. YOU HAVE BEEN FOREWARNED!

Okay in most cases you can recover by removing the CMOS battery or reflashing the eeprom with a programmer no matter how messed up your nvram is. BUT NO PROMISES.

I am not responsible for any losses or damages caused by the use of this program. USE AT YOUR OWN RISK.

# Usage
This tool is based on Windows 7/10 and python 2.7, and works for AMI UEFI BIOS
```
1. Open Windows console
2. Call AMISetup_IFR.bat <motherboard-bios-file>
3. Call python main.py
4. Copy all files in '_Setup' directory to GRUB2 config directory, overwrite the file if already exists
5. Reboot your computer from GRUB2 disk in UEFI mode
```

# Screenshots
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_00_08.png)
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_04_46.png)
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_04_46.png)

# License
MIT License
