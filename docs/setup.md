# Setup and Preparation

## Repo
First fork or clone this repo on your own Github account. I strongly suggest you use github since it will be easy to automate code deployments through Circle CI.

## Docker
Install Docker for Desktop and Docker Compose for your machine:
- https://www.docker.com/

## AWS
You will need to have an AWS IAM account, with permissions to the following services:

- Cloudformation
- S3
- API Gateway
- Lambda
- Cognito
- Cloudwatch
- Cloudfront
- Route53
- IAM *create roles and policies for lambda*

Next you will need to have or create the following resources.

#### Lambda Layer
Have a **Python 3.7** Lambda Layer you can use with the following libraries:

- pyjwt==1.7.1
- cryptography==2.8

If you need help creating one look at this repo here:<br/>
https://github.com/gugzkumar/my-python-lambda-layers


#### Route53 Domain
**You can skip this if you only want to run the app locally on your machine.**<br/>
Route53 is Amazon's DNS Webservice. You can buy domains for pretty cheap here. Cheet Sheet is setup, to integrate with Route53 so it is your best option. Be prepared to have a subdomain that you are ready to use. We will deploy the app to use the following routes:

- UI: https://`{SUB_DOMAIN}`.`{DOMAIN}`
- API: https://`{SUB_DOMAIN}`.api.`{DOMAIN}`

For example if your domain is *mydomain.com* and the subdomain is *cheet-sheet*, you will use the following routes:

- https://cheet-sheet.mydomain.com
- https://cheet-sheet.api.mydomain.com

#### ACM Certificate
**You can skip this if you only want to run the app locally on your machine.**<br/>
Set up an SSL Certificate throw through AWS' Certificate Manager. You will want to create a single certificate has the following domains:

- https://`{SUB_DOMAIN}`.`{DOMAIN}`
- https://`{SUB_DOMAIN}`.api.`{DOMAIN}`

**Tip:** I like to use wild cards for my domain so I can use the same certificate for multiple environments (dev, staging, prod, etc.)


## Setup Utility CLI
To streamline the creation of configuration variables and files we have some cli tools built with Node JS. Download node if you do not have it. Then from the the `.utils` folder run `npm install` to install the cli. Run `node main.js --help` to confirm the utility cli works.
<br/><br/>
https://nodejs.org/en/
