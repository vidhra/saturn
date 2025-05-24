# update-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# update-app

## Description

Updates a specified app.

**Required Permissions** : To use this action, an IAM user must have a Deploy or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateApp)

## Synopsis

```
update-app
--app-id <value>
[--name <value>]
[--description <value>]
[--data-sources <value>]
[--type <value>]
[--app-source <value>]
[--domains <value>]
[--enable-ssl | --no-enable-ssl]
[--ssl-configuration <value>]
[--attributes <value>]
[--environment <value>]
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

`--app-id` (string)

The app ID.

`--name` (string)

The app name.

`--description` (string)

A description of the app.

`--data-sources` (list)

The appâs data sources.

(structure)

Describes an appâs data source.

Type -> (string)

The data sourceâs type, `AutoSelectOpsworksMysqlInstance` , `OpsworksMysqlInstance` , `RdsDbInstance` , or `None` .

Arn -> (string)

The data sourceâs ARN.

DatabaseName -> (string)

The database name.

Shorthand Syntax:

```
Type=string,Arn=string,DatabaseName=string ...
```

JSON Syntax:

```
[
  {
    "Type": "string",
    "Arn": "string",
    "DatabaseName": "string"
  }
  ...
]
```

`--type` (string)

The app type.

Possible values:

- `aws-flow-ruby`
- `java`
- `rails`
- `php`
- `nodejs`
- `static`
- `other`

`--app-source` (structure)

A `Source` object that specifies the app repository.

Type -> (string)

The repository type.

Url -> (string)

The source URL. The following is an example of an Amazon S3 source URL: `https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz` .

Username -> (string)

This parameter depends on the repository type.

- For Amazon S3 bundles, set `Username` to the appropriate IAM access key ID.
- For HTTP bundles, Git repositories, and Subversion repositories, set `Username` to the user name.

Password -> (string)

When included in a request, the parameter depends on the repository type.

- For Amazon S3 bundles, set `Password` to the appropriate IAM secret access key.
- For HTTP bundles and Subversion repositories, set `Password` to the password.

For more information on how to safely handle IAM credentials, see [https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) .

In responses, OpsWorks Stacks returns `*****FILTERED*****` instead of the actual value.

SshKey -> (string)

In requests, the repositoryâs SSH key.

In responses, OpsWorks Stacks returns `*****FILTERED*****` instead of the actual value.

Revision -> (string)

The applicationâs version. OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

Shorthand Syntax:

```
Type=string,Url=string,Username=string,Password=string,SshKey=string,Revision=string
```

JSON Syntax:

```
{
  "Type": "git"|"svn"|"archive"|"s3",
  "Url": "string",
  "Username": "string",
  "Password": "string",
  "SshKey": "string",
  "Revision": "string"
}
```

`--domains` (list)

The appâs virtual host settings, with multiple domains separated by commas. For example: `'www.example.com, example.com'`

(string)

Syntax:

```
"string" "string" ...
```

`--enable-ssl` | `--no-enable-ssl` (boolean)

Whether SSL is enabled for the app.

`--ssl-configuration` (structure)

An `SslConfiguration` object with the SSL configuration.

Certificate -> (string)

The contents of the certificateâs domain.crt file.

PrivateKey -> (string)

The private key; the contents of the certificateâs domain.kex file.

Chain -> (string)

Optional. Can be used to specify an intermediate certificate authority key or client authentication.

Shorthand Syntax:

```
Certificate=string,PrivateKey=string,Chain=string
```

JSON Syntax:

```
{
  "Certificate": "string",
  "PrivateKey": "string",
  "Chain": "string"
}
```

`--attributes` (map)

One or more user-defined key/value pairs to be added to the stack attributes.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  DocumentRoot
  RailsEnv
  AutoBundleOnDeploy
  AwsFlowRubySettings
```

JSON Syntax:

```
{"DocumentRoot"|"RailsEnv"|"AutoBundleOnDeploy"|"AwsFlowRubySettings": "string"
  ...}
```

`--environment` (list)

An array of `EnvironmentVariable` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances.For more information, see [Environment Variables](https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment) .

There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variablesâ names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, âEnvironment: is too large (maximum is 20 KB).â

### Note

If you have specified one or more environment variables, you cannot modify the stackâs Chef version.

(structure)

Represents an appâs environment variable.

Key -> (string)

(Required) The environment variableâs name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

Value -> (string)

(Optional) The environment variableâs value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.

Secure -> (boolean)

(Optional) Whether the variableâs value is returned by the  DescribeApps action. To hide an environment variableâs value, set `Secure` to `true` . `DescribeApps` returns `*****FILTERED*****` instead of the actual value. The default value for `Secure` is `false` .

Shorthand Syntax:

```
Key=string,Value=string,Secure=boolean ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "Secure": true|false
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update an app**

The following example updates a specified app to change its name.

```
aws opsworks --region us-east-1 update-app --app-id 26a61ead-d201-47e3-b55c-2a7c666942f8 --name NewAppName
```

*Output*: None.

**More Information**

For more information, see [Editing Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-editing.html) in the *AWS OpsWorks User Guide*.

## Output

None