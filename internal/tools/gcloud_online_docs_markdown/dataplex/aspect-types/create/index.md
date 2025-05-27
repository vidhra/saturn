# gcloud dataplex aspect-types create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create)*

**NAME**

: **gcloud dataplex aspect-types create - create a Dataplex Aspect Type**

**SYNOPSIS**

: **`gcloud dataplex aspect-types create` (`[ASPECT_TYPE](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#ASPECT_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--location)`=`LOCATION`) `[--metadata-template-file-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--metadata-template-file-name)`=`METADATA_TEMPLATE_FILE_NAME` [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Aspect Type is a template for creating Aspects.

**EXAMPLES**

: To create Aspect Type `test-aspect-type` in project
`test-dataplex` at location `us-central1`, with
description `test description`, displayName `test display
name` and metadataTemplateFileName `file.json`, run:

```
gcloud dataplex aspect-types create test-aspect-type --location=us-central1 --project=test-project --description='test description' --display-name='test display name' --metadata-template-file-name='file.json'
```

**POSITIONAL ARGUMENTS**

: **Aspect type resource - Arguments and flags that define the Dataplex aspect type
you want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `aspect_type` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ASPECT_TYPE`**:
ID of the aspect type or fully qualified identifier for the aspect type.
To set the `aspect_type` attribute:

- provide the argument `aspect_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `aspect_type` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**REQUIRED FLAGS**

: **--metadata-template-file-name**:
The name of the JSON or YAML file to define Metadata Template.

**OPTIONAL FLAGS**

: **--description**:
Description of the Aspect Type.

**--display-name**:
Display name of the Aspect Type.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

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

: This variant is also available:

```
gcloud alpha dataplex aspect-types create
```