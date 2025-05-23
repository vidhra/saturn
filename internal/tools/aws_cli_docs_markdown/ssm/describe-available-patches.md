# describe-available-patchesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-available-patches

## Description

Lists all patches eligible to be included in a patch baseline.

### Note

Currently, `DescribeAvailablePatches` supports only the Amazon Linux 1, Amazon Linux 2, and Windows Server operating systems.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAvailablePatches)

`describe-available-patches` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Patches`

## Synopsis

```
describe-available-patches
[--filters <value>]
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

`--filters` (list)

Each element in the array is a structure containing a key-value pair.

**Windows Server**

Supported keys for Windows Server managed node patches include the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id1)`PATCH_SET` **   Sample values: `OS` | `APPLICATION`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id3)`PRODUCT` **   Sample values: `WindowsServer2012` | `Office 2010` | `MicrosoftDefenderAntivirus`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id5)`PRODUCT_FAMILY` **   Sample values: `Windows` | `Office`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id7)`MSRC_SEVERITY` **   Sample values: `ServicePacks` | `Important` | `Moderate`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id9)`CLASSIFICATION` **   Sample values: `ServicePacks` | `SecurityUpdates` | `DefinitionUpdates`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id11)`PATCH_ID` **   Sample values: `KB123456` | `KB4516046`

**Linux**

### Warning

When specifying filters for Linux patches, you must specify a key-pair for `PRODUCT` . For example, using the Command Line Interface (CLI), the following command fails:

`aws ssm describe-available-patches --filters Key=CVE_ID,Values=CVE-2018-3615`

However, the following command succeeds:

`aws ssm describe-available-patches --filters Key=PRODUCT,Values=AmazonLinux2018.03 Key=CVE_ID,Values=CVE-2018-3615`

Supported keys for Linux managed node patches include the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id13)`PRODUCT` **   Sample values: `AmazonLinux2018.03` | `AmazonLinux2.0`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id15)`NAME` **   Sample values: `kernel-headers` | `samba-python` | `php`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id17)`SEVERITY` **   Sample values: `Critical` | `Important` | `Medium` | `Low`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id19)`EPOCH` **   Sample values: `0` | `1`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id21)`VERSION` **   Sample values: `78.6.1` | `4.10.16`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id23)`RELEASE` **   Sample values: `9.56.amzn1` | `1.amzn2`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id25)`ARCH` **   Sample values: `i686` | `x86_64`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id27)`REPOSITORY` **   Sample values: `Core` | `Updates`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id29)`ADVISORY_ID` **   Sample values: `ALAS-2018-1058` | `ALAS2-2021-1594`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id31)`CVE_ID` **   Sample values: `CVE-2018-3615` | `CVE-2020-1472`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html#id33)`BUGZILLA_ID` **   Sample values: `1463241`

(structure)

Defines a filter used in Patch Manager APIs. Supported filter keys depend on the API operation that includes the filter. Patch Manager API operations that use `PatchOrchestratorFilter` include the following:

- DescribeAvailablePatches
- DescribeInstancePatches
- DescribePatchBaselines
- DescribePatchGroups

Key -> (string)

The key for the filter.

Values -> (list)

The value for the filter.

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

**To get available patches**

The following `describe-available-patches` example retrieves details about all available patches for Windows Server 2019 that have a MSRC severity of Critical.

```
aws ssm describe-available-patches \
    --filters "Key=PRODUCT,Values=WindowsServer2019" "Key=MSRC_SEVERITY,Values=Critical"
```

Output:

```
{
    "Patches": [
        {
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
        {
            "Id": "c96115e1-5587-4115-b851-22baa46a3f11",
            "ReleaseDate": 1549994410.0,
            "Title": "2019-02 Security Update for Adobe Flash Player for Windows Server 2019 for x64-based Systems (KB4487038)",
            "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.",
            "ContentUrl": "https://support.microsoft.com/en-us/kb/4487038",
            "Vendor": "Microsoft",
            "ProductFamily": "Windows",
            "Product": "WindowsServer2019",
            "Classification": "SecurityUpdates",
            "MsrcSeverity": "Critical",
            "KbNumber": "KB4487038",
            "MsrcNumber": "",
            "Language": "All"
        },
        ...
    ]
}
```

**To get details of a specific patch**

The following `describe-available-patches` example retrieves details about the specified patch.

```
aws ssm describe-available-patches \
    --filters "Key=PATCH_ID,Values=KB4480979"
```

Output:

```
{
    "Patches": [
        {
            "Id": "680861e3-fb75-432e-818e-d72e5f2be719",
            "ReleaseDate": 1546970408.0,
            "Title": "2019-01 Security Update for Adobe Flash Player for Windows Server 2016 for x64-based Systems (KB4480979)",
            "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.",
            "ContentUrl": "https://support.microsoft.com/en-us/kb/4480979",
            "Vendor": "Microsoft",
            "ProductFamily": "Windows",
            "Product": "WindowsServer2016",
            "Classification": "SecurityUpdates",
            "MsrcSeverity": "Critical",
            "KbNumber": "KB4480979",
            "MsrcNumber": "",
            "Language": "All"
        }
    ]
}
```

For more information, see [How Patch Manager Operations Work](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works.html) in the *AWS Systems Manager User Guide*.

## Output

Patches -> (list)

An array of patches. Each entry in the array is a patch structure.

(structure)

Represents metadata about a patch.

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

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.