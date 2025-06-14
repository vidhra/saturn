# gcloud scc findings list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/list](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list)*

**NAME**

: **gcloud scc findings list - list an organization or source's findings**

**SYNOPSIS**

: **`gcloud scc findings list` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#PARENT)`] [`[--compare-duration](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--compare-duration)`=`COMPARE_DURATION`] [`[--field-mask](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--field-mask)`=`FIELD_MASK`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--location)`=`LOCATION`; default="global"] [`[--order-by](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--order-by)`=`ORDER_BY`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--read-time)`=`READ_TIME`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--source)`=`SOURCE`; default="-"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--project)`=`PROJECT`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List an organization or source's findings. To list across all sources provide a
'-' as the source id.

**EXAMPLES**

: List all ACTIVE findings under organization `123456` across all
sources:

```
gcloud scc findings list 123456 --filter="state=\"ACTIVE\""
```

List all ACTIVE findings under project `abc` across all sources:

```
gcloud scc findings list projects/abc --filter="state=\"ACTIVE\""
```

List all ACTIVE findings under folder `456` across all sources:

```
gcloud scc findings list folders/456 --filter="state=\"ACTIVE\""
```

List all ACTIVE findings under organization `123456` and source
`5678`:

```
gcloud scc findings list 123456 --source=5678 --filter="state=\"ACTIVE\""
```

Only list category and resource_name of all ACTIVE findings under organization
`123456` and source `5678`:

```
gcloud scc findings list 123456 --source=5678 --filter="state=\"ACTIVE\"" --field-mask="finding.category,finding.resource_name"
```

List all ACTIVE findings of XSS category/type, under organization
`123456` and source `5678`:

```
gcloud scc findings list 123456 --source=5678 --filter="state=\"ACTIVE\" AND category=\"XSS\""
```

List all findings attached to a particular resource under organization
`123456`:

```
gcloud scc findings list 123456 --filter="resource_name=\"//container.googleapis.com/projects/pid/zones/zone-id/clusters/cluster-id\""
```

List all ACTIVE findings that took place on `2019-01-01T01:00:00 GMT`
time, under organization `123456`:

```
gcloud scc findings list 123456 --filter="state=\"ACTIVE\" AND event_time > 1546304400000""
```

List all findings under organization `123456` across all sources and
`location=eu`:

```
gcloud scc findings list 123456 --location=eu
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
(DEPRECATED) When compare_duration is set, the result's "state_change" attribute
is updated to indicate whether the finding had its state changed, the finding's
state remained unchanged, or if the finding was added during the
compare_duration period of time that precedes the read_time. This is the time
between (read_time - compare_duration) and read_time. The state_change value is
derived based on the presence and state of the finding at the two points in
time. Intermediate state changes between the two times don't affect the result.
For example, the results aren't affected if the finding is made inactive and
then active again. Possible "state_change" values when compare_duration is
specified:

- 'CHANGED': indicates that the finding was present at the start of
compare_duration, but changed its state at read_time.

- 'UNCHANGED': indicates that the finding was present at the start of
compare_duration and did not change state at read_time.

- 'ADDED': indicates that the finding was not present at the start of
compare_duration, but was present at read_time.

- 'REMOVED': indicates that the finding was present at the start of
compare_duration, but was not present at read_time.

```
If compare_duration is not specified, then the only possible
state_change is 'UNUSED', which will be the state_change set for all
findings present at read_time. If this field is set then 'state_change'
must be a specified field in 'group_by'. See $ gcloud topic datetimes
for information on supported duration formats.
```

The --compare-duration option is deprecated. For more information, [see
the deprecation notice](https://cloud.google.com/security-command-center/docs/release-notes#April_15_2024) on the SCC release notes page.

**--field-mask**:
Field mask to specify the finding fields listed in the response. An empty field
mask will list all fields. For example:
--field-mask="finding.category,finding.resource_name" will only output category
and resource_name for the findings in addition to default attributes. Notice the
difference between hyphens (-) used with flags v/s camel case used in field
masks. An empty or missing field mask will list all fields.

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

**--order-by**:
Expression that defines what fields and order to use for sorting. String value
should follow SQL syntax: comma separated list of fields. For example:
"name,resource_properties.a_property". The default sorting order is ascending.
To specify descending order for a field, a suffix " desc" should be appended to
the field name. For example: --order-by="name desc,source_properties.a_property"
will order by name in descending order while source_properties.a_property in
ascending order.

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
gcloud alpha scc findings list
```

```
gcloud beta scc findings list
```