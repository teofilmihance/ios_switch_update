#switch update
It is updating c series switches to image provided


## How to configure the play?
- copy this switch_update role in /etc/ansible/roles/ folder
- load the images into a new folder /etc/ansible/roles/switch_update/files/ folder
- set the /etc/ansible/hosts file with variable below:
   - **switch names or ips** 
   - **cxxx0_file:** with bin files names uploaded in ios_images folder
   - **cxxx0_file_md5:** MD5 from cisco web portal
- update vars_files/credentials.yml with switch ssh user and password
- run the playbook
    - swupdate_playbook.yml
