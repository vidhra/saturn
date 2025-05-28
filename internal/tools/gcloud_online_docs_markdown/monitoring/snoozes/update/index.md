# gcloud monitoring snoozes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update)*

**NAME**

: **gcloud monitoring snoozes update - updates a snooze**

**SYNOPSIS**

: **`gcloud monitoring snoozes update` `[SNOOZE](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#SNOOZE)` [`[--snooze-from-file](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#--snooze-from-file)`=`PATH_TO_FILE`] [`[--fields](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#--fields)`=[`field`,…]     | `[--display-name](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#--display-name)`=`DISPLAY_NAME` `[--end-time](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#--end-time)`=`END_TIME` `[--start-time](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#--start-time)`=`START_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a snooze.
If `--snooze-from-file` is specified, then the update rules depend on
the value of the (optional) `--fields` flag:

- If `--fields` is specified, then only the specified fields of the
snooze are updated.
- Else, all fields of the snooze are replaced. The updated snooze can be modified
further using the flags from the Snooze Settings group below.

Otherwise, the snooze will be updated with the values specified in the flags
from the Snooze Settings group.
For information about the JSON/YAML format of a snooze: [https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes)

**EXAMPLES**

: To update a snooze time interval with command-line options, run:

```
gcloud monitoring snoozes update MY-SNOOZE --start-time=START_TIME --end-time=END_TIME
```

To update a snooze display name with a file, run:

```
gcloud monitoring snoozes update --snooze-from-file=MY-FILE --fields=display_name
```

Sample contents of MY-FILE:

```
criteria:
  policies:
  - projects/MY-PROJECT/alertPolicies/MY-POLICY
interval:
  startTime: '2024-03-01T08:00:00Z'
  endTime: '2024-03-08T04:59:59.500Z'
displayName: New Snooze with New Display Name
```

**POSITIONAL ARGUMENTS**

: **Snooze resource - Name of the Snooze to be updated. This represents a Cloud
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

**FLAGS**

: **--snooze-from-file**:
The path to a JSON or YAML file containing the snooze. Use a full or relative
path to a local file containing the value of snooze.

**--fields**

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
gcloud alpha monitoring snoozes update
```

```
gcloud beta monitoring snoozes update
```