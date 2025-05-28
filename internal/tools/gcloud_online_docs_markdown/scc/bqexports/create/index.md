# gcloud scc bqexports create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create)*

**NAME**

: **gcloud scc bqexports create - create a Security Command Center BigQuery export**

**SYNOPSIS**

: **`gcloud scc bqexports create` `[BIG_QUERY_EXPORT](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#BIG_QUERY_EXPORT)` `[--dataset](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--dataset)`=`DATASET` [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--description)`=`DESCRIPTION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--filter)`=`FILTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/bqexports/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Security Command Center BigQuery export.
BigQuery exports that are created with Security Command Center API V2 and later
include a `location` attribute. If a location is not specified, the
default `global` location is used. For example, the following
BigQuery export name has `location=global` attribute:
`organizations/123/locations/global/bigQueryExports/test-bq-export`.

**EXAMPLES**

: To create a BigQuery export `test-bq-export` given organization
`123` with a dataset `abc` in project `234` and
filter on category that equals to `XSS_SCRIPTING`, run:

```
gcloud scc bqexports create test-bq-export --organization=123 --dataset=projects/234/datasets/abc --description="This is a test BigQuery export" --filter="category=\"XSS_SCRIPTING\""
```

To create a BigQuery export `test-bq-export` given folder
`456` with a dataset `abc` in project `234` and
filter on category that equals to `XSS_SCRIPTING`, run:

```
gcloud scc bqexports create test-bq-export --folder=456 --dataset=projects/234/datasets/abc --description="This is a test BigQuery export" --filter="category=\"XSS_SCRIPTING\""
```

To create a BigQuery export test-bq-export given project `789` with a
dataset `abc` in project `234` and filter on category that
equals to `XSS_SCRIPTING`, run:

```
gcloud scc bqexports create test-bq-export --project=789 --dataset=projects/234/datasets/abc --description="This is a test BigQuery export" --filter="category=\"XSS_SCRIPTING\""
```

To create a BigQuery export `test-bq-export` given organization
`123` and `location=global` to send findings with
`category=XSS_SCRIPTING` to the BigQuery dataset `abc` in
project `234`, run:

```
gcloud scc bqexports create test-bq-export --organization=123 --dataset=projects/234/datasets/abc --description="This is a test BigQuery export" --filter="category=\"XSS_SCRIPTING\"" --location=global
```

**POSITIONAL ARGUMENTS**

: **`BIG_QUERY_EXPORT`**:
ID of the BigQuery export e.g. `my-bq-export` or the full resource
name of the BigQuery export e.g.
`organizations/123/bigQueryExports/my-bq-export`.

**REQUIRED FLAGS**

: **--dataset**:
The dataset to write findings updates to.

**OPTIONAL FLAGS**

: **--description**:
The text that will be used to describe a BigQuery export.

**--filter**:
The filter string which will applied to findings muted by a BigQuery export.

**--location**:
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