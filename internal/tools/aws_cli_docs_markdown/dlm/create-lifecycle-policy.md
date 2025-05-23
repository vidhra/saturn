# create-lifecycle-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dlm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/index.html#cli-aws-dlm) ]

# create-lifecycle-policy

## Description

Creates an Amazon Data Lifecycle Manager lifecycle policy. Amazon Data Lifecycle Manager supports the following policy types:

- Custom EBS snapshot policy
- Custom EBS-backed AMI policy
- Cross-account copy event policy
- Default policy for EBS snapshots
- Default policy for EBS-backed AMIs

For more information, see [Default policies vs custom policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/policy-differences.html) .

### Warning

If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/CreateLifecyclePolicy)

## Synopsis

```
create-lifecycle-policy
--execution-role-arn <value>
--description <value>
--state <value>
[--policy-details <value>]
[--tags <value>]
[--default-policy <value>]
[--create-interval <value>]
[--retain-interval <value>]
[--copy-tags | --no-copy-tags]
[--extend-deletion | --no-extend-deletion]
[--cross-region-copy-targets <value>]
[--exclusions <value>]
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

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.

`--description` (string)

A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.

`--state` (string)

The activation state of the lifecycle policy after creation.

Possible values:

- `ENABLED`
- `DISABLED`

`--policy-details` (structure)

The configuration details of the lifecycle policy.

### Warning

If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.

PolicyType -> (string)

The type of policy. Specify `EBS_SNAPSHOT_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify `IMAGE_MANAGEMENT` to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify `EVENT_BASED_POLICY` to create an event-based policy that performs specific actions when a defined event occurs in your Amazon Web Services account.

The default is `EBS_SNAPSHOT_MANAGEMENT` .

ResourceTypes -> (list)

**[Custom snapshot policies only]** The target resource type for snapshot and AMI lifecycle policies. Use `VOLUME` to create snapshots of individual volumes or use `INSTANCE` to create multi-volume snapshots from the volumes for an instance.

(string)

ResourceLocations -> (list)

**[Custom snapshot and AMI policies only]** The location of the resources to backup.

- If the source resources are located in a Region, specify `CLOUD` . In this case, the policy targets all resources of the specified type with matching target tags across all Availability Zones in the Region.
- **[Custom snapshot policies only]** If the source resources are located in a Local Zone, specify `LOCAL_ZONE` . In this case, the policy targets all resources of the specified type with matching target tags across all Local Zones in the Region.
- If the source resources are located on an Outpost in your account, specify `OUTPOST` . In this case, the policy targets all resources of the specified type with matching target tags across all of the Outposts in your account.

(string)

TargetTags -> (list)

**[Custom snapshot and AMI policies only]** The single tag that identifies targeted resources for this policy.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

Schedules -> (list)

**[Custom snapshot and AMI policies only]** The schedules of policy-defined actions for snapshot and AMI lifecycle policies. A policy can have up to four schedulesâone mandatory schedule and up to three optional schedules.

(structure)

**[Custom snapshot and AMI policies only]** Specifies a schedule for a snapshot or AMI lifecycle policy.

Name -> (string)

The name of the schedule.

CopyTags -> (boolean)

Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.

TagsToAdd -> (list)

The tags to apply to policy-created resources. These user-defined tags are in addition to the Amazon Web Services-added lifecycle tags.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

VariableTags -> (list)

**[AMI policies and snapshot policies that target instances only]** A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: `$(instance-id)` or `$(timestamp)` . Variable tags are only valid for EBS Snapshot Management â Instance policies.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

CreateRule -> (structure)

The creation rule.

Location -> (string)

**[Custom snapshot policies only]** Specifies the destination for snapshots created by the policy. The allowed destinations depend on the location of the targeted resources.

- If the policy targets resources in a Region, then you must create snapshots in the same Region as the source resource.
- If the policy targets resources in a Local Zone, you can create snapshots in the same Local Zone or in its parent Region.
- If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost or in its parent Region.

Specify one of the following values:

- To create snapshots in the same Region as the source resource, specify `CLOUD` .
- To create snapshots in the same Local Zone as the source resource, specify `LOCAL_ZONE` .
- To create snapshots on the same Outpost as the source resource, specify `OUTPOST_LOCAL` .

Default: `CLOUD`

Interval -> (integer)

The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.

IntervalUnit -> (string)

The interval unit.

Times -> (list)

The time, in UTC, to start the operation. The supported format is hh:mm.

The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.

(string)

CronExpression -> (string)

