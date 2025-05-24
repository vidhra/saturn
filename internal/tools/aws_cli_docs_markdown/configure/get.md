# getÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/get.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/get.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html#cli-aws-configure) ]

# get

## Description

Get a configuration value from the config file.

The `aws configure get` command can be used to print a configuration value in
the AWS config file.  The `get` command supports two types of configuration
values, *unqualified* and *qualified* config values.

Note that `aws configure get` only looks at values in the AWS configuration
file.  It does **not** resolve configuration variables specified anywhere else,
including environment variables, command line arguments, etc.

### Unqualified Names

Every value in the AWS configuration file must be placed in a section (denoted
by `[section-name]` in the config file).  To retrieve a value from the
config file, the section name and the config name must be known.

An unqualified configuration name refers to a name that is not scoped to a
specific section in the configuration file.  Sections are specified by
separating parts with the `"."` character (`section.config-name`).  An
unqualified name will be scoped to the current profile.  For example,
`aws configure get aws_access_key_id` will retrieve the `aws_access_key_id`
from the current profile,  or the `default` profile if no profile is
specified.  You can still provide a `--profile` argument to the `aws
configure get` command.  For example, `aws configure get region --profile
testing` will print the region value for the `testing` profile.

### Qualified Names

A qualified name is a name that has at least one `"."` character in the name.
This name provides a way to specify the config section from which to retrieve
the config variable.  When a qualified name is provided to `aws configure
get`, the currently specified profile is ignored.  Section names that have
the format `[profile profile-name]` can be specified by using the
`profile.profile-name.config-name` syntax, and the default profile can be
specified using the `default.config-name` syntax.

## Synopsis

```
aws configure get varname [--profile profile-name]
```

## Options

`varname` (string)
The name of the config value to retrieve.

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

Suppose you had the following config file:

```
[default]
aws_access_key_id=default_access_key
aws_secret_access_key=default_secret_key

[profile testing]
aws_access_key_id=testing_access_key
aws_secret_access_key=testing_secret_key
region=us-west-2
```

The following commands would have the corresponding output:

```
$ aws configure get aws_access_key_id
default_access_key

$ aws configure get default.aws_access_key_id
default_access_key

$ aws configure get aws_access_key_id --profile testing
testing_access_key

$ aws configure get profile.testing.aws_access_key_id
testing_access_key

$ aws configure get profile.does-not-exist
$
$ echo $?
1
```