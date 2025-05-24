# describe-effective-patches-for-patch-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-patches-for-patch-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-patches-for-patch-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-effective-patches-for-patch-baseline

## Description

Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Applies to patch baselines for Windows only.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)

`describe-effective-patches-for-patch-baseline` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `EffectivePatches`

## Synopsis

```
describe-effective-patches-for-patch-baseline
--baseline-id <value>
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

`--baseline-id` (string)

The ID of the patch baseline to retrieve the effective patches for.

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

**Example 1: To get all patches defined by a custom patch baseline**

The following `describe-effective-patches-for-patch-baseline` example returns the patches defined by a custom patch baseline in the current AWS account. Note that for a custom baseline, only the ID is required for `--baseline-id`.

```
aws ssm describe-effective-patches-for-patch-baseline \
    --baseline-id "pb-08b654cf9b9681f04"
```

Output:

```
{
    "EffectivePatches": [
        {
            "Patch": {
                "Id": "fe6bd8c2-3752-4c8b-ab3e-1a7ed08767ba",
                "ReleaseDate": 1544047205.0,
                "Title": "2018-11 Update for Windows Server 2019 for x64-based Systems (KB4470788)",
                "Description": "Install this update to resolve issues in Windows. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article for more information. After you install this item, you may have to restart your computer.",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/4470788",
                "Vendor": "Microsoft",
                "ProductFamily": "Windows",
                "Product": "WindowsServer2019",
                "Classification": "SecurityUpdates",
                "MsrcSeverity": "Critical",
                "KbNumber": "KB4470788",
                "MsrcNumber": "",
                "Language": "All"
            },
            "PatchStatus": {
                "DeploymentStatus": "APPROVED",
                "ComplianceLevel": "CRITICAL",
                "ApprovalDate": 1544047205.0
            }
        },
        {
            "Patch": {
                "Id": "915a6b1a-f556-4d83-8f50-b2e75a9a7e58",
                "ReleaseDate": 1549994400.0,
                "Title": "2019-02 Cumulative Update for .NET Framework 3.5 and 4.7.2 for Windows Server 2019 for x64 (KB4483452)",
                "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/4483452",
                "Vendor": "Microsoft",
                "ProductFamily": "Windows",
                "Product": "WindowsServer2019",
                "Classification": "SecurityUpdates",
                "MsrcSeverity": "Important",
                "KbNumber": "KB4483452",
                "MsrcNumber": "",
                "Language": "All"
            },
            "PatchStatus": {
                "DeploymentStatus": "APPROVED",
                "ComplianceLevel": "CRITICAL",
                "ApprovalDate": 1549994400.0
            }
        },
        ...
    ],
    "NextToken": "--token string truncated--"
}
```

**Example 2: To get all patches defined by an AWS managed patch baseline**

The following `describe-effective-patches-for-patch-baseline` example returns the patches defined by an AWS managed patch baseline. Note that for an AWS managed baseline, the complete baseline ARN is required for `--baseline-id`

```
aws ssm describe-effective-patches-for-patch-baseline \
    --baseline-id "arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-020d361a05defe4ed"
```

See example 1 for sample output.

For more information, see [How Security Patches Are Selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works-selection.html) in the *AWS Systems Manager User Guide*.

## Output

EffectivePatches -> (list)

An array of patches and patch status.

(structure)

The `EffectivePatch` structure defines metadata about a patch along with the approval state of the patch in a particular patch baseline. The approval state includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

Patch -> (structure)

Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.

Id -> (string)

The ID of the patch. Applies to Windows patches only.

### Note

This ID isnât the same as the Microsoft Knowledge Base ID.

ReleaseDate -> (timestamp)

The date the patch was released.

Title -> (string)

The title of the patch.

Description -> (string)

The description of the patch.

ContentUrl -> (string)

The URL where more information can be obtained about the patch.

Vendor -> (string)

The name of the vendor providing the patch.

ProductFamily -> (string)

The product family the patch is applicable for. For example, `Windows` or `Amazon Linux 2` .

Product -> (string)

The specific product the patch is applicable for. For example, `WindowsServer2016` or `AmazonLinux2018.03` .

Classification -> (string)

The classification of the patch. For example, `SecurityUpdates` , `Updates` , or `CriticalUpdates` .

MsrcSeverity -> (string)

The severity of the patch, such as `Critical` , `Important` , or `Moderate` . Applies to Windows patches only.

KbNumber -> (string)

The Microsoft Knowledge Base ID of the patch. Applies to Windows patches only.

MsrcNumber -> (string)

The ID of the Microsoft Security Response Center (MSRC) bulletin the patch is related to. For example, `MS14-045` . Applies to Windows patches only.

Language -> (string)

The language of the patch if itâs language-specific.

AdvisoryIds -> (list)

The Advisory ID of the patch. For example, `RHSA-2020:3779` . Applies to Linux-based managed nodes only.

(string)

BugzillaIds -> (list)

The Bugzilla ID of the patch. For example, `1600646` . Applies to Linux-based managed nodes only.

(string)

CVEIds -> (list)

The Common Vulnerabilities and Exposures (CVE) ID of the patch. For example, `CVE-2011-3192` . Applies to Linux-based managed nodes only.

(string)

Name -> (string)

The name of the patch. Applies to Linux-based managed nodes only.

Epoch -> (integer)

The epoch of the patch. For example in `pkg-example-EE-20180914-2.2.amzn1.noarch` , the epoch value is `20180914-2` . Applies to Linux-based managed nodes only.

Version -> (string)

The version number of the patch. For example, in `example-pkg-1.710.10-2.7.abcd.x86_64` , the version number is indicated by `-1` . Applies to Linux-based managed nodes only.

Release -> (string)

The particular release of a patch. For example, in `pkg-example-EE-20180914-2.2.amzn1.noarch` , the release is `2.amaz1` . Applies to Linux-based managed nodes only.

Arch -> (string)

The architecture of the patch. For example, in `example-pkg-0.710.10-2.7.abcd.x86_64` , the architecture is indicated by `x86_64` . Applies to Linux-based managed nodes only.

Severity -> (string)

The severity level of the patch. For example, `CRITICAL` or `MODERATE` .

Repository -> (string)

The source patch repository for the operating system and version, such as `trusty-security` for Ubuntu Server 14.04 LTE and `focal-security` for Ubuntu Server 20.04 LTE. Applies to Linux-based managed nodes only.

PatchStatus -> (structure)

The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

DeploymentStatus -> (string)

The approval status of a patch.

ComplianceLevel -> (string)

The compliance severity level for a patch.

ApprovalDate -> (timestamp)

The date the patch was approved (or will be approved if the status is `PENDING_APPROVAL` ).

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.