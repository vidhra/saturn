# create-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/create-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/create-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [keyspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html#cli-aws-keyspaces) ]

# create-table

## Description

The `CreateTable` operation adds a new table to the specified keyspace. Within a keyspace, table names must be unique.

`CreateTable` is an asynchronous operation. When the request is received, the status of the table is set to `CREATING` . You can monitor the creation status of the new table by using the `GetTable` operation, which returns the current `status` of the table. You can start using a table when the status is `ACTIVE` .

For more information, see [Create a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.tables.html) in the *Amazon Keyspaces Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/keyspaces-2022-02-10/CreateTable)

## Synopsis

```
create-table
--keyspace-name <value>
--table-name <value>
--schema-definition <value>
[--comment <value>]
[--capacity-specification <value>]
[--encryption-specification <value>]
[--point-in-time-recovery <value>]
[--ttl <value>]
[--default-time-to-live <value>]
[--tags <value>]
[--client-side-timestamps <value>]
[--auto-scaling-specification <value>]
[--replica-specifications <value>]
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

`--keyspace-name` (string)

The name of the keyspace that the table is going to be created in.

`--table-name` (string)

The name of the table.

`--schema-definition` (structure)

The `schemaDefinition` consists of the following parameters.

For each column to be created:

- `name` - The name of the column.
- `type` - An Amazon Keyspaces data type. For more information, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide* .

The primary key of the table consists of the following columns:

- `partitionKeys` - The partition key can be a single column, or it can be a compound value composed of two or more columns. The partition key portion of the primary key is required and determines how Amazon Keyspaces stores your data.
- `name` - The name of each partition key column.
- `clusteringKeys` - The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.
- `name` - The name of the clustering column.
- `orderBy` - Sets the ascendant (`ASC` ) or descendant (`DESC` ) order modifier. To define a column as static use `staticColumns` - Static columns store values that are shared by all rows in the same partition:
- `name` - The name of the column.
- `type` - An Amazon Keyspaces data type.

allColumns -> (list)

The regular columns of the table.

(structure)

The names and data types of regular columns.

name -> (string)

The name of the column.

type -> (string)

The data type of the column. For a list of available data types, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide* .

partitionKeys -> (list)

The columns that are part of the partition key of the table .

(structure)

The partition key portion of the primary key is required and determines how Amazon Keyspaces stores the data. The partition key can be a single column, or it can be a compound value composed of two or more columns.

name -> (string)

The name(s) of the partition key column(s).

clusteringKeys -> (list)

The columns that are part of the clustering key of the table.

(structure)

The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.

name -> (string)

The name(s) of the clustering column(s).

orderBy -> (string)

Sets the ascendant (`ASC` ) or descendant (`DESC` ) order modifier.

staticColumns -> (list)

The columns that have been defined as `STATIC` . Static columns store values that are shared by all rows in the same partition.

(structure)

The static columns of the table. Static columns store values that are shared by all rows in the same partition.

name -> (string)

The name of the static column.

Shorthand Syntax:

```
allColumns=[{name=string,type=string},{name=string,type=string}],partitionKeys=[{name=string},{name=string}],clusteringKeys=[{name=string,orderBy=string},{name=string,orderBy=string}],staticColumns=[{name=string},{name=string}]
```

JSON Syntax:

```
{
  "allColumns": [
    {
      "name": "string",
      "type": "string"
    }
    ...
  ],
  "partitionKeys": [
    {
      "name": "string"
    }
    ...
  ],
  "clusteringKeys": [
    {
      "name": "string",
      "orderBy": "ASC"|"DESC"
    }
    ...
  ],
  "staticColumns": [
    {
      "name": "string"
    }
    ...
  ]
}
```

`--comment` (structure)

This parameter allows to enter a description of the table.

message -> (string)

An optional description of the table.

Shorthand Syntax:

```
message=string
```

JSON Syntax:

```
{
  "message": "string"
}
```

`--capacity-specification` (structure)

Specifies the read/write throughput capacity mode for the table. The options are:

- `throughputMode:PAY_PER_REQUEST` and
- `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.

The default is `throughput_mode:PAY_PER_REQUEST` .

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide* .

throughputMode -> (string)

The read/write throughput capacity mode for a table. The options are:

- `throughputMode:PAY_PER_REQUEST` and
- `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.

The default is `throughput_mode:PAY_PER_REQUEST` .

For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide* .

readCapacityUnits -> (long)

The throughput capacity specified for `read` operations defined in `read capacity units` `(RCUs)` .

writeCapacityUnits -> (long)

The throughput capacity specified for `write` operations defined in `write capacity units` `(WCUs)` .

Shorthand Syntax:

```
throughputMode=string,readCapacityUnits=long,writeCapacityUnits=long
```

JSON Syntax:

```
{
  "throughputMode": "PAY_PER_REQUEST"|"PROVISIONED",
  "readCapacityUnits": long,
  "writeCapacityUnits": long
}
```

`--encryption-specification` (structure)

Specifies how the encryption key for encryption at rest is managed for the table. You can choose one of the following KMS key (KMS key):

- `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
- `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.

The default is `type:AWS_OWNED_KMS_KEY` .

For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide* .

type -> (string)

The encryption option specified for the table. You can choose one of the following KMS keys (KMS keys):

- `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
- `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.

The default is `type:AWS_OWNED_KMS_KEY` .

For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide* .

kmsKeyIdentifier -> (string)

The Amazon Resource Name (ARN) of the customer managed KMS key, for example `kms_key_identifier:ARN` .

Shorthand Syntax:

```
type=string,kmsKeyIdentifier=string
```

JSON Syntax:

```
{
  "type": "CUSTOMER_MANAGED_KMS_KEY"|"AWS_OWNED_KMS_KEY",
  "kmsKeyIdentifier": "string"
}
```

`--point-in-time-recovery` (structure)

Specifies if `pointInTimeRecovery` is enabled or disabled for the table. The options are:

- `status=ENABLED`
- `status=DISABLED`

If itâs not specified, the default is `status=DISABLED` .

For more information, see [Point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html) in the *Amazon Keyspaces Developer Guide* .

status -> (string)

The options are:

- `status=ENABLED`
- `status=DISABLED`

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "ENABLED"|"DISABLED"
}
```

