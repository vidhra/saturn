# gcloud data-catalog taxonomies export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/export](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/export)*

**NAME**

: **gcloud data-catalog taxonomies export - export a list of taxonomies from a certain project**

**SYNOPSIS**

: **`gcloud data-catalog taxonomies export` `[TAXONOMIES](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/export#TAXONOMIES)` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/export#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a list of taxonomies from a certain project.

**EXAMPLES**

: To export 'TAXONOMY1' and 'TAXONOMY2' from your project within location LOCATION
and render the export on the command line:

```
gcloud data-catalog taxonomies export "TAXONOMY1,TAXONOMY2" --location=LOCATION
```

To export 'TAXONOMY1' and 'TAXONOMY2' from your project within location LOCATION
and store the export into a file "/path/file.yaml":

```
gcloud data-catalog taxonomies export "TAXONOMY1,TAXONOMY2" --location=LOCATION > /path/file.yaml
```

**POSITIONAL ARGUMENTS**

: **`TAXONOMIES`**:
List of taxonomies to bring.

**REQUIRED FLAGS**

: **Location resource - Location to export taxonomies from. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

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
gcloud alpha data-catalog taxonomies export
```

```
gcloud beta data-catalog taxonomies export
```