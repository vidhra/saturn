# gcloud database-migration operations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete](https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete)*

**NAME**

: **gcloud database-migration operations delete - delete a Database Migration Service operation**

**SYNOPSIS**

: **`gcloud database-migration operations delete` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete#OPERATION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Database Migration Service operation.

**EXAMPLES**

: To delete an operation.

```
gcloud database-migration operations delete OPERATION --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - Operation resource - Database Migration Service operation
to delete. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the region.
To set the `region` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

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

**NOTES**

: This variant is also available:

```
gcloud alpha database-migration operations delete
```