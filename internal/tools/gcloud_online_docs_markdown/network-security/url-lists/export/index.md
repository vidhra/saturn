# gcloud network-security url-lists export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export](https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export)*

**NAME**

: **gcloud network-security url-lists export - export Url List**

**SYNOPSIS**

: **`gcloud network-security url-lists export` (`[URL_LIST](https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export#URL_LIST)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export#--location)`=`LOCATION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/url-lists/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a Url List.

**EXAMPLES**

: To export a Url List, run:

```
gcloud network-security url-lists export my-url-list --destination=my-url-list.yaml --location=global
```

**POSITIONAL ARGUMENTS**

: **Url list resource - Name of the Url List to export. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `url_list` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`URL_LIST`**:
ID of the url list or fully qualified identifier for the url list.
To set the `url_list` attribute:

- provide the argument `url_list` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `url_list` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. The exported data
will not contain any output-only fields. Alternatively, you may omit this flag
to write to standard output. For a schema describing the export/import format,
see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/…

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

: This command uses the `networksecurity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-security url-lists export
```

```
gcloud beta network-security url-lists export
```