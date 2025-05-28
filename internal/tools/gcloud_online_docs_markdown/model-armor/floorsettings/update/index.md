# gcloud model-armor floorsettings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update)*

**NAME**

: **gcloud model-armor floorsettings update - update the FloorSetting resource**

**SYNOPSIS**

: **`gcloud model-armor floorsettings update` `[--full-uri](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--full-uri)`=`FULL_URI` [`[--enable-floor-setting-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--enable-floor-setting-enforcement)`=`ENABLE_FLOOR_SETTING_ENFORCEMENT`] [`[--malicious-uri-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--malicious-uri-filter-settings-enforcement)`=`MALICIOUS_URI_FILTER_SETTINGS_ENFORCEMENT`] [`[--add-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--add-rai-settings-filters)`=`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`] | `[--clear-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--clear-rai-settings-filters)` | `[--rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--rai-settings-filters)`=`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`] | `[--remove-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--remove-rai-settings-filters)`=`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`]] [`[--advanced-config-deidentify-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--advanced-config-deidentify-template)`=`ADVANCED_CONFIG_DEIDENTIFY_TEMPLATE` `[--advanced-config-inspect-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--advanced-config-inspect-template)`=`ADVANCED_CONFIG_INSPECT_TEMPLATE` `[--basic-config-filter-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--basic-config-filter-enforcement)`=`BASIC_CONFIG_FILTER_ENFORCEMENT`] [`[--pi-and-jailbreak-filter-settings-confidence-level](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--pi-and-jailbreak-filter-settings-confidence-level)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_CONFIDENCE_LEVEL` `[--pi-and-jailbreak-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#--pi-and-jailbreak-filter-settings-enforcement)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_ENFORCEMENT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/model-armor/floorsettings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the floor setting resource with the given name.

**REQUIRED FLAGS**

: **--full-uri**:
Full uri of the floor setting

**OPTIONAL FLAGS**

: **--enable-floor-setting-enforcement**:
Enable or disable the floor setting enforcement

**--malicious-uri-filter-settings-enforcement**

**--add-rai-settings-filters**

**--advanced-config-deidentify-template**

**--pi-and-jailbreak-filter-settings-confidence-level**

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
gcloud alpha model-armor floorsettings update
```