# EZIE
Configuration for EZIE Devices

Please checkout the [Original Upstream Repo](https://github.com/sushantr5/EZIE) for more info.

# What's different in this Fork ?

## ADDED

1. Show both ON and OFF state indicators in Dim mode.

# Instructions

- Download [this file](https://github.com/nfragment/EZIE/blob/main/autoconf/esp32/4_gang_switch.autoconf)
- Open Tasmota Web-UI of your EZIE 4-Gang device
- Click `Consoles` > `Manage File System` > `Choose File`
- Select the file which you downloaded earlier `4_gang_switch.autoconf`
- Click `Start Upload` and wait for it to finish.
- Go back to `Main Menu` and `Restart` the device
- The new config will be applied on boot

## Customization

- If you need more customization then you can build your own autoconf file
- Start by editing the berry script file - `autoexec.be`
- Modify it to your liking
- Rebuild the `autoconf` file using `gen.py` script
- Upload this modified autoconf file to your device 
