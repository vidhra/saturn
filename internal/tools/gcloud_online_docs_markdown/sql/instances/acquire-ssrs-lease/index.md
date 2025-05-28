# gcloud sql instances acquire-ssrs-lease  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease)*

**NAME**

: **gcloud sql instances acquire-ssrs-lease - acquires a SQL Server Reporting Services lease on a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances acquire-ssrs-lease` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#INSTANCE)` `[--report-database](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#--report-database)`=`REPORT_DATABASE` `[--service-login](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#--service-login)`=`SERVICE_LOGIN` `[--setup-login](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#--setup-login)`=`SETUP_LOGIN` [`[--duration](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#--duration)`=`DURATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Acquire a SQL Server Reporting Services lease on a Cloud SQL instance.

**EXAMPLES**

: To acquire a SQL Server Reporting Services lease on an instance:

```
gcloud sql instances acquire-ssrs-lease instance-foo --setup-login=setuplogin --service-login=reportuser --report-database=ReportServer --duration=4h
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**REQUIRED FLAGS**

: **--report-database**:
Existing or new report database name in the Cloud SQL for SQL Server instance
that is used for SSRS setup.

**--service-login**:
Existing login in the Cloud SQL for SQL Server instance that is used as the
service login for SSRS setup.

**--setup-login**:
Existing login in the Cloud SQL for SQL Server instance that is used as the
setup login for SSRS setup.

**OPTIONAL FLAGS**

: **--duration**:
Time duration, in hours, that the lease will be active to allow SSRS setup.
Default lease duration is 5 hours if this flag is not specified.

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