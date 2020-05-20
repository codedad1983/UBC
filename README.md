# UBC
UBC is an UEFI BIOS Configurator based on GRUB2 with setup_var

# Usage
This tool is based on Windows 7/10 and python 2.7, and work for AMI UEFI BIOS
```
1. Open Windows console
2. Call AMISetup_IFR.bat <motherboard-bios-file>
3. Call python main.py
4. Copy all files in '_Setup' directory to GRUB2 config directory, overwrite the file if already exists
5. Reboot your computer from GRUB2 disk in UEFI mode
```

# License
MIT License
