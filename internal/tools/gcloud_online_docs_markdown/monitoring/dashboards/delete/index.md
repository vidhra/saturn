# gcloud monitoring dashboards delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/delete](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/delete)*

**NAME**

: **gcloud monitoring dashboards delete - delete a Cloud Monitoring dashboard**

**SYNOPSIS**

: **`gcloud monitoring dashboards delete` `[DASHBOARD](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/delete#DASHBOARD)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Monitoring dashboard.

**EXAMPLES**

: To delete a dashboard, run:

```
gcloud monitoring dashboards delete MY-DASHBOARD
```

To delete a dashboard contained within a specific project, run:

```
gcloud monitoring dashboards delete MY-DASHBOARD --project=MY-PROJECT
```

To delete a dashboard with a fully qualified dashboard ID, run:

```
gcloud monitoring dashboards delete projects/MY-PROJECT/dashboards/MY-DASHBOARD
```

**POSITIONAL ARGUMENTS**

: **Dashboard resource - The dashboard to delete. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `dashboard` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DASHBOARD`**:
ID of the dashboard or fully qualified identifier for the dashboard.
To set the `dashboard` attribute:

- provide the argument `dashboard` on the command line.**

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

: This command uses the `monitoring/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/monitoring/api/](https://cloud.google.com/monitoring/api/)

**NOTES**

: These variants are also available:

```
gcloud alpha monitoring dashboards delete
```

```
gcloud beta monitoring dashboards delete
```