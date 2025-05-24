# update-patch-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-patch-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-patch-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# update-patch-baseline

## Description

Modifies an existing patch baseline. Fields not specified in the request are left unchanged.

### Note

For information about valid key-value pairs in `PatchFilters` for each supported operating system type, see  PatchFilter .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdatePatchBaseline)

## Synopsis

```
update-patch-baseline
--baseline-id <value>
[--name <value>]
[--global-filters <value>]
[--approval-rules <value>]
[--approved-patches <value>]
[--approved-patches-compliance-level <value>]
[--approved-patches-enable-non-security | --no-approved-patches-enable-non-security]
[--rejected-patches <value>]
[--rejected-patches-action <value>]
[--description <value>]
[--sources <value>]
[--available-security-updates-compliance-status <value>]
[--replace | --no-replace]
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

The ID of the patch baseline to update.

`--name` (string)

The name of the patch baseline.

`--global-filters` (structure)

A set of global filters used to include patches in the baseline.

### Warning

The `GlobalFilters` parameter can be configured only by using the CLI or an Amazon Web Services SDK. It canât be configured from the Patch Manager console, and its value isnât displayed in the console.

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

JSON Syntax:

```
{
  "PatchFilters": [
    {
      "Key": "ARCH"|"ADVISORY_ID"|"BUGZILLA_ID"|"PATCH_SET"|"PRODUCT"|"PRODUCT_FAMILY"|"CLASSIFICATION"|"CVE_ID"|"EPOCH"|"MSRC_SEVERITY"|"NAME"|"PATCH_ID"|"SECTION"|"PRIORITY"|"REPOSITORY"|"RELEASE"|"SEVERITY"|"SECURITY"|"VERSION",
      "Values": ["string", ...]
    }
    ...
  ]
}
```

`--approval-rules` (structure)

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

JSON Syntax:

```
{
  "PatchRules": [
    {
      "PatchFilterGroup": {
        "PatchFilters": [
          {
            "Key": "ARCH"|"ADVISORY_ID"|"BUGZILLA_ID"|"PATCH_SET"|"PRODUCT"|"PRODUCT_FAMILY"|"CLASSIFICATION"|"CVE_ID"|"EPOCH"|"MSRC_SEVERITY"|"NAME"|"PATCH_ID"|"SECTION"|"PRIORITY"|"REPOSITORY"|"RELEASE"|"SEVERITY"|"SECURITY"|"VERSION",
            "Values": ["string", ...]
          }
          ...
        ]
      },
      "ComplianceLevel": "CRITICAL"|"HIGH"|"MEDIUM"|"LOW"|"INFORMATIONAL"|"UNSPECIFIED",
      "ApproveAfterDays": integer,
      "ApproveUntilDate": "string",
      "EnableNonSecurity": true|false
    }
    ...
  ]
}
```

`--approved-patches` (list)

A list of explicitly approved patches for the baseline.

For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--approved-patches-compliance-level` (string)

Assigns a new compliance severity level to an existing patch baseline.

Possible values:

- `CRITICAL`
- `HIGH`
- `MEDIUM`
- `LOW`
- `INFORMATIONAL`
- `UNSPECIFIED`

`--approved-patches-enable-non-security` | `--no-approved-patches-enable-non-security` (boolean)

Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false` . Applies to Linux managed nodes only.

`--rejected-patches` (list)

A list of explicitly rejected patches for the baseline.

For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--rejected-patches-action` (string)

The action for Patch Manager to take on patches included in the `RejectedPackages` list.

ALLOW_AS_DEPENDENCY

**Linux and macOS** : A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as `INSTALLED_OTHER` . This is the default action if no option is specified.

**Windows Server** : Windows Server doesnât support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as `INSTALLED_OTHER` . Any package not already installed on the node is skipped. This is the default action if no option is specified.

BLOCK

**All OSs** : Packages in the rejected patches list, and packages that include them as dependencies, arenât installed by Patch Manager under any circumstances. If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, itâs considered noncompliant with the patch baseline and its status is reported as `INSTALLED_REJECTED` .

Possible values:

- `ALLOW_AS_DEPENDENCY`
- `BLOCK`

`--description` (string)

A description of the patch baseline.

`--sources` (list)

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

Shorthand Syntax:

```
Name=string,Products=string,string,Configuration=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Products": ["string", ...],
    "Configuration": "string"
  }
  ...
]
```

`--available-security-updates-compliance-status` (string)

Indicates the status to be assigned to security patches that are available but not approved because they donât meet the installation criteria specified in the patch baseline.

Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.

Supported for Windows Server managed nodes only.

Possible values:

- `COMPLIANT`
- `NON_COMPLIANT`

`--replace` | `--no-replace` (boolean)

If True, then all fields that are required by the  CreatePatchBaseline operation are also required for this API request. Optional fields that arenât specified are set to null.

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

**Example 1: To update a patch baseline**

The following `update-patch-baseline` example adds the specified two patches as rejected and one patch as approved to the specified patch baseline.

```
aws ssm update-patch-baseline \
        --baseline-id "pb-0123456789abcdef0" \
        --rejected-patches "KB2032276" "MS10-048" \
        --approved-patches "KB2124261"
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
    "ApprovedPatches": [
        "KB2124261"
    ],
    "ApprovedPatchesComplianceLevel": "UNSPECIFIED",
    "ApprovedPatchesEnableNonSecurity": false,
    "RejectedPatches": [
        "KB2032276",
        "MS10-048"
    ],
    "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY",
    "CreatedDate": 1550244180.465,
    "ModifiedDate": 1550244180.465,
    "Description": "Patches for Windows Servers",
    "Sources": []
}
```

**Example 2: To rename a patch baseline**

The following `update-patch-baseline` example renames the specified patch baseline.

```
aws ssm update-patch-baseline \
    --baseline-id "pb-0713accee01234567" \
    --name "Windows-Server-2012-R2-Important-and-Critical-Security-Updates"
```

For more information, see Update or Delete a Patch Baseline <[https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-baseline-update-or-delete.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-baseline-update-or-delete.html)>`__ in the *AWS Systems Manager User Guide*.

## Output

BaselineId -> (string)

The ID of the deleted patch baseline.

Name -> (string)

The name of the patch baseline.

OperatingSystem -> (string)

The operating system rule used by the updated patch baseline.

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

The compliance severity level assigned to the patch baseline after the update completed.

ApprovedPatchesEnableNonSecurity -> (boolean)

Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false` . Applies to Linux managed nodes only.

RejectedPatches -> (list)

A list of explicitly rejected patches for the baseline.

(string)

RejectedPatchesAction -> (string)

The action specified to take on patches included in the `RejectedPatches` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.

CreatedDate -> (timestamp)

The date when the patch baseline was created.

ModifiedDate -> (timestamp)

The date when the patch baseline was last modified.

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