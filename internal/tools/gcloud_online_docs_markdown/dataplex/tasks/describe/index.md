# gcloud dataplex tasks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe)*

**NAME**

: **gcloud dataplex tasks describe - describe a Dataplex task resource**

**SYNOPSIS**

: **`gcloud dataplex tasks describe` (`[TASK](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe#TASK)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Dataplex task resource.
Displays all details of a Dataplex task resource given a valid task ID.

**EXAMPLES**

: To describe a Dataplex task `test-task` within lake
`test-lake` in location `us-central1`, run:

```
gcloud dataplex tasks describe test-task --location=us-central1 --lake=test-lake
```

**POSITIONAL ARGUMENTS**

: **Task resource - Arguments and flags that define the Dataplex Tasks you want to
retrieve. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TASK`**:
ID of the task or fully qualified identifier for the task.
To set the `task` attribute:

- provide the argument `task` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
Identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

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

**API REFERENCE**

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex tasks describe
```