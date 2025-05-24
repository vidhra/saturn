# update-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# update-settings

## Description

Updates Audit Manager settings for the current account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/UpdateSettings)

## Synopsis

```
update-settings
[--sns-topic <value>]
[--default-assessment-reports-destination <value>]
[--default-process-owners <value>]
[--kms-key <value>]
[--evidence-finder-enabled | --no-evidence-finder-enabled]
[--deregistration-policy <value>]
[--default-export-destination <value>]
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

`--sns-topic` (string)

The Amazon Simple Notification Service (Amazon SNS) topic that Audit Manager sends notifications to.

`--default-assessment-reports-destination` (structure)

The default S3 destination bucket for storing assessment reports.

destinationType -> (string)

The destination type, such as Amazon S3.

destination -> (string)

The destination bucket where Audit Manager stores assessment reports.

Shorthand Syntax:

```
destinationType=string,destination=string
```

JSON Syntax:

```
{
  "destinationType": "S3",
  "destination": "string"
}
```

`--default-process-owners` (list)

A list of the default audit owners.

(structure)

The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

Shorthand Syntax:

```
roleType=string,roleArn=string ...
```

JSON Syntax:

```
[
  {
    "roleType": "PROCESS_OWNER"|"RESOURCE_OWNER",
    "roleArn": "string"
  }
  ...
]
```

`--kms-key` (string)

The KMS key details.

`--evidence-finder-enabled` | `--no-evidence-finder-enabled` (boolean)

Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.

### Warning

When you use this attribute to disable evidence finder, Audit Manager deletes the event data store thatâs used to query your evidence data. As a result, you canât re-enable evidence finder and use the feature again. Your only alternative is to [deregister](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html) and then [re-register](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html) Audit Manager.

`--deregistration-policy` (structure)

The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.

deleteResources -> (string)

Specifies which Audit Manager data will be deleted when you deregister Audit Manager.

- If you set the value to `ALL` , all of your data is deleted within seven days of deregistration.
- If you set the value to `DEFAULT` , none of your data is deleted at the time of deregistration. However, keep in mind that the Audit Manager data retention policy still applies. As a result, any evidence data will be deleted two years after its creation date. Your other Audit Manager resources will continue to exist indefinitely.

Shorthand Syntax:

```
deleteResources=string
```

JSON Syntax:

```
{
  "deleteResources": "ALL"|"DEFAULT"
}
```

`--default-export-destination` (structure)

The default S3 destination bucket for storing evidence finder exports.

destinationType -> (string)

The destination type, such as Amazon S3.

destination -> (string)

The destination bucket where Audit Manager stores exported files.

Shorthand Syntax:

```
destinationType=string,destination=string
```

JSON Syntax:

```
{
  "destinationType": "S3",
  "destination": "string"
}
```

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

## Output

settings -> (structure)

The current list of settings.

isAwsOrgEnabled -> (boolean)

Specifies whether Organizations is enabled.

snsTopic -> (string)

The designated Amazon Simple Notification Service (Amazon SNS) topic.

defaultAssessmentReportsDestination -> (structure)

The default S3 destination bucket for storing assessment reports.

destinationType -> (string)

The destination type, such as Amazon S3.

destination -> (string)

The destination bucket where Audit Manager stores assessment reports.

defaultProcessOwners -> (list)

The designated default audit owners.

(structure)

The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

kmsKey -> (string)

The KMS key details.

evidenceFinderEnablement -> (structure)

The current evidence finder status and event data store details.

eventDataStoreArn -> (string)

The Amazon Resource Name (ARN) of the CloudTrail Lake event data store thatâs used by evidence finder. The event data store is the lake of evidence data that evidence finder runs queries against.

enablementStatus -> (string)

The current status of the evidence finder feature and the related event data store.

- `ENABLE_IN_PROGRESS` means that you requested to enable evidence finder. An event data store is currently being created to support evidence finder queries.
- `ENABLED` means that an event data store was successfully created and evidence finder is enabled. We recommend that you wait 7 days until the event data store is backfilled with your past two yearsâ worth of evidence data. You can use evidence finder in the meantime, but not all data might be available until the backfill is complete.
- `DISABLE_IN_PROGRESS` means that you requested to disable evidence finder, and your request is pending the deletion of the event data store.
- `DISABLED` means that you have permanently disabled evidence finder and the event data store has been deleted. You canât re-enable evidence finder after this point.

backfillStatus -> (string)

The current status of the evidence data backfill process.

The backfill starts after you enable evidence finder. During this task, Audit Manager populates an event data store with your past two yearsâ worth of evidence data so that your evidence can be queried.

- `NOT_STARTED` means that the backfill hasnât started yet.
- `IN_PROGRESS` means that the backfill is in progress. This can take up to 7 days to complete, depending on the amount of evidence data.
- `COMPLETED` means that the backfill is complete. All of your past evidence is now queryable.

error -> (string)

Represents any errors that occurred when enabling or disabling evidence finder.

deregistrationPolicy -> (structure)

The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.

deleteResources -> (string)

Specifies which Audit Manager data will be deleted when you deregister Audit Manager.

- If you set the value to `ALL` , all of your data is deleted within seven days of deregistration.
- If you set the value to `DEFAULT` , none of your data is deleted at the time of deregistration. However, keep in mind that the Audit Manager data retention policy still applies. As a result, any evidence data will be deleted two years after its creation date. Your other Audit Manager resources will continue to exist indefinitely.

defaultExportDestination -> (structure)

The default S3 destination bucket for storing evidence finder exports.

destinationType -> (string)

The destination type, such as Amazon S3.

destination -> (string)

The destination bucket where Audit Manager stores exported files.