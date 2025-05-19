# gcloud alpha audit-manager audit-scopes generate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate)*

**NAME**

: **gcloud alpha audit-manager audit-scopes generate - generate Audit Scope**

**SYNOPSIS**

: **`gcloud alpha audit-manager audit-scopes generate` `[--compliance-framework](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--compliance-framework)`=`COMPLIANCE_FRAMEWORK` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--location)`=`LOCATION` `[--output-file-name](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--output-file-name)`=`OUTPUT_FILE_NAME` `[--report-format](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--report-format)`=`REPORT_FORMAT` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--folder)`=`FOLDER`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--project)`=`PROJECT`) [`[--output-directory](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#--output-directory)`=`OUTPUT_DIRECTORY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-scopes/generate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Generate a new Audit Scope.

**EXAMPLES**

: To generate an Audit Scope in the `us-central1` region, for a project
with ID `123` for compliance framework `fedramp_moderate`
in `odf` format, run:

```
gcloud alpha audit-manager audit-scopes generate --project="123" --location="us-central1" --compliance-framework="fedramp_moderate" --report-format="odf" --output-directory="scopes/currentyear" --output-file-name="auditreport"
```

**REQUIRED FLAGS**

: **--compliance-framework**:
Compliance Framework against which the Report must be generated. Eg:
FEDRAMP_MODERATE

**--location**:
The location where the scope should be generated.

**--output-file-name**:
The name by while scope report should be created .

**--report-format**:
The format in which the audit scope report should be created.
`REPORT_FORMAT` must be (only one value is supported):
`odf`.

**--folder**

**OPTIONAL FLAGS**

: **--output-directory**:
The directory path where the scope report should be created .

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud audit-manager audit-scopes generate
```