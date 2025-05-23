# create-assessment-frameworkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-assessment-framework.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-assessment-framework.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# create-assessment-framework

## Description

Creates a custom framework in Audit Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/CreateAssessmentFramework)

## Synopsis

```
create-assessment-framework
--name <value>
[--description <value>]
[--compliance-type <value>]
--control-sets <value>
[--tags <value>]
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

`--name` (string)

The name of the new custom framework.

`--description` (string)

An optional description for the new custom framework.

`--compliance-type` (string)

The compliance type that the new custom framework supports, such as CIS or HIPAA.

`--control-sets` (list)

The control sets that are associated with the framework.

(structure)

A `controlSet` entity that represents a collection of controls in Audit Manager. This doesnât contain the control set ID.

name -> (string)

The name of the control set.

controls -> (list)

The list of controls within the control set. This doesnât contain the control set ID.

(structure)

The control entity attributes that uniquely identify an existing control to be added to a framework in Audit Manager.

id -> (string)

The unique identifier of the control.

Shorthand Syntax:

```
name=string,controls=[{id=string},{id=string}] ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "controls": [
      {
        "id": "string"
      }
      ...
    ]
  }
  ...
]
```

`--tags` (map)

The tags that are associated with the framework.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

## Output

framework -> (structure)

The name of the new framework that the `CreateAssessmentFramework` API returned.

arn -> (string)

The Amazon Resource Name (ARN) of the framework.

id -> (string)

The unique identifier for the framework.

name -> (string)

The name of the framework.

type -> (string)

Specifies whether the framework is a standard framework or a custom framework.

complianceType -> (string)

The compliance type that the framework supports, such as CIS or HIPAA.

description -> (string)

The description of the framework.

logo -> (string)

The logo thatâs associated with the framework.

controlSources -> (string)

The control data sources where Audit Manager collects evidence from.

controlSets -> (list)

The control sets that are associated with the framework.

(structure)

A set of controls in Audit Manager.

id -> (string)

The identifier of the control set in the assessment. This is the control set name in a plain string format.

name -> (string)

The name of the control set.

controls -> (list)

The list of controls within the control set.

(structure)

A control in Audit Manager.

arn -> (string)

The Amazon Resource Name (ARN) of the control.

id -> (string)

The unique identifier for the control.

type -> (string)

Specifies whether the control is a standard control or a custom control.

name -> (string)

The name of the control.

description -> (string)

The description of the control.

testingInformation -> (string)

The steps that you should follow to determine if the control has been satisfied.

actionPlanTitle -> (string)

The title of the action plan for remediating the control.

actionPlanInstructions -> (string)

The recommended actions to carry out if the control isnât fulfilled.

controlSources -> (string)

The data source types that determine where Audit Manager collects evidence from for the control.

controlMappingSources -> (list)

The data mapping sources for the control.

(structure)

The data source that determines where Audit Manager collects evidence from for the control.

sourceId -> (string)

The unique identifier for the source.

sourceName -> (string)

The name of the source.

sourceDescription -> (string)

The description of the source.

sourceSetUpOption -> (string)

The setup option for the data source. This option reflects if the evidence collection method is automated or manual. If you donât provide a value for `sourceSetUpOption` , Audit Manager automatically infers and populates the correct value based on the `sourceType` that you specify.

sourceType -> (string)

Specifies which type of data source is used to collect evidence.

- The source can be an individual data source type, such as `AWS_Cloudtrail` , `AWS_Config` , `AWS_Security_Hub` , `AWS_API_Call` , or `MANUAL` .
- The source can also be a managed grouping of data sources, such as a `Core_Control` or a `Common_Control` .

sourceKeyword -> (structure)

A keyword that relates to the control data source.

For manual evidence, this keyword indicates if the manual evidence is a file or text.

For automated evidence, this keyword identifies a specific CloudTrail event, Config rule, Security Hub control, or Amazon Web Services API name.

To learn more about the supported keywords that you can use when mapping a control data source, see the following pages in the *Audit Manager User Guide* :

- [Config rules supported by Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html)
- [Security Hub controls supported by Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html)
- [API calls supported by Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html)
- [CloudTrail event names supported by Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-cloudtrail.html)

keywordInputType -> (string)

The input method for the keyword.

- `SELECT_FROM_LIST` is used when mapping a data source for automated evidence.
- When `keywordInputType` is `SELECT_FROM_LIST` , a keyword must be selected to collect automated evidence. For example, this keyword can be a CloudTrail event name, a rule name for Config, a Security Hub control, or the name of an Amazon Web Services API call.
- `UPLOAD_FILE` and `INPUT_TEXT` are only used when mapping a data source for manual evidence.
- When `keywordInputType` is `UPLOAD_FILE` , a file must be uploaded as manual evidence.
- When `keywordInputType` is `INPUT_TEXT` , text must be entered as manual evidence.

keywordValue -> (string)

The value of the keyword thatâs used when mapping a control data source. For example, this can be a CloudTrail event name, a rule name for Config, a Security Hub control, or the name of an Amazon Web Services API call.

If youâre mapping a data source to a rule in Config, the `keywordValue` that you specify depends on the type of rule:

- For [managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) , you can use the rule identifier as the `keywordValue` . You can find the rule identifier from the [list of Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) . For some rules, the rule identifier is different from the rule name. For example, the rule name `restricted-ssh` has the following rule identifier: `INCOMING_SSH_DISABLED` . Make sure to use the rule identifier, not the rule name.  Keyword example for managed rules:
- Managed rule name: [s3-bucket-acl-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-acl-prohibited.html) `keywordValue` : `S3_BUCKET_ACL_PROHIBITED`
- For [custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) , you form the `keywordValue` by adding the `Custom_` prefix to the rule name. This prefix distinguishes the custom rule from a managed rule.  Keyword example for custom rules:
- Custom rule name: my-custom-config-rule  `keywordValue` : `Custom_my-custom-config-rule`
- For [service-linked rules](https://docs.aws.amazon.com/config/latest/developerguide/service-linked-awsconfig-rules.html) , you form the `keywordValue` by adding the `Custom_` prefix to the rule name. In addition, you remove the suffix ID that appears at the end of the rule name.  Keyword examples for service-linked rules:
- Service-linked rule name: CustomRuleForAccount-conformance-pack-szsm1uv0w  `keywordValue` : `Custom_CustomRuleForAccount-conformance-pack`
- Service-linked rule name: OrgConfigRule-s3-bucket-versioning-enabled-dbgzf8ba  `keywordValue` : `Custom_OrgConfigRule-s3-bucket-versioning-enabled`

### Warning

The `keywordValue` is case sensitive. If you enter a value incorrectly, Audit Manager might not recognize the data source mapping. As a result, you might not successfully collect evidence from that data source as intended.

Keep in mind the following requirements, depending on the data source type that youâre using.

- For Config:
- For managed rules, make sure that the `keywordValue` is the rule identifier in `ALL_CAPS_WITH_UNDERSCORES` . For example, `CLOUDWATCH_LOG_GROUP_ENCRYPTED` . For accuracy, we recommend that you reference the list of [supported Config managed rules](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html) .
- For custom rules, make sure that the `keywordValue` has the `Custom_` prefix followed by the custom rule name. The format of the custom rule name itself may vary. For accuracy, we recommend that you visit the [Config console](https://console.aws.amazon.com/config/) to verify your custom rule name.
- For Security Hub: The format varies for Security Hub control names. For accuracy, we recommend that you reference the list of [supported Security Hub controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html) .
- For Amazon Web Services API calls: Make sure that the `keywordValue` is written as `serviceprefix_ActionName` . For example, `iam_ListGroups` . For accuracy, we recommend that you reference the list of [supported API calls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html) .
- For CloudTrail: Make sure that the `keywordValue` is written as `serviceprefix_ActionName` . For example, `cloudtrail_StartLogging` . For accuracy, we recommend that you review the Amazon Web Service prefix and action names in the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) .

sourceFrequency -> (string)

Specifies how often evidence is collected from the control mapping source.

troubleshootingText -> (string)

The instructions for troubleshooting the control.

createdAt -> (timestamp)

The time when the control was created.

lastUpdatedAt -> (timestamp)

The time when the control was most recently updated.

createdBy -> (string)

The user or role that created the control.

lastUpdatedBy -> (string)

The user or role that most recently updated the control.

tags -> (map)

The tags associated with the control.

key -> (string)

value -> (string)

state -> (string)

The state of the control. The `END_OF_SUPPORT` state is applicable to standard controls only. This state indicates that the standard control can still be used to collect evidence, but Audit Manager is no longer updating or maintaining that control.

createdAt -> (timestamp)

The time when the framework was created.

lastUpdatedAt -> (timestamp)

The time when the framework was most recently updated.

createdBy -> (string)

The user or role that created the framework.

lastUpdatedBy -> (string)

The user or role that most recently updated the framework.

tags -> (map)

The tags that are associated with the framework.

key -> (string)

value -> (string)