# gcloud monitoring snoozes cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/cancel](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/cancel)*

**NAME**

: **gcloud monitoring snoozes cancel - cancels a snooze**

**SYNOPSIS**

: **`gcloud monitoring snoozes cancel` `[SNOOZE](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/cancel#SNOOZE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a snooze.
If the start time is in the future, then this command is equivalent to:

- update --start-time="+PT1S" --end-time="+PT1S

Otherwise, if the start time is past and the ending time is in the future, then
this command is equivalent to:

- update --end-time="+PT1S

For information about the JSON/YAML format of a snooze: [https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes)

**EXAMPLES**

: To cancel a snooze, run:

```
gcloud monitoring snoozes cancel MY-SNOOZE
```

To cancel a snooze contained within a specific project, run:

```
gcloud monitoring snoozes cancel MY-SNOOZE --project=MY-PROJECT
```

To cancel a snooze with a fully qualified snooze ID, run:

```
gcloud monitoring snoozes cancel projects/MY-PROJECT/snoozes/MY-SNOOZE
```

**POSITIONAL ARGUMENTS**

: **Snooze resource - Name of the Snooze to be canceled. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `snooze` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SNOOZE`**:
ID of the Snooze or fully qualified identifier for the Snooze.
To set the `snooze` attribute:

- provide the argument `snooze` on the command line.**

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
gcloud alpha monitoring snoozes cancel
```

```
gcloud beta monitoring snoozes cancel
```