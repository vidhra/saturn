# gcloud dataplex glossaries categories describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe)*

**NAME**

: **gcloud dataplex glossaries categories describe - describes a glossary category**

**SYNOPSIS**

: **`gcloud dataplex glossaries categories describe` (`[GLOSSARY_CATEGORY](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe#GLOSSARY_CATEGORY)` : `[--glossary](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe#--glossary)`=`GLOSSARY` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes a glossary category.

**EXAMPLES**

: To describe a glossary category `test-category` in glossary
`test-glossary` in project `test-project` in loaction
`us-central1`, run:
```
gcloud dataplex glossaries categories describe test-category --glossary=test-glossary --location=us-central1 --project=test-project
```

**POSITIONAL ARGUMENTS**

: **Glossary category resource - Arguments and flags that define the glossary
category you want to describe. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GLOSSARY_CATEGORY`**:
ID of the glossary category or fully qualified identifier for the glossary
category.
To set the `glossary_category` attribute:

- provide the argument `glossary_category` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--glossary**:
Identifier of the Dataplex Glossary resource.
To set the `glossary` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--glossary` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex glossaries categories describe
```