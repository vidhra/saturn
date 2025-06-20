# opsworkscmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# opsworkscm

## Description

AWS OpsWorks for configuration management (CM) is a service that runs and manages configuration management servers. You can use AWS OpsWorks CM to create and manage AWS OpsWorks for Chef Automate and AWS OpsWorks for Puppet Enterprise servers, and add or remove nodes for the servers to manage.

**Glossary of terms**

- **Server** : A configuration management server that can be highly-available. The configuration management server runs on an Amazon Elastic Compute Cloud (EC2) instance, and may use various other AWS services, such as Amazon Relational Database Service (RDS) and Elastic Load Balancing. A server is a generic abstraction over the configuration manager that you want to use, much like Amazon RDS. In AWS OpsWorks CM, you do not start or stop servers. After you create servers, they continue to run until they are deleted.
- **Engine** : The engine is the specific configuration manager that you want to use. Valid values in this release include `ChefAutomate` and `Puppet` .
- **Backup** : This is an application-level backup of the data that the configuration manager stores. AWS OpsWorks CM creates an S3 bucket for backups when you launch the first server. A backup maintains a snapshot of a serverâs configuration-related attributes at the time the backup starts.
- **Events** : Events are always related to a server. Events are written during server creation, when health checks run, when backups are created, when system maintenance is performed, etc. When you delete a server, the serverâs events are also deleted.
- **Account attributes** : Every account has attributes that are assigned in the AWS OpsWorks CM database. These attributes store information about configuration limits (servers, backups, etc.) and your customer account.

**Endpoints**

AWS OpsWorks CM supports the following endpoints, all HTTPS. You must connect to one of the following endpoints. Your servers can only be accessed or managed within the endpoint in which they are created.

- opsworks-cm.us-east-1.amazonaws.com
- opsworks-cm.us-east-2.amazonaws.com
- opsworks-cm.us-west-1.amazonaws.com
- opsworks-cm.us-west-2.amazonaws.com
- opsworks-cm.ap-northeast-1.amazonaws.com
- opsworks-cm.ap-southeast-1.amazonaws.com
- opsworks-cm.ap-southeast-2.amazonaws.com
- opsworks-cm.eu-central-1.amazonaws.com
- opsworks-cm.eu-west-1.amazonaws.com

For more information, see [AWS OpsWorks endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/opsworks-service.html) in the AWS General Reference.

**Throttling limits**

All API operations allow for five requests per second with a burst of 10 requests per second.

## Available Commands

- [associate-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/associate-node.html)
- [create-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/create-backup.html)
- [create-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/create-server.html)
- [delete-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/delete-backup.html)
- [delete-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/delete-server.html)
- [describe-account-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-account-attributes.html)
- [describe-backups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-backups.html)
- [describe-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-events.html)
- [describe-node-association-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-node-association-status.html)
- [describe-servers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/describe-servers.html)
- [disassociate-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/disassociate-node.html)
- [export-server-engine-attribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/export-server-engine-attribute.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/list-tags-for-resource.html)
- [restore-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/restore-server.html)
- [start-maintenance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/start-maintenance.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/untag-resource.html)
- [update-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/update-server.html)
- [update-server-engine-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/update-server-engine-attributes.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/wait/index.html)