`--ttl` (structure)

Enables Time to Live custom settings for the table. The options are:

- `status:enabled`
- `status:disabled`

The default is `status:disabled` . After `ttl` is enabled, you canât disable it for the table.

For more information, see [Expiring data by using Amazon Keyspaces Time to Live (TTL)](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html) in the *Amazon Keyspaces Developer Guide* .

status -> (string)

Shows how to enable custom Time to Live (TTL) settings for the specified table.

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "ENABLED"
}
```

`--default-time-to-live` (integer)

The default Time to Live setting in seconds for the table.

For more information, see [Setting the default TTL value for a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl) in the *Amazon Keyspaces Developer Guide* .

`--tags` (list)

A list of key-value pair tags to be attached to the resource.

For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide* .

(structure)

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single Amazon Keyspaces resource.

Amazon Web Services-assigned tag names and values are automatically assigned the `aws:` prefix, which the user cannot assign. Amazon Web Services-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix `user:` in the Cost Allocation Report. You cannot backdate the application of a tag.

For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide* .

key -> (string)

The key of the tag. Tag keys are case sensitive. Each Amazon Keyspaces resource can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

value -> (string)

The value of the tag. Tag values are case-sensitive and can be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--client-side-timestamps` (structure)

Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:

- `status: "enabled"`

Once client-side timestamps are enabled for a table, this setting cannot be disabled.

status -> (string)

Shows how to enable client-side timestamps settings for the specified table.

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "ENABLED"
}
```

`--auto-scaling-specification` (structure)

The optional auto scaling settings for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity automatically on your behalf.

Auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your tableâs read and write capacity automatically in response to application traffic. For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide* .

By default, auto scaling is disabled for a table.

writeCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs write capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

readCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs read capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

JSON Syntax:

```
{
  "writeCapacityAutoScaling": {
    "autoScalingDisabled": true|false,
    "minimumUnits": long,
    "maximumUnits": long,
    "scalingPolicy": {
      "targetTrackingScalingPolicyConfiguration": {
        "disableScaleIn": true|false,
        "scaleInCooldown": integer,
        "scaleOutCooldown": integer,
        "targetValue": double
      }
    }
  },
  "readCapacityAutoScaling": {
    "autoScalingDisabled": true|false,
    "minimumUnits": long,
    "maximumUnits": long,
    "scalingPolicy": {
      "targetTrackingScalingPolicyConfiguration": {
        "disableScaleIn": true|false,
        "scaleInCooldown": integer,
        "scaleOutCooldown": integer,
        "targetValue": double
      }
    }
  }
}
```

`--replica-specifications` (list)

The optional Amazon Web Services Region specific settings of a multi-Region table. These settings overwrite the general settings of the table for the specified Region.

For a multi-Region table in provisioned capacity mode, you can configure the tableâs read capacity differently for each Regionâs replica. The write capacity, however, remains synchronized between all replicas to ensure that thereâs enough capacity to replicate writes across all Regions. To define the read capacity for a table replica in a specific Region, you can do so by configuring the following parameters.

- `region` : The Region where these settings are applied. (Required)
- `readCapacityUnits` : The provisioned read capacity units. (Optional)
- `readCapacityAutoScaling` : The read capacity auto scaling settings for the table. (Optional)

(structure)

The Amazon Web Services Region specific settings of a multi-Region table.

For a multi-Region table, you can configure the tableâs read capacity differently per Amazon Web Services Region. You can do this by configuring the following parameters.

- `region` : The Region where these settings are applied. (Required)
- `readCapacityUnits` : The provisioned read capacity units. (Optional)
- `readCapacityAutoScaling` : The read capacity auto scaling settings for the table. (Optional)

region -> (string)

The Amazon Web Services Region.

readCapacityUnits -> (long)

The provisioned read capacity units for the multi-Region table in the specified Amazon Web Services Region.

readCapacityAutoScaling -> (structure)

The read capacity auto scaling settings for the multi-Region table in the specified Amazon Web Services Region.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

JSON Syntax:

```
[
  {
    "region": "string",
    "readCapacityUnits": long,
    "readCapacityAutoScaling": {
      "autoScalingDisabled": true|false,
      "minimumUnits": long,
      "maximumUnits": long,
      "scalingPolicy": {
        "targetTrackingScalingPolicyConfiguration": {
          "disableScaleIn": true|false,
          "scaleInCooldown": integer,
          "scaleOutCooldown": integer,
          "targetValue": double
        }
      }
    }
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

## Output

resourceArn -> (string)

The unique identifier of the table in the format of an Amazon Resource Name (ARN).