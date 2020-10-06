import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# def test_hosts_file(host):
#     f = host.file('/etc/hosts')

#     assert f.exists
#     assert f.user == 'root'
#     assert f.group == 'root'


def test_user_gogs(host):
    u = host.user("gogs")

    assert u.exists
    assert u.shell == "/usr/sbin/nologin", "Incorrect shell value"


def test_gogs_dependencies(host):
    req_packages = _determine_packages_per_distro(
        host.system_info.distribution)
    for package in req_packages:
        assert host.package(package).is_installed


def _determine_packages_per_distro(distro):
    print(f"Checking packages for {distro}")
    if distro == "ubuntu":
        return [
            "postgresql",
            "golang-go",
            "nginx",
            "git"
        ]
    raise EnvironmentError(f"Distribution {distro} not supported")

def test_gogs_is_running(host):
    gogs = host.service("gogs")
    assert gogs.is_running
    assert gogs.is_enabled

def test_port_3000_listening(host):
    assert host.socket("tcp://3000").is_listening
