# create-package-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/create-package-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/create-package-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [panorama](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/panorama/index.html#cli-aws-panorama) ]

# create-package-import-job

## Description

Imports a node package.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/panorama-2019-07-24/CreatePackageImportJob)

## Synopsis

```
create-package-import-job
--client-token <value>
--input-config <value>
[--job-tags <value>]
--job-type <value>
--output-config <value>
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

`--client-token` (string)

A client token for the package import job.

`--input-config` (structure)

An input config for the package import job.

PackageVersionInputConfig -> (structure)

The package versionâs input configuration.

S3Location -> (structure)

A location in Amazon S3.

BucketName -> (string)

A bucket name.

ObjectKey -> (string)

An object key.

Region -> (string)

The bucketâs Region.

Shorthand Syntax:

```
PackageVersionInputConfig={S3Location={BucketName=string,ObjectKey=string,Region=string}}
```

JSON Syntax:

```
{
  "PackageVersionInputConfig": {
    "S3Location": {
      "BucketName": "string",
      "ObjectKey": "string",
      "Region": "string"
    }
  }
}
```

`--job-tags` (list)

Tags for the package import job.

(structure)

Tags for a job.

ResourceType -> (string)

The jobâs type.

Tags -> (map)

The jobâs tags.

key -> (string)

value -> (string)

Shorthand Syntax:

```
ResourceType=string,Tags={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "PACKAGE",
    "Tags": {"string": "string"
      ...}
  }
  ...
]
```

`--job-type` (string)

A job type for the package import job.

Possible values:

- `NODE_PACKAGE_VERSION`
- `MARKETPLACE_NODE_PACKAGE_VERSION`

`--output-config` (structure)

An output config for the package import job.

PackageVersionOutputConfig -> (structure)

The package versionâs output configuration.

MarkLatest -> (boolean)

Indicates that the version is recommended for all users.

PackageName -> (string)

The outputâs package name.

PackageVersion -> (string)

The outputâs package version.

Shorthand Syntax:

```
PackageVersionOutputConfig={MarkLatest=boolean,PackageName=string,PackageVersion=string}
```

JSON Syntax:

```
{
  "PackageVersionOutputConfig": {
    "MarkLatest": true|false,
    "PackageName": "string",
    "PackageVersion": "string"
  }
}
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

JobId -> (string)

The jobâs ID.