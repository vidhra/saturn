# gcloud scc assets get-parent  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent](https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent)*

**NAME**

: **gcloud scc assets get-parent - get the Parent for an asset given its resource name or asset id**

**SYNOPSIS**

: **`gcloud scc assets get-parent` [`[ORGANIZATION](https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent#ORGANIZATION)`] (`[--asset](https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent#--asset)`=`ASSET`     | `[--resource-name](https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent#--resource-name)`=`RESOURCE_NAME`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/get-parent#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
Get the Parent for an asset given its resource name or asset id.

**EXAMPLES**

: Get parent's relative resource name given an asset's full resource name
(https://cloud.google.com/apis/design/resource_names#full_resource_name) e.g.
//storage.googleapis.com/my-bucket under organization 123456:

```
gcloud scc assets get-parent 123456 --resource-name="//storage.googleapis.com/my-bucket"
```

Get parent's relative resource name given an asset's Cloud SCC id 5678 under
organization 123456.

```
gcloud scc assets get-parent 123456 --asset=5678
```

**POSITIONAL ARGUMENTS**

: **Organization resource - The organization to be used for the SCC (Security
Command Center) command. This represents a Cloud resource.

**[`ORGANIZATION`]**:
ID of the organization or fully qualified identifier for the organization.
To set the `organization` attribute:

- provide the argument `organization` on the command line;
- Set the organization property in configuration using `gcloud config set
scc/organization` if it is not specified in command line..**

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
gcloud alpha scc assets get-parent
```

```
gcloud beta scc assets get-parent
```