# get-cluster-credentialsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# get-cluster-credentials

## Description

Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with `IAM:` if `AutoCreate` is `False` or `IAMA:` if `AutoCreate` is `True` . You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see [Using IAM Authentication to Generate Database User Credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html) in the Amazon Redshift Cluster Management Guide.

The Identity and Access Management (IAM) user or role that runs GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see [Resource Policies for GetClusterCredentials](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources) in the Amazon Redshift Cluster Management Guide.

If the `DbGroups` parameter is specified, the IAM policy must allow the `redshift:JoinGroup` action with access to the listed `dbgroups` .

In addition, if the `AutoCreate` parameter is set to `True` , then the policy must include the `redshift:CreateClusterUser` permission.

If the `DbName` parameter is specified, the IAM policy must allow access to the resource `dbname` for the specified database name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/GetClusterCredentials)

## Synopsis

```
get-cluster-credentials
--db-user <value>
[--db-name <value>]
[--cluster-identifier <value>]
[--duration-seconds <value>]
[--auto-create | --no-auto-create]
[--db-groups <value>]
[--custom-domain-name <value>]
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

`--db-user` (string)

The name of a database user. If a user name matching `DbUser` exists in the database, the temporary user credentials have the same permissions as the existing user. If `DbUser` doesnât exist in the database and `Autocreate` is `True` , a new user is created using the value for `DbUser` with PUBLIC permissions. If a database user matching the value for `DbUser` doesnât exist and `Autocreate` is `False` , then the command succeeds but the connection attempt will fail because the user doesnât exist in the database.

For more information, see [CREATE USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) in the Amazon Redshift Database Developer Guide.

Constraints:

- Must be 1 to 64 alphanumeric characters or hyphens. The user name canât be `PUBLIC` .
- Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
- First character must be a letter.
- Must not contain a colon ( : ) or slash ( / ).
- Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.

`--db-name` (string)

The name of a database that `DbUser` is authorized to log on to. If `DbName` is not specified, `DbUser` can log on to any existing database.

Constraints:

- Must be 1 to 64 alphanumeric characters or hyphens
- Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
- First character must be a letter.
- Must not contain a colon ( : ) or slash ( / ).
- Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.

`--cluster-identifier` (string)

The unique identifier of the cluster that contains the database for which you are requesting credentials. This parameter is case sensitive.

`--duration-seconds` (integer)

The number of seconds until the returned temporary password expires.

Constraint: minimum 900, maximum 3600.

Default: 900

`--auto-create` | `--no-auto-create` (boolean)

Create a database user with the name specified for the user named in `DbUser` if one does not exist.

`--db-groups` (list)

A list of the names of existing database groups that the user named in `DbUser` will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.

Database group name constraints

- Must be 1 to 64 alphanumeric characters or hyphens
- Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
- First character must be a letter.
- Must not contain a colon ( : ) or slash ( / ).
- Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--custom-domain-name` (string)

The custom domain name for the cluster credentials.

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

**To get cluster credentials for an AWS account**

The following `get-cluster-credentials` example retrieves temporary credentials that enable access to an Amazon Redshift database.

```
aws redshift get-cluster-credentials \
    --db-user adminuser --db-name dev \
    --cluster-identifier mycluster
```

Output:

```
{
    "DbUser": "IAM:adminuser",
    "DbPassword": "AMAFUyyuros/QjxPTtgzcsuQsqzIasdzJEN04aCtWDzXx1O9d6UmpkBtvEeqFly/EXAMPLE==",
    "Expiration": "2019-12-10T17:25:05.770Z"
}
```

For more information, see [Generating IAM Database Credentials Using the Amazon Redshift CLI or API](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-cli-api.html) in the *Amazon Redshift Cluster Management Guide*.

## Output

DbUser -> (string)

A database user name that is authorized to log on to the database `DbName` using the password `DbPassword` . If the specified DbUser exists in the database, the new user name has the same database permissions as the the user named in DbUser. By default, the user is added to PUBLIC. If the `DbGroups` parameter is specifed, `DbUser` is added to the listed groups for any sessions created using these credentials.

DbPassword -> (string)

A temporary password that authorizes the user name returned by `DbUser` to log on to the database `DbName` .

Expiration -> (timestamp)

The date and time the password in `DbPassword` expires.