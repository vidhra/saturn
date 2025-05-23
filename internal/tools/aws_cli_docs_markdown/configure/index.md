# configureÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# configure

## Description

Configure AWS CLI options. If this command is run with no
arguments, you will be prompted for configuration values such as your AWS
Access Key Id and your AWS Secret Access Key.  You can configure a named
profile using the `--profile` argument.  If your config file does not exist
(the default location is `~/.aws/config`), the AWS CLI will create it
for you.  To keep an existing value, hit enter when prompted for the value.
When you are prompted for information, the current value will be displayed in
`[brackets]`.  If the config item has no value, it be displayed as
`[None]`.  Note that the `configure` command only works with values from the
config file.  It does not use any configuration values from environment
variables or the IAM role.

Note: the values you provide for the AWS Access Key ID and the AWS Secret
Access Key will be written to the shared credentials file
(`~/.aws/credentials`).

## Configuration Variables

The following configuration variables are supported in the config file:

- **aws_access_key_id** - The AWS access key part of your credentials
- **aws_secret_access_key** - The AWS secret access key part of your credentials
- **aws_session_token** - The session token part of your credentials (session tokens only)
- **metadata_service_timeout** - The number of seconds to wait until the metadata service
request times out.  This is used if you are using an IAM role to provide
your credentials.
- **metadata_service_num_attempts** - The number of attempts to try to retrieve
credentials.  If you know for certain you will be using an IAM role on an
Amazon EC2 instance, you can set this value to ensure any intermittent
failures are retried.  By default this value is 1.

For more information on configuration options, see [Configuring the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide*.

## Synopsis

```
aws configure [--profile profile-name]
```

## Options

*None*

## Available Commands

- [add-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/add-model.html)
- [export-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/export-credentials.html)
- [get](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/get.html)
- [import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/import.html)
- [list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/list.html)
- [list-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/list-profiles.html)
- [set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/set.html)
- [sso](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/sso.html)
- [sso-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/sso-session.html)

## Examples

To create a new configuration:

```
$ aws configure
AWS Access Key ID [None]: accesskey
AWS Secret Access Key [None]: secretkey
Default region name [None]: us-west-2
Default output format [None]:
```

To update just the region name:

```
$ aws configure
AWS Access Key ID [****]:
AWS Secret Access Key [****]:
Default region name [us-west-1]: us-west-2
Default output format [None]:
```