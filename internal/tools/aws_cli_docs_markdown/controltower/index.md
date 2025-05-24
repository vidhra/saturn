# controltowerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# controltower

## Description

Amazon Web Services Control Tower offers application programming interface (API) operations that support programmatic interaction with these types of resources:

- [`*Controls* https://docs.aws.amazon.com/controltower/latest/userguide/controls.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#id1)
- [DisableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableControl.html)
- [EnableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html)
- [GetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledControl.html)
- [GetControlOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetControlOperation.html)
- [ListControlOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListControlOperations.html)
- [ListEnabledControls](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledControls.html)
- [ResetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html)
- [UpdateEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl.html)
- [`*Landing zones* https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#id1)
- [CreateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html)
- [DeleteLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DeleteLandingZone.html)
- [GetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZone.html)
- [GetLandingZoneOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZoneOperation.html)
- [ListLandingZones](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZones.html)
- [ListLandingZoneOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZoneOperations.html)
- [ResetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetLandingZone.html)
- [UpdateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html)
- [`*Baselines* https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#id1)
- [DisableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableBaseline.html)
- [EnableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html)
- [GetBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html)
- [GetBaselineOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaselineOperation.html)
- [GetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledBaseline.html)
- [ListBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListBaselines.html)
- [ListEnabledBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html)
- [ResetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html)
- [UpdateEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledBaseline.html)
- [`*Tagging* https://docs.aws.amazon.com/controltower/latest/controlreference/tagging.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#id1)
- [ListTagsForResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListTagsForResource.html)
- [TagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UntagResource.html)

For more information about these types of resources, see the ` *Amazon Web Services Control Tower User Guide* [https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower).html`__ .

**About control APIs**

These interfaces allow you to apply the Amazon Web Services library of pre-defined *controls* to your organizational units, programmatically. In Amazon Web Services Control Tower, the terms âcontrolâ and âguardrailâ are synonyms.

To call these APIs, youâll need to know:

- the `controlIdentifier` for the controlâor guardrailâyou are targeting.
- the ARN associated with the target organizational unit (OU), which we call the `targetIdentifier` .
- the ARN associated with a resource that you wish to tag or untag.

**To get the ``controlIdentifier`` for your Amazon Web Services Control Tower control:**

The `controlIdentifier` is an ARN that is specified for each control. You can view the `controlIdentifier` in the console on the **Control details** page, as well as in the documentation.

**About identifiers for Amazon Web Services Control Tower**

The Amazon Web Services Control Tower `controlIdentifier` is unique in each Amazon Web Services Region for each control. You can find the `controlIdentifier` for each Region and control in the [Tables of control metadata](https://docs.aws.amazon.com/controltower/latest/controlreference/control-metadata-tables.html) or the [Control availability by Region tables](https://docs.aws.amazon.com/controltower/latest/controlreference/control-region-tables.html) in the *Amazon Web Services Control Tower Controls Reference Guide* .

A quick-reference list of control identifers for the Amazon Web Services Control Tower legacy *Strongly recommended* and *Elective* controls is given in [Resource identifiers for APIs and controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers.html.html) in the ` *Amazon Web Services Control Tower Controls Reference Guide* [https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers).html`__ . Remember that *Mandatory* controls cannot be added or removed.

### Note

**Some controls have two identifiers**

- **ARN format for Amazon Web Services Control Tower:** `arn:aws:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}` **Example:** `arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED`
- **ARN format for Amazon Web Services Control Catalog:** `arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}`

You can find the `{CONTROL_CATALOG_OPAQUE_ID}` in the ` *Amazon Web Services Control Tower Controls Reference Guide* [https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers).html`__ , or in the Amazon Web Services Control Tower console, on the **Control details** page.

The Amazon Web Services Control Tower APIs for enabled controls, such as `GetEnabledControl` and `ListEnabledControls` always return an ARN of the same type given when the control was enabled.

**To get the ``targetIdentifier`` :**

The `targetIdentifier` is the ARN for an OU.

In the Amazon Web Services Organizations console, you can find the ARN for the OU on the **Organizational unit details** page associated with that OU.

### Note

**OU ARN format:**

`arn:${Partition}:organizations::${MasterAccountId}:ou/o-${OrganizationId}/ou-${OrganizationalUnitId}`

**About landing zone APIs**

You can configure and launch an Amazon Web Services Control Tower landing zone with APIs. For an introduction and steps, see [Getting started with Amazon Web Services Control Tower using APIs](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-apis.html) .

For an overview of landing zone API operations, see [Amazon Web Services Control Tower supports landing zone APIs](https://docs.aws.amazon.com/controltower/latest/userguide/2023-all.html#landing-zone-apis) . The individual API operations for landing zones are detailed in this document, the [API reference manual](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Operations.html) , in the âActionsâ section.

**About baseline APIs**

You can apply the `AWSControlTowerBaseline` baseline to an organizational unit (OU) as a way to register the OU with Amazon Web Services Control Tower, programmatically. For a general overview of this capability, see [Amazon Web Services Control Tower supports APIs for OU registration and configuration with baselines](https://docs.aws.amazon.com/controltower/latest/userguide/2024-all.html#baseline-apis) .

You can call the baseline API operations to view the baselines that Amazon Web Services Control Tower enables for your landing zone, on your behalf, when setting up the landing zone. These baselines are read-only baselines.

The individual API operations for baselines are detailed in this document, the [API reference manual](https://docs.aws.amazon.com/controltower/latest/APIReference/API_Operations.html) , in the âActionsâ section. For usage examples, see [Baseline API input and output examples with CLI](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html) .

**About Amazon Web Services Control Catalog identifiers**

- The `EnableControl` and `DisableControl` API operations can be called by specifying either the Amazon Web Services Control Tower identifer or the Amazon Web Services Control Catalog identifier. The API response returns the same type of identifier that you specified when calling the API.
- If you use an Amazon Web Services Control Tower identifier to call the `EnableControl` API, and then call `EnableControl` again with an Amazon Web Services Control Catalog identifier, Amazon Web Services Control Tower returns an error message stating that the control is already enabled. Similar behavior applies to the `DisableControl` API operation.
- Mandatory controls and the landing-zone-level Region deny control have Amazon Web Services Control Tower identifiers only.

**Details and examples**

- [Control API input and output examples with CLI](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html)
- [Baseline API input and output examples with CLI](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html)
- [Enable controls with CloudFormation](https://docs.aws.amazon.com/controltower/latest/controlreference/enable-controls.html)
- [Launch a landing zone with CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/lz-apis-cfn-setup.html)
- [Control metadata tables (large page)](https://docs.aws.amazon.com/controltower/latest/controlreference/control-metadata-tables.html)
- [Control availability by Region tables (large page)](https://docs.aws.amazon.com/controltower/latest/controlreference/control-region-tables.html)
- [List of identifiers for legacy controls](https://docs.aws.amazon.com/controltower/latest/controlreference/control-identifiers.html)
- [Controls reference guide](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)
- [Controls library groupings](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html)
- [Creating Amazon Web Services Control Tower resources with Amazon Web Services CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/creating-resources-with-cloudformation.html)

To view the open source resource repository on GitHub, see [aws-cloudformation/aws-cloudformation-resource-providers-controltower](https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-controltower)

**Recording API Requests**

Amazon Web Services Control Tower supports Amazon Web Services CloudTrail, a service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine which requests the Amazon Web Services Control Tower service received, who made the request and when, and so on. For more about Amazon Web Services Control Tower and its support for CloudTrail, see [Logging Amazon Web Services Control Tower Actions with Amazon Web Services CloudTrail](https://docs.aws.amazon.com/controltower/latest/userguide/logging-using-cloudtrail.html) in the Amazon Web Services Control Tower User Guide. To learn more about CloudTrail, including how to turn it on and find your log files, see the Amazon Web Services CloudTrail User Guide.

## Available Commands

- [create-landing-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/create-landing-zone.html)
- [delete-landing-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/delete-landing-zone.html)
- [disable-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/disable-baseline.html)
- [disable-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/disable-control.html)
- [enable-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-baseline.html)
- [enable-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-control.html)
- [get-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline.html)
- [get-baseline-operation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline-operation.html)
- [get-control-operation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-control-operation.html)
- [get-enabled-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-baseline.html)
- [get-enabled-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-control.html)
- [get-landing-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-landing-zone.html)
- [get-landing-zone-operation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-landing-zone-operation.html)
- [list-baselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-baselines.html)
- [list-control-operations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-control-operations.html)
- [list-enabled-baselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-enabled-baselines.html)
- [list-enabled-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-enabled-controls.html)
- [list-landing-zone-operations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-landing-zone-operations.html)
- [list-landing-zones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-landing-zones.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-tags-for-resource.html)
- [reset-enabled-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-enabled-baseline.html)
- [reset-enabled-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-enabled-control.html)
- [reset-landing-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-landing-zone.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/untag-resource.html)
- [update-enabled-baseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-enabled-baseline.html)
- [update-enabled-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-enabled-control.html)
- [update-landing-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-landing-zone.html)