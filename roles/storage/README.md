Role Name
=========

Setup of my Solaris Zpool Storage.

Requirements
------------

The data zpool and it's keyfile.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: storage
      roles:
        - { role: storage, when: ansible_distribution == "Solaris" }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
