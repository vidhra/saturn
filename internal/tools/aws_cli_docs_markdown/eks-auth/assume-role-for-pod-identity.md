# assume-role-for-pod-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks-auth/assume-role-for-pod-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks-auth/assume-role-for-pod-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks-auth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks-auth/index.html#cli-aws-eks-auth) ]

# assume-role-for-pod-identity

## Description

The Amazon EKS Auth API and the `AssumeRoleForPodIdentity` action are only used by the EKS Pod Identity Agent.

We recommend that applications use the Amazon Web Services SDKs to connect to Amazon Web Services services; if credentials from an EKS Pod Identity association are available in the pod, the latest versions of the SDKs use them automatically.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-auth-2023-11-26/AssumeRoleForPodIdentity)

## Synopsis

```
assume-role-for-pod-identity
--cluster-name <value>
--token <value>
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

`--cluster-name` (string)

The name of the cluster for the request.

`--token` (string)

The token of the Kubernetes service account for the pod.

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

subject -> (structure)

The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.

namespace -> (string)

The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the pods that use the service account must be in this namespace.

serviceAccount -> (string)

The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.

audience -> (string)

The identity that is allowed to use the credentials. This value is always `pods.eks.amazonaws.com` .

podIdentityAssociation -> (structure)

The Amazon Resource Name (ARN) and ID of the EKS Pod Identity association.

associationArn -> (string)

The Amazon Resource Name (ARN) of the EKS Pod Identity association.

associationId -> (string)

The ID of the association.

assumedRoleUser -> (structure)

An object with the permanent IAM role identity and the temporary session name.

The ARN of the IAM role that the temporary credentials authenticate to.

The session name of the temporary session requested to STS. The value is a unique identifier that contains the role ID, a colon (`:` ), and the role session name of the role that is being assumed. The role ID is generated by IAM when the role is created. The role session name part of the value follows this format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks-auth/assume-role-for-pod-identity.html#id1)eks-*clustername* -*podname* -*random UUID* ``

arn -> (string)

The ARN of the IAM role that the temporary credentials authenticate to.

assumeRoleId -> (string)

The session name of the temporary session requested to STS. The value is a unique identifier that contains the role ID, a colon (`:` ), and the role session name of the role that is being assumed. The role ID is generated by IAM when the role is created. The role session name part of the value follows this format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks-auth/assume-role-for-pod-identity.html#id3)eks-*clustername* -*podname* -*random UUID* ``

credentials -> (structure)

The *Amazon Web Services Signature Version 4* type of temporary credentials.

sessionToken -> (string)

The token that applications inside the pods must pass to any service API to use the temporary credentials.

secretAccessKey -> (string)

The secret access key that applications inside the pods use to sign requests.

accessKeyId -> (string)

The access key ID that identifies the temporary security credentials.

expiration -> (timestamp)

The Unix epoch timestamp in seconds when the current credentials expire.