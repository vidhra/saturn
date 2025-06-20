# gcloud metastore operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/cancel)*

**NAME**

: **gcloud metastore operations cancel - cancel a Dataproc Metastore operation**

**SYNOPSIS**

: **`gcloud metastore operations cancel` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/cancel#OPERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/cancel#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a Dataproc Metastore operation.

**EXAMPLES**

: To cancel an active Dataproc Metastore operation with the name
`operation-1` in location `us-central1`, run:

```
gcloud metastore operations cancel operation-1 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The operation cancel. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

**--location**:
Location to which the operation belongs.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

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
gcloud alpha metastore operations cancel
```

```
gcloud beta metastore operations cancel
```