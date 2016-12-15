"""
Role tests
"""
import pytest

# To mark all the tests as destructive:
# pytestmark = pytest.mark.destructive

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)

# Both
# pytestmark = [
#     pytest.mark.destructive,
#     pytest.mark.docker_images("debian:jessie", "centos:7")
# ]


def test_packages(Package):
    """
    Test packages install
    """
    assert Package('collectd').is_installed


def test_service(Service):
    """
    Test service settings
    """
    assert Service('collectd').is_enabled
    assert Service('collectd').is_running

def test_process(Process):
    """
    Test process running
    """
    assert len(Process.filter(user='root', comm='collectd')) == 1

def test_config_files(File):
    """
    Test config files exists
    """
    config_files = [
        '/etc/collectd/collectd.conf',
        '/etc/collectd/my_types.db',
        '/etc/collectd/network_server_auth.db'
    ]
    for current_file in config_files:
        File(current_file).exists
        File(current_file).is_file
        File(current_file).user == 'root'
        File(current_file).group == 'root'
        File(current_file).mode == 0o0400
