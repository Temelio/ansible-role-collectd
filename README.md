# collectd

[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-collectd/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-collectd)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-collectd/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-collectd)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-collectd/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-collectd/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-collectd/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-collectd/)
[![Ansible Role](https://img.shields.io/ansible/role/11378.svg)](https://galaxy.ansible.com/Temelio/collectd/)

Install collectd package.

## Requirements

This role requires Ansible 2.4, 2.5 or 2.6
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Debian Stretch
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Repositories management
collectd_use_additional_repository: "{{ _collectd_use_additional_repository }}"
collectd_repository_cache_valid_time: 3600
collectd_repository_component: "{{ _collectd_repository_component }}"
collectd_repository_update_cache: True
collectd_repositories: "{{ _collectd_repositories | default([]) }}"
collectd_repositories_keys: "{{ _collectd_repositories_keys | default([]) }}"


# Packages management
collectd_packages: "{{ _collectd_packages }}"
collectd_plugins_dependencies: "{{ _collectd_plugins_dependencies | default([]) }}"
collectd_plugins_dependencies_state: 'present'
collectd_system_dependencies: "{{ _collectd_system_dependencies | default([]) }}"


# Service management
collectd_service_name: "{{ _collectd_service_name }}"
collectd_service_enabled: True
collectd_service_state: 'started'


# Custom types
collectd_custom_types: {}
collectd_custom_types_file_path: '/etc/collectd/my_types.db'


# Nework server auth data
collectd_network_server_auth_data: {}
collectd_network_auth_file_path: '/etc/collectd/network_server_auth.db'


# Main configuration
collectd_static_hostname: 'true'
collectd_hostname: "{{ ansible_hostname }}"
collectd_fqdn_lookup: 'true'
collectd_base_dir: '/var/lib/collectd'
collectd_plugin_dir: '/usr/lib/collectd'
collectd_types_db:
  - '"/usr/share/collectd/types.db"'
  - '"{{ collectd_custom_types_file_path }}"'

collectd_auto_load_plugin: 'false'
collectd_interval: 10
collectd_timeout: 2
colectd_read_threads: 5
colectd_write_threads: 5

collectd_write_queue_limit_high: False
collectd_write_queue_limit_low: False


# Logging plugins management
collectd_logging_plugins: "{{
  collectd_logging_plugins_config | map(attribute='name') | list }}"

collectd_logging_plugins_config:
  - name: 'syslog'
    activate_entries: []
    config_entries:
      - 'LogLevel info'


# Plugins management
collectd_plugins: "{{
  collectd_plugins_config | map(attribute='name') | list }}"

collectd_plugins_with_dependencies: "{{
  collectd_plugins_dependencies.keys()
  | intersect(collectd_plugins) }}"

collectd_plugins_config: "{{
  collectd_base_plugins_config | union(collectd_extra_plugins_config) }}"

collectd_base_plugins_config:
  - name: 'df'
    config_entries:
      - 'FSType rootfs'
      - 'FSType sysfs'
      - 'FSType proc'
      - 'FSType devtmpfs'
      - 'FSType devpts'
      - 'FSType tmpfs'
      - 'FSType fusectl'
      - 'FSType cgroup'
      - 'IgnoreSelected true'
  - name: 'disk'
  - name: 'entropy'
  - name: 'interface'
  - name: 'irq'
  - name: 'load'
  - name: 'memory'
  - name: 'processes'
  - name: 'rrdtool'
    config_entries:
      - 'DataDir "/var/lib/collectd/rrd"'
  - name: 'swap'
  - name: 'users'

collectd_extra_plugins_config: []


# Logrotate configuration
collectd_log_dir_path: '/var/log/collectd'
collectd_logrotate_managed: False
collectd_logrotate_file_path: '/etc/logrotate.d/collectd'
collectd_logrotate_file_owner: 'root'
collectd_logrotate_file_group: 'root'
collectd_logrotate_file_mode: '0644'
collectd_logrotate_pattern: "{{ collectd_log_dir_path ~ '/*.log' }}"
collectd_logrotate_options:
  - 'rotate 7'
  - 'daily'
  - 'compress'
  - 'delaycompress'
  - 'missingok'
  - "create 640 root root"
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.collectd }
```

## License

MIT

## Author Information

upgrade: Lise Machetel (for Temelio Company)
Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
