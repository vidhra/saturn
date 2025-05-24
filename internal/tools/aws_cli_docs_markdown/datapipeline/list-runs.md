# list-runsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-runs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-runs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datapipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/index.html#cli-aws-datapipeline) ]

# list-runs

## Description

Lists the times the specified pipeline has run. You can optionally filter the complete list of results to include only the runs you are interested in.

## Synopsis

```
list-runs
--pipeline-id <value>
[--status <value>]
[--start-interval <value>]
[--schedule-interval <value>]
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

`--pipeline-id` (string)
The identifier of the pipeline.

`--status` (string)
Filters the list to include only runs in the specified statuses. The valid statuses are as follows: waiting, pending, cancelled, running, finished, failed, waiting_for_runner, and waiting_on_dependencies.

`--start-interval` (string)
Filters the list to include only runs that started within the specified interval.

`--schedule-interval` (string)
Filters the list to include only runs that are scheduled to start within the specified interval.

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

**Example 1: To list your pipeline runs**

The following `list-runs` example lists the runs for the specified pipeline.

```
aws datapipeline list-runs --pipeline-id df-00627471SOVYZEXAMPLE
```

Output:

```
Name                       Scheduled Start        Status                     ID                                              Started                Ended
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1.  EC2ResourceObj             2015-04-12T17:33:02    CREATING                   @EC2ResourceObj_2015-04-12T17:33:02             2015-04-12T17:33:10
2.  S3InputLocation            2015-04-12T17:33:02    FINISHED                   @S3InputLocation_2015-04-12T17:33:02            2015-04-12T17:33:09    2015-04-12T17:33:09
3.  S3OutputLocation           2015-04-12T17:33:02    WAITING_ON_DEPENDENCIES    @S3OutputLocation_2015-04-12T17:33:02           2015-04-12T17:33:09
4.  ShellCommandActivityObj    2015-04-12T17:33:02    WAITING_FOR_RUNNER         @ShellCommandActivityObj_2015-04-12T17:33:02    2015-04-12T17:33:09
```

**Example 2: To list the pipeline runs between the specified dates**

The following `list-runs` example uses the `--start-interval` to specify the dates to include in the output.

```
aws datapipeline list-runs --pipeline-id df-01434553B58A2SHZUKO5 --start-interval 2017-10-07T00:00:00,2017-10-08T00:00:00
```