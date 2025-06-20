# gcloud metastore operations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete)*

**NAME**

: **gcloud metastore operations delete - delete one or more completed Dataproc Metastore operations**

**SYNOPSIS**

: **`gcloud metastore operations delete` (`[OPERATIONS](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete#OPERATIONS)` [`[OPERATIONS](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete#OPERATIONS)` …] : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/operations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete one or more completed Dataproc Metastore operations.

**EXAMPLES**

: To delete a Dataproc Metastore operation with the name `operation-1`
in location `us-central1`, run:

```
gcloud metastore operations delete operation-1 --location=us-central1
```

To delete multiple Dataproc Metastore services with the name
`operation-1` and `operation-2` in the same location
`us-central1`, run:

```
gcloud metastore operations delete operation-1 operation-2 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The operations to delete. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operations` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATIONS` [`OPERATIONS` …]**:
IDs of the operations or fully qualified identifiers for the operations.
To set the `operation` attribute:

- provide the argument `operations` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location to which the operations belongs.
To set the `location` attribute:

- provide the argument `operations` on the command line with a fully
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
gcloud alpha metastore operations delete
```

```
gcloud beta metastore operations delete
```