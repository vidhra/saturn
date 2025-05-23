# create-patch-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-patch-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-patch-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# create-patch-baseline

## Description

Creates a patch baseline.

### Note

For information about valid key-value pairs in `PatchFilters` for each supported operating system type, see  PatchFilter .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreatePatchBaseline)

## Synopsis

```
create-patch-baseline
[--operating-system <value>]
--name <value>
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
[--client-token <value>]
[--tags <value>]
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

`--operating-system` (string)

Defines the operating system the patch baseline applies to. The default value is `WINDOWS` .

Possible values:

- `WINDOWS`
- `AMAZON_LINUX`
- `AMAZON_LINUX_2`
- `AMAZON_LINUX_2022`
- `UBUNTU`
- `REDHAT_ENTERPRISE_LINUX`
- `SUSE`
- `CENTOS`
- `ORACLE_LINUX`
- `DEBIAN`
- `MACOS`
- `RASPBIAN`
- `ROCKY_LINUX`
- `ALMA_LINUX`
- `AMAZON_LINUX_2023`

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

Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is `UNSPECIFIED` .

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

Indicates the status you want to assign to security patches that are available but not approved because they donât meet the installation criteria specified in the patch baseline.

Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.

Supported for Windows Server managed nodes only.

Possible values:

- `COMPLIANT`
- `NON_COMPLIANT`

`--client-token` (string)

User-provided idempotency token.

`--tags` (list)

Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to. In this case, you could specify the following key-value pairs:

- `Key=PatchSeverity,Value=Critical`
- `Key=OS,Value=Windows`

### Note

To add tags to an existing patch baseline, use the  AddTagsToResource operation.

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

**Example 1: To create a patch baseline with auto-approval**

The following `create-patch-baseline` example creates a patch baseline for Windows Server that approves patches for a production environment seven days after they are released by Microsoft.

```
aws ssm create-patch-baseline \
    --name "Windows-Production-Baseline-AutoApproval" \
    --operating-system "WINDOWS" \
    --approval-rules "PatchRules=[{PatchFilterGroup={PatchFilters=[{Key=MSRC_SEVERITY,Values=[Critical,Important,Moderate]},{Key=CLASSIFICATION,Values=[SecurityUpdates,Updates,UpdateRollups,CriticalUpdates]}]},ApproveAfterDays=7}]" \
    --description "Baseline containing all updates approved for Windows Server production systems"
```

Output:

```
{
    "BaselineId": "pb-045f10b4f3EXAMPLE"
}
```

**Example 2: To create a patch baseline with an approval cutoff date**

The following `create-patch-baseline` example creates a patch baseline for Windows Server that approves all patches for a production environment that are released on or before July 7, 2020.

```
aws ssm create-patch-baseline \
    --name "Windows-Production-Baseline-AutoApproval" \
    --operating-system "WINDOWS" \
    --approval-rules "PatchRules=[{PatchFilterGroup={PatchFilters=[{Key=MSRC_SEVERITY,Values=[Critical,Important,Moderate]},{Key=CLASSIFICATION,Values=[SecurityUpdates,Updates,UpdateRollups,CriticalUpdates]}]},ApproveUntilDate=2020-07-07}]" \
    --description "Baseline containing all updates approved for Windows Server production systems"
```

Output:

```
{
    "BaselineId": "pb-045f10b4f3EXAMPLE"
}
```

**Example 3: To create a patch baseline with approval rules stored in a JSON file**

The following `create-patch-baseline` example creates a patch baseline for Amazon Linux 2017.09 that approves patches for a production environment seven days after they are released, specifies approval rules for the patch baseline, and specifies a custom repository for patches.

```
aws ssm create-patch-baseline \
    --cli-input-json file://my-amazon-linux-approval-rules-and-repo.json
```

Contents of `my-amazon-linux-approval-rules-and-repo.json`:

```
{
    "Name": "Amazon-Linux-2017.09-Production-Baseline",
    "Description": "My approval rules patch baseline for Amazon Linux 2017.09 instances",
    "OperatingSystem": "AMAZON_LINUX",
    "Tags": [
        {
            "Key": "Environment",
            "Value": "Production"
        }
    ],
    "ApprovalRules": {
        "PatchRules": [
            {
                "ApproveAfterDays": 7,
                "EnableNonSecurity": true,
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Key": "SEVERITY",
                            "Values": [
                                "Important",
                                "Critical"
                            ]
                        },
                        {
                            "Key": "CLASSIFICATION",
                            "Values": [
                                "Security",
                                "Bugfix"
                            ]
                        },
                        {
                            "Key": "PRODUCT",
                            "Values": [
                                "AmazonLinux2017.09"
                            ]
                        }
                    ]
                }
            }
        ]
    },
    "Sources": [
        {
            "Name": "My-AL2017.09",
            "Products": [
                "AmazonLinux2017.09"
            ],
            "Configuration": "[amzn-main] \nname=amzn-main-Base\nmirrorlist=http://repo./$awsregion./$awsdomain//$releasever/main/mirror.list //nmirrorlist_expire=300//nmetadata_expire=300 \npriority=10 \nfailovermethod=priority \nfastestmirror_enabled=0 \ngpgcheck=1 \ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-ga \nenabled=1 \nretries=3 \ntimeout=5\nreport_instanceid=yes"
        }
    ]
}
```

**Example 4: To create a patch baseline that specifies approved and rejected patches**

The following `create-patch-baseline` example explicitly specifies patches to approve and reject as exception to the default approval rules.

```
aws ssm create-patch-baseline \
    --name "Amazon-Linux-2017.09-Alpha-Baseline" \
    --description "My custom approve/reject patch baseline for Amazon Linux 2017.09 instances" \
    --operating-system "AMAZON_LINUX" \
    --approved-patches "CVE-2018-1234567,example-pkg-EE-2018*.amzn1.noarch" \
    --approved-patches-compliance-level "HIGH" \
    --approved-patches-enable-non-security \
    --tags "Key=Environment,Value=Alpha"
```

For more information, see [Create a Custom Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baseline-console.html) in the *AWS Systems Manager User Guide*.

## Output

BaselineId -> (string)

The ID of the created patch baseline.