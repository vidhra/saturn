# gcloud storage insights inventory-reports delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete)*

**NAME**

: **gcloud storage insights inventory-reports delete - delete an inventory report config**

**SYNOPSIS**

: **`gcloud storage insights inventory-reports delete` (`[REPORT_CONFIG](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete#REPORT_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete#--location)`=`LOCATION`) [`[--force](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an inventory report config.

**EXAMPLES**

: To delete an inventory report config with ID=1234, location=us-central1 and
project=foo:

```
gcloud storage insights inventory-reports delete 1234 --location=us-central1 --project=foo
```

To delete the same inventory report config with fully specified name:

```
gcloud storage insights inventory-reports delete /projects/foo/locations/us-central1/reportConfigs/1234
```

To delete the report config with all generated report details:

```
gcloud storage insights inventory-reports delete /projects/foo/locations/us-central1/reportConfigs/1234 --force
```

**POSITIONAL ARGUMENTS**

: **Report config resource - The Report config to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `report_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPORT_CONFIG`**:
ID of the report-config or fully qualified identifier for the report-config.
To set the `report-config` attribute:

- provide the argument `report_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the report-config.
To set the `location` attribute:

- provide the argument `report_config` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--force**:
If set, all report details for this report config will be deleted.

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

: This variant is also available:

```
gcloud alpha storage insights inventory-reports delete
```