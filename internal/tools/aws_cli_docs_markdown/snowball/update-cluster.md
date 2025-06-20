# update-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [snowball](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/index.html#cli-aws-snowball) ]

# update-cluster

## Description

While a clusterâs `ClusterState` value is in the `AwaitingQuorum` state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/UpdateCluster)

## Synopsis

```
update-cluster
--cluster-id <value>
[--role-arn <value>]
[--description <value>]
[--resources <value>]
[--on-device-service-configuration <value>]
[--address-id <value>]
[--shipping-option <value>]
[--notification <value>]
[--forwarding-address-id <value>]
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

`--cluster-id` (string)

The cluster ID of the cluster that you want to update, for example `CID123e4567-e89b-12d3-a456-426655440000` .

`--role-arn` (string)

The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) API action in Identity and Access Management (IAM).

`--description` (string)

The updated description of this cluster.

`--resources` (structure)

The updated arrays of  JobResource objects that can include updated  S3Resource objects or  LambdaResource objects.

S3Resources -> (list)

An array of `S3Resource` objects.

(structure)

Each `S3Resource` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional `KeyRange` value. The length of the range is defined at job creation, and has either an inclusive `BeginMarker` , an inclusive `EndMarker` , or both. Ranges are UTF-8 binary sorted.

BucketArn -> (string)

The Amazon Resource Name (ARN) of an Amazon S3 bucket.

KeyRange -> (structure)

For export jobs, you can provide an optional `KeyRange` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive `BeginMarker` , an inclusive `EndMarker` , or both. Ranges are UTF-8 binary sorted.

BeginMarker -> (string)

The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.

EndMarker -> (string)

The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.

TargetOnDeviceServices -> (list)

Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System).

(structure)

An object that represents the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System).

ServiceName -> (string)

Specifies the name of the service on the Snow Family device that your transferred data will be exported from or imported into.

TransferOption -> (string)

Specifies whether the data is being imported or exported. You can import or export the data, or use it locally on the device.

LambdaResources -> (list)

The Python-language Lambda functions for this job.

(structure)

Identifies

LambdaArn -> (string)

An Amazon Resource Name (ARN) that represents an Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.

EventTriggers -> (list)

The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.

(structure)

The container for the  EventTriggerDefinition$EventResourceARN .

EventResourceARN -> (string)

The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an Lambda functionâs event trigger associated with this job.

Ec2AmiResources -> (list)

The Amazon Machine Images (AMIs) associated with this job.

(structure)

A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2-compatible AMI ID and the Snow device AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the Amazon Web Services Cloud and on the device.

AmiId -> (string)

The ID of the AMI in Amazon EC2.

SnowballAmiId -> (string)

The ID of the AMI on the Snow device.

JSON Syntax:

```
{
  "S3Resources": [
    {
      "BucketArn": "string",
      "KeyRange": {
        "BeginMarker": "string",
        "EndMarker": "string"
      },
      "TargetOnDeviceServices": [
        {
          "ServiceName": "NFS_ON_DEVICE_SERVICE"|"S3_ON_DEVICE_SERVICE",
          "TransferOption": "IMPORT"|"EXPORT"|"LOCAL_USE"
        }
        ...
      ]
    }
    ...
  ],
  "LambdaResources": [
    {
      "LambdaArn": "string",
      "EventTriggers": [
        {
          "EventResourceARN": "string"
        }
        ...
      ]
    }
    ...
  ],
  "Ec2AmiResources": [
    {
      "AmiId": "string",
      "SnowballAmiId": "string"
    }
    ...
  ]
}
```

`--on-device-service-configuration` (structure)

Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family device clusters support Amazon S3 and NFS (Network File System).

NFSOnDeviceService -> (structure)

Represents the NFS (Network File System) service on a Snow Family device.

StorageLimit -> (integer)

The maximum NFS storage for one Snow Family device.

StorageUnit -> (string)

The scale unit of the NFS storage on the device.

Valid values: TB.

TGWOnDeviceService -> (structure)

Represents the Storage Gateway service Tape Gateway type on a Snow Family device.

StorageLimit -> (integer)

The maximum number of virtual tapes to store on one Snow Family device. Due to physical resource limitations, this value must be set to 80 for Snowball Edge.

StorageUnit -> (string)

The scale unit of the virtual tapes on the device.

EKSOnDeviceService -> (structure)

The configuration of EKS Anywhere on the Snow Family device.

KubernetesVersion -> (string)

The Kubernetes version for EKS Anywhere on the Snow Family device.

EKSAnywhereVersion -> (string)

The optional version of EKS Anywhere on the Snow Family device.

S3OnDeviceService -> (structure)

Configuration for Amazon S3 compatible storage on Snow family devices.

StorageLimit -> (double)

If the specified storage limit value matches storage limit of one of the defined configurations, that configuration will be used. If the specified storage limit value does not match any defined configuration, the request will fail. If more than one configuration has the same storage limit as specified, the other input need to be provided.

StorageUnit -> (string)

Storage unit. Currently the only supported unit is TB.

ServiceSize -> (integer)

Applicable when creating a cluster. Specifies how many nodes are needed for Amazon S3 compatible storage on Snow family devices. If specified, the other input can be omitted.

FaultTolerance -> (integer)

>Fault tolerance level of the cluster. This indicates the number of nodes that can go down without degrading the performance of the cluster. This additional input helps when the specified `StorageLimit` matches more than one Amazon S3 compatible storage on Snow family devices service configuration.

Shorthand Syntax:

```
NFSOnDeviceService={StorageLimit=integer,StorageUnit=string},TGWOnDeviceService={StorageLimit=integer,StorageUnit=string},EKSOnDeviceService={KubernetesVersion=string,EKSAnywhereVersion=string},S3OnDeviceService={StorageLimit=double,StorageUnit=string,ServiceSize=integer,FaultTolerance=integer}
```

JSON Syntax:

```
{
  "NFSOnDeviceService": {
    "StorageLimit": integer,
    "StorageUnit": "TB"
  },
  "TGWOnDeviceService": {
    "StorageLimit": integer,
    "StorageUnit": "TB"
  },
  "EKSOnDeviceService": {
    "KubernetesVersion": "string",
    "EKSAnywhereVersion": "string"
  },
  "S3OnDeviceService": {
    "StorageLimit": double,
    "StorageUnit": "TB",
    "ServiceSize": integer,
    "FaultTolerance": integer
  }
}
```

`--address-id` (string)

The ID of the updated  Address object.

`--shipping-option` (string)

The updated shipping option value of this clusterâs  ShippingDetails object.

Possible values:

- `SECOND_DAY`
- `NEXT_DAY`
- `EXPRESS`
- `STANDARD`

`--notification` (structure)

The new or updated  Notification object.

SnsTopicARN -> (string)

The new SNS `TopicArn` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html) Amazon SNS API action.

You can subscribe email addresses to an Amazon SNS topic through the Amazon Web Services Management Console, or by using the [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) Amazon Simple Notification Service (Amazon SNS) API action.

JobStatesToNotify -> (list)

The list of job states that will trigger a notification for this job.

(string)

NotifyAll -> (boolean)

Any change in job state will trigger a notification for this job.

DevicePickupSnsTopicARN -> (string)

Used to send SNS notifications for the person picking up the device (identified during job creation).

Shorthand Syntax:

```
SnsTopicARN=string,JobStatesToNotify=string,string,NotifyAll=boolean,DevicePickupSnsTopicARN=string
```

JSON Syntax:

```
{
  "SnsTopicARN": "string",
  "JobStatesToNotify": ["New"|"PreparingAppliance"|"PreparingShipment"|"InTransitToCustomer"|"WithCustomer"|"InTransitToAWS"|"WithAWSSortingFacility"|"WithAWS"|"InProgress"|"Complete"|"Cancelled"|"Listing"|"Pending", ...],
  "NotifyAll": true|false,
  "DevicePickupSnsTopicARN": "string"
}
```

`--forwarding-address-id` (string)

The updated ID for the forwarding address for a cluster. This field is not supported in most regions.

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

None