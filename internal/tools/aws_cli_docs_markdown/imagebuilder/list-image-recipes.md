# list-image-recipesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-recipes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-recipes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# list-image-recipes

## Description

Returns a list of image recipes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/ListImageRecipes)

## Synopsis

```
list-image-recipes
[--owner <value>]
[--filters <value>]
[--max-results <value>]
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

`--owner` (string)

The owner defines which image recipes you want to list. By default, this request will only show image recipes owned by your account. You can use this field to specify if you want to view image recipes owned by yourself, by Amazon, or those image recipes that have been shared with you by other customers.

Possible values:

- `Self`
- `Shared`
- `Amazon`
- `ThirdParty`
- `AWSMarketplace`

`--filters` (list)

Use the following filters to streamline results:

- `name`
- `parentImage`
- `platform`

(structure)

A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

name -> (string)

The name of the filter. Filter names are case-sensitive.

values -> (list)

The filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum items to return in a request.

`--next-token` (string)

A token to specify where to start paginating. This is the nextToken from a previously truncated response.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list image recipes**

The following `list-image-recipes` example lists all of your image recipes.

```
aws imagebuilder list-image-recipes
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "imageRecipeSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03",
            "name": "MyBasicRecipe",
            "platform": "Windows",
            "owner": "123456789012",
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/2019.x.x",
            "dateCreated": "2020-02-19T18:54:25.975Z",
            "tags": {
                "KeyName": "KeyValue"
            }
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/recipe-name-a1b2c3d45678/1.0.0",
            "name": "recipe-name-a1b2c3d45678",
            "platform": "Linux",
            "owner": "123456789012",
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2-x86/2019.11.21",
            "dateCreated": "2019-12-16T18:19:00.120Z",
            "tags": {
                "KeyName": "KeyValue"
            }
        }
    ]
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

imageRecipeSummaryList -> (list)

The list of image pipelines.

(structure)

A summary of an image recipe.

arn -> (string)

The Amazon Resource Name (ARN) of the image recipe.

name -> (string)

The name of the image recipe.

platform -> (string)

The platform of the image recipe.

owner -> (string)

The owner of the image recipe.

parentImage -> (string)

The base image of the image recipe.

dateCreated -> (string)

The date on which this image recipe was created.

tags -> (map)

The tags of the image recipe.

key -> (string)

value -> (string)

nextToken -> (string)

The next token used for paginated responses. When this field isnât empty, there are additional elements that the service hasnât included in this request. Use this token with the next request to retrieve additional objects.