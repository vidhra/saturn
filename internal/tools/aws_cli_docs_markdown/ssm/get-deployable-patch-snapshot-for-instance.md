# get-deployable-patch-snapshot-for-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-deployable-patch-snapshot-for-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-deployable-patch-snapshot-for-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-deployable-patch-snapshot-for-instance

## Description

Retrieves the current snapshot for the patch baseline the managed node uses. This API is primarily used by the `AWS-RunPatchBaseline` Systems Manager document (SSM document).

### Note

If you run the command locally, such as with the Command Line Interface (CLI), the system attempts to use your local Amazon Web Services credentials and the operation fails. To avoid this, you can run the command in the Amazon Web Services Systems Manager console. Use Run Command, a tool in Amazon Web Services Systems Manager, with an SSM document that enables you to target a managed node with a script or command. For example, run the command using the `AWS-RunShellScript` document or the `AWS-RunPowerShellScript` document.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance)

## Synopsis

```
get-deployable-patch-snapshot-for-instance
--instance-id <value>
--snapshot-id <value>
[--baseline-override <value>]
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

`--instance-id` (string)

The ID of the managed node for which the appropriate patch snapshot should be retrieved.

`--snapshot-id` (string)

The snapshot ID provided by the user when running `AWS-RunPatchBaseline` .

`--baseline-override` (structure)

Defines the basic information about a patch baseline override.

OperatingSystem -> (string)

The operating system rule used by the patch baseline override.

GlobalFilters -> (structure)

A set of patch filters, typically used for approval rules.

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

A set of rules defining the approval rules for a patch baseline.

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

For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

ApprovedPatchesComplianceLevel -> (string)

Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation.

RejectedPatches -> (list)

A list of explicitly rejected patches for the baseline.

For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

RejectedPatchesAction -> (string)

The action for Patch Manager to take on patches included in the `RejectedPackages` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.

ApprovedPatchesEnableNonSecurity -> (boolean)

Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false` . Applies to Linux managed nodes only.

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

Indicates whether managed nodes for which there are available security-related patches that have not been approved by the baseline are being defined as `COMPLIANT` or `NON_COMPLIANT` . This option is specified when the `CreatePatchBaseline` or `UpdatePatchBaseline` commands are run.

Applies to Windows Server managed nodes only.

JSON Syntax:

```
{
  "OperatingSystem": "WINDOWS"|"AMAZON_LINUX"|"AMAZON_LINUX_2"|"AMAZON_LINUX_2022"|"UBUNTU"|"REDHAT_ENTERPRISE_LINUX"|"SUSE"|"CENTOS"|"ORACLE_LINUX"|"DEBIAN"|"MACOS"|"RASPBIAN"|"ROCKY_LINUX"|"ALMA_LINUX"|"AMAZON_LINUX_2023",
  "GlobalFilters": {
    "PatchFilters": [
      {
        "Key": "ARCH"|"ADVISORY_ID"|"BUGZILLA_ID"|"PATCH_SET"|"PRODUCT"|"PRODUCT_FAMILY"|"CLASSIFICATION"|"CVE_ID"|"EPOCH"|"MSRC_SEVERITY"|"NAME"|"PATCH_ID"|"SECTION"|"PRIORITY"|"REPOSITORY"|"RELEASE"|"SEVERITY"|"SECURITY"|"VERSION",
        "Values": ["string", ...]
      }
      ...
    ]
  },
  "ApprovalRules": {
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
  },
  "ApprovedPatches": ["string", ...],
  "ApprovedPatchesComplianceLevel": "CRITICAL"|"HIGH"|"MEDIUM"|"LOW"|"INFORMATIONAL"|"UNSPECIFIED",
  "RejectedPatches": ["string", ...],
  "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY"|"BLOCK",
  "ApprovedPatchesEnableNonSecurity": true|false,
  "Sources": [
    {
      "Name": "string",
      "Products": ["string", ...],
      "Configuration": "string"
    }
    ...
  ],
  "AvailableSecurityUpdatesComplianceStatus": "COMPLIANT"|"NON_COMPLIANT"
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

**To retrieve the current snapshot for the patch baseline an instance uses**

The following `get-deployable-patch-snapshot-for-instance` example retrieves details for the current snapshot for the specified patch baseline used by an instance. This command must be run from the instance using the instance credentials. To ensure it uses the instance credentials, run `aws configure` and specify only the Region of your instance. Leave the `Access Key` and `Secret Key` fields empty.

Tip: Use `uuidgen` to generate a `snapshot-id`.

```
aws ssm get-deployable-patch-snapshot-for-instance \
    --instance-id "i-1234567890abcdef0" \
    --snapshot-id "521c3536-930c-4aa9-950e-01234567abcd"
```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0",
    "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd",
    "Product": "AmazonLinux2018.03",
    "SnapshotDownloadUrl": "https://patch-baseline-snapshot-us-east-1.s3.amazonaws.com/ed85194ef27214f5984f28b4d664d14f7313568fea7d4b6ac6c10ad1f729d7e7-773304212436/AMAZON_LINUX-521c3536-930c-4aa9-950e-01234567abcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190215T164031Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJ5C56P35AEBRX2QQ%2F20190215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=efaaaf6e3878e77f48a6697e015efdbda9c426b09c5822055075c062f6ad2149"
}
```

For more information, see [Parameter name: Snapshot ID](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html#patch-manager-about-aws-runpatchbaseline-parameters-snapshot-id) in the *AWS Systems Manager User Guide*.

## Output

InstanceId -> (string)

The managed node ID.

SnapshotId -> (string)

The user-defined snapshot ID.

SnapshotDownloadUrl -> (string)

A pre-signed Amazon Simple Storage Service (Amazon S3) URL that can be used to download the patch snapshot.

Product -> (string)

Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the managed node for the specified patch snapshot.