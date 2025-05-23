# put-repository-catalog-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/put-repository-catalog-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/put-repository-catalog-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr-public](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/index.html#cli-aws-ecr-public) ]

# put-repository-catalog-data

## Description

Creates or updates the catalog data for a repository in a public registry.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-public-2020-10-30/PutRepositoryCatalogData)

## Synopsis

```
put-repository-catalog-data
[--registry-id <value>]
--repository-name <value>
--catalog-data <value>
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

`--registry-id` (string)

The Amazon Web Services account ID thatâs associated with the public registry the repository is in. If you do not specify a registry, the default public registry is assumed.

`--repository-name` (string)

The name of the repository to create or update the catalog data for.

`--catalog-data` (structure)

An object containing the catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.

description -> (string)

A short description of the contents of the repository. This text appears in both the image details and also when searching for repositories on the Amazon ECR Public Gallery.

architectures -> (list)

The system architecture that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported architectures appear as badges on the repository and are used as search filters.

### Note

If an unsupported tag is added to your repository catalog data, itâs associated with the repository and can be retrieved using the API but isnât discoverable in the Amazon ECR Public Gallery.

- `ARM`
- `ARM 64`
- `x86`
- `x86-64`

(string)

operatingSystems -> (list)

The operating systems that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported operating systems appear as badges on the repository and are used as search filters.

### Note

If an unsupported tag is added to your repository catalog data, itâs associated with the repository and can be retrieved using the API but isnât discoverable in the Amazon ECR Public Gallery.

- `Linux`
- `Windows`

(string)

logoImageBlob -> (blob)

The base64-encoded repository logo payload.

### Note

The repository logo is only publicly visible in the Amazon ECR Public Gallery for verified accounts.

aboutText -> (string)

A detailed description of the contents of the repository. Itâs publicly visible in the Amazon ECR Public Gallery. The text must be in markdown format.

usageText -> (string)

Detailed information about how to use the contents of the repository. Itâs publicly visible in the Amazon ECR Public Gallery. The usage text provides context, support information, and additional usage details for users of the repository. The text must be in markdown format.

Shorthand Syntax:

```
description=string,architectures=string,string,operatingSystems=string,string,logoImageBlob=blob,aboutText=string,usageText=string
```

JSON Syntax:

```
{
  "description": "string",
  "architectures": ["string", ...],
  "operatingSystems": ["string", ...],
  "logoImageBlob": blob,
  "aboutText": "string",
  "usageText": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create or update the catalog data for a repository in a public registry**

The following `put-repository-catalog-data` example creates or update catalog data for reposiotry named project-a/nginx-web-app in a public registry, along with logoImageBlob, aboutText, usageText and tags information.

```
aws ecr-public put-repository-catalog-data \
    --repository-name project-a/nginx-web-app \
    --cli-input-json file://repository-catalog-data.json \
    --region us-east-1
```

Contents of `repository-catalog-data.json`:

```
{
    "repositoryName": "project-a/nginx-web-app",
    "catalogData": {
        "description": "My project-a ECR Public Repository",
        "architectures": [
            "ARM",
            "ARM 64",
            "x86",
            "x86-64"
        ],
        "operatingSystems": [
            "Linux"
        ],
        "logoImageBlob": "iVBORw0KGgoA<<truncated-for-better-reading>>ErkJggg==",
        "aboutText": "## Quick reference.",
        "usageText": "## Supported architectures are as follows."
    }
}
```

Output:

```
{
    "catalogData": {
        "description": "My project-a ECR Public Repository",
        "architectures": [
            "ARM",
            "ARM 64",
            "x86",
            "x86-64"
        ],
        "operatingSystems": [
            "Linux"
        ],
        "logoUrl": "https://d3g9o9u8re44ak.cloudfront.net/logo/df86cf58-ee60-4061-b804-0be24d97ccb1/4a9ed9b2-69e4-4ede-b924-461462d20ef0.png",
        "aboutText": "## Quick reference.",
        "usageText": "## Supported architectures are as follows."
    }
}
```

For more information, see [Repository catalog data](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html) in the *Amazon ECR Public*.

## Output

catalogData -> (structure)

The catalog data for the repository.

description -> (string)

The short description of the repository.

architectures -> (list)

The architecture tags that are associated with the repository.

### Note

Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see  RepositoryCatalogDataInput .

(string)

operatingSystems -> (list)

The operating system tags that are associated with the repository.

### Note

Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see  RepositoryCatalogDataInput .

(string)

logoUrl -> (string)

The URL that contains the logo thatâs associated with the repository.

aboutText -> (string)

The longform description of the contents of the repository. This text appears in the repository details on the Amazon ECR Public Gallery.

usageText -> (string)

The longform usage details of the contents of the repository. The usage text provides context for users of the repository.

marketplaceCertified -> (boolean)

Indicates whether the repository is certified by Amazon Web Services Marketplace.