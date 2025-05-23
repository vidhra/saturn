# waitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# wait

## Description

Wait until a particular condition is satisfied. Each subcommand polls an API until the listed requirement is met.

## Available Commands

- [annotation-import-job-created](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/annotation-import-job-created.html)
- [annotation-store-created](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/annotation-store-created.html)
- [annotation-store-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/annotation-store-deleted.html)
- [annotation-store-version-created](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/annotation-store-version-created.html)
- [annotation-store-version-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/annotation-store-version-deleted.html)
- [read-set-activation-job-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/read-set-activation-job-completed.html)
- [read-set-export-job-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/read-set-export-job-completed.html)
- [read-set-import-job-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/read-set-import-job-completed.html)
- [reference-import-job-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/reference-import-job-completed.html)
- [run-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/run-completed.html)
- [run-running](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/run-running.html)
- [task-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/task-completed.html)
- [task-running](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/task-running.html)
- [variant-import-job-created](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/variant-import-job-created.html)
- [variant-store-created](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/variant-store-created.html)
- [variant-store-deleted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/variant-store-deleted.html)
- [workflow-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/workflow-active.html)
- [workflow-version-active](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/wait/workflow-version-active.html)

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To wait for an annotation store to be ready**

The following `wait` example waits for an annotation storeâs status to be `ACTIVE`.

```
aws omics wait annotation-store-created \
    --name my_ann_store
```

For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html) in the *Amazon Omics Developer Guide*.