# create-invalidation-for-distribution-tenantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-invalidation-for-distribution-tenant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-invalidation-for-distribution-tenant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# create-invalidation-for-distribution-tenant

## Description

Creates an invalidation for a distribution tenant. For more information, see [Invalidating files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) in the *Amazon CloudFront Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/CreateInvalidationForDistributionTenant)

## Synopsis

```
create-invalidation-for-distribution-tenant
--id <value>
--invalidation-batch <value>
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

`--id` (string)

The ID of the distribution tenant.

`--invalidation-batch` (structure)

An invalidation batch.

Paths -> (structure)

A complex type that contains information about the objects that you want to invalidate. For more information, see [Specifying the Objects to Invalidate](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of invalidation paths specified for the objects that you want to invalidate.

Items -> (list)

A complex type that contains a list of the paths that you want to invalidate.

(string)

CallerReference -> (string)

A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for `CallerReference` and change other values in the request as applicable. One way to ensure that the value of `CallerReference` is unique is to use a `timestamp` , for example, `20120301090000` .

If you make a second invalidation request with the same value for `CallerReference` , and if the rest of the request is the same, CloudFront doesnât create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same `CallerReference` .

If `CallerReference` is a value you already sent in a previous invalidation batch request but the content of any `Path` is different from the original request, CloudFront returns an `InvalidationBatchAlreadyExists` error.

Shorthand Syntax:

```
Paths={Quantity=integer,Items=[string,string]},CallerReference=string
```

JSON Syntax:

```
{
  "Paths": {
    "Quantity": integer,
    "Items": ["string", ...]
  },
  "CallerReference": "string"
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

Location -> (string)

The location for the invalidation.

Invalidation -> (structure)

An invalidation.

Id -> (string)

The identifier for the invalidation request. For example: `IDFDVBD632BHDS5` .

Status -> (string)

The status of the invalidation request. When the invalidation batch is finished, the status is `Completed` .

CreateTime -> (timestamp)

The date and time the invalidation request was first made.

InvalidationBatch -> (structure)

The current invalidation information for the batch request.

Paths -> (structure)

A complex type that contains information about the objects that you want to invalidate. For more information, see [Specifying the Objects to Invalidate](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of invalidation paths specified for the objects that you want to invalidate.

Items -> (list)

A complex type that contains a list of the paths that you want to invalidate.

(string)

CallerReference -> (string)

A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for `CallerReference` and change other values in the request as applicable. One way to ensure that the value of `CallerReference` is unique is to use a `timestamp` , for example, `20120301090000` .

If you make a second invalidation request with the same value for `CallerReference` , and if the rest of the request is the same, CloudFront doesnât create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same `CallerReference` .

If `CallerReference` is a value you already sent in a previous invalidation batch request but the content of any `Path` is different from the original request, CloudFront returns an `InvalidationBatchAlreadyExists` error.