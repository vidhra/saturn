# list-protectionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [shield](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/index.html#cli-aws-shield) ]

# list-protections

## Description

Retrieves  Protection objects for the account. You can retrieve all protections or you can provide filtering criteria and retrieve just the subset of protections that match the criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListProtections)

`list-protections` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Protections`

## Synopsis

```
list-protections
[--inclusion-filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--inclusion-filters` (structure)

Narrows the set of protections that the call retrieves. You can retrieve a single protection by providing its name or the ARN (Amazon Resource Name) of its protected resource. You can also retrieve all protections for a specific resource type. You can provide up to one criteria per filter type. Shield Advanced returns protections that exactly match all of the filter criteria that you provide.

ResourceArns -> (list)

The ARN (Amazon Resource Name) of the resource whose protection you want to retrieve.

(string)

ProtectionNames -> (list)

The name of the protection that you want to retrieve.

(string)

ResourceTypes -> (list)

The type of protected resource whose protections you want to retrieve.

(string)

Shorthand Syntax:

```
ResourceArns=string,string,ProtectionNames=string,string,ResourceTypes=string,string
```

JSON Syntax:

```
{
  "ResourceArns": ["string", ...],
  "ProtectionNames": ["string", ...],
  "ResourceTypes": ["CLOUDFRONT_DISTRIBUTION"|"ROUTE_53_HOSTED_ZONE"|"ELASTIC_IP_ALLOCATION"|"CLASSIC_LOAD_BALANCER"|"APPLICATION_LOAD_BALANCER"|"GLOBAL_ACCELERATOR", ...]
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve protection summaries from AWS Shield Advanced**

The following `list-protections` example retrieves summaries of the protections that are enabled for the account.

```
aws shield list-protections
```

Output:

```
{
    "Protections": [
        {
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Name": "Protection for CloudFront distribution",
            "ResourceArn": "arn:aws:cloudfront::123456789012:distribution/E198WC25FXOWY8"
        }
    ]
}
```

For more information, see [Specify Your Resources to Protect](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html) in the *AWS Shield Advanced Developer Guide*.

## Output

Protections -> (list)

The array of enabled  Protection objects.

(structure)

An object that represents a resource that is under DDoS protection.

Id -> (string)

The unique identifier (ID) of the protection.

Name -> (string)

The name of the protection. For example, `My CloudFront distributions` .

ResourceArn -> (string)

The ARN (Amazon Resource Name) of the Amazon Web Services resource that is protected.

HealthCheckIds -> (list)

The unique identifier (ID) for the Route 53 health check thatâs associated with the protection.

(string)

ProtectionArn -> (string)

The ARN (Amazon Resource Name) of the protection.

ApplicationLayerAutomaticResponseConfiguration -> (structure)

The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.

Status -> (string)

Indicates whether automatic application layer DDoS mitigation is enabled for the protection.

Action -> (structure)

Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.

Block -> (structure)

Specifies that Shield Advanced should configure its WAF rules with the WAF `Block` action.

You must specify exactly one action, either `Block` or `Count` .

Count -> (structure)

Specifies that Shield Advanced should configure its WAF rules with the WAF `Count` action.

You must specify exactly one action, either `Block` or `Count` .

NextToken -> (string)

When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.

You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.

Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.