# get-patch-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-patch-baseline

## Description

Retrieves information about a patch baseline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetPatchBaseline)

## Synopsis

```
get-patch-baseline
--baseline-id <value>
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

`--baseline-id` (string)

The ID of the patch baseline to retrieve.

### Note

To retrieve information about an Amazon Web Services managed patch baseline, specify the full Amazon Resource Name (ARN) of the baseline. For example, for the baseline `AWS-AmazonLinuxDefaultPatchBaseline` , specify `arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0e392de35e7c563b7` instead of `pb-0e392de35e7c563b7` .

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

**To display a patch baseline**

The following `get-patch-baseline` example retrieves the details for the specified patch baseline.

```
aws ssm get-patch-baseline \
    --baseline-id "pb-0123456789abcdef0"
```

Output:

```
{
    "BaselineId": "pb-0123456789abcdef0",
    "Name": "WindowsPatching",
    "OperatingSystem": "WINDOWS",
    "GlobalFilters": {
        "PatchFilters": []
    },
    "ApprovalRules": {
        "PatchRules": [
            {
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Key": "PRODUCT",
                            "Values": [
                                "WindowsServer2016"
                            ]
                        }
                    ]
                },
                "ComplianceLevel": "CRITICAL",
                "ApproveAfterDays": 0,
                "EnableNonSecurity": false
            }
        ]
    },
    "ApprovedPatches": [],
    "ApprovedPatchesComplianceLevel": "UNSPECIFIED",
    "ApprovedPatchesEnableNonSecurity": false,
    "RejectedPatches": [],
    "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY",
    "PatchGroups": [
        "QA",
        "DEV"
    ],
    "CreatedDate": 1550244180.465,
    "ModifiedDate": 1550244180.465,
    "Description": "Patches for Windows Servers",
    "Sources": []
}
```

For more information, see [About Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-baselines.html) in the *AWS Systems Manager User Guide*.

## Output

BaselineId -> (string)

The ID of the retrieved patch baseline.

Name -> (string)

The name of the patch baseline.

OperatingSystem -> (string)

Returns the operating system specified for the patch baseline.

GlobalFilters -> (structure)

A set of global filters used to exclude patches from the baseline.

PatchFilters -> (list)

The set of patch filters that make up the group.

(structure)

Defines which patches should be included in a patch baseline.

A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for `WINDOWS` are `PATCH_SET` , `PRODUCT` , `PRODUCT_FAMILY` , `CLASSIFICATION` , and `MSRC_SEVERITY` .

The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is `PRODUCT` and the filter values are `["Office 2013", "Office 2016"]` , then the filter accepts all patches where product name is either âOffice 2013â or âOffice 2016â. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.

You can view lists of valid values for the patch properties by running the `DescribePatchProperties` command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key -> (string)

The key for the filter.

Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values -> (list)

The value for the filter key.

Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string)

ApprovalRules -> (structure)

A set of rules used to include patches in the baseline.

PatchRules -> (list)

The rules that make up the rule group.

(structure)

Defines an approval rule for a patch baseline.

PatchFilterGroup -> (structure)

The patch filter group that defines the criteria for the rule.

PatchFilters -> (list)

The set of patch filters that make up the group.

(structure)

Defines which patches should be included in a patch baseline.

A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for `WINDOWS` are `PATCH_SET` , `PRODUCT` , `PRODUCT_FAMILY` , `CLASSIFICATION` , and `MSRC_SEVERITY` .

The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is `PRODUCT` and the filter values are `["Office 2013", "Office 2016"]` , then the filter accepts all patches where product name is either âOffice 2013â or âOffice 2016â. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.

You can view lists of valid values for the patch properties by running the `DescribePatchProperties` command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key -> (string)

The key for the filter.

Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values -> (list)

The value for the filter key.

Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string)

ComplianceLevel -> (string)

A compliance severity level for all approved patches in a patch baseline.

ApproveAfterDays -> (integer)

The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of `7` means that patches are approved seven days after they are released.

This parameter is marked as `Required: No` , but your request must include a value for either `ApproveAfterDays` or `ApproveUntilDate` .

Not supported for Debian Server or Ubuntu Server.

### Warning

Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the *Amazon Web Services Systems Manager User Guide* .

ApproveUntilDate -> (string)

The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically.

Enter dates in the format `YYYY-MM-DD` . For example, `2024-12-31` .

This parameter is marked as `Required: No` , but your request must include a value for either `ApproveUntilDate` or `ApproveAfterDays` .

Not supported for Debian Server or Ubuntu Server.

### Warning

Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the *Amazon Web Services Systems Manager User Guide* .

EnableNonSecurity -> (boolean)

For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is `false` . Applies to Linux managed nodes only.

ApprovedPatches -> (list)

A list of explicitly approved patches for the baseline.

(string)

ApprovedPatchesComplianceLevel -> (string)

Returns the specified compliance severity level for approved patches in the patch baseline.

ApprovedPatchesEnableNonSecurity -> (boolean)

Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false` . Applies to Linux managed nodes only.

RejectedPatches -> (list)

A list of explicitly rejected patches for the baseline.

(string)

RejectedPatchesAction -> (string)

The action specified to take on patches included in the `RejectedPatches` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.

PatchGroups -> (list)

Patch groups included in the patch baseline.

(string)

CreatedDate -> (timestamp)

The date the patch baseline was created.

ModifiedDate -> (timestamp)

The date the patch baseline was last modified.

Description -> (string)

A description of the patch baseline.

Sources -> (list)

Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.

(structure)

Information about the patches to use to update the managed nodes, including target operating systems and source repository. Applies to Linux managed nodes only.

Name -> (string)

The name specified to identify the patch source.

Products -> (list)

The specific operating system versions a patch repository applies to, such as âUbuntu16.04â, âAmazonLinux2016.09â, âRedhatEnterpriseLinux7.2â or âSuse12.7â. For lists of supported product values, see  PatchFilter .

(string)

Configuration -> (string)

The value of the yum repo configuration. For example:

`[main]`

`name=MyCustomRepository`

`baseurl=https://my-custom-repository`

`enabled=1`

### Note

For information about other options available for your yum repository configuration, see [dnf.conf(5)](https://man7.org/linux/man-pages/man5/dnf.conf.5.html) .

AvailableSecurityUpdatesComplianceStatus -> (string)

Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the `CreatePatchBaseline` or `UpdatePatchBaseline` commands are run.

Applies to Windows Server managed nodes only.