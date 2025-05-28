# gcloud scc manage custom-modules etd update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update)*

**NAME**

: **gcloud scc manage custom-modules etd update - update an Event Threat Detection custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules etd update` `[MODULE_ID_OR_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#MODULE_ID_OR_NAME)` (`[--custom-config-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--custom-config-file)`=`PATH_TO_FILE` `[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--enablement-state)`=`ENABLEMENT_STATE`) [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--validate-only)`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#--project)`=`PROJECT_ID_OR_NUMBER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update an Event Threat Detection custom module with ID 123456 for
organization 123, run:

```
gcloud scc manage custom-modules etd update 123456 --organization=organizations/123 --enablement-state="ENABLED" --custom-config-file=custom_config.json
```

**POSITIONAL ARGUMENTS**

: **`MODULE_ID_OR_NAME`**:
The custom module ID or name. The expected format is
{parent}/[locations/global]/eventThreatDetectionCustomModules/{module_id} or
just {module_id}. Where module_id is a numeric identifier 1-20 characters in
length. Parent is of the form organizations/{id}, projects/{id or name},
folders/{id}.

**REQUIRED FLAGS**

: **--custom-config-file**

**OPTIONAL FLAGS**

: **--validate-only**:
If present, the request is validated (including IAM checks) but no action is
taken.

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
gcloud alpha scc manage custom-modules etd update
```