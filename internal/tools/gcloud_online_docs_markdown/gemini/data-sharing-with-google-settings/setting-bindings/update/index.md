# gcloud gemini data-sharing-with-google-settings setting-bindings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update)*

**NAME**

: **gcloud gemini data-sharing-with-google-settings setting-bindings update - update settingBindings**

**SYNOPSIS**

: **`gcloud gemini data-sharing-with-google-settings setting-bindings update` (`[SETTING_BINDING](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#SETTING_BINDING)` : `[--data-sharing-with-google-setting](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--data-sharing-with-google-setting)`=`DATA_SHARING_WITH_GOOGLE_SETTING` `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--async)`] [`[--product](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--product)`=`PRODUCT`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--request-id)`=`REQUEST_ID`] [`[--target](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--target)`=`TARGET`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a settingBinding

**EXAMPLES**

: To update the settingBinding, run:
$ [gcloud
gemini data-sharing-with-google-settings setting-bindings](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings) \
```
update
```

**POSITIONAL ARGUMENTS**

: **SettingBinding resource - Identifier. Name of the resource.
Format:projects/{project}/locations/{location}/{settingType}/{setting}/settingBindings/{setting_binding}
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SETTING_BINDING`**:
ID of the settingBinding or fully qualified identifier for the settingBinding.
To set the `setting_binding` attribute:

- provide the argument `setting_binding` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--data-sharing-with-google-setting**:
The dataSharingWithGoogleSetting id of the settingBinding resource.
To set the `data-sharing-with-google-setting` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--data-sharing-with-google-setting` on the
command line.

**--location**:
The location id of the settingBinding resource.
To set the `location` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--product**:
Product type of the setting binding. `PRODUCT` must be one
of:

**`gemini-cloud-assist`**:
Gemini Cloud Assist.

**`gemini-code-assist`**:
Gemini Code Assist.

**`gemini-in-bigquery`**:
Gemini in BigQuery.

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--target**:
Target of the binding.

**--labels**

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

: This command uses the `cloudaicompanion/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/gemini](https://cloud.google.com/gemini)