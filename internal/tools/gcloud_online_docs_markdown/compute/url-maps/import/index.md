# gcloud compute url-maps import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import)*

**NAME**

: **gcloud compute url-maps import - import a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps import` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import#URL_MAP)` [`[--source](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import#--source)`=`SOURCE`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Imports a URL map's configuration from a file.

**EXAMPLES**

: A URL map can be imported by running:

```
gcloud compute url-maps import NAME --source=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to import.

**FLAGS**

: **--source**:
Path to a YAML file containing configuration export data. Alternatively, you may
omit this flag to read from standard input.For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/UrlMap.yaml.

```
Note: $CLOUDSDKROOT represents the Google Cloud CLI's installation directory.
```

**--global**

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
gcloud alpha compute url-maps import
```

```
gcloud beta compute url-maps import
```