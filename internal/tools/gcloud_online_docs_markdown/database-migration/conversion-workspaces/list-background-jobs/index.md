# gcloud database-migration conversion-workspaces list-background-jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs)*

**NAME**

: **gcloud database-migration conversion-workspaces list-background-jobs - list background jobs in the conversion workspaces**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces list-background-jobs` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs#--region)`=`REGION`) [`[--max-size](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs#--max-size)`=`MAX_SIZE`] [`[--most-recent-per-job-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs#--most-recent-per-job-type)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/list-background-jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List background jobs in the conversion workspaces.

**EXAMPLES**

: To list the background jobs in a conversion workspaces in a project and location
`us-central1`, run:

```
gcloud database-migration conversion-workspaces list-background-jobs my-conversion-workspace --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace you want to get the
details of. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONVERSION_WORKSPACE`**:
ID of the conversion_workspace or fully qualified identifier for the
conversion_workspace.
To set the `conversion_workspace` attribute:

- provide the argument `conversion_workspace` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the region.
To set the `region` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--max-size**:
The maximum number of jobs to return. The service may return fewer than this
value. If unspecified, at most 100 jobs will be returned. The maximum value is
100; values above 100 will be coerced to 100.

**--most-recent-per-job-type**:
Returns only the most recent job per job type.

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

: This command uses the `datamigration/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/database-migration/](https://cloud.google.com/database-migration/)