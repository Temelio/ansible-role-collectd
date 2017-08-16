"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('collectd'),
    ('collectd-core'),
])
def test_packages(host, name):
    """
    Test installed packages
    """

    assert host.package(name).is_installed


def test_service(host):
    """
    Test service settings
    """

    assert host.service('collectd').is_enabled
    if host.system_info.codename in ['jessie', 'trusty']:
        assert 'is running' in host.check_output('service collectd status')
    else:
        assert host.service('collectd').is_running


def test_process(host):
    """
    Test process running
    """

    assert len(host.process.filter(user='root', comm='collectd')) == 1


@pytest.mark.parametrize('path', [
    ('/etc/collectd/collectd.conf'),
    ('/etc/collectd/my_types.db'),
    ('/etc/collectd/network_server_auth.db'),
])
def test_config_files(host, path):
    """
    Test config files exists
    """

    current_file = host.file(path)
    current_file.exists
    current_file.is_file
    current_file.user == 'root'
    current_file.group == 'root'
    current_file.mode == 0o0400
