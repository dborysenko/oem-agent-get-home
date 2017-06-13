OEM agent get home
=========

Role to retrieve OEM agent oracle home and owner.

Requirements
------------

Tested on OEM 12c (12.1.0.4).

Role Variables
--------------

    OEM_URL: https://oem.example.com:8090/em # URL which can be used to login to OEM.
    OEM_PASSWORD: sysman password for OEM.
    OEM_HOST: oms1.example.com # One of OEM's nodes. Ansible host should have ssh-key based access to it.
    OEM_AGENT_PORT: 3872 # agent port


Example Playbook
----------------
site.yml

    - hosts: weblogic, adminsu, singlehosts      
      roles:
        - oem-agent-get-home
        
hosts


    [adminserver]    
    
    [singlehosts]
    webserver.example.com
    
    [weblogic]
    
    [all]
    
    [all:children]
    adminserver
    singlehosts
    weblogic
    
    [all:vars]
    ansible_user=dborysenko
    ansible_become_method=su
    ansible_become_exe=dzdo
    ansible_become_flags="su -"
    
    [deleg]
    oms1.example.com
    
    [deleg:vars]
    ansible_user=oracle

License
-------

BSD

Author Information
------------------

Dmytro Borysenko borysenus@gmail.com
