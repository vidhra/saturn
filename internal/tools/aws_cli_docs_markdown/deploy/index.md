# deployÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# deploy

## Description

CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances running in your own facility, serverless Lambda functions, or applications in an Amazon ECS service.

You can deploy a nearly unlimited variety of application content, such as an updated Lambda function, updated applications in an Amazon ECS service, code, web and configuration files, executables, packages, scripts, multimedia files, and so on. CodeDeploy can deploy application content stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. You do not need to make changes to your existing code before you can use CodeDeploy.

CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications, without many of the risks associated with error-prone manual deployments.

**CodeDeploy Components**

Use the information in this guide to help you work with the following CodeDeploy components:

- **Application** : A name that uniquely identifies the application you want to deploy. CodeDeploy uses this name, which functions as a container, to ensure the correct combination of revision, deployment configuration, and deployment group are referenced during a deployment.
- **Deployment group** : A set of individual instances, CodeDeploy Lambda deployment configuration settings, or an Amazon ECS service and network details. A Lambda deployment group specifies how to route traffic to a new version of a Lambda function. An Amazon ECS deployment group specifies the service created in Amazon ECS to deploy, a load balancer, and a listener to reroute production traffic to an updated containerized application. An Amazon EC2/On-premises deployment group contains individually tagged instances, Amazon EC2 instances in Amazon EC2 Auto Scaling groups, or both. All deployment groups can specify optional trigger, alarm, and rollback settings.
- **Deployment configuration** : A set of deployment rules and deployment success and failure conditions used by CodeDeploy during a deployment.
- **Deployment** : The process and the components used when updating a Lambda function, a containerized application in an Amazon ECS service, or of installing content on one or more instances.
- **Application revisions** : For an Lambda deployment, this is an AppSpec file that specifies the Lambda function to be updated and one or more functions to validate deployment lifecycle events. For an Amazon ECS deployment, this is an AppSpec file that specifies the Amazon ECS task definition, container, and port where production traffic is rerouted. For an EC2/On-premises deployment, this is an archive file that contains source contentâsource code, webpages, executable files, and deployment scriptsâalong with an AppSpec file. Revisions are stored in Amazon S3 buckets or GitHub repositories. For Amazon S3, a revision is uniquely identified by its Amazon S3 object key and its ETag, version, or both. For GitHub, a revision is uniquely identified by its commit ID.

This guide also contains information to help you get details about the instances in your deployments, to make on-premises instances available for CodeDeploy deployments, to get details about a Lambda function deployment, and to get details about Amazon ECS service deployments.

**CodeDeploy Information Resources**

- [CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide)
- [CodeDeploy API Reference Guide](https://docs.aws.amazon.com/codedeploy/latest/APIReference/)
- [CLI Reference for CodeDeploy](https://docs.aws.amazon.com/cli/latest/reference/deploy/index.html)
- [CodeDeploy Developer Forum](https://forums.aws.amazon.com/forum.jspa?forumID=179)

## Available Commands

- [add-tags-to-on-premises-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/add-tags-to-on-premises-instances.html)
- [batch-get-application-revisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-application-revisions.html)
- [batch-get-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-applications.html)
- [batch-get-deployment-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployment-groups.html)
- [batch-get-deployment-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployment-targets.html)
- [batch-get-deployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployments.html)
- [batch-get-on-premises-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-on-premises-instances.html)
- [continue-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/continue-deployment.html)
- [create-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-application.html)
- [create-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html)
- [create-deployment-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-config.html)
- [create-deployment-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html)
- [delete-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-application.html)
- [delete-deployment-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-config.html)
- [delete-deployment-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-group.html)
- [delete-git-hub-account-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-git-hub-account-token.html)
- [delete-resources-by-external-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-resources-by-external-id.html)
- [deregister](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister.html)
- [deregister-on-premises-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html)
- [get-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application.html)
- [get-application-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application-revision.html)
- [get-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html)
- [get-deployment-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-config.html)
- [get-deployment-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-group.html)
- [get-deployment-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-target.html)
- [get-on-premises-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-on-premises-instance.html)
- [install](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/install.html)
- [list-application-revisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-application-revisions.html)
- [list-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-applications.html)
- [list-deployment-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-configs.html)
- [list-deployment-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html)
- [list-deployment-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-targets.html)
- [list-deployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html)
- [list-git-hub-account-token-names](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-git-hub-account-token-names.html)
- [list-on-premises-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-tags-for-resource.html)
- [push](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/push.html)
- [put-lifecycle-event-hook-execution-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/put-lifecycle-event-hook-execution-status.html)
- [register](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register.html)
- [register-application-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-application-revision.html)
- [register-on-premises-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-on-premises-instance.html)
- [remove-tags-from-on-premises-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/remove-tags-from-on-premises-instances.html)
- [stop-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/stop-deployment.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/tag-resource.html)
- [uninstall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/uninstall.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/untag-resource.html)
- [update-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-application.html)
- [update-deployment-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/wait/index.html)