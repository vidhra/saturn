# create-scraperÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/create-scraper.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/create-scraper.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/index.html#cli-aws-amp) ]

# create-scraper

## Description

The `CreateScraper` operation creates a scraper to collect metrics. A scraper pulls metrics from Prometheus-compatible sources within an Amazon EKS cluster, and sends them to your Amazon Managed Service for Prometheus workspace. Scrapers are flexible, and can be configured to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your cluster. You must configure this role with a policy that allows it to scrape metrics from your cluster. For more information, see [Configuring your Amazon EKS cluster](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup) in the *Amazon Managed Service for Prometheus User Guide* .

The `scrapeConfiguration` parameter contains the base-64 encoded YAML configuration for the scraper.

### Note

For more information about collectors, including what metrics are collected, and how to configure the scraper, see [Using an Amazon Web Services managed collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) in the *Amazon Managed Service for Prometheus User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amp-2020-08-01/CreateScraper)

## Synopsis

```
create-scraper
[--alias <value>]
[--client-token <value>]
--destination <value>
[--role-configuration <value>]
--scrape-configuration <value>
--source <value>
[--tags <value>]
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

`--alias` (string)

(optional) An alias to associate with the scraper. This is for your use, and does not need to be unique.

`--client-token` (string)

(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.

`--destination` (tagged union structure)

The Amazon Managed Service for Prometheus workspace to send metrics to.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ampConfiguration`.

ampConfiguration -> (structure)

The Amazon Managed Service for Prometheus workspace to send metrics to.

workspaceArn -> (string)

ARN of the Amazon Managed Service for Prometheus workspace.

Shorthand Syntax:

```
ampConfiguration={workspaceArn=string}
```

JSON Syntax:

```
{
  "ampConfiguration": {
    "workspaceArn": "string"
  }
}
```

`--role-configuration` (structure)

Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.

sourceRoleArn -> (string)

The Amazon Resource Name (ARN) of the role used in the source account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write) .

targetRoleArn -> (string)

The Amazon Resource Name (ARN) of the role used in the target account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write) .

Shorthand Syntax:

```
sourceRoleArn=string,targetRoleArn=string
```

JSON Syntax:

```
{
  "sourceRoleArn": "string",
  "targetRoleArn": "string"
}
```

`--scrape-configuration` (tagged union structure)

The configuration file to use in the new scraper. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration) in the *Amazon Managed Service for Prometheus User Guide* .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `configurationBlob`.

configurationBlob -> (blob)

The base 64 encoded scrape configuration file.

Shorthand Syntax:

```
configurationBlob=blob
```

JSON Syntax:

```
{
  "configurationBlob": blob
}
```

`--source` (tagged union structure)

The Amazon EKS cluster from which the scraper will collect metrics.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `eksConfiguration`.

eksConfiguration -> (structure)

The Amazon EKS cluster from which a scraper collects metrics.

clusterArn -> (string)

ARN of the Amazon EKS cluster.

securityGroupIds -> (list)

A list of the security group IDs for the Amazon EKS cluster VPC configuration.

(string)

ID of a VPC security group.

subnetIds -> (list)

A list of subnet IDs for the Amazon EKS cluster VPC configuration.

(string)

ID of a VPC subnet.

Shorthand Syntax:

```
eksConfiguration={clusterArn=string,securityGroupIds=[string,string],subnetIds=[string,string]}
```

JSON Syntax:

```
{
  "eksConfiguration": {
    "clusterArn": "string",
    "securityGroupIds": ["string", ...],
    "subnetIds": ["string", ...]
  }
}
```

`--tags` (map)

(Optional) The list of tag keys and values to associate with the scraper.

key -> (string)

The key of the tag. Must not begin with `aws:` .

value -> (string)

The value of the tag.

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

arn -> (string)

The Amazon Resource Name (ARN) of the new scraper.

scraperId -> (string)

The ID of the new scraper.

status -> (structure)

A structure that displays the current status of the scraper.

statusCode -> (string)

The current status of the scraper.

tags -> (map)

The list of tag keys and values that are associated with the scraper.

key -> (string)

The key of the tag. Must not begin with `aws:` .

value -> (string)

The value of the tag.