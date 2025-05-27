# gcloud data-catalog tag-templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create)*

**NAME**

: **gcloud data-catalog tag-templates create - create a Data Catalog tag template**

**SYNOPSIS**

: **`gcloud data-catalog tag-templates create` (`[TAG_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create#TAG_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create#--location)`=`LOCATION`) `[--field](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create#--field)`=[`id`=`ID`,`type`=`TYPE`,`display-name`=`DISPLAY_NAME`,`required`=`REQUIRED`,…] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
aspect-types](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead.
Create a Data Catalog tag template.

**EXAMPLES**

: Create a string tag template with a required string field:

```
gcloud data-catalog tag-templates create TEMPLATE --field=id=ID,display-name=DISPLAY,type=string,required=TRUE
```

Create an enum tag template with an optional enum field with values 'A' and 'B':

```
gcloud data-catalog tag-templates create TEMPLATE --field=id=ID,display-name=DISPLAY,type='enum(A|B)'
```

Create a tag template with a optional string field and a required enum field
with values 'A' and 'B':

```
gcloud data-catalog tag-templates create TEMPLATE --field=id=ID1,display-name=DISPLAY1,type=string --field=id=ID2,display-name=DISPLAY2,type='enum(A|B)',required=TRUE
```

**POSITIONAL ARGUMENTS**

: **Tag template resource - Tag template to create. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `tag_template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TAG_TEMPLATE`**:
ID of the tag template or fully qualified identifier for the tag template.
To set the `tag_template` attribute:

- provide the argument `tag_template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the tag template.
To set the `location` attribute:

- provide the argument `tag_template` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--field**:
Specification for a tag template field. This flag can be repeated to specify
multiple fields. The following keys are allowed:

```
*id*::: (Required) ID of the tag template field.
```

```
*type*::: (Required) Type of the tag template field. Choices are
    double, string, bool, timestamp, and enum.
```

```
To specify a string field:
  `type=string`
```

```
To specify an enum field with values 'A' and 'B':
  `type=enum(A|B)`
```

```
*display-name*::: Display name of the tag template field.
```

```
*required*::: Indicates if the tag template field is required.
    Defaults to FALSE.
```

**OPTIONAL FLAGS**

: **--display-name**:
Human-readable name for the tag template.

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
gcloud alpha data-catalog tag-templates create
```

```
gcloud beta data-catalog tag-templates create
```