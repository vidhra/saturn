# waitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/wait/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/wait/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# wait

## Description

Wait until a particular condition is satisfied. Each subcommand polls an API until the listed requirement is met.

## Available Commands

- [cluster-running](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/wait/cluster-running.html)
- [cluster-terminated](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/wait/cluster-terminated.html)
- [step-complete](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/wait/step-complete.html)

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

The following command waits until a cluster with the cluster ID `j-3SD91U2E1L2QX` is up and running:

```
aws emr wait cluster-running --cluster-id j-3SD91U2E1L2QX
```