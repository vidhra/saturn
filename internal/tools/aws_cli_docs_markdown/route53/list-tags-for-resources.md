# list-tags-for-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-tags-for-resources

## Description

Lists tags for up to 10 health checks or hosted zones.

For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *Billing and Cost Management User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTagsForResources)

## Synopsis

```
list-tags-for-resources
--resource-type <value>
--resource-ids <value>
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

`--resource-type` (string)

The type of the resources.

- The resource type for health checks is `healthcheck` .
- The resource type for hosted zones is `hostedzone` .

Possible values:

- `healthcheck`
- `hostedzone`

`--resource-ids` (list)

A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.

(string)

Syntax:

```
"string" "string" ...
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

ResourceTagSets -> (list)

A list of `ResourceTagSet` s containing tags associated with the specified resources.

(structure)

A complex type containing a resource and its associated tags.

ResourceType -> (string)

The type of the resource.

- The resource type for health checks is `healthcheck` .
- The resource type for hosted zones is `hostedzone` .

ResourceId -> (string)

The ID for the specified resource.

Tags -> (list)

The tags associated with the specified resource.

(structure)

A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

Key -> (string)

The value of `Key` depends on the operation that you want to perform:

- **Add a tag to a health check or hosted zone** : `Key` is the name that you want to give the new tag.
- **Edit a tag** : `Key` is the name of the tag that you want to change the `Value` for.
- **Delete a key** : `Key` is the name of the tag you want to remove.
- **Give a name to a health check** : Edit the default `Name` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that youâve given to each health check.

Value -> (string)

The value of `Value` depends on the operation that you want to perform:

- **Add a tag to a health check or hosted zone** : `Value` is the value that you want to give the new tag.
- **Edit a tag** : `Value` is the new value that you want to assign the tag.