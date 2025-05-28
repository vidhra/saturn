# gcloud gemini data-sharing-with-google-settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update)*

**NAME**

: **gcloud gemini data-sharing-with-google-settings update - update dataSharingWithGoogleSettings**

**SYNOPSIS**

: **`gcloud gemini data-sharing-with-google-settings update` (`[DATA_SHARING_WITH_GOOGLE_SETTING](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#DATA_SHARING_WITH_GOOGLE_SETTING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--location)`=`LOCATION`) [`[--[no-]enable-preview-data-sharing](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--[no-]enable-preview-data-sharing)`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--request-id)`=`REQUEST_ID`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a dataSharingWithGoogleSetting

**EXAMPLES**

: To update the dataSharingWithGoogleSetting, run:

```
gcloud gemini data-sharing-with-google-settings update
```

**POSITIONAL ARGUMENTS**

: **DataSharingWithGoogleSetting resource - Identifier. Name of the resource.
Format:projects/{project}/locations/{location}/dataSharingWithGoogleSettings/{dataSharingWithGoogleSetting}
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `data_sharing_with_google_setting` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATA_SHARING_WITH_GOOGLE_SETTING`**:
ID of the dataSharingWithGoogleSetting or fully qualified identifier for the
dataSharingWithGoogleSetting.
To set the `data_sharing_with_google_setting` attribute:

- provide the argument `data_sharing_with_google_setting` on the
command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the dataSharingWithGoogleSetting resource.
To set the `location` attribute:

- provide the argument `data_sharing_with_google_setting` on the
command line with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--[no-]enable-preview-data-sharing**:
Whether preview data sharing should be enabled. Use
`--enable-preview-data-sharing` to enable and
`--no-enable-preview-data-sharing` to disable.

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