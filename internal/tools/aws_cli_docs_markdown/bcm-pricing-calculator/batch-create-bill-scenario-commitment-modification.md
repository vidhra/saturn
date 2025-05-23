# batch-create-bill-scenario-commitment-modificationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-create-bill-scenario-commitment-modification.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-create-bill-scenario-commitment-modification.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-pricing-calculator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/index.html#cli-aws-bcm-pricing-calculator) ]

# batch-create-bill-scenario-commitment-modification

## Description

Create Compute Savings Plans, EC2 Instance Savings Plans, or EC2 Reserved Instances commitments that you want to model in a Bill Scenario.

### Note

The `BatchCreateBillScenarioCommitmentModification` operation doesnât have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission `bcm-pricing-calculator:CreateBillScenarioCommitmentModification` in your policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)

## Synopsis

```
batch-create-bill-scenario-commitment-modification
--bill-scenario-id <value>
--commitment-modifications <value>
[--client-token <value>]
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

`--bill-scenario-id` (string)

The ID of the Bill Scenario for which you want to create the modeled commitment.

`--commitment-modifications` (list)

List of commitments that you want to model in the Bill Scenario.

(structure)

Represents an entry object in the batch operation to create bill scenario commitment modifications.

key -> (string)

A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key.

group -> (string)

An optional group identifier for the commitment modification.

usageAccountId -> (string)

The Amazon Web Services account ID to which this commitment will be applied to.

commitmentAction -> (tagged union structure)

The specific commitment action to be taken (e.g., adding a Reserved Instance or Savings Plan).

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `addReservedInstanceAction`, `addSavingsPlanAction`, `negateReservedInstanceAction`, `negateSavingsPlanAction`.

addReservedInstanceAction -> (structure)

Action to add a Reserved Instance to the scenario.

reservedInstancesOfferingId -> (string)

The ID of the Reserved Instance offering to add. For more information, see [DescribeReservedInstancesOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html) .

instanceCount -> (integer)

The number of instances to add for this Reserved Instance offering.

addSavingsPlanAction -> (structure)

Action to add a Savings Plan to the scenario.

savingsPlanOfferingId -> (string)

The ID of the Savings Plan offering to add. For more information, see [DescribeSavingsPlansOfferings](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html) .

commitment -> (double)

The hourly commitment, in the same currency of the `savingsPlanOfferingId` . This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.

negateReservedInstanceAction -> (structure)

Action to remove a Reserved Instance from the scenario.

reservedInstancesId -> (string)

The ID of the Reserved Instance to remove.

negateSavingsPlanAction -> (structure)

Action to remove a Savings Plan from the scenario.

savingsPlanId -> (string)

The ID of the Savings Plan to remove.

Shorthand Syntax:

```
key=string,group=string,usageAccountId=string,commitmentAction={addReservedInstanceAction={reservedInstancesOfferingId=string,instanceCount=integer},addSavingsPlanAction={savingsPlanOfferingId=string,commitment=double},negateReservedInstanceAction={reservedInstancesId=string},negateSavingsPlanAction={savingsPlanId=string}} ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "group": "string",
    "usageAccountId": "string",
    "commitmentAction": {
      "addReservedInstanceAction": {
        "reservedInstancesOfferingId": "string",
        "instanceCount": integer
      },
      "addSavingsPlanAction": {
        "savingsPlanOfferingId": "string",
        "commitment": double
      },
      "negateReservedInstanceAction": {
        "reservedInstancesId": "string"
      },
      "negateSavingsPlanAction": {
        "savingsPlanId": "string"
      }
    }
  }
  ...
]
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

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

items -> (list)

Returns the list of successful commitment line items that were created for the Bill Scenario.

(structure)

Represents a successfully created item in a batch operation for bill scenario commitment modifications.

key -> (string)

The key of the successfully created entry. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key.

id -> (string)

The unique identifier assigned to the created commitment modification.

group -> (string)

The group identifier for the created commitment modification.

usageAccountId -> (string)

The Amazon Web Services account ID associated with the created commitment modification.

commitmentAction -> (tagged union structure)

The specific commitment action that was taken.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `addReservedInstanceAction`, `addSavingsPlanAction`, `negateReservedInstanceAction`, `negateSavingsPlanAction`.

addReservedInstanceAction -> (structure)

Action to add a Reserved Instance to the scenario.

reservedInstancesOfferingId -> (string)

The ID of the Reserved Instance offering to add. For more information, see [DescribeReservedInstancesOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html) .

instanceCount -> (integer)

The number of instances to add for this Reserved Instance offering.

addSavingsPlanAction -> (structure)

Action to add a Savings Plan to the scenario.

savingsPlanOfferingId -> (string)

The ID of the Savings Plan offering to add. For more information, see [DescribeSavingsPlansOfferings](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html) .

commitment -> (double)

The hourly commitment, in the same currency of the `savingsPlanOfferingId` . This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.

negateReservedInstanceAction -> (structure)

Action to remove a Reserved Instance from the scenario.

reservedInstancesId -> (string)

The ID of the Reserved Instance to remove.

negateSavingsPlanAction -> (structure)

Action to remove a Savings Plan from the scenario.

savingsPlanId -> (string)

The ID of the Savings Plan to remove.

errors -> (list)

Returns the list of errors reason and the commitment item keys that cannot be created in the Bill Scenario.

(structure)

Represents an error that occurred during a batch create operation for bill scenario commitment modifications.

key -> (string)

The key of the entry that caused the error.

errorMessage -> (string)

A descriptive message for the error that occurred.

errorCode -> (string)

The error code associated with the failed operation.