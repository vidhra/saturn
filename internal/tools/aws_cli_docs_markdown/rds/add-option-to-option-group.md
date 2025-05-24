# add-option-to-option-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-option-to-option-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-option-to-option-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# add-option-to-option-group

## Description

Modifies an existing option group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyOptionGroup)

## Synopsis

```
add-option-to-option-group
--option-group-name <value>
[--apply-immediately | --no-apply-immediately]
[--options <value>]
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

`--option-group-name` (string)

The name of the option group to be modified.

Permanent options, such as the TDE option for Oracle Advanced Security TDE, canât be removed from an option group, and that option group canât be removed from a DB instance once it is associated with a DB instance

`--apply-immediately` | `--no-apply-immediately` (boolean)

Specifies whether to apply the change immediately or during the next maintenance window for each instance associated with the option group.

`--options` (list)

Options in this list are added to the option group or, if already present, the specified configuration is used to update the existing configuration.

(structure)

A list of all available options for an option group.

OptionName -> (string)

The configuration of options to include in a group.

Port -> (integer)

The optional port for the option.

OptionVersion -> (string)

The version for the option.

DBSecurityGroupMemberships -> (list)

A list of DB security groups used for this option.

(string)

VpcSecurityGroupMemberships -> (list)

A list of VPC security group names used for this option.

(string)

OptionSettings -> (list)

The option settings to include in an option group.

(structure)

Option settings are the actual settings being applied or configured for that option. It is used when you modify an option group or describe option groups. For example, the NATIVE_NETWORK_ENCRYPTION option has a setting called SQLNET.ENCRYPTION_SERVER that can have several different values.

Name -> (string)

The name of the option that has settings that you can set.

Value -> (string)

The current value of the option setting.

DefaultValue -> (string)

The default value of the option setting.

Description -> (string)

The description of the option setting.

ApplyType -> (string)

The DB engine specific parameter type.

DataType -> (string)

The data type of the option setting.

AllowedValues -> (string)

The allowed values of the option setting.

IsModifiable -> (boolean)

Indicates whether the option setting can be modified from the default.

IsCollection -> (boolean)

Indicates whether the option setting is part of a collection.

Shorthand Syntax:

```
OptionName=string,Port=integer,OptionVersion=string,DBSecurityGroupMemberships=string,string,VpcSecurityGroupMemberships=string,string,OptionSettings=[{Name=string,Value=string,DefaultValue=string,Description=string,ApplyType=string,DataType=string,AllowedValues=string,IsModifiable=boolean,IsCollection=boolean},{Name=string,Value=string,DefaultValue=string,Description=string,ApplyType=string,DataType=string,AllowedValues=string,IsModifiable=boolean,IsCollection=boolean}] ...
```

JSON Syntax:

```
[
  {
    "OptionName": "string",
    "Port": integer,
    "OptionVersion": "string",
    "DBSecurityGroupMemberships": ["string", ...],
    "VpcSecurityGroupMemberships": ["string", ...],
    "OptionSettings": [
      {
        "Name": "string",
        "Value": "string",
        "DefaultValue": "string",
        "Description": "string",
        "ApplyType": "string",
        "DataType": "string",
        "AllowedValues": "string",
        "IsModifiable": true|false,
        "IsCollection": true|false
      }
      ...
    ]
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

**To add an option to an option group**

The following `add-option-to-option-group` example adds an option to the specified option group.

```
aws rds add-option-to-option-group \
    --option-group-name myoptiongroup \
    --options OptionName=OEM,Port=5500,DBSecurityGroupMemberships=default \
    --apply-immediately
```

Output:

```
{
    "OptionGroup": {
        "OptionGroupName": "myoptiongroup",
        "OptionGroupDescription": "Test Option Group",
        "EngineName": "oracle-ee",
        "MajorEngineVersion": "12.1",
        "Options": [
            {
                "OptionName": "Timezone",
                "OptionDescription": "Change time zone",
                "Persistent": true,
                "Permanent": false,
                "OptionSettings": [
                    {
                        "Name": "TIME_ZONE",
                        "Value": "Australia/Sydney",
                        "DefaultValue": "UTC",
                        "Description": "Specifies the timezone the user wants to change the system time to",
                        "ApplyType": "DYNAMIC",
                        "DataType": "STRING",
                        "AllowedValues": "Africa/Cairo,Africa/Casablanca,Africa/Harare,Africa/Lagos,Africa/Luanda,Africa/Monrovia,Africa/Nairobi,Africa/Tripoli,Africa/Windhoek,America/Araguaina,America/Argentina/Buenos_Aires,America/Asuncion,America/Bogota,America/Caracas,America/Chicago,America/Chihuahua,America/Cuiaba,America/Denver,America/Detroit,America/Fortaleza,America/Godthab,America/Guatemala,America/Halifax,America/Lima,America/Los_Angeles,America/Manaus,America/Matamoros,America/Mexico_City,America/Monterrey,America/Montevideo,America/New_York,America/Phoenix,America/Santiago,America/Sao_Paulo,America/Tijuana,America/Toronto,Asia/Amman,Asia/Ashgabat,Asia/Baghdad,Asia/Baku,Asia/Bangkok,Asia/Beirut,Asia/Calcutta,Asia/Damascus,Asia/Dhaka,Asia/Hong_Kong,Asia/Irkutsk,Asia/Jakarta,Asia/Jerusalem,Asia/Kabul,Asia/Karachi,Asia/Kathmandu,Asia/Kolkata,Asia/Krasnoyarsk,Asia/Magadan,Asia/Manila,Asia/Muscat,Asia/Novosibirsk,Asia/Rangoon,Asia/Riyadh,Asia/Seoul,Asia/Shanghai,Asia/Singapore,Asia/Taipei,Asia/Tehran,Asia/Tokyo,Asia/Ulaanbaatar,Asia/Vladivostok,Asia/Yakutsk,Asia/Yerevan,Atlantic/Azores,Atlantic/Cape_Verde,Australia/Adelaide,Australia/Brisbane,Australia/Darwin,Australia/Eucla,Australia/Hobart,Australia/Lord_Howe,Australia/Perth,Australia/Sydney,Brazil/DeNoronha,Brazil/East,Canada/Newfoundland,Canada/Saskatchewan,Etc/GMT-3,Europe/Amsterdam,Europe/Athens,Europe/Berlin,Europe/Dublin,Europe/Helsinki,Europe/Kaliningrad,Europe/London,Europe/Madrid,Europe/Moscow,Europe/Paris,Europe/Prague,Europe/Rome,Europe/Sarajevo,Pacific/Apia,Pacific/Auckland,Pacific/Chatham,Pacific/Fiji,Pacific/Guam,Pacific/Honolulu,Pacific/Kiritimati,Pacific/Marquesas,Pacific/Samoa,Pacific/Tongatapu,Pacific/Wake,US/Alaska,US/Central,US/East-Indiana,US/Eastern,US/Pacific,UTC",
                        "IsModifiable": true,
                        "IsCollection": false
                    }
                ],
                "DBSecurityGroupMemberships": [],
                "VpcSecurityGroupMemberships": []
            },
            {
                "OptionName": "OEM",
                "OptionDescription": "Oracle 12c EM Express",
                "Persistent": false,
                "Permanent": false,
                "Port": 5500,
                "OptionSettings": [],
                "DBSecurityGroupMemberships": [
                    {
                        "DBSecurityGroupName": "default",
                        "Status": "authorized"
                    }
                ],
                "VpcSecurityGroupMemberships": []
            }
        ],
        "AllowsVpcAndNonVpcInstanceMemberships": false,
        "OptionGroupArn": "arn:aws:rds:us-east-1:123456789012:og:myoptiongroup"
    }
}
```

For more information, see [Adding an Option to an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.AddOption) in the *Amazon RDS User Guide*.

## Output

OptionGroup -> (structure)

OptionGroupName -> (string)

Specifies the name of the option group.

OptionGroupDescription -> (string)

Provides a description of the option group.

EngineName -> (string)

Indicates the name of the engine that this option group can be applied to.

MajorEngineVersion -> (string)

Indicates the major engine version associated with this option group.

Options -> (list)

Indicates what options are available in the option group.

(structure)

The details of an option.

OptionName -> (string)

The name of the option.

OptionDescription -> (string)

The description of the option.

Persistent -> (boolean)

Indicates whether this option is persistent.

Permanent -> (boolean)

Indicates whether this option is permanent.

Port -> (integer)

If required, the port configured for this option to use.

OptionVersion -> (string)

The version of the option.

OptionSettings -> (list)

The option settings for this option.

(structure)

Option settings are the actual settings being applied or configured for that option. It is used when you modify an option group or describe option groups. For example, the NATIVE_NETWORK_ENCRYPTION option has a setting called SQLNET.ENCRYPTION_SERVER that can have several different values.

Name -> (string)

The name of the option that has settings that you can set.

Value -> (string)

The current value of the option setting.

DefaultValue -> (string)

The default value of the option setting.

Description -> (string)

The description of the option setting.

ApplyType -> (string)

The DB engine specific parameter type.

DataType -> (string)

The data type of the option setting.

AllowedValues -> (string)

The allowed values of the option setting.

IsModifiable -> (boolean)

Indicates whether the option setting can be modified from the default.

IsCollection -> (boolean)

Indicates whether the option setting is part of a collection.

DBSecurityGroupMemberships -> (list)

If the option requires access to a port, then this DB security group allows access to the port.

(structure)

This data type is used as a response element in the following actions:

- `ModifyDBInstance`
- `RebootDBInstance`
- `RestoreDBInstanceFromDBSnapshot`
- `RestoreDBInstanceToPointInTime`

DBSecurityGroupName -> (string)

The name of the DB security group.

Status -> (string)

The status of the DB security group.

VpcSecurityGroupMemberships -> (list)

If the option requires access to a port, then this VPC security group allows access to the port.

(structure)

This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The membership status of the VPC security group.

Currently, the only valid status is `active` .

AllowsVpcAndNonVpcInstanceMemberships -> (boolean)

Indicates whether this option group can be applied to both VPC and non-VPC instances. The value `true` indicates the option group can be applied to both VPC and non-VPC instances.

VpcId -> (string)

If **AllowsVpcAndNonVpcInstanceMemberships** is `false` , this field is blank. If **AllowsVpcAndNonVpcInstanceMemberships** is `true` and this field is blank, then this option group can be applied to both VPC and non-VPC instances. If this field contains a value, then this option group can only be applied to instances that are in the VPC indicated by this field.

OptionGroupArn -> (string)

Specifies the Amazon Resource Name (ARN) for the option group.

SourceOptionGroup -> (string)

Specifies the name of the option group from which this option group is copied.

SourceAccountId -> (string)

Specifies the Amazon Web Services account ID for the option group from which this option group is copied.

CopyTimestamp -> (timestamp)

Indicates when the option group was copied.