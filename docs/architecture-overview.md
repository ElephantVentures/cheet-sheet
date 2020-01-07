# Architecture Diagrams and Overview

## Architecture Diagram
<p align="left">
  <img
    alt="Remote Environment"
    src="/docs/images/architecture/Remote-Environment.png"
    width="100%"
  />
</p>
<br/>
When the user visits our web page, the frontend loads from an S3 bucket that saves all of our published Angular Code. When the website get's used, REST requests get send to Api Gateway which asks a Lambda function to handle it. Lambda then queries our Sheet Data S3 bucket to read and change our application's state (this is where all our sheets and index cards are saved). We are able to support package dependencies through a Lambda Layer.
<br/><br/>
Our Api uses a monolithic function, this means all requests are handled by the same function.
<br/><br/>
Authentication is handled by Cognito. When the user is a verified, a secure JWT token is received and saved in the browser. Then when making authenticated requests to the api, lambda makes sure that the token is properly signed and encrypted. This is what prevents a user from accessing and editing Workspaces they don't belong to.
<br/><br/>
The Api Deployment bucket does not play an active role in the Infrastructure. But, it is something that is needed when we want to make updates to our API logic.

### Deployment Process
<p align="left">
  <img
    alt="Deployment Process"
    src="/docs/images/architecture/Deployment-Process.png"
    width="100%"
  />
</p>
<br/>
This Diagram outlines the process of deploying the app to AWS using the tools provided in this repo. We divide deployment into three Cloudformation Stacks. This does does two things:

1. If different people in your organization have different privileges to your cloud account, you can divide the responsibilities.
    - Example 1: You may not have permission to change the DNS records. Instead you can just deploy the first two stacks, and then let a Network Admin handle the routing.
    - Example 2: You may want to give the development team the ability to update code, but not Cognito. Then give them access to the **Code Stack**.
1. It properly distributes risk so that we secure our application's integrity. The Code Stack for instance, is something you may want to update continuously through CI/CD. But you do not want give it permissions to be able to delete or change policies on our Bucket's.

Scroll down to see which resources each stack makes.

Other things to note:

- The ACM certificates and the Lambda layer are resources you must provide (are not created for you)
- While the frontend code is not deployed through the **Code Stack** it is part of the same step
- The repo has CircleCi configurations to support continuous deployment of the **Code Stack** (making updates to the api and frontend easy)

### Infrastructure Stack
<p align="left">
  <img
    alt="Infrastructure Stack"
    src="/docs/images/architecture/Infrastructure-Stack.png"
    width="100%"
  />
</p>

### Code Stack
<p align="left">
  <img
    alt="Code Stack"
    src="/docs/images/architecture/Code-Stack.png"
    width="100%"
  />
</p>

### Network Stack
<p align="left">
  <img
    alt="Network Stack"
    src="/docs/images/architecture/Network-Stack.png"
    width="100%"
  />
</p>


## Local Development
<p align="left">
  <img
    alt="Local Environment"
    src="/docs/images/architecture/Local-Environment.png"
    width="100%"
  />
</p>

This repo also supports local development. This is so we can develop and test new features on our own machine before deploying them. To do this the Api and the UI are dockerized. Both services use mounted volumes so code changes can be reflected in real time.

The Api Service uses SAM local. Anytime a request is sent to the Api, SAM will run a temporary Docker container to simulate the Lambda function.

Rather than mocking it, we use real AWS services for our Sheet data bucket and Cognito Userpool. If you have a large team you can share the same Userpool but I suggest giving each developer a different bucket.
