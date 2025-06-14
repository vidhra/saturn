# gcloud dataplex aspect-types update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update)*

**NAME**

: **gcloud dataplex aspect-types update - update a Dataplex Aspect Type**

**SYNOPSIS**

: **`gcloud dataplex aspect-types update` (`[ASPECT_TYPE](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#ASPECT_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--etag)`=`ETAG`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--metadata-template-file-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--metadata-template-file-name)`=`METADATA_TEMPLATE_FILE_NAME`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex Aspect Type.

**EXAMPLES**

: To update Aspect Type `test-aspect-type` in project
`test-project` at location `us-central1`, with description
`updated description` and display name `updated display
name`, run:

```
gcloud dataplex aspect-types update test-aspect-type --location=us-central1 --project=test-project --description='updated description' --display-name='updated display name'
```

**POSITIONAL ARGUMENTS**

: **Aspect type resource - Arguments and flags that define the Dataplex aspect type
you want to update. The arguments in this group can be used to specify the
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

**FLAGS**

: **--description**:
Description of the Aspect Type.

**--display-name**:
Display name of the Aspect Type.

**--etag**:
etag value for particular Aspect Type.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--metadata-template-file-name**:
The name of the JSON or YAML file to define Metadata Template.

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
gcloud alpha dataplex aspect-types update
```