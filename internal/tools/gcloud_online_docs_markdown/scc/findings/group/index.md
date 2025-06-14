# gcloud scc findings group  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/group](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group)*

**NAME**

: **gcloud scc findings group - filter an organization or source's findings and groups them by their specified properties**

**SYNOPSIS**

: **`gcloud scc findings group` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#PARENT)`] [`[--compare-duration](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--compare-duration)`=`COMPARE_DURATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--filter)`=`FILTER`] [`[--group-by](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--group-by)`=`GROUP_BY`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--location)`=`LOCATION`; default="global"] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--page-token)`=`PAGE_TOKEN`] [`[--read-time](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--read-time)`=`READ_TIME`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#--source)`=`SOURCE`; default="-"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/group#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To group across all sources provide a '-' as the source id.

**EXAMPLES**

: Group findings under organization `123456` across all sources by
their category:

```
gcloud scc findings group 123456 --group-by="category"
```

Group findings under project `example-project` across all sources by
their category:

```
gcloud scc findings group projects/example-project --group-by="category"
```

Group findings under folders `456` across all sources by their
category:

```
gcloud scc findings group folders/456 --group-by="category"
```

Group findings under organization `123456` and source
`5678`, by their category:

```
gcloud scc findings group 123456 --source=5678 --group-by="category"
```

Group ACTIVE findings under organization `123456` and source
`5678`, by their category:

```
gcloud scc findings group 123456 --source=5678 --group-by="category" --filter="state=\"ACTIVE\""
```

Group findings under organization `123456` and
`location=eu` across all sources by their category:

```
gcloud scc findings group 123456 --group-by="category" --location=eu
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

**--filter**:
Expression that defines the filter to apply across findings. The expression is a
list of one or more restrictions combined via logical operators 'AND' and 'OR'.
Parentheses are supported, and 'OR' has higher precedence than 'AND'.
Restrictions have the form '<field> <operator> <value>' and
may have a '-' character in front of them to indicate negation. Examples
include: name, source_properties.a_property, security_marks.marks.marka. The
supported operators are:

- '=' for all value types.
- '>', '<', '>=', '<=' for integer values.
- ':', meaning substring matching, for strings.

The supported value types are:string literals in quotes, integer literals
without quotes, boolean literals 'true' and 'false' without quotes. Some example
filters: 'source_properties.size = 100', 'category=\"XSS\" AND event_time >
10' etc.

**--group-by**:
Expression that defines what findings fields to use for grouping (including
'state'). String value should follow SQL syntax: comma separated list of fields.
For example: "parent,resource_name". The following fields are supported:

- resource_name
- category
- state
- parent

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

**--page-size**:
Maximum number of results to return in a single response. Default is 10, minimum
is 1, maximum is 1000.

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
gcloud alpha scc findings group
```

```
gcloud beta scc findings group
```