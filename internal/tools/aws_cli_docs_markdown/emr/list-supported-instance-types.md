# list-supported-instance-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-supported-instance-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-supported-instance-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# list-supported-instance-types

## Description

A list of the instance types that Amazon EMR supports. You can filter the list by Amazon Web Services Region and Amazon EMR release.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListSupportedInstanceTypes)

## Synopsis

```
list-supported-instance-types
--release-label <value>
[--marker <value>]
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

`--release-label` (string)

The Amazon EMR release label determines the [versions of open-source application packages](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-app-versions-6.x.html) that Amazon EMR has installed on the cluster. Release labels are in the format `emr-x.x.x` , where x.x.x is an Amazon EMR release number such as `emr-6.10.0` . For more information about Amazon EMR releases and their included application versions and features, see the * [Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html) * .

`--marker` (string)

The pagination token that marks the next set of results to retrieve.

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

SupportedInstanceTypes -> (list)

The list of instance types that the release specified in `ListSupportedInstanceTypesInput$ReleaseLabel` supports, filtered by Amazon Web Services Region.

(structure)

An instance type that the specified Amazon EMR release supports.

Type -> (string)

The [Amazon EC2 instance type](http://aws.amazon.com/ec2/instance-types/) , for example `m5.xlarge` , of the `SupportedInstanceType` .

MemoryGB -> (float)

The amount of memory that is available to Amazon EMR from the `SupportedInstanceType` . The kernel and hypervisor software consume some memory, so this value might be lower than the overall memory for the instance type.

StorageGB -> (integer)

`StorageGB` represents the storage capacity of the `SupportedInstanceType` . This value is `0` for Amazon EBS-only instance types.

VCPU -> (integer)

The number of vCPUs available for the `SupportedInstanceType` .

Is64BitsOnly -> (boolean)

Indicates whether the `SupportedInstanceType` only supports 64-bit architecture.

InstanceFamilyId -> (string)

The Amazon EC2 family and generation for the `SupportedInstanceType` .

EbsOptimizedAvailable -> (boolean)

Indicates whether the `SupportedInstanceType` supports Amazon EBS optimization.

EbsOptimizedByDefault -> (boolean)

Indicates whether the `SupportedInstanceType` uses Amazon EBS optimization by default.

NumberOfDisks -> (integer)

Number of disks for the `SupportedInstanceType` . This value is `0` for Amazon EBS-only instance types.

EbsStorageOnly -> (boolean)

Indicates whether the `SupportedInstanceType` only supports Amazon EBS.

Architecture -> (string)

The CPU architecture, for example `X86_64` or `AARCH64` .

Marker -> (string)

The pagination token that marks the next set of results to retrieve.