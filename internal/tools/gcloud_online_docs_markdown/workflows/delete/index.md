# gcloud workflows delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workflows/delete](https://cloud.google.com/sdk/gcloud/reference/workflows/delete)*

**NAME**

: **gcloud workflows delete - delete a workflow**

**SYNOPSIS**

: **`gcloud workflows delete` (`[WORKFLOW](https://cloud.google.com/sdk/gcloud/reference/workflows/delete#WORKFLOW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workflows/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workflows/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workflows/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a workflow and all of its executions.

**EXAMPLES**

: To delete the workflow 'my-workflow', run:

```
gcloud workflows delete my-workflow
```

You may also skip waiting for the operation to finish:

```
gcloud workflows delete my-workflow --async
```

**POSITIONAL ARGUMENTS**

: **Workflow resource - The name of the workflow to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKFLOW`**:
ID of the workflow or fully qualified identifier for the workflow.
To set the `workflow` attribute:

- provide the argument `workflow` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the workflow. Alternatively, set the property
[workflows/location].
To set the `location` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `workflows/location`.**

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

**API REFERENCE**

: This command uses the `workflows/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/workflows](https://cloud.google.com/workflows)

**NOTES**

: This variant is also available:

```
gcloud beta workflows delete
```