# gcloud scc sources describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe](https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe)*

**NAME**

: **gcloud scc sources describe - describe a source given its display name or source id**

**SYNOPSIS**

: **`gcloud scc sources describe` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe#PARENT)`] (`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe#--source)`=`SOURCE`     | `[--source-display-name](https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe#--source-display-name)`=`SOURCE_DISPLAY_NAME`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/sources/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a source given its display name or source id.

**EXAMPLES**

: Describe source with display name `Security Scanner`:

```
gcloud scc sources describe 123456 --source-display-name="Security Scanner"
```

Describe source with source id '5678':

```
gcloud scc sources describe 123456 --source=5678
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

**REQUIRED FLAGS**

: **--source**

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

: This command uses the `securitycenter/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: These variants are also available:

```
gcloud alpha scc sources describe
```

```
gcloud beta scc sources describe
```