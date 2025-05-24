# create-role-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-role-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-role-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# create-role-associations

## Description

Creates role associations of given IAM role with EMR service accounts such that it can be used with Amazon EMR on EKS with the given namespace from the given EKS cluster.

Note:
The command would associate EMR service accounts with provided IAM role to EKS pod identity:

- âemr-containers-sa-%(FRAMEWORK)s-%(COMPONENT)s-%(AWS_ACCOUNT_ID)s-%(BASE36_ENCODED_ROLE_NAME)sâ

Here:

```
<FRAMEWORK> = EMR on EKS framework such as spark, flink, livy
<COMPONENT> = Task component for the framework. Such as client, driver, executor for spark; flink-operator, jobmanager, taskmanager for flink.
<AWS_ACCOUNT_ID> = AWS Account ID of the EKS cluster
<BASE36_ENCODED_ROLE_NAME> = Base36 encoded form of the IAM Role name
```

You can use the **âtype** option to select which submission model to associate.

You can use the **âoperator-namespace** option if your operator/livy jobs are running in a different operator namespace other than your job/application namespace. **ânamespace** should be the Job/Application Namespace, and this option is for operator namespace to associate operator/livy service account.

You can use the **âservice-account-name** option to associate a custom service account with the role.

## Synopsis

```
create-role-associations
--cluster-name <value>
--namespace <value>
--role-name <value>
[--type <value>]
[--operator-namespace <value>]
[--service-account-name <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--cluster-name` (string)
Specify the name of the Amazon EKS cluster with which the IAM Role would be associated.

`--namespace` (string)
Specify the job/application namespace from the Amazon EKS cluster with which the IAM Role would be associated.

`--role-name` (string)
Specify the IAM Role name that you want to associate with Amazon EMR on EKS.

`--type` (string)
Specify the Amazon EMR on EKS submission model and choose service accounts that you want to associate with Amazon EMR on EKS. The default is start_job_run. Supported types: start_job_run, interactive_endpoint, spark_operator, flink_operator, livy.

`--operator-namespace` (string)
Specify the namespace that you want to associate the operator service account with the IAM role. Default to the job/application namespace specified. Note: If jobs are running in a different namespace than the operator installation namespace, this parameter needs to be set as the namespace that the operator is running on.

`--service-account-name` (string)
Specify the service account name that you want to associate with the IAM role. By default, Amazon EMR on EKS service accounts will be used for association.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create role associations of an IAM Role with EMR service accounts to be used with Amazon EMR on EKS**

The following `create-role-associations` example command creates EKS pod identity associations of a role named **example_iam_role** with EMR service accounts such that it can be used with Amazon EMR on EKS with
**example_namespace** namespace from an EKS cluster named **example_cluster**.:

```
aws emr-containers create-role-associations \
    --cluster-name example_cluster \
    --namespace example_namespace \
    --role-name example_iam_role
```

Output:

```
[
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-client-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/a-bgyr1umgdmrk1kdtq",
        "associationId": "a-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-driver-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/b-bgyr1umgdmrk1kdtq",
        "associationId": "b-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-executor-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/c-bgyr1umgdmrk1kdtq",
        "associationId": "c-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    }
]
```