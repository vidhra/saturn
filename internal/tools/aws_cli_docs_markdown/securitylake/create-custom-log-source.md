# create-custom-log-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securitylake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html#cli-aws-securitylake) ]

# create-custom-log-source

## Description

Adds a third-party custom source in Amazon Security Lake, from the Amazon Web Services Region where you want to create a custom source. Security Lake can collect logs and events from third-party custom sources. After creating the appropriate IAM role to invoke Glue crawler, use this API to add a custom source name in Security Lake. This operation creates a partition in the Amazon S3 bucket for Security Lake as the target location for log files from the custom source. In addition, this operation also creates an associated Glue table and an Glue crawler.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securitylake-2018-05-10/CreateCustomLogSource)

## Synopsis

```
create-custom-log-source
--configuration <value>
[--event-classes <value>]
--source-name <value>
[--source-version <value>]
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

`--configuration` (structure)

The configuration used for the third-party custom source.

crawlerConfiguration -> (structure)

The configuration used for the Glue Crawler for a third-party custom source.

roleArn -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be used by the Glue crawler. The recommended IAM policies are:

- The managed policy `AWSGlueServiceRole`
- A custom policy granting access to your Amazon S3 Data Lake

providerIdentity -> (structure)

The identity of the log provider for the third-party custom source.

externalId -> (string)

The external ID used to establish trust relationship with the Amazon Web Services identity.

principal -> (string)

The Amazon Web Services identity principal.

Shorthand Syntax:

```
crawlerConfiguration={roleArn=string},providerIdentity={externalId=string,principal=string}
```

JSON Syntax:

```
{
  "crawlerConfiguration": {
    "roleArn": "string"
  },
  "providerIdentity": {
    "externalId": "string",
    "principal": "string"
  }
}
```

`--event-classes` (list)

The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass) .

(string)

Syntax:

```
"string" "string" ...
```

`--source-name` (string)

Specify the name for a third-party custom source. This must be a Regionally unique value. The `sourceName` you enter here, is used in the `LogProviderRole` name which follows the convention `AmazonSecurityLake-Provider-{name of the custom source}-{region}` . You must use a `CustomLogSource` name that is shorter than or equal to 20 characters. This ensures that the `LogProviderRole` name is below the 64 character limit.

`--source-version` (string)

Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.

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

**To add a custom source as an Amazon Security Lake source**

The following `create-custom-logsource` example adds a custom source as a Security Lake source in the designated log provider account and the designated Region.

```
aws securitylake create-custom-log-source \
    --source-name "VPC_FLOW" \
    --event-classes '["DNS_ACTIVITY", "NETWORK_ACTIVITY"]' \
    --configuration '{"crawlerConfiguration": {"roleArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4"},"providerIdentity": {"principal": "029189416600","externalId": "123456789012"}}' --region "us-east-1"
```

Output:

```
{
    "customLogSource": {
        "attributes": {
            "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4",
            "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/E1WG1ZNPRXT0D4",
            "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/E1WG1ZNPRXT0D4"
        },
        "provider": {
            "location": "amzn-s3-demo-bucket--usw2-az1--x-s3",
            "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-Provider-testCustom2-eu-west-2"
        },
        "sourceName": "testCustom2"
        "sourceVersion": "2.0"
    }
}
```

For more information, see [Adding a custom source](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html#adding-custom-sources) in the *Amazon Security Lake User Guide*.

## Output

source -> (structure)

The third-party custom source that was created.

attributes -> (structure)

The attributes of a third-party custom source.

crawlerArn -> (string)

The ARN of the Glue crawler.

databaseArn -> (string)

The ARN of the Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*` .

tableArn -> (string)

The ARN of the Glue table.

provider -> (structure)

The details of the log provider for a third-party custom source.

location -> (string)

The location of the partition in the Amazon S3 bucket for Security Lake.

roleArn -> (string)

The ARN of the IAM role to be used by the entity putting logs into your custom source partition. Security Lake will apply the correct access policies to this role, but you must first manually create the trust policy for this role. The IAM role name must start with the text âSecurity Lakeâ. The IAM role must trust the `logProviderAccountId` to assume the role.

sourceName -> (string)

The name for a third-party custom source. This must be a Regionally unique value.

sourceVersion -> (string)

The version for a third-party custom source. This must be a Regionally unique value.