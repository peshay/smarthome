Role Name
=========

Common Tasks for my homeserver setup.

Requirements
------------

Role Variables
--------------

ssh_pubkey_ed: Must be defined. Path to local SSH ED public key.

Dependencies
------------

Example Playbook
----------------

    - hosts: storage
      become: yes
      roles:
          - common
