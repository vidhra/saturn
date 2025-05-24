# put-lifecycle-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# put-lifecycle-configuration

## Description

Use this action to manage storage for your file system. A `LifecycleConfiguration` consists of one or more `LifecyclePolicy` objects that define the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id1)`TransitionToIA` ** â When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access (IA) storage.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id3)`TransitionToArchive` ** â When to move files in the file system from their current storage class (either IA or Standard storage) into the Archive storage. File systems cannot transition into Archive storage before transitioning into IA storage. Therefore, TransitionToArchive must either not be set or must be later than TransitionToIA.

### Note

The Archive storage class is available only for file systems that use the Elastic throughput mode and the General Purpose performance mode.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id5)`TransitionToPrimaryStorageClass` ** â Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA or Archive storage.

For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) .

Each Amazon EFS file system supports one lifecycle configuration, which applies to all files in the file system. If a `LifecycleConfiguration` object already exists for the specified file system, a `PutLifecycleConfiguration` call modifies the existing configuration. A `PutLifecycleConfiguration` call with an empty `LifecyclePolicies` array in the request body deletes any existing `LifecycleConfiguration` . In the request, specify the following:

- The ID for the file system for which you are enabling, disabling, or modifying lifecycle management.
- A `LifecyclePolicies` array of `LifecyclePolicy` objects that define when to move files to IA storage, to Archive storage, and back to primary storage.

### Note

Amazon EFS requires that each `LifecyclePolicy` object have only have a single transition, so the `LifecyclePolicies` array needs to be structured with separate `LifecyclePolicy` objects. See the example requests in the following section for more information.

This operation requires permissions for the `elasticfilesystem:PutLifecycleConfiguration` operation.

To apply a `LifecycleConfiguration` object to an encrypted file system, you need the same Key Management Service permissions as when you created the encrypted file system.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/PutLifecycleConfiguration)

## Synopsis

```
put-lifecycle-configuration
--file-system-id <value>
--lifecycle-policies <value>
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

`--file-system-id` (string)

The ID of the file system for which you are creating the `LifecycleConfiguration` object (String).

`--lifecycle-policies` (list)

An array of `LifecyclePolicy` objects that define the file systemâs `LifecycleConfiguration` object. A `LifecycleConfiguration` object informs lifecycle management of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id7)`TransitionToIA` ** â When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access (IA) storage.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id9)`TransitionToArchive` ** â When to move files in the file system from their current storage class (either IA or Standard storage) into the Archive storage. File systems cannot transition into Archive storage before transitioning into IA storage. Therefore, TransitionToArchive must either not be set or must be later than TransitionToIA.

### Note

The Archive storage class is available only for file systems that use the Elastic throughput mode and the General Purpose performance mode.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html#id11)`TransitionToPrimaryStorageClass` ** â Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA or Archive storage.

### Note

When using the `put-lifecycle-configuration` CLI command or the `PutLifecycleConfiguration` API action, Amazon EFS requires that each `LifecyclePolicy` object have only a single transition. This means that in a request body, `LifecyclePolicies` must be structured as an array of `LifecyclePolicy` objects, one object for each storage transition. See the example requests in the following section for more information.

(structure)

Describes a policy used by lifecycle management that specifies when to transition files into and out of storage classes. For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) .

### Note

When using the `put-lifecycle-configuration` CLI command or the `PutLifecycleConfiguration` API action, Amazon EFS requires that each `LifecyclePolicy` object have only a single transition. This means that in a request body, `LifecyclePolicies` must be structured as an array of `LifecyclePolicy` objects, one object for each transition. For more information, see the request examples in  PutLifecycleConfiguration .

TransitionToIA -> (string)

The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory donât count as file access events.

TransitionToPrimaryStorageClass -> (string)

Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory donât count as file access events.

TransitionToArchive -> (string)

The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory donât count as file access events.

Shorthand Syntax:

```
TransitionToIA=string,TransitionToPrimaryStorageClass=string,TransitionToArchive=string ...
```

JSON Syntax:

```
[
  {
    "TransitionToIA": "AFTER_7_DAYS"|"AFTER_14_DAYS"|"AFTER_30_DAYS"|"AFTER_60_DAYS"|"AFTER_90_DAYS"|"AFTER_1_DAY"|"AFTER_180_DAYS"|"AFTER_270_DAYS"|"AFTER_365_DAYS",
    "TransitionToPrimaryStorageClass": "AFTER_1_ACCESS",
    "TransitionToArchive": "AFTER_1_DAY"|"AFTER_7_DAYS"|"AFTER_14_DAYS"|"AFTER_30_DAYS"|"AFTER_60_DAYS"|"AFTER_90_DAYS"|"AFTER_180_DAYS"|"AFTER_270_DAYS"|"AFTER_365_DAYS"
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

LifecyclePolicies -> (list)

An array of lifecycle management policies. EFS supports a maximum of one policy per file system.

(structure)

Describes a policy used by lifecycle management that specifies when to transition files into and out of storage classes. For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) .

### Note

When using the `put-lifecycle-configuration` CLI command or the `PutLifecycleConfiguration` API action, Amazon EFS requires that each `LifecyclePolicy` object have only a single transition. This means that in a request body, `LifecyclePolicies` must be structured as an array of `LifecyclePolicy` objects, one object for each transition. For more information, see the request examples in  PutLifecycleConfiguration .

TransitionToIA -> (string)

The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory donât count as file access events.

TransitionToPrimaryStorageClass -> (string)

Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory donât count as file access events.

TransitionToArchive -> (string)

The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory donât count as file access events.