The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see the [Cron expressions reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html) in the *Amazon EventBridge User Guide* .

Scripts -> (list)

**[Custom snapshot policies that target instances only]** Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances. This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation.

For more information, see [Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html) .

(structure)

**[Custom snapshot policies that target instances only]** Information about pre and/or post scripts for a snapshot lifecycle policy that targets instances. For more information, see [Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html) .

Stages -> (list)

Indicate which scripts Amazon Data Lifecycle Manager should run on target instances. Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation.

- To run a pre script only, specify `PRE` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation.
- To run a post script only, specify `POST` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the `post-script` parameter after initiating snapshot creation.
- To run both pre and post scripts, specify both `PRE` and `POST` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation, and then it calls the SSM document again with the `post-script` parameter after initiating snapshot creation.

If you are automating VSS Backups, omit this parameter.

Default: PRE and POST

(string)

ExecutionHandlerService -> (string)

Indicates the service used to execute the pre and/or post scripts.

- If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify `AWS_SYSTEMS_MANAGER` .
- If you are automating VSS Backups, omit this parameter.

Default: AWS_SYSTEMS_MANAGER

ExecutionHandler -> (string)

The SSM document that includes the pre and/or post scripts to run.

- If you are automating VSS backups, specify `AWS_VSS_BACKUP` . In this case, Amazon Data Lifecycle Manager automatically uses the `AWSEC2-CreateVssSnapshot` SSM document.
- If you are automating application-consistent snapshots for SAP HANA workloads, specify `AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA` .
- If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.

ExecuteOperationOnScriptFailure -> (boolean)

Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails.

- To default to crash consistent snapshot if the pre script fails, specify `true` .
- To skip the instance for snapshot creation if the pre script fails, specify `false` .

This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter.

Default: true

ExecutionTimeout -> (integer)

Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually.

If you are automating VSS Backups, omit this parameter.

Default: 10

MaximumRetryCount -> (integer)

Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail.

- If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts.
- If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created.

If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify `0` .

Default: 0

RetainRule -> (structure)

The retention rule for snapshots or AMIs created by the policy.

Count -> (integer)

The number of snapshots to retain for each volume, up to a maximum of 1000. For example if you want to retain a maximum of three snapshots, specify `3` . When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) .

Interval -> (integer)

The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit -> (string)

The unit of time for time-based retention. For example, to retain snapshots for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS` . Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) .

FastRestoreRule -> (structure)

**[Custom snapshot policies only]** The rule for enabling fast snapshot restore.

Count -> (integer)

The number of snapshots to be enabled with fast snapshot restore.

Interval -> (integer)

The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit -> (string)

The unit of time for enabling fast snapshot restore.

AvailabilityZones -> (list)

The Availability Zones in which to enable fast snapshot restore.

(string)

CrossRegionCopyRules -> (list)

Specifies a rule for copying snapshots or AMIs across Regions.

### Note

You canât specify cross-Region copy rules for policies that create snapshots on an Outpost or in a Local Zone. If the policy creates snapshots in a Region, then snapshots can be copied to up to three Regions or Outposts.

(structure)

**[Custom snapshot and AMI policies only]** Specifies a cross-Region copy rule for a snapshot and AMI policies.

### Note

To specify a cross-Region copy action for event-based polices, use [CrossRegionCopyAction](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html) .

TargetRegion -> (string)

### Note

Use this parameter for AMI policies only. For snapshot policies, use **Target** instead. For snapshot policies created before the **Target** parameter was introduced, this parameter indicates the target Region for snapshot copies.

**[Custom AMI policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.

Target -> (string)

### Note

Use this parameter for snapshot policies only. For AMI policies, use **TargetRegion** instead.

**[Custom snapshot policies only]** The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.

Encrypted -> (boolean)

To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.

CmkArn -> (string)

The Amazon Resource Name (ARN) of the KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.

CopyTags -> (boolean)

Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.

RetainRule -> (structure)

The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.

Interval -> (integer)

The amount of time to retain a cross-Region snapshot or AMI copy. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit -> (string)

The unit of time for time-based retention. For example, to retain a cross-Region copy for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS` .

DeprecateRule -> (structure)

**[Custom AMI policies only]** The AMI deprecation rule for cross-Region AMI copies created by the rule.

Interval -> (integer)

The period after which to deprecate the cross-Region AMI copies. The period must be less than or equal to the cross-Region AMI copy retention period, and it canât be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.

IntervalUnit -> (string)

The unit of time in which to measure the **Interval** . For example, to deprecate a cross-Region AMI copy after 3 months, specify `Interval=3` and `IntervalUnit=MONTHS` .

