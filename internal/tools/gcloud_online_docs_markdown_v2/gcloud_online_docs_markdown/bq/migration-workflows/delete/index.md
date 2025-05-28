# gcloud bq migration-workflows delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bq/migration-workflows/delete](https://cloud.google.com/sdk/gcloud/reference/bq/migration-workflows/delete)*

**NAME**

: **gcloud bq migration-workflows delete - delete migration workflows**

**SYNOPSIS**

: **`gcloud bq migration-workflows delete` (`[WORKFLOW](https://cloud.google.com/sdk/gcloud/reference/bq/migration-workflows/delete#WORKFLOW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/bq/migration-workflows/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bq/migration-workflows/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a migration workflow

**EXAMPLES**

: To delete a migration workflow
`projects/123/locations/eu/workflows/1234`, run:

```
gcloud bq migration-workflows delete projects/123/locations/eu/workflows/1234
```

**POSITIONAL ARGUMENTS**

: **Workflow resource - The unique identifier for the migration workflow. Example:
`projects/123/locations/us/workflows/1234` The arguments in this
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
The location id of the workflow resource.
To set the `location` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `bigquerymigration/v2` API. The full
documentation for this API can be found at: [https://cloud.google.com/solutions/migration/dw2bq/dw-bq-migration-overview](https://cloud.google.com/solutions/migration/dw2bq/dw-bq-migration-overview)

**NOTES**

: These variants are also available:

```
gcloud alpha bq migration-workflows delete
```

```
gcloud beta bq migration-workflows delete
```