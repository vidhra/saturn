# start-export-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-export-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-export-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html#cli-aws-discovery) ]

# start-export-task

## Description

Begins the export of a discovered data report to an Amazon S3 bucket managed by Amazon Web Services.

### Note

Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of Amazon Web Services services, which might vary from the estimates provided in this report.

If you do not specify `preferences` or `agentIds` in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.

If you specify `agentIds` in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using `startTime` and `endTime` . Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.

If you enable `ec2RecommendationsPreferences` in `preferences` , an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the `ec2RecommendationsPreferences` changes the criteria of the recommendation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/StartExportTask)

## Synopsis

```
start-export-task
[--export-data-format <value>]
[--filters <value>]
[--start-time <value>]
[--end-time <value>]
[--preferences <value>]
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

`--export-data-format` (list)

The file format for the returned export data. Default value is `CSV` . **Note:** *The* `GRAPHML` *option has been deprecated.*

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CSV
```

`--filters` (list)

If a filter is present, it selects the single `agentId` of the Application Discovery Agent for which data is exported. The `agentId` can be found in the results of the `DescribeAgents` API or CLI. If no filter is present, `startTime` and `endTime` are ignored and exported data includes both Amazon Web Services Application Discovery Service Agentless Collector collectors data and summary data from Application Discovery Agent agents.

(structure)

Used to select which agentâs data is to be exported. A single agent ID may be selected for export using the [StartExportTask](http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html) action.

name -> (string)

A single `ExportFilter` name. Supported filters: `agentIds` .

values -> (list)

A single agent ID for a Discovery Agent. An agent ID can be found using the [DescribeAgents](http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeAgents.html) action. Typically an ADS agent ID is in the form `o-0123456789abcdef0` .

(string)

condition -> (string)

Supported condition: `EQUALS`

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

`--start-time` (timestamp)

The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.

`--end-time` (timestamp)

The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.

`--preferences` (tagged union structure)

Indicates the type of data that needs to be exported. Only one [ExportPreferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html) can be enabled at any time.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ec2RecommendationsPreferences`.

ec2RecommendationsPreferences -> (structure)

If enabled, exported data includes EC2 instance type matches for on-premises servers discovered through Amazon Web Services Application Discovery Service.

enabled -> (boolean)

If set to true, the export [preferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html#API_StartExportTask_RequestSyntax) is set to `Ec2RecommendationsExportPreferences` .

cpuPerformanceMetricBasis -> (structure)

The recommended EC2 instance type that matches the CPU usage metric of server performance data.

name -> (string)

A utilization metric that is used by the recommendations.

percentageAdjust -> (double)

Specifies the percentage of the specified utilization metric that is used by the recommendations.

ramPerformanceMetricBasis -> (structure)

The recommended EC2 instance type that matches the Memory usage metric of server performance data.

name -> (string)

A utilization metric that is used by the recommendations.

percentageAdjust -> (double)

Specifies the percentage of the specified utilization metric that is used by the recommendations.

tenancy -> (string)

The target tenancy to use for your recommended EC2 instances.

excludedInstanceTypes -> (list)

An array of instance types to exclude from recommendations.

(string)

preferredRegion -> (string)

The target Amazon Web Services Region for the recommendations. You can use any of the Region codes available for the chosen service, as listed in [Amazon Web Services service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference* .

reservedInstanceOptions -> (structure)

The contract type for a reserved instance. If blank, we assume an On-Demand instance is preferred.

purchasingOption -> (string)

The payment plan to use for your Reserved Instance.

offeringClass -> (string)

The flexibility to change the instance types needed for your Reserved Instance.

termLength -> (string)

The preferred duration of the Reserved Instance term.

Shorthand Syntax:

```
ec2RecommendationsPreferences={enabled=boolean,cpuPerformanceMetricBasis={name=string,percentageAdjust=double},ramPerformanceMetricBasis={name=string,percentageAdjust=double},tenancy=string,excludedInstanceTypes=[string,string],preferredRegion=string,reservedInstanceOptions={purchasingOption=string,offeringClass=string,termLength=string}}
```

JSON Syntax:

```
{
  "ec2RecommendationsPreferences": {
    "enabled": true|false,
    "cpuPerformanceMetricBasis": {
      "name": "string",
      "percentageAdjust": double
    },
    "ramPerformanceMetricBasis": {
      "name": "string",
      "percentageAdjust": double
    },
    "tenancy": "DEDICATED"|"SHARED",
    "excludedInstanceTypes": ["string", ...],
    "preferredRegion": "string",
    "reservedInstanceOptions": {
      "purchasingOption": "ALL_UPFRONT"|"PARTIAL_UPFRONT"|"NO_UPFRONT",
      "offeringClass": "STANDARD"|"CONVERTIBLE",
      "termLength": "ONE_YEAR"|"THREE_YEAR"
    }
  }
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

## Output

exportId -> (string)

A unique identifier used to query the status of an export request.