ShareRules -> (list)

**[Custom snapshot policies only]** The rule for sharing snapshots with other Amazon Web Services accounts.

(structure)

**[Custom snapshot policies only]** Specifies a rule for sharing snapshots across Amazon Web Services accounts.

TargetAccounts -> (list)

The IDs of the Amazon Web Services accounts with which to share the snapshots.

(string)

UnshareInterval -> (integer)

The period after which snapshots that are shared with other Amazon Web Services accounts are automatically unshared.

UnshareIntervalUnit -> (string)

The unit of time for the automatic unsharing interval.

DeprecateRule -> (structure)

**[Custom AMI policies only]** The AMI deprecation rule for the schedule.

Count -> (integer)

If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate. The count must be less than or equal to the scheduleâs retention count, and it canât be greater than 1000.

Interval -> (integer)

If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule. The period must be less than or equal to the scheduleâs retention period, and it canât be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.

IntervalUnit -> (string)

The unit of time in which to measure the **Interval** .

ArchiveRule -> (structure)

**[Custom snapshot policies that target volumes only]** The snapshot archiving rule for the schedule. When you specify an archiving rule, snapshots are automatically moved from the standard tier to the archive tier once the scheduleâs retention threshold is met. Snapshots are then retained in the archive tier for the archive retention period that you specify.

For more information about using snapshot archiving, see [Considerations for snapshot lifecycle policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive) .

RetainRule -> (structure)

Information about the retention period for the snapshot archiving rule.

RetentionArchiveTier -> (structure)

Information about retention period in the Amazon EBS Snapshots Archive. For more information, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html) .

Count -> (integer)

The maximum number of snapshots to retain in the archive storage tier for each volume. The count must ensure that each snapshot remains in the archive tier for at least 90 days. For example, if the schedule creates snapshots every 30 days, you must specify a count of 3 or more to ensure that each snapshot is archived for at least 90 days.

Interval -> (integer)

Specifies the period of time to retain snapshots in the archive tier. After this period expires, the snapshot is permanently deleted.

IntervalUnit -> (string)

The unit of time in which to measure the **Interval** . For example, to retain a snapshots in the archive tier for 6 months, specify `Interval=6` and `IntervalUnit=MONTHS` .

Parameters -> (structure)

**[Custom snapshot and AMI policies only]** A set of optional parameters for snapshot and AMI lifecycle policies.

### Note

If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You canât omit this parameter or set its values to null.

ExcludeBootVolume -> (boolean)

**[Custom snapshot policies that target instances only]** Indicates whether to exclude the root volume from multi-volume snapshot sets. The default is `false` . If you specify `true` , then the root volumes attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.

NoReboot -> (boolean)

**[Custom AMI policies only]** Indicates whether targeted instances are rebooted when the lifecycle policy runs. `true` indicates that targeted instances are not rebooted when the policy runs. `false` indicates that target instances are rebooted when the policy runs. The default is `true` (instances are not rebooted).

ExcludeDataVolumeTags -> (list)

**[Custom snapshot policies that target instances only]** The tags used to identify data (non-root) volumes to exclude from multi-volume snapshot sets.

If you create a snapshot lifecycle policy that targets instances and you specify tags for this parameter, then data volumes with the specified tags that are attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

EventSource -> (structure)

**[Event-based policies only]** The event that activates the event-based policy.

Type -> (string)

The source of the event. Currently only managed CloudWatch Events rules are supported.

Parameters -> (structure)

Information about the event.

EventType -> (string)

The type of event. Currently, only snapshot sharing events are supported.

SnapshotOwner -> (list)

The IDs of the Amazon Web Services accounts that can trigger policy by sharing snapshots with your account. The policy only runs if one of the specified Amazon Web Services accounts shares a snapshot with your account.

(string)

DescriptionRegex -> (string)

The snapshot description that can trigger the policy. The description pattern is specified using a regular expression. The policy runs only if a snapshot with a description that matches the specified pattern is shared with your account.

For example, specifying `^.*Created for policy: policy-1234567890abcdef0.*$` configures the policy to run only if snapshots created by policy `policy-1234567890abcdef0` are shared with your account.

Actions -> (list)

**[Event-based policies only]** The actions to be performed when the event-based policy is activated. You can specify only one action per policy.

(structure)

**[Event-based policies only]** Specifies an action for an event-based policy.

Name -> (string)

A descriptive name for the action.

CrossRegionCopy -> (list)

