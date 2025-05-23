# get-admin-scopeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-admin-scope.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-admin-scope.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/index.html#cli-aws-fms) ]

# get-admin-scope

## Description

Returns information about the specified accountâs administrative scope. The administrative scope defines the resources that an Firewall Manager administrator can manage.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetAdminScope)

## Synopsis

```
get-admin-scope
--admin-account <value>
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

`--admin-account` (string)

The administrator account that you want to get the details for.

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

AdminScope -> (structure)

Contains details about the administrative scope of the requested account.

AccountScope -> (structure)

Defines the accounts that the specified Firewall Manager administrator can apply policies to.

Accounts -> (list)

The list of accounts within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of `ExcludeSpecifiedAccounts` . If `ExcludeSpecifiedAccounts` is set to `true` , then the Firewall Manager administrator can apply policies to all members of the organization except for the accounts in this list. If `ExcludeSpecifiedAccounts` is set to `false` , then the Firewall Manager administrator can only apply policies to the accounts in this list.

(string)

AllAccountsEnabled -> (boolean)

A boolean value that indicates if the administrator can apply policies to all accounts within an organization. If true, the administrator can apply policies to all accounts within the organization. You can either enable management of all accounts through this operation, or you can specify a list of accounts to manage in `AccountScope$Accounts` . You cannot specify both.

ExcludeSpecifiedAccounts -> (boolean)

A boolean value that excludes the accounts in `AccountScope$Accounts` from the administratorâs scope. If true, the Firewall Manager administrator can apply policies to all members of the organization except for the accounts listed in `AccountScope$Accounts` . You can either specify a list of accounts to exclude by `AccountScope$Accounts` , or you can enable management of all accounts by `AccountScope$AllAccountsEnabled` . You cannot specify both.

OrganizationalUnitScope -> (structure)

Defines the Organizations organizational units that the specified Firewall Manager administrator can apply policies to. For more information about OUs in Organizations, see [Managing organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *Organizations User Guide* .

OrganizationalUnits -> (list)

The list of OUs within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits` . If `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits` is set to `true` , then the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs in this list. If `OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits` is set to `false` , then the Firewall Manager administrator can only apply policies to the OUs in this list.

(string)

AllOrganizationalUnitsEnabled -> (boolean)

A boolean value that indicates if the administrator can apply policies to all OUs within an organization. If true, the administrator can manage all OUs within the organization. You can either enable management of all OUs through this operation, or you can specify OUs to manage in `OrganizationalUnitScope$OrganizationalUnits` . You cannot specify both.

ExcludeSpecifiedOrganizationalUnits -> (boolean)

A boolean value that excludes the OUs in `OrganizationalUnitScope$OrganizationalUnits` from the administratorâs scope. If true, the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs listed in `OrganizationalUnitScope$OrganizationalUnits` . You can either specify a list of OUs to exclude by `OrganizationalUnitScope$OrganizationalUnits` , or you can enable management of all OUs by `OrganizationalUnitScope$AllOrganizationalUnitsEnabled` . You cannot specify both.

RegionScope -> (structure)

Defines the Amazon Web Services Regions that the specified Firewall Manager administrator can perform actions in.

Regions -> (list)

The Amazon Web Services Regions that the specified Firewall Manager administrator can perform actions in.

(string)

AllRegionsEnabled -> (boolean)

Allows the specified Firewall Manager administrator to manage all Amazon Web Services Regions.

PolicyTypeScope -> (structure)

Defines the Firewall Manager policy types that the specified Firewall Manager administrator can create and manage.

PolicyTypes -> (list)

The list of policy types that the specified Firewall Manager administrator can manage.

(string)

AllPolicyTypesEnabled -> (boolean)

Allows the specified Firewall Manager administrator to manage all Firewall Manager policy types, except for third-party policy types. Third-party policy types can only be managed by the Firewall Manager default administrator.

Status -> (string)

The current status of the request to onboard a member account as an Firewall Manager administrator.

- `ONBOARDING` - The account is onboarding to Firewall Manager as an administrator.
- `ONBOARDING_COMPLETE` - Firewall Manager The account is onboarded to Firewall Manager as an administrator, and can perform actions on the resources defined in their  AdminScope .
- `OFFBOARDING` - The account is being removed as an Firewall Manager administrator.
- `OFFBOARDING_COMPLETE` - The account has been removed as an Firewall Manager administrator.