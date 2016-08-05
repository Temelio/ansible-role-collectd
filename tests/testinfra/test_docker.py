"""
Role tests
"""
import pytest

# To mark all the tests as destructive:
# pytestmark = pytest.mark.destructive

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images('infopen/ubuntu-trusty-ssh',
                                       'infopen/ubuntu-xenial-ssh-py27')

# Both
# pytestmark = [
#     pytest.mark.destructive,
#     pytest.mark.docker_images("debian:jessie", "centos:7")
# ]


def test_packages(Package):
    assert Package('collectd').is_installed


def test_service(Service):
    assert Service('collectd').is_enabled
    assert Service('collectd').is_running

def test_process(Process):
    assert len(Process.filter(user='root', comm='collectd')) == 1
