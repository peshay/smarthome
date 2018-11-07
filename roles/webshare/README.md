Role Name
=========

Setup to share directory via HTTP/SSL certificate from LetsEncrypt

Requirements
------------

Vault for webuser password and LetsEncrypt Account Key at /Volumes/Image/private_key.yml

Dependencies
------------

    - common

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: storage
      become: yes
      roles:
          - { role: webshare, when: ansible_distribution == "Solaris" }
