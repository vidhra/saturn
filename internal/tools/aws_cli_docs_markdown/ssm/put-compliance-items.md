# put-compliance-itemsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# put-compliance-items

## Description

Registers a compliance type and other compliance details on a designated resource. This operation lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.

ComplianceType can be one of the following:

- ExecutionId: The execution ID when the patch, association, or custom compliance item was applied.
- ExecutionType: Specify patch, association, or Custom:`string` .
- ExecutionTime. The time the patch, association, or custom compliance item was applied to the managed node.
- Id: The patch, association, or custom compliance ID.
- Title: A title.
- Status: The status of the compliance item. For example, `approved` for patches, or `Failed` for associations.
- Severity: A patch severity. For example, `Critical` .
- DocumentName: An SSM document name. For example, `AWS-RunPatchBaseline` .
- DocumentVersion: An SSM document version number. For example, 4.
- Classification: A patch classification. For example, `security updates` .
- PatchBaselineId: A patch baseline ID.
- PatchSeverity: A patch severity. For example, `Critical` .
- PatchState: A patch state. For example, `InstancesWithFailedPatches` .
- PatchGroup: The name of a patch group.
- InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutComplianceItems)

## Synopsis

```
put-compliance-items
--resource-id <value>
--resource-type <value>
--compliance-type <value>
--execution-summary <value>
--items <value>
[--item-content-hash <value>]
[--upload-type <value>]
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

`--resource-id` (string)

Specify an ID for this resource. For a managed node, this is the node ID.

`--resource-type` (string)

Specify the type of resource. `ManagedInstance` is currently the only supported resource type.

`--compliance-type` (string)

Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:`string` .

`--execution-summary` (structure)

A summary of the call execution that includes an execution ID, the type of execution (for example, `Command` ), and the date/time of the execution using a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

ExecutionTime -> (timestamp)

The time the execution ran as a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

ExecutionId -> (string)

An ID created by the system when `PutComplianceItems` was called. For example, `CommandID` is a valid execution ID. You can use this ID in subsequent calls.

ExecutionType -> (string)

The type of execution. For example, `Command` is a valid execution type.

Shorthand Syntax:

```
ExecutionTime=timestamp,ExecutionId=string,ExecutionType=string
```

JSON Syntax:

```
{
  "ExecutionTime": timestamp,
  "ExecutionId": "string",
  "ExecutionType": "string"
}
```

`--items` (list)

Information about the compliance as defined by the resource type. For example, for a patch compliance type, `Items` includes information about the PatchSeverity, Classification, and so on.

(structure)

Information about a compliance item.

Id -> (string)

The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.

Title -> (string)

The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.

Severity -> (string)

The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.

Status -> (string)

The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.

Details -> (map)

A âKeyâ: âValueâ tag combination for the compliance item.

key -> (string)

value -> (string)

Shorthand Syntax:

```
Id=string,Title=string,Severity=string,Status=string,Details={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "Id": "string",
    "Title": "string",
    "Severity": "CRITICAL"|"HIGH"|"MEDIUM"|"LOW"|"INFORMATIONAL"|"UNSPECIFIED",
    "Status": "COMPLIANT"|"NON_COMPLIANT",
    "Details": {"string": "string"
      ...}
  }
  ...
]
```

`--item-content-hash` (string)

MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.

`--upload-type` (string)

The mode for uploading compliance items. You can specify `COMPLETE` or `PARTIAL` . In `COMPLETE` mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.

In `PARTIAL` mode, the system overwrites compliance information for a specific association. The association must be configured with `SyncCompliance` set to `MANUAL` . By default, all requests use `COMPLETE` mode.

### Note

This attribute is only valid for association compliance.

Possible values:

- `COMPLETE`
- `PARTIAL`

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

**To register a compliance type and compliance details to a designated instance**

This example registers the compliance type `Custom:AVCheck` to the specified managed instance. There is no output if the command succeeds.

Command:

```
aws ssm put-compliance-items --resource-id "i-1234567890abcdef0" --resource-type "ManagedInstance" --compliance-type "Custom:AVCheck" --execution-summary "ExecutionTime=2019-02-18T16:00:00Z" --items "Id=Version2.0,Title=ScanHost,Severity=CRITICAL,Status=COMPLIANT"
```

## Output

None