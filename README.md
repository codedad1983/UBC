# UBC
UBC is an UEFI BIOS Configurator based on GRUB2 with setup_var. It works similarly to setup_var, but rather than changing variables through the GRUB command line manually, it creates GRUB menu entries based on the locations and offsets of the variables. It does this by creating GRUB config files taken from the extracted IFR of your BIOS binary, as well as a master GRUB config file. You must use a GRUB shell that has the setup_var command, but you don't necessarily have to use the one included in here. There are guides on how to manually apply the setup_var patch and compile GRUB from the source.

# Warning
Most laptop manufactures lock down their BIOSes very securely with RSA signing nowadays. This bypasses the dillema of finding a bypass to flash a modified BIOS and instead modifies the NVRAM registers instead.

USE WITH CAUTION AND ENSURE YOU HAVE EXAMINED YOU ARE ACCESSING RIGHT SETUP VARIABLE OR YOU WILL RISK BRICKING YOUR COMPUTER!!! I AM NOT RESPONSIBLE IF ANYTHING HAPPENS TO YOUR COMPUTER, INCLUDING BUT NOT LIMITED TO: SPONTANEOUS COMBUSTION, IMPLOSION, THERMONUCLEAR MELTDOWN. YOU HAVE BEEN FOREWARNED!

Okay in most cases you can recover by removing the CMOS battery or reflashing the eeprom with a programmer no matter how messed up your nvram is. BUT NO PROMISES.

I am not responsible for any losses or damages caused by the use of this program. USE AT YOUR OWN RISK.

# Usage
This tool is based on Windows 7/10 and python 2.7, and works for AMI UEFI BIOS
```
1. Open Windows console
2. Call cmd /k AMISetup_IFR.bat <motherboard-bios-file>
3. Call python2 main.py
4. Copy all files in '_Setup' directory to GRUB2 config directory, overwrite the file if already exists
5. Reboot your computer from GRUB2 disk in UEFI mode
```

# Screenshots
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_00_08.png)
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_00_53.png)
![UBC](https://github.com/qianchendi/assets/raw/master/VirtualBox_UEFI_20_05_2020_23_04_46.png)

# License
MIT License
