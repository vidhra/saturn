# gcloud storage insights inventory-reports update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update)*

**NAME**

: **gcloud storage insights inventory-reports update - update an inventory report config**

**SYNOPSIS**

: **`gcloud storage insights inventory-reports update` (`[REPORT_CONFIG](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#REPORT_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--location)`=`LOCATION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--destination)`=`DESTINATION_URL`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--display-name)`=`DISPLAY_NAME`] [`[--schedule-repeats](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--schedule-repeats)`=`FREQUENCY`] [`[--schedule-repeats-until](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--schedule-repeats-until)`=`END_DATE`] [`[--schedule-starts](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--schedule-starts)`=`START_DATE`] [`[--metadata-fields](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--metadata-fields)`=[`METADATA_FIELDS`,…]     | `[--add-metadata-fields](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--add-metadata-fields)`=[`METADATA_FIELDS`,…] `[--remove-metadata-fields](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--remove-metadata-fields)`=[`METADATA_FIELDS`,…]] [`[--parquet](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--parquet)`     | `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--csv-delimiter)`=`DELIMITER` `[--[no-]csv-header](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--[no-]csv-header)` `[--csv-separator](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#--csv-separator)`=`SEPARATOR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an inventory report config.

**EXAMPLES**

: To update the display-name of an inventory report config with ID=1234,
location=us-central1, and project=foo:

```
gcloud storage insights inventory-reports update 1234 --location=us-central1 --project=foo --display-name=bar
```

To update the same inventory report config with fully specified name:

```
gcloud storage insights inventory-reports update /projects/foo/locations/us-central1/reportConfigs/1234 --display-name=bar
```

**POSITIONAL ARGUMENTS**

: **Report config resource - The Report config to update. The arguments in this
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

: **--destination**:
Sets the URL of the destination bucket and path where generated reports are
stored.

**--display-name**:
Sets the editable name of the report configuration.

**--schedule-repeats**:
Sets how often the inventory report configuration will run.
`FREQUENCY` must be one of: `daily`,
`weekly`.

**--schedule-repeats-until**:
Sets date after which you want to stop generating inventory reports. For
example, 2022-03-30.

**--schedule-starts**:
Sets the date you want to start generating inventory reports. For example,
2022-01-30. Should be tomorrow or later based on UTC timezone.

**--metadata-fields**

**--parquet**

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
gcloud alpha storage insights inventory-reports update
```