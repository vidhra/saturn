# gcloud scc assets list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/list](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list)*

**NAME**

: **gcloud scc assets list - list Cloud Security Command Center assets**

**SYNOPSIS**

: **`gcloud scc assets list` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#PARENT)`] [`[--compare-duration](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--compare-duration)`=`COMPARE_DURATION`] [`[--field-mask](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--field-mask)`=`FIELD_MASK`] [`[--order-by](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--order-by)`=`ORDER_BY`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--read-time)`=`READ_TIME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
List Cloud Security Command Center assets.

**EXAMPLES**

: List all assets under organization (123456)

```
gcloud scc assets list 123456
```

List all assets under project (example-project)

```
gcloud scc assets list projects/example-project
```

List all assets under folder (456)

```
gcloud scc assets list folders/456
```

List all assets under organization (123456) that were present as of
2019-01-01T01:00:00 GMT time.

```
gcloud scc assets list 123456 --read-time="2019-01-01T01:00:00Z"
```

Only list category and resource_name for all assets under organization (123456):

```
gcloud scc assets list 123456 --field-mask="category,resource_name"
```

List all compute instances under organization (123456):

```
gcloud scc assets list 123456 --filter="security_center_properties.resource_type=\"google.compute.Instance\""
```

List all firewall rules that have open HTTP Ports:

```
gcloud scc assets list 123456 --filter="security_center_properties.resource_type = \"google.compute.Firewall\" AND resource_properties.name =\"default-allow-http\""
```

List all assets that belong to either projects: 5678 OR 78910 (project's numeric
identifier).

```
gcloud scc assets list 123456 --filter="security_center_properties.resource_parent = \"//cloudresourcemanager.googleapis.com/projects/5678\" OR security_center_properties.resource_parent = "\78910\""
```

List all projects that are owned by a user:someone@domain.com. Notice the usage
of : which enforces partial matching.

```
gcloud scc assets list 123456 --filter="security_center_properties.resource_type = \"google.cloud.resourcemanager.Project\" AND security_center_properties.resource_owners : \"user:someone@domain.com\""
```

List assets and add a state_change property that indicates if the asset was
added, removed, or remained present during the past 24 hours period:

```
gcloud scc assets list 123456 --compare-duration=86400s
```

**POSITIONAL ARGUMENTS**

: **Parent resource - parent organization, folder, or project in the Google Cloud
resource hierarchy to be used for the `[gcloud scc](https://cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the
argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the
preceding examples. This represents a Cloud resource.

**[`PARENT`]**:
ID of the parent or fully qualified identifier for the parent.
To set the `parent` attribute:

- provide the argument `parent` on the command line;
- Set the parent property in configuration using `gcloud config set
scc/parent` if it is not specified in command line.**

**FLAGS**

: **--compare-duration**:
The result's "state_change" attribute is updated to indicate whether the asset
was added, removed, or remained present during the compare_duration period of
time that precedes the read_time. See `$ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on supported duration formats.

**--field-mask**:
Field mask to specify the Asset fields to be listed in the response. An empty
field mask will list all fields. Example field mask:
"asset.security_center_properties.resource_type,asset.security_center_properties.resource_parent"

**--order-by**:
Expression that defines what fields and order to use for sorting. Example order
by: "resource_properties.sort_prop ASC"

**--page-token**:
The value returned by the last 'ListAssetsResponse'; indicates that this is a
continuation of a prior 'ListAssets' call, and that the system should return the
next page of data.

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
gcloud alpha scc assets list
```

```
gcloud beta scc assets list
```