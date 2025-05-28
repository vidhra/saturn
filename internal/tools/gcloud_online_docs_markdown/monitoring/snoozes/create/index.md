# gcloud monitoring snoozes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create)*

**NAME**

: **gcloud monitoring snoozes create - create a new snooze**

**SYNOPSIS**

: **`gcloud monitoring snoozes create` [`[--snooze-from-file](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--snooze-from-file)`=`PATH_TO_FILE`] [`[--criteria-filter](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--criteria-filter)`=`CRITERIA_FILTER` `[--criteria-policies](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--criteria-policies)`=`CRITERIA_POLICIES`,[…] `[--display-name](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--display-name)`=`DISPLAY_NAME` `[--end-time](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--end-time)`=`END_TIME` `[--start-time](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#--start-time)`=`START_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/snoozes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new snooze. A snooze can be specified as a JSON/YAML value passed in
as a file through the `--snooze-from-file` flag. A snooze can also be
specified through command line flags. If a snooze is specified through
`--snooze-from-file`, and additional flags are supplied, the flags
will override the snooze's settings.
For information about the JSON/YAML format of a snooze: [https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes)

**EXAMPLES**

: To create a snooze with command-line options, run:

```
gcloud monitoring snoozes create --criteria-policies=LIST_OF_POLICIES --criteria-filter=FILTER --display-name=DISPLAY_NAME --start-time=START_TIME --end-time=END_TIME
```

To create a snooze with a file, run:

```
gcloud monitoring snoozes create --snooze-from-file=MY-FILE
```

Sample contents of MY-FILE:

```
criteria:
  policies:
  - projects/MY-PROJECT/alertPolicies/MY-POLICY
  filter: 'resource.labels.zone="us-central1-a" AND resource.labels.instance_id="1234567890"'
interval:
  startTime: '2024-03-01T08:00:00Z'
  endTime: '2024-03-08T04:59:59.500Z'
displayName: New Snooze
```

**FLAGS**

: **--snooze-from-file**:
The path to a JSON or YAML file containing the snooze. Use a full or relative
path to a local file containing the value of snooze.

**--snooze-from-file**

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
gcloud alpha monitoring snoozes create
```

```
gcloud beta monitoring snoozes create
```