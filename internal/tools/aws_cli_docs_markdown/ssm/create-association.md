# create-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# create-association

## Description

A State Manager association defines the state that you want to maintain on your managed nodes. For example, an association can specify that anti-virus software must be installed and running on your managed nodes, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an Amazon Web Services resource group or an Amazon Web Services autoscaling group, State Manager, a tool in Amazon Web Services Systems Manager applies the configuration when new managed nodes are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software isnât installed, then State Manager installs it. If the software is installed, but the service isnât running, then the association might instruct State Manager to start the service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateAssociation)

## Synopsis

```
create-association
--name <value>
[--document-version <value>]
[--instance-id <value>]
[--parameters <value>]
[--targets <value>]
[--schedule-expression <value>]
[--output-location <value>]
[--association-name <value>]
[--automation-target-parameter-name <value>]
[--max-errors <value>]
[--max-concurrency <value>]
[--compliance-severity <value>]
[--sync-compliance <value>]
[--apply-only-at-cron-interval | --no-apply-only-at-cron-interval]
[--calendar-names <value>]
[--target-locations <value>]
[--schedule-offset <value>]
[--duration <value>]
[--target-maps <value>]
[--tags <value>]
[--alarm-configuration <value>]
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

`--name` (string)

The name of the SSM Command document or Automation runbook that contains the configuration information for the managed node.

You can specify Amazon Web Services-predefined documents, documents you created, or a document that is shared with you from another Amazon Web Services account.

For Systems Manager documents (SSM documents) that are shared with you from other Amazon Web Services accounts, you must specify the complete SSM document ARN, in the following format:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html#id1)arn:*partition* :ssm:*region* :*account-id* :document/*document-name* ``

For example:

`arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`

For Amazon Web Services-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, `AWS-ApplyPatchBaseline` or `My-Document` .

`--document-version` (string)

The document version you want to associate with the targets. Can be a specific version or the default version.

### Warning

State Manager doesnât support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the `default` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to `default` .

`--instance-id` (string)

The managed node ID.

### Note

`InstanceId` has been deprecated. To specify a managed node ID for an association, use the `Targets` parameter. Requests that include the parameter `InstanceID` with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter `InstanceId` , you canât use the parameters `AssociationName` , `DocumentVersion` , `MaxErrors` , `MaxConcurrency` , `OutputLocation` , or `ScheduleExpression` . To use these parameters, you must use the `Targets` parameter.

`--parameters` (map)

The parameters for the runtime configuration of the document.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
```

`--targets` (list)

The targets for the association. You can target managed nodes by using tags, Amazon Web Services resource groups, all managed nodes in an Amazon Web Services account, or individual managed node IDs. You can target all managed nodes in an Amazon Web Services account by specifying the `InstanceIds` key with a value of `*` . For more information about choosing targets for an association, see [Understanding targets and rate controls in State Manager associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html) in the *Amazon Web Services Systems Manager User Guide* .

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--schedule-expression` (string)

A cron expression when the association will be applied to the targets.

`--output-location` (structure)

An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.

S3Location -> (structure)

An S3 bucket where you want to store the results of this request.

OutputS3Region -> (string)

The Amazon Web Services Region of the S3 bucket.

OutputS3BucketName -> (string)

The name of the S3 bucket.

OutputS3KeyPrefix -> (string)

The S3 bucket subfolder.

Shorthand Syntax:

```
S3Location={OutputS3Region=string,OutputS3BucketName=string,OutputS3KeyPrefix=string}
```

JSON Syntax:

```
{
  "S3Location": {
    "OutputS3Region": "string",
    "OutputS3BucketName": "string",
    "OutputS3KeyPrefix": "string"
  }
}
```

`--association-name` (string)

Specify a descriptive name for the association.

`--automation-target-parameter-name` (string)

Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in Amazon Web Services Systems Manager.

`--max-errors` (string)

The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set `MaxError` to 10%, then the system stops sending the request when the sixth error is received.

Executions that are already running an association when `MaxErrors` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there wonât be more than max-errors failed executions, set `MaxConcurrency` to 1 so that executions proceed one at a time.

`--max-concurrency` (string)

The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.

If a new managed node starts and attempts to run an association while Systems Manager is running `MaxConcurrency` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for `MaxConcurrency` .

`--compliance-severity` (string)

The severity level to assign to the association.

Possible values:

- `CRITICAL`
- `HIGH`
- `MEDIUM`
- `LOW`
- `UNSPECIFIED`

`--sync-compliance` (string)

The mode for generating association compliance. You can specify `AUTO` or `MANUAL` . In `AUTO` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is `COMPLIANT` . If the association execution doesnât run successfully, the association is `NON-COMPLIANT` .

In `MANUAL` mode, you must specify the `AssociationId` as a parameter for the  PutComplianceItems API operation. In this case, compliance data isnât managed by State Manager. It is managed by your direct call to the  PutComplianceItems API operation.

By default, all associations use `AUTO` mode.

Possible values:

- `AUTO`
- `MANUAL`

`--apply-only-at-cron-interval` | `--no-apply-only-at-cron-interval` (boolean)

By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified and when target changes are detected. Specify `true` for `ApplyOnlyAtCronInterval` if you want the association to run only according to the schedule you specified.

For more information, see [Understanding when associations are applied to resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#state-manager-about-scheduling) and [>About target updates with Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#runbook-target-updates) in the *Amazon Web Services Systems Manager User Guide* .

This parameter isnât supported for rate expressions.

`--calendar-names` (list)

The names of Amazon Resource Names (ARNs) of the Change Calendar type documents you want to gate your associations under. The associations only run when that change calendar is open. For more information, see [Amazon Web Services Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar) in the *Amazon Web Services Systems Manager User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--target-locations` (list)

