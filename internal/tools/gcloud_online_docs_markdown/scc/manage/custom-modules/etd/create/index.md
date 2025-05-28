# gcloud scc manage custom-modules etd create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create)*

**NAME**

: **gcloud scc manage custom-modules etd create - create an Event Threat Detection custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules etd create` `[--custom-config-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--custom-config-file)`=`CUSTOM_CONFIG` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--display-name)`=`DISPLAY-NAME` `[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--enablement-state)`=`ENABLEMENT_STATE` `[--module-type](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--module-type)`=`MODULE_TYPE` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--project)`=`PROJECT_ID_OR_NUMBER`) [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an Event Threat Detection custom module for organization
`123`, run:

```
gcloud scc manage custom-modules etd create --organization=organizations/123 --display-name="test_display_name" --module-type="CONFIGURABLE_BAD_IP" --enablement-state="ENABLED" --custom-config-file=config.json
```

**REQUIRED FLAGS**

: **--custom-config-file**:
Path to a JSON custom configuration file of the ETD custom module. Use a full or
relative path to a local file containing the value of custom_config_file.

**--display-name**:
The display name of the custom module.

**--enablement-state**:
Sets the enablement state of the Event Threat Detection custom module. Valid
options are ENABLED, DISABLED, OR INHERITED.

**--module-type**:
Type of the custom module. For a list of valid module types please visit [https://cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates](https://cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates).

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
gcloud alpha scc manage custom-modules etd create
```