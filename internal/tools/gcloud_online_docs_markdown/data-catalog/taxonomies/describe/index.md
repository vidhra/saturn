# gcloud data-catalog taxonomies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/describe](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/describe)*

**NAME**

: **gcloud data-catalog taxonomies describe - describe a Policy Tag Taxonomy**

**SYNOPSIS**

: **`gcloud data-catalog taxonomies describe` (`[TAXONOMY](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/describe#TAXONOMY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Policy Tag Taxonomy.

**EXAMPLES**

: To describe the Taxonomy 'TAXONOMY' in the location 'LOCATION', run:

```
gcloud data-catalog taxonomies describe TAXONOMY --location='LOCATION'
```

**POSITIONAL ARGUMENTS**

: **Taxonomy resource - Policy tag taxonomy to describe. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `taxonomy` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TAXONOMY`**:
ID of the taxonomy or fully qualified identifier for the taxonomy.
To set the `taxonomy` attribute:

- provide the argument `taxonomy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the taxonomy.
To set the `location` attribute:

- provide the argument `taxonomy` on the command line with a fully
specified name;
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

**API REFERENCE**

: This command uses the `datacatalog/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/data-catalog/docs/](https://cloud.google.com/data-catalog/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog taxonomies describe
```

```
gcloud beta data-catalog taxonomies describe
```