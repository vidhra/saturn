# gcloud metastore services query-metadata  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata)*

**NAME**

: **gcloud metastore services query-metadata - execute a SQL query against a Dataproc Metastore Service's metadata**

**SYNOPSIS**

: **`gcloud metastore services query-metadata` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata#--location)`=`LOCATION`) `[--query](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata#--query)`=`QUERY` [`[--format](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata#--format)`=`FORMAT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Execute a SQL query against a Dataproc Metastore Service's metadata.

**EXAMPLES**

: To query metadata against a Dataproc Metastore service with the name
`my-metastore-service` in location `us-central1`, and the
sql query "show tables;", run:

```
gcloud metastore services query-metadata my-metastore-service --location=us-central1 --query="show tables;"
```

**POSITIONAL ARGUMENTS**

: **Service resource - The service to query metadata. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
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
Location to which the service belongs.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

**REQUIRED FLAGS**

: **--query**:
Use Google Standard SQL query for Cloud Spanner and MySQL query syntax for Cloud
SQL. Cloud Spanner SQL is described at
https://cloud.google.com/spanner/docs/query-syntax)"

**COMMONLY USED FLAGS**

: **--format**:
Sets the format for printing command output resources. The default is a
command-specific human-friendly output format. If both `core/format`
and `--format` are specified, `--format` takes precedence.
`--format` and `core/format` both take precedence over
`core/default_format`. The supported formats are limited to:
`config`, `csv`, `default`, `diff`,
`disable`, `flattened`, `get`,
`json`, `list`, `multi`, `none`,
`object`, `table`, `text`, `value`,
`yaml`. For more details run $ [gcloud](https://cloud.google.com/sdk/gcloud/reference) topic formats. Run `$ [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set) --help` to
see more information about `core/format`

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
gcloud alpha metastore services query-metadata
```

```
gcloud beta metastore services query-metadata
```