# gcloud composer operations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete](https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete)*

**NAME**

: **gcloud composer operations delete - delete one or more completed Cloud Composer operations**

**SYNOPSIS**

: **`gcloud composer operations delete` (`[OPERATIONS](https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete#OPERATIONS)` [`[OPERATIONS](https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete#OPERATIONS)` …] : `[--location](https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/operations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete operations that are done. If more than one operation is specified, all
deletes will be attempted. If any of the deletes fail, those operations and
their failure messages will be listed on the standard error, and the command
will exit with a non-zero status.

**EXAMPLES**

: To delete the operation ``operation-1``, run:

```
gcloud composer operations delete operation-1
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
Compute Engine region in which to create the operations.
To set the `location` attribute:

- provide the argument `operations` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

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
gcloud alpha composer operations delete
```

```
gcloud beta composer operations delete
```