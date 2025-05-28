# gcloud scc assets run-discovery  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/run-discovery](https://cloud.google.com/sdk/gcloud/reference/scc/assets/run-discovery)*

**NAME**

: **gcloud scc assets run-discovery - scan an organization for new/modified/deleted assets**

**SYNOPSIS**

: **`gcloud scc assets run-discovery` [`[ORGANIZATION](https://cloud.google.com/sdk/gcloud/reference/scc/assets/run-discovery#ORGANIZATION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/run-discovery#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Security Command Center Asset APIs are deprecated and
will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset).
For more information, [see
the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).
Scan an organization for new/modified/deleted assets. Note that this API can
only be called with limited frequency for an organization. If it is called too
frequently the caller will receive a TOO_MANY_REQUESTS error.

**EXAMPLES**

: Run new scan for organization (123456):

```
gcloud scc assets run-discovery 123456
```

**POSITIONAL ARGUMENTS**

: **Organization resource - The organization for which scan should be run. This
represents a Cloud resource.

**[`ORGANIZATION`]**:
ID of the organization or fully qualified identifier for the organization.
To set the `organization` attribute:

- provide the argument `organization` on the command line;
- Set the organization property in configuration using `gcloud config set
scc/organization` if it is not specified in command line..**

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
gcloud alpha scc assets run-discovery
```

```
gcloud beta scc assets run-discovery
```