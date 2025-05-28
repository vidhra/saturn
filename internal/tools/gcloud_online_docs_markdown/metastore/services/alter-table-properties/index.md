# gcloud metastore services alter-table-properties  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties)*

**NAME**

: **gcloud metastore services alter-table-properties - alter metadata table properties**

**SYNOPSIS**

: **`gcloud metastore services alter-table-properties` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#--location)`=`LOCATION`) `[--properties](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#--properties)`=[`KEY`=`VALUE`,…] `[--table-name](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#--table-name)`=`TABLE_NAME` `[--update-mask](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#--update-mask)`=`UPDATE_MASK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Alter metadata table properties from a Dataproc Metastore service's underlying
metadata store.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the creation via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To alter metadata table properties a and b on table-name
`databases/{database_id}/tables/{table_id}` , use the update-mask
`properties.a,properties.b` , and run:

```
gcloud metastore services alter-table-properties my-metastore-service --location=us-central1 --table-name=databases/my-database/tables/my-table --update-mask=properties.a,properties.b --properties=a=1,b=2
```

**POSITIONAL ARGUMENTS**

: **Service resource - Arguments and flags that specify the table you want to alter.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

: **--properties**:
A string where field names are separated by a comma. Describes the desired
values to mutate. If update-mask is empty, the properties will not update.
Otherwise, the properties only alter the values whose associated paths exist in
the update mask.
For example, the desired key-value pairs.
a=2,b=3,c=4

**--table-name**:
The name of the table containing the properties you're altering in the following
format.
`databases/{database_id}/tables/{table_id}`

**--update-mask**:
A string where field names are separated by a comma. Specifies the metadata
table properties fields that are overwritten by the update. Fields specified in
the `update-mask` are relative to the resource (not to the full
request). A field is overwritten if it is in the mask.
For example, given the target properties:

```
properties {
  a: 1
  b: 2
}
```

And an update properties:

```
properties {
  a: 2
  b: 3
  c: 4
}
```

then if the field mask is:
`properties.b,properties.c`
then the updated result will be:

```
properties {
  a: 1
  b: 3
  c: 4
}
```

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
gcloud alpha metastore services alter-table-properties
```

```
gcloud beta metastore services alter-table-properties
```