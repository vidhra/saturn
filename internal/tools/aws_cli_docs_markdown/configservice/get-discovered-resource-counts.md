# get-discovered-resource-countsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-discovered-resource-counts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-discovered-resource-counts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# get-discovered-resource-counts

## Description

Returns the resource types, the number of each resource type, and the total number of resources that Config is recording in this region for your Amazon Web Services account.

**Example**

- Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets.
- You make a call to the `GetDiscoveredResourceCounts` action and specify that you want all resource types.
- Config returns the following:
- The resource types (EC2 instances, IAM users, and S3 buckets).
- The number of each resource type (25, 20, and 15).
- The total number of all resources (60).

The response is paginated. By default, Config lists 100  ResourceCount objects on each page. You can customize this number with the `limit` parameter. The response includes a `nextToken` string. To get the next page of results, run the request again and specify the string for the `nextToken` parameter.

### Note

If you make a call to the  GetDiscoveredResourceCounts action, you might not immediately receive resource counts in the following situations:

- You are a new Config customer.
- You just enabled resource recording.

It might take a few minutes for Config to record and count your resources. Wait a few minutes and then retry the  GetDiscoveredResourceCounts action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetDiscoveredResourceCounts)

## Synopsis

```
get-discovered-resource-counts
[--resource-types <value>]
[--limit <value>]
[--next-token <value>]
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

`--resource-types` (list)

The comma-separated list that specifies the resource types that you want Config to return (for example, `"AWS::EC2::Instance"` , `"AWS::IAM::User"` ).

If a value for `resourceTypes` is not specified, Config returns all resource types that Config is recording in the region for your account.

### Note

If the configuration recorder is turned off, Config returns an empty list of  ResourceCount objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of  ResourceCount objects.

(string)

Syntax:

```
"string" "string" ...
```

`--limit` (integer)

The maximum number of  ResourceCount objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.

`--next-token` (string)

The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.

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

totalDiscoveredResources -> (long)

The total number of resources that Config is recording in the region for your account. If you specify resource types in the request, Config returns only the total number of resources for those resource types.

**Example**

- Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.
- You make a call to the `GetDiscoveredResourceCounts` action and specify the resource type, `"AWS::EC2::Instances"` , in the request.
- Config returns 25 for `totalDiscoveredResources` .

resourceCounts -> (list)

The list of `ResourceCount` objects. Each object is listed in descending order by the number of resources.

(structure)

An object that contains the resource type and the number of resources.

resourceType -> (string)

The resource type (for example, `"AWS::EC2::Instance"` ).

count -> (long)

The number of resources.

nextToken -> (string)

The string that you use in a subsequent request to get the next page of results in a paginated response.