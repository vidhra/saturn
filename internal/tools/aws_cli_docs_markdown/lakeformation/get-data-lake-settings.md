# get-data-lake-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-data-lake-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-data-lake-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lakeformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/index.html#cli-aws-lakeformation) ]

# get-data-lake-settings

## Description

Retrieves the list of the data lake administrators of a Lake Formation-managed data lake.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GetDataLakeSettings)

## Synopsis

```
get-data-lake-settings
[--catalog-id <value>]
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

`--catalog-id` (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

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

**To retrieve AWS Lake Formation-managed data lake settings**

The following `get-data-lake-settings` example retrieves the list of data lake administrators and other data lake settings.

```
aws lakeformation get-data-lake-settings \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "123456789111"
}
```

Output:

```
{
    "DataLakeSettings": {
        "DataLakeAdmins": [{
            "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin"
        }],
        "CreateDatabaseDefaultPermissions": [],
        "CreateTableDefaultPermissions": [
                {
                        "Principal": {
                            "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                        },
                        "Permissions": [
                            "ALL"
                        ]
                }
        ],
        "TrustedResourceOwners": [],
        "AllowExternalDataFiltering": true,
        "ExternalDataFilteringAllowList": [{
            "DataLakePrincipalIdentifier": "123456789111"
        }],
        "AuthorizedSessionTagValueList": [
            "Amazon EMR"
        ]
    }
}
```

For more information, see [Changing the default security settings for your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html) in the *AWS Lake Formation Developer Guide*.

## Output

DataLakeSettings -> (structure)

A structure representing a list of Lake Formation principals designated as data lake administrators.

DataLakeAdmins -> (list)

A list of Lake Formation principals. Supported principals are IAM users or IAM roles.

(structure)

The Lake Formation principal. Supported principals are IAM users or IAM roles.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

ReadOnlyAdmins -> (list)

A list of Lake Formation principals with only view access to the resources, without the ability to make changes. Supported principals are IAM users or IAM roles.

(structure)

The Lake Formation principal. Supported principals are IAM users or IAM roles.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

CreateDatabaseDefaultPermissions -> (list)

Specifies whether access control on newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.

A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM_ALLOWED_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting âUse only IAM access control,â and is for backward compatibility with the Glue permission model implemented by IAM permissions.

The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM_ALLOWED_PRINCIPALS.

For more information, see [Changing the Default Security Settings for Your Data Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html) .

(structure)

Permissions granted to a principal.

Principal -> (structure)

The principal who is granted permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Permissions -> (list)

The permissions that are granted to the principal.

(string)

CreateTableDefaultPermissions -> (list)

Specifies whether access control on newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.

A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM_ALLOWED_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting âUse only IAM access control,â and is for backward compatibility with the Glue permission model implemented by IAM permissions.

The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM_ALLOWED_PRINCIPALS.

For more information, see [Changing the Default Security Settings for Your Data Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html) .

(structure)

Permissions granted to a principal.

Principal -> (structure)

The principal who is granted permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Permissions -> (list)

The permissions that are granted to the principal.

(string)

Parameters -> (map)

A key-value map that provides an additional configuration on your data lake. CROSS_ACCOUNT_VERSION is the key you can configure in the Parameters field. Accepted values for the CrossAccountVersion key are 1, 2, 3, and 4.

key -> (string)

value -> (string)

TrustedResourceOwners -> (list)

A list of the resource-owning account IDs that the callerâs account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource ownerâs CloudTrail log.

You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

(string)

AllowExternalDataFiltering -> (boolean)

Whether to allow Amazon EMR clusters to access data managed by Lake Formation.

If true, you allow Amazon EMR clusters to access data in Amazon S3 locations that are registered with Lake Formation.

If false or null, no Amazon EMR clusters will be able to access data in Amazon S3 locations that are registered with Lake Formation.

For more information, see [(Optional) Allow external data filtering](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter) .

AllowFullTableExternalDataAccess -> (boolean)

Whether to allow a third-party query engine to get data access credentials without session tags when a caller has full data access permissions.

ExternalDataFilteringAllowList -> (list)

A list of the account IDs of Amazon Web Services accounts with Amazon EMR clusters that are to perform data filtering.>

(structure)

The Lake Formation principal. Supported principals are IAM users or IAM roles.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

AuthorizedSessionTagValueList -> (list)

Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the userâs role while assuming it. Lake Formation will publish the acceptable key-value pair, for example key = âLakeFormationTrustedCallerâ and value = âTRUEâ and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formationâs administrative APIs.

(string)