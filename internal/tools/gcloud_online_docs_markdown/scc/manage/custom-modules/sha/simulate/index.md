# gcloud scc manage custom-modules sha simulate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate)*

**NAME**

: **gcloud scc manage custom-modules sha simulate - command to simulate a SHA custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules sha simulate` `[--custom-config-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--custom-config-from-file)`=`CUSTOM_CONFIG` `[--resource-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--resource-from-file)`=`TEST_DATA` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#--project)`=`PROJECT_ID_OR_NUMBER`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To simulate a Security Health Analytics custom module with ID
`123456` for organization `123`, run:

```
gcloud scc manage custom-modules sha simulate 123456 --organization=123 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml
```

To simulate a Security Health Analytics custom module with ID
`123456` for folder `456`, run:

```
gcloud scc manage custom-modules sha simulate 123456 --folder=456 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml
```

To simulate a Security Health Analytics custom module with ID
`123456` for project `789`, run:

```
gcloud scc manage custom-modules sha simulate 123456 --project=789 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml
```

You can also specify the parent more generally:

```
gcloud scc manage custom-modules sha simulate 123456 --parent=organizations/123 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml
```

Or just specify the fully qualified module name:

```
gcloud scc manage custom-modules sha simulate organizations/123/locations/global/effectiveSecurityHealthAnalyticsCustomModules/123456 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml
```

**REQUIRED FLAGS**

: **--custom-config-from-file**:
Path to a YAML custom configuration file. Use a full or relative path to a local
file containing the value of custom_config.

**--resource-from-file**:
Path to a YAML file that contains the resource data to validate the Security
Health Analytics custom module against. Use a full or relative path to a local
file containing the value of resource.

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

: This variant is also available:

```
gcloud alpha scc manage custom-modules sha simulate
```