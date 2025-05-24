# cloud9Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cloud9

## Description

Cloud9 is a collection of tools that you can use to code, build, run, test, debug, and release software in the cloud.

For more information about Cloud9, see the [Cloud9 User Guide](https://docs.aws.amazon.com/cloud9/latest/user-guide) .

### Warning

Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. [Learn moreâ](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

Cloud9 supports these operations:

- `CreateEnvironmentEC2` : Creates an Cloud9 development environment, launches an Amazon EC2 instance, and then connects from the instance to the environment.
- `CreateEnvironmentMembership` : Adds an environment member to an environment.
- `DeleteEnvironment` : Deletes an environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.
- `DeleteEnvironmentMembership` : Deletes an environment member from an environment.
- `DescribeEnvironmentMemberships` : Gets information about environment members for an environment.
- `DescribeEnvironments` : Gets information about environments.
- `DescribeEnvironmentStatus` : Gets status information for an environment.
- `ListEnvironments` : Gets a list of environment identifiers.
- `ListTagsForResource` : Gets the tags for an environment.
- `TagResource` : Adds tags to an environment.
- `UntagResource` : Removes tags from an environment.
- `UpdateEnvironment` : Changes the settings of an existing environment.
- `UpdateEnvironmentMembership` : Changes the settings of an existing environment member for an environment.

## Available Commands

- [create-environment-ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html)
- [create-environment-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html)
- [delete-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html)
- [delete-environment-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html)
- [describe-environment-memberships](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html)
- [describe-environment-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-status.html)
- [describe-environments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html)
- [list-environments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/untag-resource.html)
- [update-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment.html)
- [update-environment-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html)