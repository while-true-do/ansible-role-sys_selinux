import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_selinux_config(host):
    file = host.file('/etc/selinux/config')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.contains('SELINUX=enforcing')
    assert file.contains('SELINUXTYPE=targeted')


@pytest.mark.parametrize("name", [
    ("policycoreutils"),
    ("selinux-policy"),
    ("selinux-policy-targeted"),
    ("setroubleshoot-server"),
    ("setools"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
