# update-work-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# update-work-group

## Description

Updates the workgroup with the specified name. The workgroupâs name cannot be changed. Only `ConfigurationUpdates` can be specified.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/UpdateWorkGroup)

## Synopsis

```
update-work-group
--work-group <value>
[--description <value>]
[--configuration-updates <value>]
[--state <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
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

`--work-group` (string)

The specified workgroup that will be updated.

`--description` (string)

The workgroup description.

`--configuration-updates` (structure)

Contains configuration updates for an Athena SQL workgroup.

EnforceWorkGroupConfiguration -> (boolean)

If set to âtrueâ, the settings for the workgroup override client-side settings. If set to âfalseâ client-side settings are used. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

ResultConfigurationUpdates -> (structure)

The result configuration information about the queries in this workgroup that will be updated. Includes the updated results location and an updated option for encrypting query results.

OutputLocation -> (string)

The location in Amazon S3 where your query and calculation results are stored, such as `s3://path/to/query/bucket/` . If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The âworkgroup settings overrideâ is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration` . See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

RemoveOutputLocation -> (boolean)

If set to âtrueâ, indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to âfalseâ or not set, and a value is present in the `OutputLocation` in `ResultConfigurationUpdates` (the client-side setting), the `OutputLocation` in the workgroupâs `ResultConfiguration` will be updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

EncryptionConfiguration -> (structure)

The encryption configuration for query and calculation results.

EncryptionOption -> (string)

Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3` ), server-side encryption with KMS-managed keys (`SSE_KMS` ), or client-side encryption with KMS-managed keys (`CSE_KMS` ) is used.

If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroupâs setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey -> (string)

For `SSE_KMS` and `CSE_KMS` , this is the KMS key ARN or ID.

RemoveEncryptionConfiguration -> (boolean)

If set to âtrueâ, indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to âfalseâ or not set, and a value is present in the `EncryptionConfiguration` in `ResultConfigurationUpdates` (the client-side setting), the `EncryptionConfiguration` in the workgroupâs `ResultConfiguration` will be updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

ExpectedBucketOwner -> (string)

The Amazon Web Services account ID that you expect to be the owner of the Amazon S3 bucket specified by  ResultConfiguration$OutputLocation . If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner` Amazon Web Services account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.

If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

RemoveExpectedBucketOwner -> (boolean)

If set to âtrueâ, removes the Amazon Web Services account ID previously specified for  ResultConfiguration$ExpectedBucketOwner . If set to âfalseâ or not set, and a value is present in the `ExpectedBucketOwner` in `ResultConfigurationUpdates` (the client-side setting), the `ExpectedBucketOwner` in the workgroupâs `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

AclConfiguration -> (structure)

The ACL configuration for the query results.

S3AclOption -> (string)

The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL` . If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroupâs settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) in the *Amazon S3 User Guide* .

RemoveAclConfiguration -> (boolean)

