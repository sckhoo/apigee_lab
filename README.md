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

-----------------

   98  git add .
   99  git commit -m "add git howto"
  100  git push -u origin main

To deploy to app engine
C:\Users\Swee-Chuan Khoo\Documents\apigee_lab>gcloud app deploy hello_world_fastapi\app.yaml hello_world_flask\app.yaml hello_world_nodejs\app.yaml

To deplot to cloud run
C:\Users\Swee-Chuan Khoo\Documents\apigee_lab\cloud_run\hello_world_nodejs>gcloud builds submit --tag gcr.io/{project}/sckhoo_nodejs_cloudrun_helloworld
C:\Users\Swee-Chuan Khoo\Documents\apigee_lab\cloud_run\hello_world_nodejs>gcloud run deploy --image gcr.io/{project}/sckhoo_nodejs_cloudrun_helloworld --allow-unauthenticated --region=asia-southeast1
C:\Users\Swee-Chuan Khoo\Documents\apigee_lab\cloud_run\hello_world_nodejs>gcloud run deploy sckhoohelloworld --image gcr.io/{project}/sckhoo_nodejs_cloudrun_helloworld --allow-unauthenticated --region=asia-southeast1




