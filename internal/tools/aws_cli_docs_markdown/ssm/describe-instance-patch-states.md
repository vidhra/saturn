# describe-instance-patch-statesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-instance-patch-states

## Description

Retrieves the high-level patch state of one or more managed nodes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStates)

`describe-instance-patch-states` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InstancePatchStates`

## Synopsis

```
describe-instance-patch-states
--instance-ids <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--instance-ids` (list)

The ID of the managed node for which patch state information should be retrieved.

(string)

Syntax:

```
"string" "string" ...
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To get the patch summary states for instances**

This `describe-instance-patch-states` example gets the patch summary states for an instance.

```
aws ssm describe-instance-patch-states \
    --instance-ids "i-1234567890abcdef0"
```

Output:

```
{
    "InstancePatchStates": [
        {
            "InstanceId": "i-1234567890abcdef0",
            "PatchGroup": "my-patch-group",
            "BaselineId": "pb-0713accee01234567",
            "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd",
            "CriticalNonCompliantCount": 2,
            "SecurityNonCompliantCount": 2,
            "OtherNonCompliantCount": 1,
            "InstalledCount": 123,
            "InstalledOtherCount": 334,
            "InstalledPendingRebootCount": 0,
            "InstalledRejectedCount": 0,
            "MissingCount": 1,
            "FailedCount": 2,
            "UnreportedNotApplicableCount": 11,
            "NotApplicableCount": 2063,
            "OperationStartTime": "2021-05-03T11:00:56-07:00",
            "OperationEndTime": "2021-05-03T11:01:09-07:00",
            "Operation": "Scan",
            "LastNoRebootInstallOperationTime": "2020-06-14T12:17:41-07:00",
            "RebootOption": "RebootIfNeeded"
        }
    ]
}
```

For more information, see [About Patch Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance.html) in the *AWS Systems Manager User Guide*.

## Output

InstancePatchStates -> (list)

The high-level patch state for the requested managed nodes.

(structure)

Defines the high-level patch compliance state for a managed node, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the managed node.

InstanceId -> (string)

The ID of the managed node the high-level patch compliance information was collected for.

PatchGroup -> (string)

The name of the patch group the managed node belongs to.

BaselineId -> (string)

The ID of the patch baseline used to patch the managed node.

SnapshotId -> (string)

The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.

InstallOverrideList -> (string)

An https URL or an Amazon Simple Storage Service (Amazon S3) path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an S3 bucket in YAML format and specify in the SSM document `AWS-RunPatchBaseline` , overrides the patches specified by the default patch baseline.

For more information about the `InstallOverrideList` parameter, see SSM Command document for patching: ``AWS-RunPatchBaseline` [https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline).html`__ in the *Amazon Web Services Systems Manager User Guide* .

OwnerInformation -> (string)

Placeholder information. This field will always be empty in the current release of the service.

InstalledCount -> (integer)

The number of patches from the patch baseline that are installed on the managed node.

InstalledOtherCount -> (integer)

The number of patches not specified in the patch baseline that are installed on the managed node.

InstalledPendingRebootCount -> (integer)

The number of patches installed by Patch Manager since the last time the managed node was rebooted.

InstalledRejectedCount -> (integer)

The number of patches installed on a managed node that are specified in a `RejectedPatches` list. Patches with a status of `InstalledRejected` were typically installed before they were added to a `RejectedPatches` list.

### Note

If `ALLOW_AS_DEPENDENCY` is the specified option for `RejectedPatchesAction` , the value of `InstalledRejectedCount` will always be `0` (zero).

MissingCount -> (integer)

The number of patches from the patch baseline that are applicable for the managed node but arenât currently installed.

FailedCount -> (integer)

The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.

UnreportedNotApplicableCount -> (integer)

The number of patches beyond the supported limit of `NotApplicableCount` that arenât reported by name to Inventory. Inventory is a tool in Amazon Web Services Systems Manager.

NotApplicableCount -> (integer)

The number of patches from the patch baseline that arenât applicable for the managed node and therefore arenât installed on the node. This number may be truncated if the list of patch names is very large. The number of patches beyond this limit are reported in `UnreportedNotApplicableCount` .

AvailableSecurityUpdateCount -> (integer)

The number of security-related patches that are available but not approved because they didnât meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.

Applies to Windows Server managed nodes only.

OperationStartTime -> (timestamp)

The time the most recent patching operation was started on the managed node.

OperationEndTime -> (timestamp)

The time the most recent patching operation completed on the managed node.

Operation -> (string)

The type of patching operation that was performed: or

- `SCAN` assesses the patch compliance state.
- `INSTALL` installs missing patches.

LastNoRebootInstallOperationTime -> (timestamp)

The time of the last attempt to patch the managed node with `NoReboot` specified as the reboot option.

RebootOption -> (string)

Indicates the reboot option specified in the patch baseline.

### Note

Reboot options apply to `Install` operations only. Reboots arenât attempted for Patch Manager `Scan` operations.

- `RebootIfNeeded` : Patch Manager tries to reboot the managed node if it installed any patches, or if any patches are detected with a status of `InstalledPendingReboot` .
- `NoReboot` : Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of `InstalledPendingReboot` . These patches might not be in effect until a reboot is performed.

CriticalNonCompliantCount -> (integer)

The number of patches per node that are specified as `Critical` for compliance reporting in the patch baseline arenât installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT` .

SecurityNonCompliantCount -> (integer)

The number of patches per node that are specified as `Security` in a patch advisory arenât installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT` .

OtherNonCompliantCount -> (integer)

The number of patches per node that are specified as other than `Critical` or `Security` but arenât compliant with the patch baseline. The status of these managed nodes is `NON_COMPLIANT` .

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.