If set to `true` , indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null. If set to `false` or not set, and a value is present in the `AclConfiguration` of `ResultConfigurationUpdates` , the `AclConfiguration` in the workgroupâs `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

PublishCloudWatchMetricsEnabled -> (boolean)

Indicates whether this workgroup enables publishing metrics to Amazon CloudWatch.

BytesScannedCutoffPerQuery -> (long)

The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.

RemoveBytesScannedCutoffPerQuery -> (boolean)

Indicates that the data usage control limit per query is removed.  WorkGroupConfiguration$BytesScannedCutoffPerQuery

RequesterPaysEnabled -> (boolean)

If set to `true` , allows members assigned to a workgroup to specify Amazon S3 Requester Pays buckets in queries. If set to `false` , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is `false` . For more information about Requester Pays buckets, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service Developer Guide* .

EngineVersion -> (structure)

The engine version requested when a workgroup is updated. After the update, all queries on the workgroup run on the requested engine version. If no value was previously set, the default is Auto. Queries on the `AmazonAthenaPreviewFunctionality` workgroup run on the preview engine regardless of this setting.

SelectedEngineVersion -> (string)

The engine version requested by the user. Possible values are determined by the output of `ListEngineVersions` , including AUTO. The default is AUTO.

EffectiveEngineVersion -> (string)

Read only. The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a `CreateWorkGroup` or `UpdateWorkGroup` operation, the `EffectiveEngineVersion` field is ignored.

RemoveCustomerContentEncryptionConfiguration -> (boolean)

Removes content encryption configuration from an Apache Spark-enabled Athena workgroup.

AdditionalConfiguration -> (string)

Contains a user defined string in JSON format for a Spark-enabled workgroup.

ExecutionRole -> (string)

The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.

CustomerContentEncryptionConfiguration -> (structure)

Specifies the customer managed KMS key that is used to encrypt the userâs data stores in Athena. When an Amazon Web Services managed key is used, this value is null. This setting does not apply to Athena SQL workgroups.

KmsKey -> (string)

The customer managed KMS key that is used to encrypt the userâs data stores in Athena.

EnableMinimumEncryptionConfiguration -> (boolean)

Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries. This setting does not apply to Spark-enabled workgroups.

The `EnforceWorkGroupConfiguration` setting takes precedence over the `EnableMinimumEncryptionConfiguration` flag. This means that if `EnforceWorkGroupConfiguration` is true, the `EnableMinimumEncryptionConfiguration` flag is ignored, and the workgroup configuration for encryption is used.

QueryResultsS3AccessGrantsConfiguration -> (structure)

Specifies whether Amazon S3 access grants are enabled for query results.

EnableS3AccessGrants -> (boolean)

Specifies whether Amazon S3 access grants are enabled for query results.

CreateUserLevelPrefix -> (boolean)

When enabled, appends the user ID as an Amazon S3 path prefix to the query result output location.

AuthenticationType -> (string)

The authentication type used for Amazon S3 access grants. Currently, only `DIRECTORY_IDENTITY` is supported.

Shorthand Syntax:

```
EnforceWorkGroupConfiguration=boolean,ResultConfigurationUpdates={OutputLocation=string,RemoveOutputLocation=boolean,EncryptionConfiguration={EncryptionOption=string,KmsKey=string},RemoveEncryptionConfiguration=boolean,ExpectedBucketOwner=string,RemoveExpectedBucketOwner=boolean,AclConfiguration={S3AclOption=string},RemoveAclConfiguration=boolean},PublishCloudWatchMetricsEnabled=boolean,BytesScannedCutoffPerQuery=long,RemoveBytesScannedCutoffPerQuery=boolean,RequesterPaysEnabled=boolean,EngineVersion={SelectedEngineVersion=string,EffectiveEngineVersion=string},RemoveCustomerContentEncryptionConfiguration=boolean,AdditionalConfiguration=string,ExecutionRole=string,CustomerContentEncryptionConfiguration={KmsKey=string},EnableMinimumEncryptionConfiguration=boolean,QueryResultsS3AccessGrantsConfiguration={EnableS3AccessGrants=boolean,CreateUserLevelPrefix=boolean,AuthenticationType=string}
```

JSON Syntax:

```
{
  "EnforceWorkGroupConfiguration": true|false,
  "ResultConfigurationUpdates": {
    "OutputLocation": "string",
    "RemoveOutputLocation": true|false,
    "EncryptionConfiguration": {
      "EncryptionOption": "SSE_S3"|"SSE_KMS"|"CSE_KMS",
      "KmsKey": "string"
    },
    "RemoveEncryptionConfiguration": true|false,
    "ExpectedBucketOwner": "string",
    "RemoveExpectedBucketOwner": true|false,
    "AclConfiguration": {
      "S3AclOption": "BUCKET_OWNER_FULL_CONTROL"
    },
    "RemoveAclConfiguration": true|false
  },
  "PublishCloudWatchMetricsEnabled": true|false,
  "BytesScannedCutoffPerQuery": long,
  "RemoveBytesScannedCutoffPerQuery": true|false,
  "RequesterPaysEnabled": true|false,
  "EngineVersion": {
    "SelectedEngineVersion": "string",
    "EffectiveEngineVersion": "string"
  },
  "RemoveCustomerContentEncryptionConfiguration": true|false,
  "AdditionalConfiguration": "string",
  "ExecutionRole": "string",
  "CustomerContentEncryptionConfiguration": {
    "KmsKey": "string"
  },
  "EnableMinimumEncryptionConfiguration": true|false,
  "QueryResultsS3AccessGrantsConfiguration": {
    "EnableS3AccessGrants": true|false,
    "CreateUserLevelPrefix": true|false,
    "AuthenticationType": "DIRECTORY_IDENTITY"
  }
}
```

`--state` (string)

The workgroup state that will be updated for the given workgroup.

Possible values:

- `ENABLED`
- `DISABLED`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

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

**To update a workgroup**

The following `update-work-group` example disables the `Data_Analyst_Group` workgroup. Users cannot run or create queries in the disabled workgroup, but can still view metrics, data usage limit controls, workgroup settings, query history, and saved queries.

```
aws athena update-work-group \
    --work-group Data_Analyst_Group \
    --state DISABLED
```

This command produces no output. To verify the change in state, use `aws athena get-work-group --work-group Data_Analyst_Group` and check the `State` property in the output.

For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) in the *Amazon Athena User Guide*.

## Output

None