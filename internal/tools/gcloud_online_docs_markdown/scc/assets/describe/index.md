# gcloud scc assets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe](https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe)*

**NAME**

: **gcloud scc assets describe - describe an asset given its resource name or asset id**

**SYNOPSIS**

: **`gcloud scc assets describe` [`[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe#PARENT)`] (`[--asset](https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe#--asset)`=`ASSET`     | `[--resource-name](https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe#--resource-name)`=`RESOURCE_NAME`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
Describe an asset given its resource name or asset id.

**EXAMPLES**

: Describe an asset under organization 123456, given its full resource name
(https://cloud.google.com/apis/design/resource_names#full_resource_name) e.g.
//storage.googleapis.com/my-bucket:

```
gcloud scc assets describe 123456 --resource-name="//storage.googleapis.com/my-bucket"
```

Describe an asset under organization 123456, given its Cloud SCC asset id 5678

```
gcloud scc assets describe 123456 --asset=5678
```

Describe an asset under project example-project, given its Cloud SCC asset id
5678

```
gcloud scc assets describe projects/example-project/assets/5678
```

Describe an asset under folder 456, given its Cloud SCC asset id 5678

```
gcloud scc assets describe folders/456/assets/5678
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

: **--asset**

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
gcloud alpha scc assets describe
```

```
gcloud beta scc assets describe
```