A location is a combination of Amazon Web Services Regions and Amazon Web Services accounts where you want to run the association. Use this action to create an association in multiple Regions and multiple accounts.

(structure)

The combination of Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Automation execution.

Accounts -> (list)

The Amazon Web Services accounts targeted by the current Automation execution.

(string)

Regions -> (list)

The Amazon Web Services Regions targeted by the current Automation execution.

(string)

TargetLocationMaxConcurrency -> (string)

The maximum number of Amazon Web Services Regions and Amazon Web Services accounts allowed to run the Automation concurrently.

TargetLocationMaxErrors -> (string)

The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName -> (string)

The Automation execution role used by the currently running Automation. If not specified, the default value is `AWS-SystemsManager-AutomationExecutionRole` .

TargetLocationAlarmConfiguration -> (structure)

The details for the CloudWatch alarm you want to apply to an automation or command.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

IncludeChildOrganizationUnits -> (boolean)

Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is `false` .

ExcludeAccounts -> (list)

Amazon Web Services accounts or organizational units to exclude as expanded targets.

(string)

Targets -> (list)

A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for `TargetParameterName` .

This `Targets` parameter takes precedence over the `StartAutomationExecution:Targets` parameter if both are supplied.

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

TargetsMaxConcurrency -> (string)

The maximum number of targets allowed to run this task in parallel. This `TargetsMaxConcurrency` takes precedence over the `StartAutomationExecution:MaxConcurrency` parameter if both are supplied.

TargetsMaxErrors -> (string)

The maximum number of errors that are allowed before the system stops running the automation on additional targets. This `TargetsMaxErrors` parameter takes precedence over the `StartAutomationExecution:MaxErrors` parameter if both are supplied.

JSON Syntax:

```
[
  {
    "Accounts": ["string", ...],
    "Regions": ["string", ...],
    "TargetLocationMaxConcurrency": "string",
    "TargetLocationMaxErrors": "string",
    "ExecutionRoleName": "string",
    "TargetLocationAlarmConfiguration": {
      "IgnorePollAlarmFailure": true|false,
      "Alarms": [
        {
          "Name": "string"
        }
        ...
      ]
    },
    "IncludeChildOrganizationUnits": true|false,
    "ExcludeAccounts": ["string", ...],
    "Targets": [
      {
        "Key": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "TargetsMaxConcurrency": "string",
    "TargetsMaxErrors": "string"
  }
  ...
]
```

`--schedule-offset` (integer)

