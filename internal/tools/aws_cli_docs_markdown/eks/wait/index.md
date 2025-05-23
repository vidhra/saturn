# waitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# wait

## Description

Wait until a particular condition is satisfied. Each subcommand polls an API until the listed requirement is met.

## Available Commands

- [addon-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/addon-active.html)
- [addon-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/addon-deleted.html)
- [cluster-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/cluster-active.html)
- [cluster-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/cluster-deleted.html)
- [fargate-profile-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/fargate-profile-active.html)
- [fargate-profile-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/fargate-profile-deleted.html)
- [nodegroup-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/nodegroup-active.html)
- [nodegroup-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/wait/nodegroup-deleted.html)

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To wait for a cluster to become active**

This example command waits for a cluster named `example` to become active.

Command:

```
aws eks wait cluster-active --name example
```

**To wait for a cluster to be deleted**

This example command waits for a cluster named `example` to be deleted.

Command:

```
aws eks wait cluster-deleted --name example
```