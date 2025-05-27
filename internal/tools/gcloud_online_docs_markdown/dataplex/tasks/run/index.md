# gcloud dataplex tasks run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run)*

**NAME**

: **gcloud dataplex tasks run - trigger one-time run of a Dataplex task**

**SYNOPSIS**

: **`gcloud dataplex tasks run` (`[TASK](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run#TASK)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run#--location)`=`LOCATION`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/run#GCLOUD-WIDE-FLAGS) …`] [-- `execution-spec-args` …]**

**DESCRIPTION**

: Trigger one-time run of a Dataplex task.

**EXAMPLES**

: To trigger a one-time run of a Dataplex task `test-task` within lake
`test-lake` in location `us-central1`, run:

```
gcloud dataplex tasks run test-task --location=us-central1 --lake=test-lake
```

**POSITIONAL ARGUMENTS**

: **Tasks resource - Arguments and flags that define the Dataplex task you want to
run. The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TASK`**:
ID of the tasks or fully qualified identifier for the tasks.
To set the `task` attribute:

- provide the argument `task` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**[-- `execution-spec-args` …]**:
Execution spec arguments to pass to the driver. Follows the format
argKey=argValue.
The '--' argument must be specified between gcloud specific args on the left and
execution-spec-args on the right.

**FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

: This variant is also available:

```
gcloud alpha dataplex tasks run
```