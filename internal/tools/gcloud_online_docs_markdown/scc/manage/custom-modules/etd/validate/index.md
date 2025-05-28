# gcloud scc manage custom-modules etd validate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate)*

**NAME**

: **gcloud scc manage custom-modules etd validate - command to validate an ETD custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules etd validate` `[--custom-config-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--custom-config-file)`=`CUSTOM_CONFIG` `[--module-type](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--module-type)`=`MODULE_TYPE` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#--project)`=`PROJECT_ID_OR_NUMBER`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/validate#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To validate an Event Threat Detection custom module 'config.json' with a module
type 'CONFIGURABLE_BAD_IP', run:

```
gcloud scc manage custom-modules etd validate --organization=organizations/252600681248 --custom-config-file=config.json --module-type=CONFIGURABLE_BAD_IP
```

You can also specify the parent more generally:

```
gcloud scc manage custom-modules etd validate --parent=organizations/252600681248 --custom-config-file=config.json --module-type=CONFIGURABLE_BAD_IP
```

**REQUIRED FLAGS**

: **--custom-config-file**:
Path to a JSON custom configuration file of the ETD custom module. Use a full or
relative path to a local file containing the value of custom_config_file.

**--module-type**:
Type of the custom module. For a list of valid module types please visit [https://cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates](https://cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates).

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
gcloud alpha scc manage custom-modules etd validate
```