The rule for copying shared snapshots across Regions.

(structure)

**[Event-based policies only]** Specifies a cross-Region copy action for event-based policies.

### Note

To specify a cross-Region copy rule for snapshot and AMI policies, use [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html) .

Target -> (string)

The target Region.

EncryptionConfiguration -> (structure)

The encryption settings for the copied snapshot.

Encrypted -> (boolean)

To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.

CmkArn -> (string)

The Amazon Resource Name (ARN) of the KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.

RetainRule -> (structure)

Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies. After the retention period expires, the cross-Region copy is deleted.

Interval -> (integer)

The amount of time to retain a cross-Region snapshot or AMI copy. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit -> (string)

The unit of time for time-based retention. For example, to retain a cross-Region copy for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS` .

PolicyLanguage -> (string)

The type of policy to create. Specify one of the following:

- `SIMPLIFIED` To create a default policy.
- `STANDARD` To create a custom policy.

ResourceType -> (string)

**[Default policies only]** Specify the type of default policy to create.

- To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME` .
- To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE` .

CreateInterval -> (integer)

**[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.

Default: 1

RetainInterval -> (integer)

**[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.

Default: 7

CopyTags -> (boolean)

**[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false` .

Default: false

CrossRegionCopyTargets -> (list)

**[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.

(structure)

**[Default policies only]** Specifies a destination Region for cross-Region copy actions.

TargetRegion -> (string)

The target Region, for example `us-east-1` .

ExtendDeletion -> (boolean)

**[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.

By default (**ExtendDeletion=false** ):

- If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true` .
- If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true` .

If you enable extended deletion (**ExtendDeletion=true** ), you override both default behaviors simultaneously.

If you do not specify a value, the default is `false` .

Default: false

Exclusions -> (structure)

**[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

ExcludeBootVolumes -> (boolean)

**[Default policies for EBS snapshots only]** Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify `true` .

ExcludeVolumeTypes -> (list)

**[Default policies for EBS snapshots only]** Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.

(string)

ExcludeTags -> (list)

**[Default policies for EBS-backed AMIs only]** Specifies whether to exclude volumes that have specific tags.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

JSON Syntax:

```
{
  "PolicyType": "EBS_SNAPSHOT_MANAGEMENT"|"IMAGE_MANAGEMENT"|"EVENT_BASED_POLICY",
  "ResourceTypes": ["VOLUME"|"INSTANCE", ...],
  "ResourceLocations": ["CLOUD"|"OUTPOST"|"LOCAL_ZONE", ...],
  "TargetTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ],
  "Schedules": [
    {
      "Name": "string",
      "CopyTags": true|false,
      "TagsToAdd": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ],
      "VariableTags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ],
      "CreateRule": {
        "Location": "CLOUD"|"OUTPOST_LOCAL"|"LOCAL_ZONE",
        "Interval": integer,
        "IntervalUnit": "HOURS",
        "Times": ["string", ...],
        "CronExpression": "string",
        "Scripts": [
          {
            "Stages": ["PRE"|"POST", ...],
            "ExecutionHandlerService": "AWS_SYSTEMS_MANAGER",
            "ExecutionHandler": "string",
            "ExecuteOperationOnScriptFailure": true|false,
            "ExecutionTimeout": integer,
            "MaximumRetryCount": integer
          }
          ...
        ]
      },
      "RetainRule": {
        "Count": integer,
        "Interval": integer,
        "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      },
      "FastRestoreRule": {
        "Count": integer,
        "Interval": integer,
        "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS",
        "AvailabilityZones": ["string", ...]
      },
      "CrossRegionCopyRules": [
        {
          "TargetRegion": "string",
          "Target": "string",
          "Encrypted": true|false,
          "CmkArn": "string",
          "CopyTags": true|false,
          "RetainRule": {
            "Interval": integer,
            "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
          },
          "DeprecateRule": {
            "Interval": integer,
            "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
          }
        }
        ...
      ],
      "ShareRules": [
        {
          "TargetAccounts": ["string", ...],
          "UnshareInterval": integer,
          "UnshareIntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
        }
        ...
      ],
      "DeprecateRule": {
        "Count": integer,
        "Interval": integer,
        "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      },
      "ArchiveRule": {
        "RetainRule": {
          "RetentionArchiveTier": {
            "Count": integer,
            "Interval": integer,
            "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
          }
        }
      }
    }
    ...
  ],
  "Parameters": {
    "ExcludeBootVolume": true|false,
    "NoReboot": true|false,
    "ExcludeDataVolumeTags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  },
  "EventSource": {
    "Type": "MANAGED_CWE",
    "Parameters": {
      "EventType": "shareSnapshot",
      "SnapshotOwner": ["string", ...],
      "DescriptionRegex": "string"
    }
  },
  "Actions": [
    {
      "Name": "string",
      "CrossRegionCopy": [
        {
          "Target": "string",
          "EncryptionConfiguration": {
            "Encrypted": true|false,
            "CmkArn": "string"
          },
          "RetainRule": {
            "Interval": integer,
            "IntervalUnit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
          }
        }
        ...
      ]
    }
    ...
  ],
  "PolicyLanguage": "SIMPLIFIED"|"STANDARD",
  "ResourceType": "VOLUME"|"INSTANCE",
  "CreateInterval": integer,
  "RetainInterval": integer,
  "CopyTags": true|false,
  "CrossRegionCopyTargets": [
    {
      "TargetRegion": "string"
    }
    ...
  ],
  "ExtendDeletion": true|false,
  "Exclusions": {
    "ExcludeBootVolumes": true|false,
    "ExcludeVolumeTypes": ["string", ...],
    "ExcludeTags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
}
```

`--tags` (map)

The tags to apply to the lifecycle policy during creation.

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

`--default-policy` (string)

**[Default policies only]** Specify the type of default policy to create.

- To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME` .
- To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE` .

Possible values:

- `VOLUME`
- `INSTANCE`

`--create-interval` (integer)

**[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.

Default: 1

`--retain-interval` (integer)

**[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.

Default: 7

`--copy-tags` | `--no-copy-tags` (boolean)

**[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false` .

Default: false

`--extend-deletion` | `--no-extend-deletion` (boolean)

**[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.

By default (**ExtendDeletion=false** ):

- If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true` .
- If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true` .

If you enable extended deletion (**ExtendDeletion=true** ), you override both default behaviors simultaneously.

If you do not specify a value, the default is `false` .

Default: false

`--cross-region-copy-targets` (list)

**[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.

(structure)

**[Default policies only]** Specifies a destination Region for cross-Region copy actions.

TargetRegion -> (string)

The target Region, for example `us-east-1` .

Shorthand Syntax:

```
TargetRegion=string ...
```

JSON Syntax:

```
[
  {
    "TargetRegion": "string"
  }
  ...
]
```

`--exclusions` (structure)

**[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

ExcludeBootVolumes -> (boolean)

**[Default policies for EBS snapshots only]** Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify `true` .

ExcludeVolumeTypes -> (list)

**[Default policies for EBS snapshots only]** Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.

(string)

ExcludeTags -> (list)

**[Default policies for EBS-backed AMIs only]** Specifies whether to exclude volumes that have specific tags.

(structure)

Specifies a tag for a resource.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

Shorthand Syntax:

```
ExcludeBootVolumes=boolean,ExcludeVolumeTypes=string,string,ExcludeTags=[{Key=string,Value=string},{Key=string,Value=string}]
```

JSON Syntax:

```
{
  "ExcludeBootVolumes": true|false,
  "ExcludeVolumeTypes": ["string", ...],
  "ExcludeTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ]
}
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

**To create a lifecycle policy**

The following `create-lifecycle-policy` example creates a lifecycle policy that creates a daily snapshot of volumes at the specified time. The specified tags are added to the snapshots, and tags are also copied from the volume and added to the snapshots. If creating a new snapshot exceeds the specified maximum count, the oldest snapshot is deleted.

```
aws dlm create-lifecycle-policy \
    --description "My first policy" \
    --state ENABLED \
    --execution-role-arn arn:aws:iam::12345678910:role/AWSDataLifecycleManagerDefaultRole \
    --policy-details file://policyDetails.json
```

Contents of `policyDetails.json`:

```
{
    "ResourceTypes": [
        "VOLUME"
    ],
    "TargetTags": [
        {
            "Key": "costCenter",
            "Value": "115"
        }
    ],
    "Schedules":[
        {
            "Name": "DailySnapshots",
            "CopyTags": true,
            "TagsToAdd": [
                {
                    "Key": "type",
                     "Value": "myDailySnapshot"
                }
            ],
            "CreateRule": {
                "Interval": 24,
                "IntervalUnit": "HOURS",
                "Times": [
                    "03:00"
                ]
            },
            "RetainRule": {
                "Count":5
            }
        }
    ]
}
```

Output:

```
{
    "PolicyId": "policy-0123456789abcdef0"
}
```

## Output

PolicyId -> (string)

The identifier of the lifecycle policy.