# list-virtual-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-virtual-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-virtual-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# list-virtual-clusters

## Description

Lists information about the specified virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-containers-2020-10-01/ListVirtualClusters)

`list-virtual-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `virtualClusters`

## Synopsis

```
list-virtual-clusters
[--container-provider-id <value>]
[--container-provider-type <value>]
[--created-after <value>]
[--created-before <value>]
[--states <value>]
[--eks-access-entry-integrated | --no-eks-access-entry-integrated]
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

`--container-provider-id` (string)

The container provider ID of the virtual cluster.

`--container-provider-type` (string)

The container provider type of the virtual cluster. Amazon EKS is the only supported type as of now.

Possible values:

- `EKS`

`--created-after` (timestamp)

The date and time after which the virtual clusters are created.

`--created-before` (timestamp)

The date and time before which the virtual clusters are created.

`--states` (list)

The states of the requested virtual clusters.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  RUNNING
  TERMINATING
  TERMINATED
  ARRESTED
```

`--eks-access-entry-integrated` | `--no-eks-access-entry-integrated` (boolean)

Optional Boolean that specifies whether the operation should return the virtual clusters that have the access entry integration enabled or disabled. If not specified, the operation returns all applicable virtual clusters.

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

## Output

virtualClusters -> (list)

This output lists the specified virtual clusters.

(structure)

This entity describes a virtual cluster. A virtual cluster is a Kubernetes namespace that Amazon EMR is registered with. Amazon EMR uses virtual clusters to run jobs and host endpoints. Multiple virtual clusters can be backed by the same physical cluster. However, each virtual cluster maps to one namespace on an Amazon EKS cluster. Virtual clusters do not create any active resources that contribute to your bill or that require lifecycle management outside the service.

id -> (string)

The ID of the virtual cluster.

name -> (string)

The name of the virtual cluster.

arn -> (string)

The ARN of the virtual cluster.

state -> (string)

The state of the virtual cluster.

containerProvider -> (structure)

The container provider of the virtual cluster.

type -> (string)

The type of the container provider. Amazon EKS is the only supported type as of now.

id -> (string)

The ID of the container cluster.

info -> (tagged union structure)

The information about the container cluster.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `eksInfo`.

eksInfo -> (structure)

The information about the Amazon EKS cluster.

namespace -> (string)

The namespaces of the Amazon EKS cluster.

createdAt -> (timestamp)

The date and time when the virtual cluster is created.

tags -> (map)

The assigned tags of the virtual cluster.

key -> (string)

value -> (string)

securityConfigurationId -> (string)

The ID of the security configuration.

nextToken -> (string)

This output displays the token for the next set of virtual clusters.