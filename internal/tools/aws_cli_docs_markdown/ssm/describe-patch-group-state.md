# describe-patch-group-stateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-group-state.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-group-state.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-patch-group-state

## Description

Returns high-level aggregated patch compliance state information for a patch group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroupState)

## Synopsis

```
describe-patch-group-state
--patch-group <value>
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

`--patch-group` (string)

The name of the patch group whose patch snapshot should be retrieved.

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

**To get the state of a patch group**

The following `describe-patch-group-state` example retrieves the high-level patch compliance summary for a patch group.

```
aws ssm describe-patch-group-state \
    --patch-group "Production"
```

Output:

```
{
    "Instances": 21,
    "InstancesWithCriticalNonCompliantPatches": 1,
    "InstancesWithFailedPatches": 2,
    "InstancesWithInstalledOtherPatches": 3,
    "InstancesWithInstalledPatches": 21,
    "InstancesWithInstalledPendingRebootPatches": 2,
    "InstancesWithInstalledRejectedPatches": 1,
    "InstancesWithMissingPatches": 3,
    "InstancesWithNotApplicablePatches": 4,
    "InstancesWithOtherNonCompliantPatches": 1,
    "InstancesWithSecurityNonCompliantPatches": 1,
    "InstancesWithUnreportedNotApplicablePatches": 2
}
```

For more information, see About patch groups <[https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html)>__ and [Understanding patch compliance state values](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance-states.html) in the *AWS Systems Manager User Guide*.

## Output

Instances -> (integer)

The number of managed nodes in the patch group.

InstancesWithInstalledPatches -> (integer)

The number of managed nodes with installed patches.

InstancesWithInstalledOtherPatches -> (integer)

The number of managed nodes with patches installed that arenât defined in the patch baseline.

InstancesWithInstalledPendingRebootPatches -> (integer)

The number of managed nodes with patches installed by Patch Manager that havenât been rebooted after the patch installation. The status of these managed nodes is `NON_COMPLIANT` .

InstancesWithInstalledRejectedPatches -> (integer)

The number of managed nodes with patches installed that are specified in a `RejectedPatches` list. Patches with a status of `INSTALLED_REJECTED` were typically installed before they were added to a `RejectedPatches` list.

### Note

If `ALLOW_AS_DEPENDENCY` is the specified option for `RejectedPatchesAction` , the value of `InstancesWithInstalledRejectedPatches` will always be `0` (zero).

InstancesWithMissingPatches -> (integer)

The number of managed nodes with missing patches from the patch baseline.

InstancesWithFailedPatches -> (integer)

The number of managed nodes with patches from the patch baseline that failed to install.

InstancesWithNotApplicablePatches -> (integer)

The number of managed nodes with patches that arenât applicable.

InstancesWithUnreportedNotApplicablePatches -> (integer)

The number of managed nodes with `NotApplicable` patches beyond the supported limit, which arenât reported by name to Inventory. Inventory is a tool in Amazon Web Services Systems Manager.

InstancesWithCriticalNonCompliantPatches -> (integer)

The number of managed nodes where patches that are specified as `Critical` for compliance reporting in the patch baseline arenât installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT` .

InstancesWithSecurityNonCompliantPatches -> (integer)

The number of managed nodes where patches that are specified as `Security` in a patch advisory arenât installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT` .

InstancesWithOtherNonCompliantPatches -> (integer)

The number of managed nodes with patches installed that are specified as other than `Critical` or `Security` but arenât compliant with the patch baseline. The status of these managed nodes is `NON_COMPLIANT` .

InstancesWithAvailableSecurityUpdates -> (integer)

The number of managed nodes for which security-related patches are available but not approved because because they didnât meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.

Applies to Windows Server managed nodes only.