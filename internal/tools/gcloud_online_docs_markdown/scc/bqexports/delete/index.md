# gcloud scc bqexports delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete)*

**NAME**

: **gcloud scc bqexports delete - delete a Security Command Center BigQuery export**

**SYNOPSIS**

: **`gcloud scc bqexports delete` `[BIG_QUERY_EXPORT](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#BIG_QUERY_EXPORT)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Security Command Center BigQuery export.
BigQuery exports that are created with Security Command Center API V2 and later
include a `location` attribute. If the `location`
attribute is included in the resource name of a BigQuery export, you must
specify it when referencing the export. For example, the following BigQuery
export name has `location=eu`:
`organizations/123/locations/eu/bigQueryExports/test-bq-export`.

**EXAMPLES**

: To delete a BigQuery export given organization `123` with id
`test-bq-export`, run:

```
gcloud scc bqexports delete test-bq-export --organization=123
```

To delete a BigQuery export given folder `456` with `id
test-bq-export`, run:

```
gcloud scc bqexports delete test-bq-export --folder=456
```

To delete a BigQuery export given project `789` with id
`test-bq-export`, run:

```
gcloud scc bqexports delete test-bq-export --project=789
```

To delete the BigQuery export `test-bq-export`, with
`location=global`, from organization `123`, run:

```
gcloud scc bqexports delete test-bq-export --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **`BIG_QUERY_EXPORT`**:
ID of the BigQuery export e.g. `my-bq-export` or the full resource
name of the BigQuery export e.g.
`organizations/123/bigQueryExports/my-bq-export`.

**FLAGS**

: **--location**:
When data residency controls are enabled, this attribute specifies the location
in which the resource is located and applicable. The `location`
attribute can be provided as part of the fully specified resource name or with
the `--location` argument on the command line. The default location
is `global`. NOTE: If you override the endpoint to a [regional
endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data
location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated
to the default location that is specified when data residency controls are
enabled for Security Command Center.

**--folder**

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

: This command uses the Security Command Center API. For more information, see [Security
Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)