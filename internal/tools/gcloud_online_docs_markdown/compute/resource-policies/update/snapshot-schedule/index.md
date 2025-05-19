# gcloud compute resource-policies update snapshot-schedule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule)*

**NAME**

: **gcloud compute resource-policies update snapshot-schedule - update a Compute Engine Snapshot Schedule Resource Policy**

**SYNOPSIS**

: **`gcloud compute resource-policies update snapshot-schedule` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--description)`=`DESCRIPTION`] [`[--max-retention-days](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--max-retention-days)`=`MAX_RETENTION_DAYS`] [`[--on-source-disk-delete](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--on-source-disk-delete)`=`ON_SOURCE_DISK_DELETE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--region)`=`REGION`] [`[--snapshot-labels](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--snapshot-labels)`=[`KEY`=`VALUE`,…]] [`[--weekly-schedule-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--weekly-schedule-from-file)`=`PATH_TO_FILE`     | `[--start-time](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--start-time)`=`START_TIME` (`[--daily-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--daily-schedule)` | `[--hourly-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--hourly-schedule)`=`HOURS` | `[--weekly-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#--weekly-schedule)`=`WEEKLY_CYCLE`)] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/snapshot-schedule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine Snapshot Schedule Resource Policy.

**EXAMPLES**

: The following command updates a Compute Engine Snapshot Schedule Resource Policy
to take a daily snapshot at 13:00 UTC

```
gcloud compute resource-policies update snapshot-schedule my-resource-policy --region=REGION --start-time=13:00 --daily-schedule
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the resource policy to operate on.

**FLAGS**

: **--description**:
An optional, textual description for the backend.

**--max-retention-days**:
Maximum number of days snapshot can be retained.

**--on-source-disk-delete**:
Retention behavior of automatic snapshots in the event of source disk deletion.
`ON_SOURCE_DISK_DELETE` must be one of:

**`apply-retention-policy`**:
Continue to apply the retention window to automatically-created snapshots when
the source disk is deleted.

**`keep-auto-snapshots`**:
Keep automatically-created snapshots when the source disk is deleted. This is
the default behavior.

**--region**:
Region of the resource policy to operate on. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--snapshot-labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.
The label is added to each snapshot created by the schedule.

**--weekly-schedule-from-file**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha compute resource-policies update snapshot-schedule
```

```
gcloud beta compute resource-policies update snapshot-schedule
```