# list-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/list-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/list-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html#cli-aws-discovery) ]

# list-configurations

## Description

Retrieves a list of configuration items as specified by the value passed to the required parameter `configurationType` . Optional filtering may be applied to refine search results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/ListConfigurations)

`list-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `configurations`

## Synopsis

```
list-configurations
--configuration-type <value>
[--filters <value>]
[--order-by <value>]
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

`--configuration-type` (string)

A valid configuration identified by Application Discovery Service.

Possible values:

- `SERVER`
- `PROCESS`
- `CONNECTION`
- `APPLICATION`

`--filters` (list)

You can filter the request using various logical operators and a *key* -*value* format. For example:

`{"key": "serverType", "value": "webServer"}`

For a complete list of filter options and guidance about using them with this action, see [Using the ListConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations) in the *Amazon Web Services Application Discovery Service User Guide* .

(structure)

A filter that can use conditional operators.

For more information about filters, see [Querying Discovered Configuration Items](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html) in the *Amazon Web Services Application Discovery Service User Guide* .

name -> (string)

The name of the filter.

values -> (list)

A string value on which to filter. For example, if you choose the `destinationServer.osVersion` filter name, you could specify `Ubuntu` for the value.

(string)

condition -> (string)

A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND* . If you specify multiple values for a particular filter, the system differentiates the values using *OR* . Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.

Shorthand Syntax:

```
name=string,values=string,string,condition=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...],
    "condition": "string"
  }
  ...
]
```

`--order-by` (list)

Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see [Using the ListConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations) in the *Amazon Web Services Application Discovery Service User Guide* .

(structure)

A field and direction for ordered output.

fieldName -> (string)

The field on which to order.

sortOrder -> (string)

Ordering direction.

Shorthand Syntax:

```
fieldName=string,sortOrder=string ...
```

JSON Syntax:

```
[
  {
    "fieldName": "string",
    "sortOrder": "ASC"|"DESC"
  }
  ...
]
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

**To list all of the discovered servers meeting a set of filter conditions**

This example command lists discovered servers matching either of two hostname patterns and not running Ubuntu.

Command:

```
aws discovery list-configurations --configuration-type SERVER --filters name="server.hostName",values="172-31-35","172-31-42",condition="CONTAINS" name="server.osName",values="Ubuntu",condition="NOT_CONTAINS"
```

Output:

```
{
    "configurations": [
      {
            "server.osVersion": "3.14.48-33.39.amzn1.x86_64",
            "server.type": "EC2",
            "server.hostName": "ip-172-31-42-208",
            "server.timeOfCreation": "2016-10-28 23:44:30.0",
            "server.configurationId": "d-server-099385097ef9fbcfb",
            "server.osName": "Linux - Amazon Linux AMI release 2015.03",
            "server.agentId": "i-c142b99e"
        },
        {
            "server.osVersion": "3.14.48-33.39.amzn1.x86_64",
            "server.type": "EC2",
            "server.hostName": "ip-172-31-35-152",
            "server.timeOfCreation": "2016-10-28 23:44:00.0",
            "server.configurationId": "d-server-0c4f2dd1fee22c6c1",
            "server.osName": "Linux - Amazon Linux AMI release 2015.03",
            "server.agentId": "i-4447bc1b"
        }
    ]
}
```

## Output

configurations -> (list)

Returns configuration details, including the configuration ID, attribute names, and attribute values.

(map)

key -> (string)

value -> (string)

nextToken -> (string)

Token to retrieve the next set of results. For example, if your call to ListConfigurations returned 100 items, but you set `ListConfigurationsRequest$maxResults` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.