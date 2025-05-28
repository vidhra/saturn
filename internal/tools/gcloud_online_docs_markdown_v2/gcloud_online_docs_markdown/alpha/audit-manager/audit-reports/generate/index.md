# gcloud alpha audit-manager audit-reports generate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate)*

**NAME**

: **gcloud alpha audit-manager audit-reports generate - generate Audit Report**

**SYNOPSIS**

: **`gcloud alpha audit-manager audit-reports generate` `[--compliance-framework](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--compliance-framework)`=`COMPLIANCE_FRAMEWORK` `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--gcs-uri)`=`GCS_URI` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--location)`=`LOCATION` `[--report-format](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--report-format)`=`REPORT_FORMAT` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--folder)`=`FOLDER`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#--project)`=`PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Generate a new Audit Report.

**EXAMPLES**

: To generate an Audit Report in the `us-central1` region, for a
project with ID `123` for compliance framework
`fedramp_moderate` in `odf` format and store it in
`gs://testbucketauditmanager` bucket, run:

```
gcloud alpha audit-manager audit-reports generate --project=123 --location=us-central1 --compliance-framework=fedramp_moderate --report-format=odf --gcs-uri=gs://testbucketauditmanager
```

**REQUIRED FLAGS**

: **--compliance-framework**:
Compliance Framework against which the Report must be generated. Eg:
FEDRAMP_MODERATE

**--gcs-uri**:
Destination Cloud storage bucket where report and evidence must be uploaded. The
Cloud storage bucket provided here must be selected among the buckets entered
during the enrollment process.

**--location**:
The location where the report should be generated.

**--report-format**:
The format in which the audit report should be created.
`REPORT_FORMAT` must be (only one value is supported):
`odf`.

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud audit-manager audit-reports generate
```