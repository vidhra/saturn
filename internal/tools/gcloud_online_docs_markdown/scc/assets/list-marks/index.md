# gcloud scc assets list-marks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks)*

**NAME**

: **gcloud scc assets list-marks - list an assets's security marks**

**SYNOPSIS**

: **`gcloud scc assets list-marks` (`[ASSET](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#ASSET)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--organization)`=`ORGANIZATION`) [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--read-time)`=`READ_TIME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list-marks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
List an assets's security marks.

**EXAMPLES**

: List all security marks for asset (8910) under organization (123456):

```
gcloud scc assets list-marks 8910 --organization=123456
```

List all security marks for asset (8910) under project (example-project):

```
gcloud scc assets list-marks projects/example-project/assets/8910 --organization=123456
```

List all security marks for asset (8910) under folder (456):

```
gcloud scc assets list-marks folders/456/assets/8910 --organization=123456
```

**POSITIONAL ARGUMENTS**

: **Asset resource - The asset to be used for the SCC (Security Command Center)
command. The arguments in this group can be used to specify the attributes of
this resource.
This must be specified.

**`ASSET`**:
ID of the asset or fully qualified identifier for the asset.
To set the `asset` attribute:

- provide the argument `asset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
(Optional) If the full resource name isn't provided e.g. organizations/123, then
provide the organization id which is the suffix of the organization. Example:
organizations/123, the id is 123.
To set the `organization` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line;
- Set the organization property in configuration using `gcloud config set
scc/organization` if it is not specified in command line..**

**FLAGS**

: **--page-token**:
Response objects will return a non-null value for page-token to indicate that
there is at least one additional page of data. User can either directly request
that page by specifying the page-token explicitly or let gcloud fetch
one-page-at-a-time.

**--read-time**:
Time used as a reference point when filtering. Absence of this field will
default to the API's version of NOW. See `$ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on supported time formats.

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

: This command uses the `securitycenter/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: These variants are also available:

```
gcloud alpha scc assets list-marks
```

```
gcloud beta scc assets list-marks
```