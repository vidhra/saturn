# describe-directoriesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/index.html#cli-aws-ds) ]

# describe-directories

## Description

Obtains information about the directories that belong to this account.

You can retrieve information about specific directories by passing the directory identifiers in the `DirectoryIds` parameter. Otherwise, all directories that belong to the current account are returned.

This operation supports pagination with the use of the `NextToken` request and response parameters. If more results are available, the `DescribeDirectoriesResult.NextToken` member contains a token that you pass in the next call to  DescribeDirectories to retrieve the next set of items.

You can also specify a maximum number of return results with the `Limit` parameter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDirectories)

`describe-directories` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DirectoryDescriptions`

## Synopsis

```
describe-directories
[--directory-ids <value>]
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

`--directory-ids` (list)

A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.

An empty list results in an `InvalidParameterException` being thrown.

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

**To get details about your directories**

The following `describe-directories` example displays details about the specified directory.

```
aws ds describe-directories \
   --directory-id d-a1b2c3d4e5
```

Output:

```
{
    "DirectoryDescriptions": [
        {
            "DirectoryId": "d-a1b2c3d4e5",
            "Name": "mydirectory.example.com",
            "ShortName": "mydirectory",
            "Size": "Small",
            "Edition": "Standard",
            "Alias": "d-a1b2c3d4e5",
            "AccessUrl": "d-a1b2c3d4e5.awsapps.com",
            "Stage": "Active",
            "ShareStatus": "Shared",
            "ShareMethod": "HANDSHAKE",
            "ShareNotes": "These are my share notes",
            "LaunchTime": "2019-07-08T15:33:46.327000-07:00",
            "StageLastUpdatedDateTime": "2019-07-08T15:59:12.307000-07:00",
            "Type": "SharedMicrosoftAD",
            "SsoEnabled": false,
            "DesiredNumberOfDomainControllers": 0,
            "OwnerDirectoryDescription": {
                "DirectoryId": "d-b2c3d4e5f6",
                "AccountId": "123456789111",
                "DnsIpAddrs": [
                    "203.113.0.248",
                    "203.113.0.253"
                ],
                "VpcSettings": {
                    "VpcId": "vpc-a1b2c3d4",
                    "SubnetIds": [
                        "subnet-a1b2c3d4",
                        "subnet-d4c3b2a1"
                    ],
                    "AvailabilityZones": [
                        "us-west-2a",
                        "us-west-2c"
                    ]
                }
            }
        }
    ]
}
```

## Output

DirectoryDescriptions -> (list)

The list of available  DirectoryDescription objects that were retrieved.

It is possible that this list contains less than the number of items specified in the `Limit` member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.

(structure)

Contains information about an Directory Service directory.

DirectoryId -> (string)

The directory identifier.

Name -> (string)

The fully qualified name of the directory.

ShortName -> (string)

The short name of the directory.

Size -> (string)

The directory size.

Edition -> (string)

The edition associated with this directory.

Alias -> (string)

The alias for the directory. If no alias has been created for the directory, the alias is the directory identifier, such as `d-XXXXXXXXXX` .

AccessUrl -> (string)

The access URL for the directory, such as `http://<alias>.awsapps.com` . If no alias has been created for the directory, `<alias>` is the directory identifier, such as `d-XXXXXXXXXX` .

Description -> (string)

The description for the directory.

DnsIpAddrs -> (list)

The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IP addresses of the DNS servers or domain controllers in your self-managed directory to which the AD Connector is connected.

(string)

Stage -> (string)

The current stage of the directory.

ShareStatus -> (string)

Current directory status of the shared Managed Microsoft AD directory.

ShareMethod -> (string)

The method used when sharing a directory to determine whether the directory should be shared within your Amazon Web Services organization (`ORGANIZATIONS` ) or with any Amazon Web Services account by sending a shared directory request (`HANDSHAKE` ).

ShareNotes -> (string)

A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.

LaunchTime -> (timestamp)

Specifies when the directory was created.

StageLastUpdatedDateTime -> (timestamp)

The date and time that the stage was last updated.

Type -> (string)

The directory type.

VpcSettings -> (structure)

A  DirectoryVpcSettingsDescription object that contains additional information about a directory. This member is only present if the directory is a Simple AD or Managed Microsoft AD directory.

