# setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html#cli-aws-configure) ]

# set

## Description

Set a configuration value from the config file.

The `aws configure set` command can be used to set a single configuration
value in the AWS config file.  The `set` command supports both the
*qualified* and *unqualified* config values documented in the `get` command
(see `aws configure get help` for more information).

To set a single value, provide the configuration name followed by the
configuration value.

If the config file does not exist, one will automatically be created.  If the
configuration value already exists in the config file, it will updated with the
new configuration value.

Setting a value for the `aws_access_key_id`, `aws_secret_access_key`, or
the `aws_session_token` will result in the value being written to the
shared credentials file (`~/.aws/credentials`).  All other values will
be written to the config file (default location is `~/.aws/config`).

## Synopsis

```
aws configure set varname value [--profile profile-name]
```

## Options

`varname` (string)
The name of the config value to set.

`value` (string)
The value to set.

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

Given an empty config file, the following commands:

```
$ aws configure set aws_access_key_id default_access_key
$ aws configure set aws_secret_access_key default_secret_key
$ aws configure set default.region us-west-2
$ aws configure set default.ca_bundle /path/to/ca-bundle.pem
$ aws configure set region us-west-1 --profile testing
$ aws configure set profile.testing2.region eu-west-1
```

will produce the following config file:

```
[default]
region = us-west-2
ca_bundle = /path/to/ca-bundle.pem

[profile testing]
region = us-west-1

[profile testing2]
region = eu-west-1
```

and the following `~/.aws/credentials` file:

```
[default]
aws_access_key_id = default_access_key
aws_secret_access_key = default_secret_key
```

To perform bulk profiles update `list-profiles` command can be piped with `set` command.
For update region for all profiles, the following command can be used:

```
aws configure list-profiles | xargs -I {} aws configure set region us-west-2 --profile {}
```

will produce the following updated config file:

```
[default]
region = us-west-2
ca_bundle = /path/to/ca-bundle.pem

[profile testing]
region = us-west-2

[profile testing2]
region = us-west-2
```

For update profiles by pattern âtesting*â, the following command can be used:

```
aws configure list-profiles | grep 'testing*' | xargs -I {} aws configure set cli_pager '' --profile {}
```

will produce the following updated config file:

```
[default]
region = us-west-2
ca_bundle = /path/to/ca-bundle.pem

[profile testing]
region = us-west-2
cli_pager =

[profile testing2]
region = us-west-2
cli_pager =
```