Number of days to wait after the scheduled day to run an association. For example, if you specified a cron schedule of `cron(0 0 ? * THU#2 *)` , you could specify an offset of 3 to run the association each Sunday after the second Thursday of the month. For more information about cron schedules for associations, see [Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the *Amazon Web Services Systems Manager User Guide* .

### Note

To use offsets, you must specify the `ApplyOnlyAtCronInterval` parameter. This option tells the system not to run an association immediately after you create it.

`--duration` (integer)

The number of hours the association can run before it is canceled. Duration applies to associations that are currently running, and any pending and in progress commands on all targets. If a target was taken offline for the association to run, it is made available again immediately, without a reboot.

The `Duration` parameter applies only when both these conditions are true:

- The association for which you specify a duration is cancelable according to the parameters of the SSM command document or Automation runbook associated with this execution.
- The command specifies the `` [ApplyOnlyAtCronInterval](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html#systemsmanager-CreateAssociation-request-ApplyOnlyAtCronInterval) `` parameter, which means that the association doesnât run immediately after it is created, but only according to the specified schedule.

`--target-maps` (list)

A key-value mapping of document parameters to target resources. Both Targets and TargetMaps canât be specified together.

(map)

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string ...
```

JSON Syntax:

```
[
  {"string": ["string", ...]
    ...}
  ...
]
```

`--tags` (list)

Adds or overwrites one or more tags for a State Manager association. *Tags* are metadata that you can assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

(structure)

Metadata that you assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Amazon Web Services Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

Key -> (string)

The name of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--alarm-configuration` (structure)

The details for the CloudWatch alarm you want to apply to an automation or command.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

Shorthand Syntax:

```
IgnorePollAlarmFailure=boolean,Alarms=[{Name=string},{Name=string}]
```

JSON Syntax:

```
{
  "IgnorePollAlarmFailure": true|false,
  "Alarms": [
    {
      "Name": "string"
    }
    ...
  ]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To associate a document using instance IDs**

This example associates a configuration document with an instance, using instance IDs.

```
aws ssm create-association \
    --instance-id "i-0cb2b964d3e14fd9f" \
    --name "AWS-UpdateSSMAgent"
```

Output:

```
{
    "AssociationDescription": {
        "Status": {
            "Date": 1487875500.33,
            "Message": "Associated with AWS-UpdateSSMAgent",
            "Name": "Associated"
        },
        "Name": "AWS-UpdateSSMAgent",
        "InstanceId": "i-0cb2b964d3e14fd9f",
        "Overview": {
            "Status": "Pending",
            "DetailedStatus": "Creating"
        },
        "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189",
        "DocumentVersion": "$DEFAULT",
        "LastUpdateAssociationDate": 1487875500.33,
        "Date": 1487875500.33,
        "Targets": [
            {
                "Values": [
                    "i-0cb2b964d3e14fd9f"
                ],
                "Key": "InstanceIds"
            }
        ]
    }
}
```

For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html) in the *AWS Systems Manager API Reference*.

**Example 2: To associate a document using targets**

This example associates a configuration document with an instance, using targets.

```
aws ssm create-association \
    --name "AWS-UpdateSSMAgent" \
    --targets "Key=instanceids,Values=i-0cb2b964d3e14fd9f"
```

Output:

```
{
    "AssociationDescription": {
        "Status": {
            "Date": 1487875500.33,
            "Message": "Associated with AWS-UpdateSSMAgent",
            "Name": "Associated"
        },
        "Name": "AWS-UpdateSSMAgent",
        "InstanceId": "i-0cb2b964d3e14fd9f",
        "Overview": {
            "Status": "Pending",
            "DetailedStatus": "Creating"
        },
        "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189",
        "DocumentVersion": "$DEFAULT",
        "LastUpdateAssociationDate": 1487875500.33,
        "Date": 1487875500.33,
        "Targets": [
            {
                "Values": [
                    "i-0cb2b964d3e14fd9f"
                ],
                "Key": "InstanceIds"
            }
        ]
    }
}
```

For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html) in the *AWS Systems Manager API Reference*.

**Example 3: To create an association that runs only once**

This example creates a new association that only runs once on the specified date and time. Associations created with a date in the past or present (by the time it is processed the date is in the past) run immediately.

```
aws ssm create-association \
    --name "AWS-UpdateSSMAgent" \
    --targets "Key=instanceids,Values=i-0cb2b964d3e14fd9f" \
    --schedule-expression "at(2020-05-14T15:55:00)"  \
    --apply-only-at-cron-interval
```

Output:

```
{
    "AssociationDescription": {
        "Status": {
            "Date": 1487875500.33,
            "Message": "Associated with AWS-UpdateSSMAgent",
            "Name": "Associated"
        },
        "Name": "AWS-UpdateSSMAgent",
        "InstanceId": "i-0cb2b964d3e14fd9f",
        "Overview": {
            "Status": "Pending",
            "DetailedStatus": "Creating"
        },
        "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189",
        "DocumentVersion": "$DEFAULT",
        "LastUpdateAssociationDate": 1487875500.33,
        "Date": 1487875500.33,
        "Targets": [
            {
                "Values": [
                    "i-0cb2b964d3e14fd9f"
                ],
                "Key": "InstanceIds"
            }
        ]
    }
}
```

For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html) in the *AWS Systems Manager API Reference* or [Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the *AWS Systems Manager User Guide*.

## Output

AssociationDescription -> (structure)

Information about the association.

Name -> (string)

The name of the SSM document.

InstanceId -> (string)

The managed node ID.

AssociationVersion -> (string)

The association version.

Date -> (timestamp)

The date when the association was made.

LastUpdateAssociationDate -> (timestamp)

The date when the association was last updated.

Status -> (structure)

The association status.

Date -> (timestamp)

The date when the status changed.

Name -> (string)

The status.

Message -> (string)

The reason for the status.

AdditionalInfo -> (string)

A user-defined string.

Overview -> (structure)

Information about the association.

Status -> (string)

The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus -> (string)

A detailed status of the association.

AssociationStatusAggregatedCount -> (map)

Returns the number of targets for the association status. For example, if you created an association with two managed nodes, and one of them was successful, this would return the count of managed nodes by status.

key -> (string)

value -> (integer)

DocumentVersion -> (string)

The document version.

AutomationTargetParameterName -> (string)

Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in Amazon Web Services Systems Manager.

Parameters -> (map)

A description of the parameters for a document.

key -> (string)

value -> (list)

(string)

AssociationId -> (string)

The association ID.

Targets -> (list)

The managed nodes targeted by the request.

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

ScheduleExpression -> (string)

A cron expression that specifies a schedule when the association runs.

OutputLocation -> (structure)

An S3 bucket where you want to store the output details of the request.

S3Location -> (structure)

An S3 bucket where you want to store the results of this request.

OutputS3Region -> (string)

The Amazon Web Services Region of the S3 bucket.

OutputS3BucketName -> (string)

The name of the S3 bucket.

OutputS3KeyPrefix -> (string)

The S3 bucket subfolder.

LastExecutionDate -> (timestamp)

The date on which the association was last run.

LastSuccessfulExecutionDate -> (timestamp)

The last date on which the association was successfully run.

AssociationName -> (string)

The association name.

MaxErrors -> (string)

The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set `MaxError` to 10%, then the system stops sending the request when the sixth error is received.

Executions that are already running an association when `MaxErrors` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there wonât be more than max-errors failed executions, set `MaxConcurrency` to 1 so that executions proceed one at a time.

MaxConcurrency -> (string)

The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.

If a new managed node starts and attempts to run an association while Systems Manager is running `MaxConcurrency` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for `MaxConcurrency` .

ComplianceSeverity -> (string)

The severity level that is assigned to the association.

SyncCompliance -> (string)

The mode for generating association compliance. You can specify `AUTO` or `MANUAL` . In `AUTO` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is `COMPLIANT` . If the association execution doesnât run successfully, the association is `NON-COMPLIANT` .

In `MANUAL` mode, you must specify the `AssociationId` as a parameter for the  PutComplianceItems API operation. In this case, compliance data isnât managed by State Manager, a tool in Amazon Web Services Systems Manager. It is managed by your direct call to the  PutComplianceItems API operation.

By default, all associations use `AUTO` mode.

ApplyOnlyAtCronInterval -> (boolean)

By default, when you create a new associations, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you donât want an association to run immediately after you create it. This parameter isnât supported for rate expressions.

CalendarNames -> (list)

The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that change calendar is open. For more information, see [Amazon Web Services Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar) in the *Amazon Web Services Systems Manager User Guide* .

(string)

TargetLocations -> (list)

The combination of Amazon Web Services Regions and Amazon Web Services accounts where you want to run the association.

(structure)

The combination of Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Automation execution.

Accounts -> (list)

The Amazon Web Services accounts targeted by the current Automation execution.

(string)

Regions -> (list)

The Amazon Web Services Regions targeted by the current Automation execution.

(string)

TargetLocationMaxConcurrency -> (string)

The maximum number of Amazon Web Services Regions and Amazon Web Services accounts allowed to run the Automation concurrently.

TargetLocationMaxErrors -> (string)

The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName -> (string)

The Automation execution role used by the currently running Automation. If not specified, the default value is `AWS-SystemsManager-AutomationExecutionRole` .

TargetLocationAlarmConfiguration -> (structure)

The details for the CloudWatch alarm you want to apply to an automation or command.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

IncludeChildOrganizationUnits -> (boolean)

Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is `false` .

ExcludeAccounts -> (list)

Amazon Web Services accounts or organizational units to exclude as expanded targets.

(string)

Targets -> (list)

A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for `TargetParameterName` .

This `Targets` parameter takes precedence over the `StartAutomationExecution:Targets` parameter if both are supplied.

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

TargetsMaxConcurrency -> (string)

The maximum number of targets allowed to run this task in parallel. This `TargetsMaxConcurrency` takes precedence over the `StartAutomationExecution:MaxConcurrency` parameter if both are supplied.

TargetsMaxErrors -> (string)

The maximum number of errors that are allowed before the system stops running the automation on additional targets. This `TargetsMaxErrors` parameter takes precedence over the `StartAutomationExecution:MaxErrors` parameter if both are supplied.

ScheduleOffset -> (integer)

Number of days to wait after the scheduled day to run an association.

Duration -> (integer)

The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.

TargetMaps -> (list)

A key-value mapping of document parameters to target resources. Both Targets and TargetMaps canât be specified together.

(map)

key -> (string)

value -> (list)

(string)

AlarmConfiguration -> (structure)

The details for the CloudWatch alarm you want to apply to an automation or command.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

TriggeredAlarms -> (list)

The CloudWatch alarm that was invoked during the association.

(structure)

The details about the state of your CloudWatch alarm.

Name -> (string)

The name of your CloudWatch alarm.

State -> (string)

The state of your CloudWatch alarm.