VpcId -> (string)

The identifier of the VPC that the directory is in.

SubnetIds -> (list)

The identifiers of the subnets for the directory servers.

(string)

SecurityGroupId -> (string)

The domain controller security group identifier for the directory.

AvailabilityZones -> (list)

The list of Availability Zones that the directory is in.

(string)

ConnectSettings -> (structure)

A  DirectoryConnectSettingsDescription object that contains additional information about an AD Connector directory. This member is only present if the directory is an AD Connector directory.

VpcId -> (string)

The identifier of the VPC that the AD Connector is in.

SubnetIds -> (list)

A list of subnet identifiers in the VPC that the AD Connector is in.

(string)

CustomerUserName -> (string)

The user name of the service account in your self-managed directory.

SecurityGroupId -> (string)

The security group identifier for the AD Connector directory.

AvailabilityZones -> (list)

A list of the Availability Zones that the directory is in.

(string)

ConnectIps -> (list)

The IP addresses of the AD Connector servers.

(string)

RadiusSettings -> (structure)

A  RadiusSettings object that contains information about the RADIUS server configured for this directory.

RadiusServers -> (list)

An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.

(string)

RadiusPort -> (integer)

The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the Directory Service servers.

RadiusTimeout -> (integer)

The amount of time, in seconds, to wait for the RADIUS server to respond.

RadiusRetries -> (integer)

The maximum number of times that communication with the RADIUS server is retried after the initial attempt.

SharedSecret -> (string)

Required for enabling RADIUS on the directory.

AuthenticationProtocol -> (string)

The protocol specified for your RADIUS endpoints.

DisplayLabel -> (string)

Not currently used.

UseSameUsername -> (boolean)

Not currently used.

RadiusStatus -> (string)

The status of the RADIUS MFA server connection.

StageReason -> (string)

Additional information about the directory stage.

SsoEnabled -> (boolean)

Indicates if single sign-on is enabled for the directory. For more information, see  EnableSso and  DisableSso .

DesiredNumberOfDomainControllers -> (integer)

The desired number of domain controllers in the directory if the directory is Microsoft AD.

OwnerDirectoryDescription -> (structure)

Describes the Managed Microsoft AD directory in the directory owner account.

DirectoryId -> (string)

Identifier of the Managed Microsoft AD directory in the directory owner account.

AccountId -> (string)

Identifier of the directory owner account.

DnsIpAddrs -> (list)

IP address of the directoryâs domain controllers.

(string)

VpcSettings -> (structure)

Information about the VPC settings for the directory.

VpcId -> (string)

The identifier of the VPC that the directory is in.

SubnetIds -> (list)

The identifiers of the subnets for the directory servers.

(string)

SecurityGroupId -> (string)

The domain controller security group identifier for the directory.

AvailabilityZones -> (list)

The list of Availability Zones that the directory is in.

(string)

RadiusSettings -> (structure)

A  RadiusSettings object that contains information about the RADIUS server.

RadiusServers -> (list)

An array of strings that contains the fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.

(string)

RadiusPort -> (integer)

The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the Directory Service servers.

RadiusTimeout -> (integer)

The amount of time, in seconds, to wait for the RADIUS server to respond.

RadiusRetries -> (integer)

The maximum number of times that communication with the RADIUS server is retried after the initial attempt.

SharedSecret -> (string)

Required for enabling RADIUS on the directory.

AuthenticationProtocol -> (string)

The protocol specified for your RADIUS endpoints.

DisplayLabel -> (string)

Not currently used.

UseSameUsername -> (boolean)

Not currently used.

RadiusStatus -> (string)

Information about the status of the RADIUS server.

RegionsInfo -> (structure)

Lists the Regions where the directory has replicated.

PrimaryRegion -> (string)

The Region where the Managed Microsoft AD directory was originally created.

AdditionalRegions -> (list)

Lists the Regions where the directory has been replicated, excluding the primary Region.

(string)

OsVersion -> (string)

The operating system (OS) version of the directory.

NextToken -> (string)

If not null, more results are available. Pass this value for the `NextToken` parameter in a subsequent call to  DescribeDirectories to retrieve the next set of items.