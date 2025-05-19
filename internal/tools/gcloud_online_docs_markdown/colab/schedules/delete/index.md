# gcloud colab schedules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete)*

**NAME**

: **gcloud colab schedules delete - delete a schedule**

**SYNOPSIS**

: **`gcloud colab schedules delete` (`[SCHEDULE](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete#SCHEDULE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Colab Enterprise notebook execution schedule.

**EXAMPLES**

: To delete a schedule with id `my-schedule`, in region
`us-central1`, run:

```
gcloud colab schedules delete my-schedule --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Schedule resource - Unique, system-generated resource name of the schedule to
delete. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `schedule` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCHEDULE`**:
ID of the schedule or fully qualified identifier for the schedule.
To set the `name` attribute:

- provide the argument `schedule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the schedule.
To set the `region` attribute:

- provide the argument `schedule` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `colab/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud beta colab schedules delete
```