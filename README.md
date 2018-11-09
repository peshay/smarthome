# smarthome
Personal Smart Home Setup as a Code

## System Setups
### Storage
Base OS: [Solaris 11.4](https://www.oracle.com/technetwork/server-storage/solaris11/downloads/install-2245079.html "Solaris 11 Download Page")
#### Install minimal-server
Standard Installer installs large-server, to get it down to minimal server:
```bash
$ pkg list -Hv entire
pkg://solaris/entire@11.4-11.4.0.0.1.10.0:20180702T173343Z
$ pkg exact-install --be-name 11.4.0min entire@11.4-11.4.0 solaris-minimal-server
```

### Pi
Base OS: [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian Download Page")

### (upcoming) Pi Cluster
Base OS: [Hypriot OS](https://blog.hypriot.com/downloads/ "Hypriot OS Download Page")
#### Flash latest Hypriot OS to SD card
```bash
hypriot_flash_latest=$(curl -s https://api.github.com/repos/hypriot/flash/releases/latest | jq -r ".assets[0].browser_download_url")
hypriot_os_url_latest=$(curl -s https://api.github.com/repos/hypriot/image-builder-rpi/releases/latest | jq -r ".assets[0].browser_download_url")
curl -LO $hypriot_flash_latest
chmod +x flash
./flash $hypriot_os_url_latest
rm flash
```

## Standard Tasks
### Update all Systems
```bash
ansible-playbook -i inventory/inventory playbooks/site.yml -t update
```

### Renew LetsEncrypt certificate
```bash
ansible-playbook -i inventory/inventory playbooks/site.yml -t renew_cert
```

### remount encrypted filesystem
```bash
ansible-playbook -i inventory/inventory playbooks/site.yml -t remount
```
