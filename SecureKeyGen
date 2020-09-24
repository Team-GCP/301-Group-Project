#!/bin/bash
 
  read -p "Enter new username " username
  useradd -m -s /bin/bash $username
  passwd $username
 
  echo -e '$username\tALL=(ALL)\tNOPASSWD:\tALL' > /etc/sudoers.d/$username
 
  mkpasswd --method=SHA-512 > 'secret01'

  su - $username
  ssh-keygen -t rsa

        # _____________________________________
 ########|This is where the key generation ends|####### 
        #|________________Mr.B_________________|
