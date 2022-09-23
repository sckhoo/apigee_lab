testing

23 sept 2022

sckhoos-MacBook-Pro:apigee_lab khoosweechuan$ ssh -T git@github.com
The authenticity of host 'github.com (20.205.243.166)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi sckhoo! You've successfully authenticated, but GitHub does not provide shell access.

sckhoos-MacBook-Pro:apigee_lab khoosweechuan$ git remote set-url origin git@github.com:sckhoo/apigee_lab.git

sckhoos-MacBook-Pro:apigee_lab khoosweechuan$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 245 bytes | 245.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:sckhoo/apigee_lab.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.

sckhoos-MacBook-Pro:apigee_lab khoosweechuan$
