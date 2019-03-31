import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cmdline_txt_file(host):
    f = host.file('/boot/cmdline.txt')

    assert f.exists
    assert f.content == b'dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=6af5c44e-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait cgroup_memory=1 cgroup_enable=memory'
    assert f.user == 'root'
    assert f.group == 'root'
