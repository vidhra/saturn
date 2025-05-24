# opsworksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# opsworks

## Description

Welcome to the *OpsWorks Stacks API Reference* . This guide provides descriptions, syntax, and usage examples for OpsWorks Stacks actions and data types, including common parameters and error codes.

OpsWorks Stacks is an application management service that provides an integrated experience for managing the complete application lifecycle. For information about OpsWorks, see the [OpsWorks](http://aws.amazon.com/opsworks/) information page.

**SDKs and CLI**

Use the OpsWorks Stacks API by using the Command Line Interface (CLI) or by using one of the Amazon Web Services SDKs to implement applications in your preferred language. For more information, see:

- [CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- [SDK for Java](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/opsworks/AWSOpsWorksClient.html)
- [SDK for .NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/OpsWorks/NOpsWorks.html)
- [SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.OpsWorks.OpsWorksClient.html)
- [SDK for Ruby](http://docs.aws.amazon.com/sdkforruby/api/)
- [Amazon Web Services SDK for Node.js](http://aws.amazon.com/documentation/sdkforjavascript/)
- [SDK for Python (Boto)](http://docs.pythonboto.org/en/latest/ref/opsworks.html)

**Endpoints**

OpsWorks Stacks supports the following endpoints, all HTTPS. You must connect to one of the following endpoints. Stacks can only be accessed or managed within the endpoint in which they are created.

- opsworks.us-east-1.amazonaws.com
- opsworks.us-east-2.amazonaws.com
- opsworks.us-west-1.amazonaws.com
- opsworks.us-west-2.amazonaws.com
- opsworks.ca-central-1.amazonaws.com (API only; not available in the Amazon Web Services Management Console)
- opsworks.eu-west-1.amazonaws.com
- opsworks.eu-west-2.amazonaws.com
- opsworks.eu-west-3.amazonaws.com
- opsworks.eu-central-1.amazonaws.com
- opsworks.ap-northeast-1.amazonaws.com
- opsworks.ap-northeast-2.amazonaws.com
- opsworks.ap-south-1.amazonaws.com
- opsworks.ap-southeast-1.amazonaws.com
- opsworks.ap-southeast-2.amazonaws.com
- opsworks.sa-east-1.amazonaws.com

**Chef Versions**

When you call  CreateStack ,  CloneStack , or  UpdateStack we recommend you use the `ConfigurationManager` parameter to specify the Chef version. The recommended and default value for Linux stacks is currently 12. Windows stacks use Chef 12.2. For more information, see [Chef Versions](https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-chef11.html) .

### Note

You can specify Chef 12, 11.10, or 11.4 for your Linux stack. We recommend migrating your existing Linux stacks to Chef 12 as soon as possible.

## Available Commands

- [assign-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-instance.html)
- [assign-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-volume.html)
- [associate-elastic-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/associate-elastic-ip.html)
- [attach-elastic-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/attach-elastic-load-balancer.html)
- [clone-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/clone-stack.html)
- [create-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-app.html)
- [create-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-deployment.html)
- [create-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html)
- [create-layer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-layer.html)
- [create-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-stack.html)
- [create-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-user-profile.html)
- [delete-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-app.html)
- [delete-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-instance.html)
- [delete-layer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-layer.html)
- [delete-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-stack.html)
- [delete-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-user-profile.html)
- [deregister-ecs-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-ecs-cluster.html)
- [deregister-elastic-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-elastic-ip.html)
- [deregister-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-instance.html)
- [deregister-rds-db-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-rds-db-instance.html)
- [deregister-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-volume.html)
- [describe-agent-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-agent-versions.html)
- [describe-apps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-apps.html)
- [describe-commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-commands.html)
- [describe-deployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-deployments.html)
- [describe-ecs-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-ecs-clusters.html)
- [describe-elastic-ips](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-ips.html)
- [describe-elastic-load-balancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-load-balancers.html)
- [describe-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html)
- [describe-layers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-layers.html)
- [describe-load-based-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-load-based-auto-scaling.html)
- [describe-my-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-my-user-profile.html)
- [describe-operating-systems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-operating-systems.html)
- [describe-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-permissions.html)
- [describe-raid-arrays](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-raid-arrays.html)
- [describe-rds-db-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-rds-db-instances.html)
- [describe-service-errors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-service-errors.html)
- [describe-stack-provisioning-parameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stack-provisioning-parameters.html)
- [describe-stack-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stack-summary.html)
- [describe-stacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stacks.html)
- [describe-time-based-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-time-based-auto-scaling.html)
- [describe-user-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-user-profiles.html)
- [describe-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-volumes.html)
- [detach-elastic-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/detach-elastic-load-balancer.html)
- [disassociate-elastic-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/disassociate-elastic-ip.html)
- [get-hostname-suggestion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/get-hostname-suggestion.html)
- [grant-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/grant-access.html)
- [list-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/list-tags.html)
- [reboot-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/reboot-instance.html)
- [register](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register.html)
- [register-ecs-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-ecs-cluster.html)
- [register-elastic-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-elastic-ip.html)
- [register-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html)
- [register-rds-db-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-rds-db-instance.html)
- [register-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-volume.html)
- [set-load-based-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-load-based-auto-scaling.html)
- [set-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-permission.html)
- [set-time-based-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-time-based-auto-scaling.html)
- [start-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-instance.html)
- [start-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-stack.html)
- [stop-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-instance.html)
- [stop-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-stack.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/tag-resource.html)
- [unassign-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-instance.html)
- [unassign-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-volume.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/untag-resource.html)
- [update-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-app.html)
- [update-elastic-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-elastic-ip.html)
- [update-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-instance.html)
- [update-layer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-layer.html)
- [update-my-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-my-user-profile.html)
- [update-rds-db-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-rds-db-instance.html)
- [update-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html)
- [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-user-profile.html)
- [update-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-volume.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/wait/index.html)