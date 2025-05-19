# gcloud compute url-maps edit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit)*

**NAME**

: **gcloud compute url-maps edit - modify URL maps**

**SYNOPSIS**

: **`gcloud compute url-maps edit` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit#URL_MAP)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps edit` can be used to modify a URL map. The
URL map resource is fetched from the server and presented in a text editor.
After the file is saved and closed, this command will update the resource. Only
fields that can be modified are displayed in the editor.
The editor used to modify the resource is chosen by inspecting the
``EDITOR`` environment variable.

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**FLAGS**

: **--global**

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

: These variants are also available:

```
gcloud alpha compute url-maps edit
```

```
gcloud beta compute url-maps edit
```