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
Base OS: [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian Download Page")
#### Flash latest Raspbian to SD card
To use following code, this should have been installed
```bash
brew install pv jq
```
```bash
hypriot_flash_latest=$(curl -s https://api.github.com/repos/hypriot/flash/releases/latest | jq -r ".assets[0].browser_download_url")
curl -LO $hypriot_flash_latest
chmod +x flash
./flash https://downloads.raspberrypi.org/raspbian_lite_latest
rm flash
```
remount SD card and activate SSH
```bash
touch /Volumes/boot/ssh
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



# Reinvent project
https://aporcupine.com/2020/03/pi4-kubernetes-cluster/