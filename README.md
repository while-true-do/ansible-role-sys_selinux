<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_selinux.svg)](https://github.com/while-true-do/ansible-role-sys_selinux/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_selinux.svg)](https://github.com/while-true-do/ansible-role-sys_selinux/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_selinux.svg)](https://github.com/while-true-do/ansible-role-sys_selinux/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_selinux.svg)](https://github.com/while-true-do/ansible-role-sys_selinux/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_selinux.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_selinux)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_selinux%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_selinux)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_selinux%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_selinux)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_selinux%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_selinux)

# Ansible Role: sys_selinux

An Ansible Role to install and configure SELinux.

## Motivation

[SELinux](https://github.com/SELinuxProject/) is used on many enterprise OS and
therefore mandatory for many use cases.

## Description

This role installs and configures SELinux.

-   install SELinux
-   configure policy
-   configure mode

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible SELinux Module](https://docs.ansible.com/ansible/latest/modules/selinux_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_selinux)
```
ansible-galaxy install while_true_do.sys_selinux
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_selinux)
```
git clone https://github.com/while-true-do/ansible-role-sys_selinux.git while_true_do.sys_selinux
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_selinux

wtd_sys_selinux_package:
  - policycoreutils
  - policycoreutils-python
  - selinux-policy
  - selinux-policy-targeted
  - libselinux-python
  - libselinux-utils
  - setroubleshoot-server
  - setools
  - setools-console
  - mcstrans
# State can be present|latest|absent
wtd_sys_selinux_package_state: "present"

# wtd_sys_selinux_mode can be:
# enforcing   =>  SELinux security policy is enforced
# permissive  =>  SELinux prints warnings instead of enforcing
# disabled    =>  No SELinux policy is loaded
wtd_sys_selinux_mode: "enforcing"

# wtd_sys_selinux_policy can be:
# targeted  =>  Targeted processes are protected
# minimum   =>  Modification of targeted policy. Only selected processes are protected
# mls       =>  Multi Level Security protection
wtd_sys_selinux_policy: "targeted"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_selinux
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_selinux/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_selinux/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
