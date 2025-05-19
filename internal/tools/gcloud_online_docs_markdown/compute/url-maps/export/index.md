# gcloud compute url-maps export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export)*

**NAME**

: **gcloud compute url-maps export - export a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps export` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export#URL_MAP)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export#--destination)`=`DESTINATION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a URL map's configuration to a file. This configuration can be imported
at a later time.

**EXAMPLES**

: A URL map can be exported by running:

```
gcloud compute url-maps export NAME --destination=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to export.

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output. For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/UrlMap.yaml.

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
gcloud alpha compute url-maps export
```

```
gcloud beta compute url-maps export
```