# gcloud data-catalog tag-templates fields enum-values rename  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename)*

**NAME**

: **gcloud data-catalog tag-templates fields enum-values rename - rename an enum value in Data Catalog tag template enum field**

**SYNOPSIS**

: **`gcloud data-catalog tag-templates fields enum-values rename` (`[ENUM_VALUE](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#ENUM_VALUE)` : `[--field](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#--field)`=`FIELD` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#--location)`=`LOCATION` `[--tag-template](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#--tag-template)`=`TAG_TEMPLATE`) `[--new-id](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#--new-id)`=`NEW_ID` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/enum-values/rename#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
aspect-types](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead.
Rename an enum value in Data Catalog tag template enum field.

**EXAMPLES**

: Rename an enum value in tag template enum field:

```
gcloud data-catalog tag-templates fields enum-values rename ENUM_VALUE --new-id="new-id"
```

**POSITIONAL ARGUMENTS**

: **Enum value resource - Enum value to rename. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `enum_value` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENUM_VALUE`**:
ID of the enum value or fully qualified identifier for the enum value.
To set the `enum_value` attribute:

- provide the argument `enum_value` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--field**:
Tag template field that contains enum value.
To set the `field` attribute:

- provide the argument `enum_value` on the command line with a fully
specified name;
- provide the argument `--field` on the command line.

**--location**:
Location of the enum value.
To set the `location` attribute:

- provide the argument `enum_value` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--tag-template**:
Tag template that contains enum value.
To set the `tag-template` attribute:

- provide the argument `enum_value` on the command line with a fully
specified name;
- provide the argument `--tag-template` on the command line.**

**REQUIRED FLAGS**

: **--new-id**:
New display name of the enum value.

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
gcloud alpha data-catalog tag-templates fields enum-values rename
```

```
gcloud beta data-catalog tag-templates fields enum-values rename
```