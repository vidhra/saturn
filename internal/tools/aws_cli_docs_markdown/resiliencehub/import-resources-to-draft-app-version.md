# import-resources-to-draft-app-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/import-resources-to-draft-app-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/import-resources-to-draft-app-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# import-resources-to-draft-app-version

## Description

Imports resources to Resilience Hub application draft version from different input sources. For more information about the input sources supported by Resilience Hub, see [Discover the structure and describe your Resilience Hub application](https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ImportResourcesToDraftAppVersion)

## Synopsis

```
import-resources-to-draft-app-version
--app-arn <value>
[--eks-sources <value>]
[--import-strategy <value>]
[--source-arns <value>]
[--terraform-sources <value>]
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

`--app-arn` (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

`--eks-sources` (list)

The input sources of the Amazon Elastic Kubernetes Service resources you need to import.

(structure)

The input source of the Amazon Elastic Kubernetes Service cluster.

eksClusterArn -> (string)

Amazon Resource Name (ARN) of the Amazon Elastic Kubernetes Service cluster. The format for this ARN is: arn:`aws` :eks:`region` :`account-id` :cluster/`cluster-name` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

namespaces -> (list)

The list of namespaces located on your Amazon Elastic Kubernetes Service cluster.

(string)

Shorthand Syntax:

```
eksClusterArn=string,namespaces=string,string ...
```

JSON Syntax:

```
[
  {
    "eksClusterArn": "string",
    "namespaces": ["string", ...]
  }
  ...
]
```

`--import-strategy` (string)

The import strategy you would like to set to import resources into Resilience Hub application.

Possible values:

- `AddOnly`
- `ReplaceAll`

`--source-arns` (list)

The Amazon Resource Names (ARNs) for the resources.

(string)

Syntax:

```
"string" "string" ...
```

`--terraform-sources` (list)

A list of terraform file s3 URLs you need to import.

(structure)

The Terraform s3 state file you need to import.

s3StateFileUrl -> (string)

The URL of the Terraform s3 state file you need to import.

Shorthand Syntax:

```
s3StateFileUrl=string ...
```

JSON Syntax:

```
[
  {
    "s3StateFileUrl": "string"
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

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

appVersion -> (string)

The version of the application.

eksSources -> (list)

The input sources of the Amazon Elastic Kubernetes Service resources you have imported.

(structure)

The input source of the Amazon Elastic Kubernetes Service cluster.

eksClusterArn -> (string)

Amazon Resource Name (ARN) of the Amazon Elastic Kubernetes Service cluster. The format for this ARN is: arn:`aws` :eks:`region` :`account-id` :cluster/`cluster-name` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

namespaces -> (list)

The list of namespaces located on your Amazon Elastic Kubernetes Service cluster.

(string)

sourceArns -> (list)

The Amazon Resource Names (ARNs) for the resources you have imported.

(string)

status -> (string)

Status of the action.

terraformSources -> (list)

A list of terraform file s3 URLs you have imported.

(structure)

The Terraform s3 state file you need to import.

s3StateFileUrl -> (string)

The URL of the Terraform s3 state file you need to import.