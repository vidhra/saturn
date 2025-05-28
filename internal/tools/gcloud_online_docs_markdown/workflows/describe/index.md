# gcloud workflows describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workflows/describe](https://cloud.google.com/sdk/gcloud/reference/workflows/describe)*

**NAME**

: **gcloud workflows describe - show metadata for a workflow**

**SYNOPSIS**

: **`gcloud workflows describe` (`[WORKFLOW](https://cloud.google.com/sdk/gcloud/reference/workflows/describe#WORKFLOW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workflows/describe#--location)`=`LOCATION`) [`[--revision-id](https://cloud.google.com/sdk/gcloud/reference/workflows/describe#--revision-id)`=`REVISION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workflows/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display all metadata associated with a workflow of given name and revisionID. If
revisionID is not provided, the metadata for the latest revision is retrieved.

**EXAMPLES**

: To describe the workflow 'my-workflow' at revision '000001-dc1', run:

```
gcloud workflows describe my-workflow `--revision-id=000001-dc1`
```

**POSITIONAL ARGUMENTS**

: **Workflow resource - The name of the workflow to describe. The arguments in this
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

: **--revision-id**:
The revision ID of the workflow to describe.

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
gcloud beta workflows describe
```