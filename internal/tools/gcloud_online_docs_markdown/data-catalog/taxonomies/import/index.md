# gcloud data-catalog taxonomies import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/import](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/import)*

**NAME**

: **gcloud data-catalog taxonomies import - export a file with serialized taxonomies to a certain project**

**SYNOPSIS**

: **`gcloud data-catalog taxonomies import` `[TAXONOMIES](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/import#TAXONOMIES)` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/import#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a file with serialized taxonomies to a certain project.

**EXAMPLES**

: To parse and import the taxonomies contained in '/tmp/taxonomies.json' to your
project within location LOCATION:

```
gcloud data-catalog taxonomies import "/tmp/taxonomies.json" --location="LOCATION"
```

**POSITIONAL ARGUMENTS**

: **`TAXONOMIES`**:
File containing serialized taxonomy.

**REQUIRED FLAGS**

: **Location resource - Location to import taxonomies to. This represents a Cloud
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
gcloud alpha data-catalog taxonomies import
```

```
gcloud beta data-catalog taxonomies import
```