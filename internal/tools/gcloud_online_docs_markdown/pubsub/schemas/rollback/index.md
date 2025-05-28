# gcloud pubsub schemas rollback  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback)*

**NAME**

: **gcloud pubsub schemas rollback - roll back a Pub/Sub schema to a specified revision**

**SYNOPSIS**

: **`gcloud pubsub schemas rollback` `[SCHEMA](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback#SCHEMA)` `[--revision-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback#--revision-id)`=`REVISION_ID` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Roll back a Pub/Sub schema to a specified revision.

**EXAMPLES**

: To roll back to an existing schema revision called "key-schema" with
revision_id: "0a0b0c0d", run:

```
gcloud pubsub schemas rollback key-schema --revision-id=0a0b0c0d
```

**POSITIONAL ARGUMENTS**

: **Schema resource - Name of the schema to rollback. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `schema` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCHEMA`**:
ID of the schema or fully qualified identifier for the schema.
To set the `schema` attribute:

- provide the argument `schema` on the command line.**

**REQUIRED FLAGS**

: **--revision-id**:
The revision to roll back to.

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
gcloud alpha pubsub schemas rollback
```

```
gcloud beta pubsub schemas rollback
```