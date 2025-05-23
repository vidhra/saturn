# restore-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/restore-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/restore-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [keyspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html#cli-aws-keyspaces) ]

# restore-table

## Description

Restores the table to the specified point in time within the `earliest_restorable_timestamp` and the current time. For more information about restore points, see [Time window for PITR continuous backups](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_window) in the *Amazon Keyspaces Developer Guide* .

Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.

When you restore using point in time recovery, Amazon Keyspaces restores your source tableâs schema and data to the state based on the selected timestamp `(day:hour:minute:second)` to a new table. The Time to Live (TTL) settings are also restored to the state based on the selected timestamp.

In addition to the tableâs schema, data, and TTL settings, `RestoreTable` restores the capacity mode, auto scaling settings, encryption settings, and point-in-time recovery settings from the source table. Unlike the tableâs schema data and TTL settings, which are restored based on the selected timestamp, these settings are always restored based on the tableâs settings as of the current time or when the table was deleted.

You can also overwrite these settings during restore:

- Read/write capacity mode
- Provisioned throughput capacity units
- Auto scaling settings
- Point-in-time (PITR) settings
- Tags

For more information, see [PITR restore settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_settings) in the *Amazon Keyspaces Developer Guide* .

Note that the following settings are not restored, and you must configure them manually for the new table:

- Identity and Access Management (IAM) policies
- Amazon CloudWatch metrics and alarms

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/keyspaces-2022-02-10/RestoreTable)

## Synopsis

```
restore-table
--source-keyspace-name <value>
--source-table-name <value>
--target-keyspace-name <value>
--target-table-name <value>
[--restore-timestamp <value>]
[--capacity-specification-override <value>]
[--encryption-specification-override <value>]
[--point-in-time-recovery-override <value>]
[--tags-override <value>]
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

`--source-keyspace-name` (string)

The keyspace name of the source table.

`--source-table-name` (string)

The name of the source table.

`--target-keyspace-name` (string)

The name of the target keyspace.

`--target-table-name` (string)

The name of the target table.

`--restore-timestamp` (timestamp)

The restore timestamp in ISO 8601 format.

`--capacity-specification-override` (structure)

Specifies the read/write throughput capacity mode for the target table. The options are:

- `throughputMode:PAY_PER_REQUEST`
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

`--encryption-specification-override` (structure)

Specifies the encryption settings for the target table. You can choose one of the following KMS key (KMS key):

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

`--point-in-time-recovery-override` (structure)

Specifies the `pointInTimeRecovery` settings for the target table. The options are:

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

`--tags-override` (list)

A list of key-value pair tags to be attached to the restored table.

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

`--auto-scaling-specification` (structure)

The optional auto scaling settings for the restored table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your tableâs read and write capacity automatically in response to application traffic.

For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide* .

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

The optional Region specific settings of a multi-Regional table.

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

restoredTableARN -> (string)

The Amazon Resource Name (ARN) of the restored table.