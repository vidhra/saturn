# gcloud metastore services alter-metadata-resource-location  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location)*

**NAME**

: **gcloud metastore services alter-metadata-resource-location - alter metadata resource location**

**SYNOPSIS**

: **`gcloud metastore services alter-metadata-resource-location` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location#--location)`=`LOCATION`) `--location_uri`=`LOCATION_URI` `--resource_name`=`RESOURCE_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Alter metadata resource location from a Dataproc Metastore service's underlying
metadata store.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the creation via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To alter metadata resource location with the resource_name
`databases/{database_id}` or
`databases/{database_id}/tables/{table_id}` or and location_uri in
location `us-central`, run:

```
gcloud metastore services alter-metadata-resource-location my-metastore-service --location=us-central1 --resource_name=databases/my-db --location_uri=gs://destination_bucket/destination_object
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the resource and the
location you want to alter. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

**REQUIRED FLAGS**

: **--location_uri**:
The new location URI for the metadata resource.

**--resource_name**:
The relative metadata resource name in the following format.
`databases/{database_id}` or
`databases/{database_id}/tables/{table_id}` or
`databases/{database_id}/tables/{table_id}/partitions/{partition_id}`

**OPTIONAL FLAGS**

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

**API REFERENCE**

: This command uses the `metastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataproc-metastore/docs](https://cloud.google.com/dataproc-metastore/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha metastore services alter-metadata-resource-location
```

```
gcloud beta metastore services alter-metadata-resource-location
```