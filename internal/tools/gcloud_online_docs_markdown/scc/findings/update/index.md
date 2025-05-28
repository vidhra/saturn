# gcloud scc findings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/update](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update)*

**NAME**

: **gcloud scc findings update - update a Security Command Center finding**

**SYNOPSIS**

: **`gcloud scc findings update` `[FINDING](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#FINDING)` [`[--event-time](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--event-time)`=`EVENT_TIME`] [`[--external-uri](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--external-uri)`=`EXTERNAL_URI`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--location)`=`LOCATION`; default="global"] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--source)`=`SOURCE`; default="-"] [`[--source-properties](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--source-properties)`=[`KEY`=`VALUE`,…]] [`[--state](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--state)`=`STATE`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--update-mask)`=`UPDATE_MASK`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Security Command Center finding.

**EXAMPLES**

: Update testFinding's state from `ACTIVE` to `INACTIVE`:

```
gcloud scc findings update `testFinding` --organization=123456 --source=5678 --state=INACTIVE
```

Update testFinding's state from `ACTIVE` to `INACTIVE`
using project name for example-project:

```
gcloud scc findings update projects/example-project/sources/5678/findings/testFinding --state=INACTIVE
```

Update testFinding's state from `ACTIVE` to `INACTIVE`
using folder name `456`:

```
gcloud scc findings update folders/456/sources/5678/findings/testFinding --state=INACTIVE
```

Override all source properties on `testFinding`:

```
gcloud scc findings update `testFinding` --organization=123456 --source=5678 --source-properties="propKey1=propVal1,propKey2=propVal2"
```

Selectively update a specific source property on `testFinding`:

```
gcloud scc findings update `testFinding` --organization=123456 --source=5678 --source-properties="propKey1=propVal1,propKey2=propVal2" --update-mask="source_properties.propKey1"
```

Update finding `testFinding` with `location=eu`, state
from `ACTIVE` to `INACTIVE`:

```
gcloud scc findings update `testFinding` --organization=123456 --source=5678 --state=INACTIVE --location=eu
```

**POSITIONAL ARGUMENTS**

: **`FINDING`**:
ID of the finding or fully qualified identifier for the finding.

**FLAGS**

: **--event-time**:
Time at which the event took place. For example, if the finding represents an
open firewall it would capture the time the open firewall was detected. If
event-time is not provided, it will default to UTC version of NOW. See `$
[gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats.

**--external-uri**:
URI that, if available, points to a web page outside of Cloud SCC (Security
Command Center) where additional information about the finding can be found.
This field is guaranteed to be either empty or a well formed URL.

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

**--source**:
Source id. Defaults to all sources.

**--source-properties**:
Source specific properties. These properties are managed by the source that
writes the finding. The key names in the source_properties map must be between 1
and 255 characters, and must start with a letter and contain alphanumeric
characters or underscores only. For example "key1=val1,key2=val2"

**--state**:
State is one of: [ACTIVE, INACTIVE]. `STATE` must be one
of: `active`, `inactive`, `state-unspecified`.

**--update-mask**:
Optional: If left unspecified (default), an update-mask is automatically created
using the flags specified in the command and only those values are updated. For
example: --external-uri='<some-uri>' --event-time='<some-time>'
would automatically generate --update-mask='external_uri,event_time'. Note that
as a result, only external-uri and event-time are updated for the given finding
and everything else remains untouched. If you want to delete
attributes/properties (that are not being changed in the update command) use an
empty update-mask (''). That will delete all the mutable properties/attributes
that aren't specified as flags in the update command. In the above example it
would delete source-properties. State can be toggled from ACTIVE to INACTIVE and
vice-versa but it cannot be deleted.

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

**NOTES**

: These variants are also available:

```
gcloud alpha scc findings update
```

```
gcloud beta scc findings update
```