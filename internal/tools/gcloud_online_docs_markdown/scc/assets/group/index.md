# gcloud scc assets group  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/group](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group)*

**NAME**

: **gcloud scc assets group - filter an organization's assets and groups them by their specified properties**

**SYNOPSIS**

: **`gcloud scc assets group` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#PARENT)`] [`[--compare-duration](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--compare-duration)`=`COMPARE_DURATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--filter)`=`FILTER`] [`[--group-by](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--group-by)`=`GROUP_BY`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#--read-time)`=`READ_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/group#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
Filter an organization's assets and groups them by their specified properties.

**EXAMPLES**

: Group assets under organization 123456 by their type (e.g. project, disk,
compute instance, service etc):

```
gcloud scc assets group 123456 --group-by="security_center_properties.resource_type"
```

Group assets under project example-project by their type (e.g. project, disk,
compute instance, service etc):

```
gcloud scc assets group projects/example-project --group-by="security_center_properties.resource_type"
```

Group assets under folder 456 by their type (e.g. project, disk, compute
instance, service etc):

```
gcloud scc assets group folders/456 --group-by="security_center_properties.resource_type"
```

Group compute instances (assets) under organization 123456 by their respective
projects:

```
gcloud scc assets group 123456 --filter="security_center_properties.resource_type=\"google.compute.Instance\"" --group-by="security_center_properties.resource_project"
```

Group assets that were updated on or after 2019-01-01T01:00:00 GMT by their
types.

```
gcloud scc assets group 123456 --filter="update_time >= 1546304400000" --group-by="security_center_properties.resource_type"
```

Group assets into following 3 state_changes (ADDED/DELETED/ACTIVE) based on the
activity during past 24 hours:

```
gcloud scc assets group 123456 --compare-duration=86400s --group-by="state_change"
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

**--filter**:
Expression is a list of one or more restrictions combined via logical operators
'AND' and 'OR'. Parentheses are not supported, and 'OR' has higher precedence
than 'AND'. For example, 'update_time > 100 AND
security_center_properties.resource_type=\"google.cloud.resourcemanager.Organization\"'
is a valid filter string.

**--group-by**:
Expression that defines what asset fields to use for grouping (including
'state'). String value should follow SQL syntax: comma separated list of fields.
For example: "parent,resource_name". The following fields are supported:

- security_center_properties.resource_project
- security_center_properties.resource_type
- security_center_properties.resource_parent
- state_change

**--page-size**:
The maximum number of results to return in a single response. Default is 10,
minimum is 1, maximum is 1000.

**--page-token**:
Value returned by the last 'GroupAssetsResponse'; indicates that this is a
continuation of a prior 'GroupAssets' call, and that the system should return
the next page of data.

**--read-time**:
Time used as a reference point when filtering. Absence of this field will
default to the API's version of NOW. See `$ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on supported time formats.

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
gcloud alpha scc assets group
```

```
gcloud beta scc assets group
```