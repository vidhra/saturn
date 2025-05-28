# gcloud scc manage custom-modules sha create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create)*

**NAME**

: **gcloud scc manage custom-modules sha create - create an Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules sha create` `[--custom-config-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--custom-config-from-file)`=`CUSTOM_CONFIG` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--display-name)`=`DISPLAY-NAME` `[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--enablement-state)`=`ENABLEMENT_STATE` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--project)`=`PROJECT_ID_OR_NUMBER`) [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a Security Health Analytics custom module for organization
`123`, run:

```
gcloud scc manage custom-modules sha create --organization=organizations/123 --display-name="test_display_name" --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

**REQUIRED FLAGS**

: **--custom-config-from-file**:
Path to a YAML custom configuration file. Use a full or relative path to a local
file containing the value of custom_config.

**--display-name**:
The display name of the custom module.

**--enablement-state**:
Sets the enablement state of the Security Health Analytics custom module. Valid
options are ENABLED, DISABLED, OR INHERITED.

**--folder**

**OPTIONAL FLAGS**

: **--validate-only**:
If present, the request is validated (including IAM checks) but no action is
taken.

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
gcloud alpha scc manage custom-modules sha create
```