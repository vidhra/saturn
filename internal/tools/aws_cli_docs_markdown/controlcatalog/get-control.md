# get-controlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/get-control.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/get-control.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [controlcatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/index.html#cli-aws-controlcatalog) ]

# get-control

## Description

Returns details about a specific control, most notably a list of Amazon Web Services Regions where this control is supported. Input a value for the *ControlArn* parameter, in ARN form. `GetControl` accepts *controltower* or *controlcatalog* control ARNs as input. Returns a *controlcatalog* ARN format.

In the API response, controls that have the value `GLOBAL` in the `Scope` field do not show the `DeployableRegions` field, because it does not apply. Controls that have the value `REGIONAL` in the `Scope` field return a value for the `DeployableRegions` field, as shown in the example.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/controlcatalog-2018-05-10/GetControl)

## Synopsis

```
get-control
--control-arn <value>
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

`--control-arn` (string)

The Amazon Resource Name (ARN) of the control. It has one of the following formats:

*Global format*

`arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}`

*Or Regional format*

`arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}`

Here is a more general pattern that covers Amazon Web Services Control Tower and Control Catalog ARNs:

`^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$`

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

Arn -> (string)

The Amazon Resource Name (ARN) of the control.

Name -> (string)

The display name of the control.

Description -> (string)

A description of what the control does.

Behavior -> (string)

A term that identifies the controlâs functional behavior. One of `Preventive` , `Detective` , `Proactive`

Severity -> (string)

An enumerated type, with the following possible values:

RegionConfiguration -> (structure)

Returns information about the control, including the scope of the control, if enabled, and the Regions in which the control currently is available for deployment. For more information about scope, see [Global services](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html) .

If you are applying controls through an Amazon Web Services Control Tower landing zone environment, remember that the values returned in the `RegionConfiguration` API operation are not related to the governed Regions in your landing zone. For example, if you are governing Regions `A` ,``B`` ,and `C` while the control is available in Regions `A` , `B` , C``,`` and `D` , youâd see a response with `DeployableRegions` of `A` , `B` , `C` , and `D` for a control with `REGIONAL` scope, even though you may not intend to deploy the control in Region `D` , because you do not govern it through your landing zone.

Scope -> (string)

The coverage of the control, if deployed. Scope is an enumerated type, with value `Regional` , or `Global` . A control with Global scope is effective in all Amazon Web Services Regions, regardless of the Region from which it is enabled, or to which it is deployed. A control implemented by an SCP is usually Global in scope. A control with Regional scope has operations that are restricted specifically to the Region from which it is enabled and to which it is deployed. Controls implemented by Config rules and CloudFormation hooks usually are Regional in scope. Security Hub controls usually are Regional in scope.

DeployableRegions -> (list)

Regions in which the control is available to be deployed.

(string)

Implementation -> (structure)

Returns information about the control, as an `ImplementationDetails` object that shows the underlying implementation type for a control.

Type -> (string)

A string that describes a controlâs implementation type.

Identifier -> (string)

A service-specific identifier for the control, assigned by the service that implemented the control. For example, this identifier could be an Amazon Web Services Config Rule ID or a Security Hub Control ID.

Parameters -> (list)

Returns an array of `ControlParameter` objects that specify the parameters a control supports. An empty list is returned for controls that donât support parameters.

(structure)

Five types of control parameters are supported.

- **AllowedRegions** : List of Amazon Web Services Regions exempted from the control. Each string is expected to be an Amazon Web Services Region code. This parameter is mandatory for the **OU Region deny** control, **CT.MULTISERVICE.PV.1** . Example: `["us-east-1","us-west-2"]`
- **ExemptedActions** : List of Amazon Web Services IAM actions exempted from the control. Each string is expected to be an IAM action. Example: `["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults"]`
- **ExemptedPrincipalArns** : List of Amazon Web Services IAM principal ARNs exempted from the control. Each string is expected to be an IAM principal that follows the pattern `^arn:(aws|aws-us-gov):(iam|sts)::.+:.+$`   Example: `["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]`
- **ExemptedResourceArns** : List of resource ARNs exempted from the control. Each string is expected to be a resource ARN. Example: `["arn:aws:s3:::my-bucket-name"]`
- **ExemptAssumeRoot** : A parameter that lets you choose whether to exempt requests made with `AssumeRoot` from this control, for this OU. For member accounts, the `AssumeRoot` property is included in requests initiated by IAM centralized root access. This parameter applies only to the `AWS-GR_RESTRICT_ROOT_USER` control. If you add the parameter when enabling the control, the `AssumeRoot` exemption is allowed. If you omit the parameter, the `AssumeRoot` exception is not permitted. The parameter does not accept `False` as a value.  [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controlcatalog/get-control.html#id1)Example: Enabling the control and allowing `AssumeRoot` *    `{ "controlIdentifier": "arn:aws:controlcatalog:::control/5kvme4m5d2b4d7if2fs5yg2ui", "parameters": [ { "key": "ExemptAssumeRoot", "value": true } ], "targetIdentifier": "arn:aws:organizations::8633900XXXXX:ou/o-6jmn81636m/ou-qsah-jtiihcla" }`

Name -> (string)

The parameter name. This name is the parameter `key` when you call ` `EnableControl` [https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl).html`__ or ` `UpdateEnabledControl` [https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl).html`__ .

CreateTime -> (timestamp)

A timestamp that notes the time when the control was released (start of its life) as a governance capability in Amazon Web Services.