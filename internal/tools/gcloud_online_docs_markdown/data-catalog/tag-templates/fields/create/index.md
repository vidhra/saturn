# gcloud data-catalog tag-templates fields create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create)*

**NAME**

: **gcloud data-catalog tag-templates fields create - create a Data Catalog tag template field**

**SYNOPSIS**

: **`gcloud data-catalog tag-templates fields create` (`[FIELD](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#FIELD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#--location)`=`LOCATION` `[--tag-template](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#--tag-template)`=`TAG_TEMPLATE`) `[--type](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#--type)`=`TYPE` [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/fields/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
aspect-types](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types)` instead.
Create a Data Catalog tag template field.

**EXAMPLES**

: Create a string tag template field:

```
gcloud data-catalog tag-templates fields create create FIELD --display-name=DISPLAY --type=string
```

Create an enum tag template field with values 'A' and 'B':

```
gcloud data-catalog tag-templates fields create FIELD --display-name=DISPLAY --type="enum(A|B)"
```

**POSITIONAL ARGUMENTS**

: **Tag template field resource - Tag template field to create. The arguments in
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

**REQUIRED FLAGS**

: **--type**:
Type of the tag template field. Choices are double, string, bool, timestamp, and
enum.

```
To specify a string field:
  `type=string`
```

```
To specify an enum field with values 'A' and 'B':
  `type="enum(A|B)"`
```

**OPTIONAL FLAGS**

: **--display-name**:
Display name of the tag template field.

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
gcloud alpha data-catalog tag-templates fields create
```

```
gcloud beta data-catalog tag-templates fields create
```