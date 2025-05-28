# gcloud run jobs executions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe)*

**NAME**

: **gcloud run jobs executions describe - obtain details about executions**

**SYNOPSIS**

: **`gcloud run jobs executions describe` `[EXECUTION](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe#EXECUTION)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Obtain details about executions.

**EXAMPLES**

: To describe an execution:

```
gcloud run jobs executions describe my-execution
```

**POSITIONAL ARGUMENTS**

: **Execution resource - Execution to describe. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `EXECUTION` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EXECUTION`**:
ID of the Execution or fully qualified identifier for the Execution.
To set the `executions` attribute:

- provide the argument `EXECUTION` on the command line.**

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

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
gcloud alpha run jobs executions describe
```

```
gcloud beta run jobs executions describe
```