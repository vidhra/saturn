# list-recommendation-templatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-recommendation-templates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-recommendation-templates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# list-recommendation-templates

## Description

Lists the recommendation templates for the Resilience Hub applications.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ListRecommendationTemplates)

## Synopsis

```
list-recommendation-templates
[--assessment-arn <value>]
[--max-results <value>]
[--name <value>]
[--next-token <value>]
[--recommendation-template-arn <value>]
[--reverse-order | --no-reverse-order]
[--status <value>]
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

`--assessment-arn` (string)

Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app-assessment/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

`--max-results` (integer)

Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.

`--name` (string)

The name for one of the listed recommendation templates.

`--next-token` (string)

Null, or the token from a previous call to get the next set of results.

`--recommendation-template-arn` (string)

The Amazon Resource Name (ARN) for a recommendation template.

`--reverse-order` | `--no-reverse-order` (boolean)

The default is to sort by ascending **startTime** . To sort by descending **startTime** , set reverseOrder to `true` .

`--status` (list)

Status of the action.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Pending
  InProgress
  Failed
  Success
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

nextToken -> (string)

Token for the next set of results, or null if there are no more results.

recommendationTemplates -> (list)

The recommendation templates for the Resilience Hub applications.

(structure)

Defines a recommendation template created with the  CreateRecommendationTemplate action.

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

assessmentArn -> (string)

Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app-assessment/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

endTime -> (timestamp)

The end time for the action.

format -> (string)

Format of the recommendation template.

CfnJson

The template is CloudFormation JSON.

CfnYaml

The template is CloudFormation YAML.

message -> (string)

Message for the recommendation template.

name -> (string)

Name for the recommendation template.

needsReplacements -> (boolean)

Indicates if replacements are needed.

recommendationIds -> (list)

Identifiers for the recommendations used in the recommendation template.

(string)

recommendationTemplateArn -> (string)

Amazon Resource Name (ARN) for the recommendation template.

recommendationTypes -> (list)

An array of strings that specify the recommendation template type or types.

Alarm

The template is an  AlarmRecommendation template.

Sop

The template is a  SopRecommendation template.

Test

The template is a  TestRecommendation template.

(string)

startTime -> (timestamp)

The start time for the action.

status -> (string)

Status of the action.

tags -> (map)

Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.

key -> (string)

value -> (string)

templatesLocation -> (structure)

The file location of the template.

bucket -> (string)

The name of the Amazon S3 bucket.

prefix -> (string)

The prefix for the Amazon S3 bucket.