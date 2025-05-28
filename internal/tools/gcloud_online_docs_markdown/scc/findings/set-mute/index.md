# gcloud scc findings set-mute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute)*

**NAME**

: **gcloud scc findings set-mute - update a Security Command Center finding's mute state**

**SYNOPSIS**

: **`gcloud scc findings set-mute` `[FINDING](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#FINDING)` `[--mute](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--mute)`=`MUTE` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--location)`=`LOCATION`; default="global"] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--source)`=`SOURCE`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Security Command Center finding's mute state.

**EXAMPLES**

: To update finding's mute state to ``MUTED``,
given finding `organizations/123/sources/456/findings/789`, run:

```
gcloud scc findings set-mute 789 --organization=organizations/123 --source=456 --mute=MUTED
```

To update finding's mute state to ``UNMUTED``,
given finding `organizations/123/sources/456/findings/789`, run:

```
gcloud scc findings set-mute 789 --organization=organizations/123 --source=456 --mute=UNMUTED
```

To update finding's mute state to ``MUTED``,
given finding `folders/123/sources/456/findings/789`, run:

```
gcloud scc findings set-mute 789 --folder=folders/123 --source=456 --mute=MUTED
```

To update finding's mute state to ``MUTED``,
given finding `projects/123/sources/456/findings/789`, run:

```
gcloud scc findings set-mute 789 --project=projects/123 --source=456 --mute=MUTED
```

To update finding's mute state to ``MUTED``,
given finding `organizations/123/sources/456/findings/789` and
`location=eu`, run:

```
gcloud scc findings set-mute 789 --organization=organizations/123 --source=456 --mute=MUTED --location=locations/eu
```

**POSITIONAL ARGUMENTS**

: **`FINDING`**:
ID of the finding or the full resource name of the finding.

**REQUIRED FLAGS**

: **--mute**:
Desired mute state of the finding. `MUTE` must be one of:
`muted`, `unmuted`, `undefined`.

**OPTIONAL FLAGS**

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

**--source**:
ID of the source.

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

: This variant is also available:

```
gcloud alpha scc findings set-mute
```