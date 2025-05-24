# modify-ipam-resource-discoveryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-resource-discovery.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-resource-discovery.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-ipam-resource-discovery

## Description

Modifies a resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyIpamResourceDiscovery)

## Synopsis

```
modify-ipam-resource-discovery
[--dry-run | --no-dry-run]
--ipam-resource-discovery-id <value>
[--description <value>]
[--add-operating-regions <value>]
[--remove-operating-regions <value>]
[--add-organizational-unit-exclusions <value>]
[--remove-organizational-unit-exclusions <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--ipam-resource-discovery-id` (string)

A resource discovery ID.

`--description` (string)

A resource discovery description.

`--add-operating-regions` (list)

Add operating Regions to the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.

(structure)

Add an operating Region to an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.

For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide* .

RegionName -> (string)

The name of the operating Region.

Shorthand Syntax:

```
RegionName=string ...
```

JSON Syntax:

```
[
  {
    "RegionName": "string"
  }
  ...
]
```

`--remove-operating-regions` (list)

Remove operating Regions.

(structure)

Remove an operating Region from an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.

For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide*

RegionName -> (string)

The name of the operating Region you want to remove.

Shorthand Syntax:

```
RegionName=string ...
```

JSON Syntax:

```
[
  {
    "RegionName": "string"
  }
  ...
]
```

`--add-organizational-unit-exclusions` (list)

Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

### Note

The resulting set of exclusions must not result in âoverlapâ, meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in [Add or remove OU exclusions](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete) in the *Amazon VPC User Guide* .

(structure)

Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

OrganizationsEntityPath -> (string)

An Amazon Web Services Organizations entity path. Build the path for the OU(s) using Amazon Web Services Organizations IDs separated by a `/` . Include all child OUs by ending the path with `/*` .

- Example 1
- Path to a child OU: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
- In this example, `o-a1b2c3d4e5` is the organization ID, `r-f6g7h8i9j0example` is the root ID , `ou-ghi0-awsccccc` is an OU ID, and `ou-jkl0-awsddddd` is a child OU ID.
- IPAM will not manage the IP addresses in accounts in the child OU.
- Example 2
- Path where all child OUs will be part of the exclusion: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*`
- In this example, IPAM will not manage the IP addresses in accounts in the OU (`ou-ghi0-awsccccc` ) or in accounts in any OUs that are children of the OU.

For more information on how to construct an entity path, see [Understand the Amazon Web Services Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the *Amazon Web Services Identity and Access Management User Guide* .

Shorthand Syntax:

```
OrganizationsEntityPath=string ...
```

JSON Syntax:

```
[
  {
    "OrganizationsEntityPath": "string"
  }
  ...
]
```

`--remove-organizational-unit-exclusions` (list)

Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

### Note

The resulting set of exclusions must not result in âoverlapâ, meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in [Add or remove OU exclusions](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete) in the *Amazon VPC User Guide* .

(structure)

Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

OrganizationsEntityPath -> (string)

An Amazon Web Services Organizations entity path. Build the path for the OU(s) using Amazon Web Services Organizations IDs separated by a `/` . Include all child OUs by ending the path with `/*` .

- Example 1
- Path to a child OU: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
- In this example, `o-a1b2c3d4e5` is the organization ID, `r-f6g7h8i9j0example` is the root ID , `ou-ghi0-awsccccc` is an OU ID, and `ou-jkl0-awsddddd` is a child OU ID.
- IPAM will not manage the IP addresses in accounts in the child OU.
- Example 2
- Path where all child OUs will be part of the exclusion: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*`
- In this example, IPAM will not manage the IP addresses in accounts in the OU (`ou-ghi0-awsccccc` ) or in accounts in any OUs that are children of the OU.

For more information on how to construct an entity path, see [Understand the Amazon Web Services Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the *Amazon Web Services Identity and Access Management User Guide* .

Shorthand Syntax:

```
OrganizationsEntityPath=string ...
```

JSON Syntax:

```
[
  {
    "OrganizationsEntityPath": "string"
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

**To modify the operating regions of a resource discovery**

In this example, youâre an IPAM delegated admin who wants to modify the operating regions of a resource discovery.

To complete this request:

- You cannot modify a default resource discovery and you must be the owner of the resource discovery.
- You need the resource discovery ID, which you can get with [describe-ipam-resource-discoveries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-resource-discoveries.html).

The following `modify-ipam-resource-discovery` example modifies a non-default resource discovery in your AWS account.

```
aws ec2 modify-ipam-resource-discovery \
    --ipam-resource-discovery-id ipam-res-disco-0f4ef577a9f37a162 \
    --add-operating-regions RegionName='us-west-1' \
    --remove-operating-regions RegionName='us-east-2' \
    --region us-east-1
```

Output:

```
{
    "IpamResourceDiscovery": {
        "OwnerId": "149977607591",
        "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe",
        "IpamResourceDiscoveryArn": "arn:aws:ec2::149977607591:ipam-resource-discovery/ipam-res-disco-0365d2977fc1672fe",
        "IpamResourceDiscoveryRegion": "us-east-1",
        "Description": "Example",
        "OperatingRegions": [
            {
                "RegionName": "us-east-1"
            },
            {
                "RegionName": "us-west-1"
            }
        ],
        "IsDefault": false,
        "State": "modify-in-progress"
    }
}
```

For more information, see [Work with resource discoveries](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with.html) in the *Amazon VPC IPAM User Guide*.

## Output

IpamResourceDiscovery -> (structure)

A resource discovery.

OwnerId -> (string)

The ID of the owner.

IpamResourceDiscoveryId -> (string)

The resource discovery ID.

IpamResourceDiscoveryArn -> (string)

The resource discovery Amazon Resource Name (ARN).

IpamResourceDiscoveryRegion -> (string)

The resource discovery Region.

Description -> (string)

The resource discovery description.

OperatingRegions -> (list)

The operating Regions for the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.

(structure)

The operating Regions for an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.

For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide* .

RegionName -> (string)

The name of the operating Region.

IsDefault -> (boolean)

Defines if the resource discovery is the default. The default resource discovery is the resource discovery automatically created when you create an IPAM.

State -> (string)

The lifecycle state of the resource discovery.

- `create-in-progress` - Resource discovery is being created.
- `create-complete` - Resource discovery creation is complete.
- `create-failed` - Resource discovery creation has failed.
- `modify-in-progress` - Resource discovery is being modified.
- `modify-complete` - Resource discovery modification is complete.
- `modify-failed` - Resource discovery modification has failed.
- `delete-in-progress` - Resource discovery is being deleted.
- `delete-complete` - Resource discovery deletion is complete.
- `delete-failed` - Resource discovery deletion has failed.
- `isolate-in-progress` - Amazon Web Services account that created the resource discovery has been removed and the resource discovery is being isolated.
- `isolate-complete` - Resource discovery isolation is complete.
- `restore-in-progress` - Amazon Web Services account that created the resource discovery and was isolated has been restored.

Tags -> (list)

A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

OrganizationalUnitExclusions -> (list)

If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.

(structure)

If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.

OrganizationsEntityPath -> (string)

An Amazon Web Services Organizations entity path. For more information on the entity path, see [Understand the Amazon Web Services Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the *Amazon Web Services Identity and Access Management User Guide* .