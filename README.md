# collectd

[![Build Status](https://travis-ci.org/Temelio/ansible-role-collectd.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-collectd)

Install collectd package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for collectd role

# Package installation management
# Instead collectd_use_ppa set to True, if ansible_distribution_release not
# referenced in collectd_ppa_managed_distributions ppa, ppa will not installed
collectd_use_ppa: True
collectd_ppa_managed_distributions:
  - 'trusty'
  - 'xenial'
collectd_ppa_key_id: '7543C08D555DC473B9270ACDAF7ECBB3476ACEB3'
collectd_ppk_key_server: 'keyserver.ubuntu.com'
collectd_ppa_source: 'ppa:collectd/collectd-5.5'

collectd_packages:
  - 'collectd=5.5.2*'
  - 'collectd-core=5.5.2*'
collectd_package_state: 'present'
collectd_cache_valid_time: 3600
collectd_update_cache: True
collectd_plugins_dependencies: "{{ _collectd_plugins_dependencies | default([]) }}"


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

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
