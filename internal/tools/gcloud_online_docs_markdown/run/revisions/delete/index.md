# gcloud run revisions delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete)*

**NAME**

: **gcloud run revisions delete - delete a revision**

**SYNOPSIS**

: **`gcloud run revisions delete` (`[REVISION](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete#REVISION)` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete#--namespace)`=`NAMESPACE`) [`[--[no-]async](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete#--[no-]async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a revision.

**EXAMPLES**

: To delete a revision:

```
gcloud run revisions delete <revision-name>
```

**POSITIONAL ARGUMENTS**

: **Revision resource - Revision to delete. The arguments in this group can be used
to specify the attributes of this resource.
This must be specified.

**`REVISION`**:
ID of the revision or fully qualified identifier for the revision.
To set the `revision` attribute:

- provide the argument `REVISION` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--namespace**:
Specific to Cloud Run for Anthos: Kubernetes namespace for the revision.
To set the `namespace` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line;
- set the property `run/namespace`;
- For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults
to project ID.;
- provide the argument `project` on the command line;
- set the property `core/project`.**

**FLAGS**

: **--[no-]async**:
Return immediately, without waiting for the operation in progress to complete.
Defaults to --no-async. Use `--async` to enable and
`--no-async` to disable.

**--region**:
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
gcloud alpha run revisions delete
```

```
gcloud beta run revisions delete
```