# gcloud metastore services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete)*

**NAME**

: **gcloud metastore services delete - delete one or more Dataproc Metastore services**

**SYNOPSIS**

: **`gcloud metastore services delete` (`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete#SERVICES)` [`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete#SERVICES)` …] : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If run asynchronously with `--async`, exits after printing one or
more operation names that can be used to poll the status of the deletion(s) via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To delete a Dataproc Metastore service with the name
`my-metastore-service` in location `us-central1`, run:

```
gcloud metastore services delete my-metastore-service --location=us-central1
```

To delete multiple Dataproc Metastore services with the name
`service-1` and `service-2` in the same location
`us-central1`, run:

```
gcloud metastore services delete service-1 service-2 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Service resource - The services to delete. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `services` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICES` [`SERVICES` …]**:
IDs of the services or fully qualified identifiers for the services.
To set the `service` attribute:

- provide the argument `services` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location to which the services belongs.
To set the `location` attribute:

- provide the argument `services` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

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

**NOTES**

: These variants are also available:

```
gcloud alpha metastore services delete
```

```
gcloud beta metastore services delete
```