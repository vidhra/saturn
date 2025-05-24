# create-pull-through-cache-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-pull-through-cache-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-pull-through-cache-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html#cli-aws-ecr) ]

# create-pull-through-cache-rule

## Description

Creates a pull through cache rule. A pull through cache rule provides a way to cache images from an upstream registry source in your Amazon ECR private registry. For more information, see [Using pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) in the *Amazon Elastic Container Registry User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/CreatePullThroughCacheRule)

## Synopsis

```
create-pull-through-cache-rule
--ecr-repository-prefix <value>
--upstream-registry-url <value>
[--registry-id <value>]
[--upstream-registry <value>]
[--credential-arn <value>]
[--custom-role-arn <value>]
[--upstream-repository-prefix <value>]
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

`--ecr-repository-prefix` (string)

The repository name prefix to use when caching images from the source registry.

### Warning

There is always an assumed `/` applied to the end of the prefix. If you specify `ecr-public` as the prefix, Amazon ECR treats that as `ecr-public/` .

`--upstream-registry-url` (string)

The registry URL of the upstream public registry to use as the source for the pull through cache rule. The following is the syntax to use for each supported upstream registry.

- Amazon ECR (`ecr` ) â `dkr.ecr.<region>.amazonaws.com`
- Amazon ECR Public (`ecr-public` ) â `public.ecr.aws`
- Docker Hub (`docker-hub` ) â `registry-1.docker.io`
- GitHub Container Registry (`github-container-registry` ) â `ghcr.io`
- GitLab Container Registry (`gitlab-container-registry` ) â `registry.gitlab.com`
- Kubernetes (`k8s` ) â `registry.k8s.io`
- Microsoft Azure Container Registry (`azure-container-registry` ) â `<custom>.azurecr.io`
- Quay (`quay` ) â `quay.io`

`--registry-id` (string)

The Amazon Web Services account ID associated with the registry to create the pull through cache rule for. If you do not specify a registry, the default registry is assumed.

`--upstream-registry` (string)

The name of the upstream registry.

Possible values:

- `ecr`
- `ecr-public`
- `quay`
- `k8s`
- `docker-hub`
- `github-container-registry`
- `azure-container-registry`
- `gitlab-container-registry`

`--credential-arn` (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.

`--custom-role-arn` (string)

Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.

`--upstream-repository-prefix` (string)

The repository name prefix of the upstream registry to match with the upstream repository name. When this field isnât specified, Amazon ECR will use the `ROOT` .

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

ecrRepositoryPrefix -> (string)

The Amazon ECR repository prefix associated with the pull through cache rule.

upstreamRegistryUrl -> (string)

The upstream registry URL associated with the pull through cache rule.

createdAt -> (timestamp)

The date and time, in JavaScript date format, when the pull through cache rule was created.

registryId -> (string)

The registry ID associated with the request.

upstreamRegistry -> (string)

The name of the upstream registry associated with the pull through cache rule.

credentialArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule.

customRoleArn -> (string)

The ARN of the IAM role associated with the pull through cache rule.

upstreamRepositoryPrefix -> (string)

The upstream repository prefix associated with the pull through cache rule.