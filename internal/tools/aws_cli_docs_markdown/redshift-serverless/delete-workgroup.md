# delete-workgroupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/delete-workgroup.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/delete-workgroup.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# delete-workgroup

## Description

Deletes a workgroup.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/DeleteWorkgroup)

## Synopsis

```
delete-workgroup
--workgroup-name <value>
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

`--workgroup-name` (string)

The name of the workgroup to be deleted.

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

## Output

workgroup -> (structure)

The deleted workgroup object.

baseCapacity -> (integer)

The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

configParameters -> (list)

An array of parameters to set for advanced control over a database. The options are `auto_mv` , `datestyle` , `enable_case_sensitive_identifier` , `enable_user_activity_logging` , `query_group` , `search_path` , `require_ssl` , `use_fips_ssl` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) .

(structure)

An array of key-value pairs to set for advanced control over Amazon Redshift Serverless.

parameterKey -> (string)

The key of the parameter. The options are `auto_mv` , `datestyle` , `enable_case_sensitive_identifier` , `enable_user_activity_logging` , `query_group` , `search_path` , `require_ssl` , `use_fips_ssl` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) .

parameterValue -> (string)

The value of the parameter to set.

creationDate -> (timestamp)

The creation date of the workgroup.

crossAccountVpcs -> (list)

A list of VPCs. Each entry is the unique identifier of a virtual private cloud with access to Amazon Redshift Serverless. If all of the VPCs for the grantee are allowed, it shows an asterisk.

(string)

customDomainCertificateArn -> (string)

The custom domain nameâs certificate Amazon resource name (ARN).

customDomainCertificateExpiryTime -> (timestamp)

The expiration time for the certificate.

customDomainName -> (string)

The custom domain name associated with the workgroup.

endpoint -> (structure)

The endpoint that is created from the workgroup.

address -> (string)

The DNS address of the VPC endpoint.

port -> (integer)

The port that Amazon Redshift Serverless listens on.

vpcEndpoints -> (list)

An array of `VpcEndpoint` objects.

(structure)

The connection endpoint for connecting to Amazon Redshift Serverless through the proxy.

networkInterfaces -> (list)

One or more network interfaces of the endpoint. Also known as an interface endpoint.

(structure)

Contains information about a network interface in an Amazon Redshift Serverless managed VPC endpoint.

availabilityZone -> (string)

The availability Zone.

ipv6Address -> (string)

The IPv6 address of the network interface within the subnet.

networkInterfaceId -> (string)

The unique identifier of the network interface.

privateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

subnetId -> (string)

The unique identifier of the subnet.

vpcEndpointId -> (string)

The connection endpoint ID for connecting to Amazon Redshift Serverless.

vpcId -> (string)

The VPC identifier that the endpoint is associated with.

enhancedVpcRouting -> (boolean)

The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

ipAddressType -> (string)

The IP address type that the workgroup supports. Possible values are `ipv4` and `dualstack` .

maxCapacity -> (integer)

The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.

namespaceName -> (string)

The namespace the workgroup is associated with.

patchVersion -> (string)

The patch version of your Amazon Redshift Serverless workgroup. For more information about patch versions, see [Cluster versions for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html) .

pendingTrackName -> (string)

The name for the track that you want to assign to the workgroup. When the track changes, the workgroup is switched to the latest workgroup release available for the track. At this point, the track name is applied.

port -> (integer)

The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

pricePerformanceTarget -> (structure)

An object that represents the price performance target settings for the workgroup.

level -> (integer)

The target price performance level for the workgroup. Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH_PERFORMANCE.

status -> (string)

Whether the price performance target is enabled for the workgroup.

publiclyAccessible -> (boolean)

A value that specifies whether the workgroup can be accessible from a public network.

securityGroupIds -> (list)

An array of security group IDs to associate with the workgroup.

(string)

status -> (string)

The status of the workgroup.

subnetIds -> (list)

An array of subnet IDs the workgroup is associated with.

(string)

trackName -> (string)

The name of the track for the workgroup.

workgroupArn -> (string)

The Amazon Resource Name (ARN) that links to the workgroup.

workgroupId -> (string)

The unique identifier of the workgroup.

workgroupName -> (string)

The name of the workgroup.

workgroupVersion -> (string)

The Amazon Redshift Serverless version of your workgroup. For more information about Amazon Redshift Serverless versions, see`Cluster versions for Amazon Redshift <[https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html)>`__ .