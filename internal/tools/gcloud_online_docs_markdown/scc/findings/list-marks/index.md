# gcloud scc findings list-marks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks)*

**NAME**

: **gcloud scc findings list-marks - list a finding's security marks**

**SYNOPSIS**

: **`gcloud scc findings list-marks` `[FINDING](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#FINDING)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--location)`=`LOCATION`; default="global"] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--read-time)`=`READ_TIME`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--source)`=`SOURCE`; default="-"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--project)`=`PROJECT`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List a finding's security marks.

**EXAMPLES**

: List all security marks for `testFinding` under organization
`123456` and source `5678`:

```
gcloud scc findings list-marks `testFinding` --organization=123456 --source=5678
```

List all security marks for `testFinding` under project
`example-project` and source `5678`:

```
gcloud scc findings list-marks projects/example-project/sources/5678/findings/testFinding
```

List all security marks for `testFinding` under folder
`456` and source `5678`:

```
gcloud scc findings list-marks folders/456/sources/5678/findings/testFinding
```

List all security marks for `testFinding` under organization
`123456`, source `5678` and `location=eu`:

```
gcloud scc findings list-marks `testFinding` --organization=123456 --source=5678 --location=eu
```

**POSITIONAL ARGUMENTS**

: **`FINDING`**:
ID of the finding or fully qualified identifier for the finding.

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

**--page-token**:
Response objects will return a non-null value for page-token to indicate that
there is at least one additional page of data. User can either directly request
that page by specifying the page-token explicitly or let gcloud fetch
one-page-at-a-time.

**--read-time**:
(DEPRECATED) Time used as a reference point when filtering. Absence of this
field will default to the API's version of NOW. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on supported time formats.
The --read-time option is deprecated. For more information, [see
the deprecation notice](https://cloud.google.com/security-command-center/docs/release-notes#April_15_2024) on the SCC release notes page.

**--source**:
Source id. Defaults to all sources.

**--folder**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

**NOTES**

: These variants are also available:

```
gcloud alpha scc findings list-marks
```

```
gcloud beta scc findings list-marks
```