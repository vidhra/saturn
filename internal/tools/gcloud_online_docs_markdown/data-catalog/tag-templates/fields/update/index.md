# gcloud data-catalog tag-templates fields update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update)*

**NAME**

: **gcloud data-catalog tag-templates fields update - update a Data Catalog tag template field**

**SYNOPSIS**

: **`gcloud data-catalog tag-templates fields update` (`[FIELD](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#FIELD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#--location)`=`LOCATION` `[--tag-template](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#--tag-template)`=`TAG_TEMPLATE`) [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#--display-name)`=`DISPLAY_NAME`] [`[--enum-values](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#--enum-values)`=[`ENUM_VALUES`,…]] [`[--required](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#--required)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
aspect-types](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead.
Update a Data Catalog tag template field.

**EXAMPLES**

: Update the display name of a tag template field:

```
gcloud data-catalog tag-templates fields update FIELD --display-name=NAME
```

Set tag template enum field values to be 'A' and 'B':

```
gcloud data-catalog tag-templates fields update FIELD --enum-values=A,B
```

Set a tag template field to be optional:

```
gcloud data-catalog tag-templates fields update FIELD --no-required
```

**POSITIONAL ARGUMENTS**

: **Tag template field resource - Tag template field to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FIELD`**:
ID of the tag template field or fully qualified identifier for the tag template
field.
To set the `field` attribute:

- provide the argument `field` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the tag template field.
To set the `location` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--tag-template**:
Tag template of the tag template field.
To set the `tag-template` attribute:

- provide the argument `field` on the command line with a fully
specified name;
- provide the argument `--tag-template` on the command line.**

**FLAGS**

: **--display-name**:
Display name of the tag template field.

**--enum-values**:
Comma-separated list of enum values. The list of enum values passed with this
flag replaces the existing one in tag template enum field. That means:

- the enum values passed to the flag and not present in tag template enum field
get created
- the enum values present in tag template enum field and missing in the list get
removed
- the order of the items on the list is preserved

Enum values can only be removed from optional enum fields for now.

**--required**:
Indicates if the tag template field is required. Updating from FALSE (optional)
to TRUE (required) is NOT allowed.

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
gcloud alpha data-catalog tag-templates fields update
```

```
gcloud beta data-catalog tag-templates fields update
```