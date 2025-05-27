# gcloud dataplex entry-types create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create)*

**NAME**

: **gcloud dataplex entry-types create - create a Dataplex Entry Type**

**SYNOPSIS**

: **`gcloud dataplex entry-types create` (`[ENTRY_TYPE](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#ENTRY_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--platform](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--platform)`=`PLATFORM`] [`[--required-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--required-aspects)`=[`type`=`TYPE`]] [`[--system](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--system)`=`SYSTEM`] [`[--type-aliases](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--type-aliases)`=[`TYPE_ALIASES`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Entry Type is a template for creating Entries.

**EXAMPLES**

: To create Entry Type `test-entry-type` in project
`test-dataplex` at location `us-central1`, with
description `test description`, displayName `test display
name` and required aspect type
`projects/test-dataplex/locations/us-central1/aspectTypes/test-aspect-type`,
run:

```
gcloud dataplex entry-types create test-entry-type --location=us-central1 --project=test-project --description='test description' --display-name='test display name' --required-aspects=type='projects/test-dataplex/locations/us-central1/aspectTypes/test-aspect-type'
```

**POSITIONAL ARGUMENTS**

: **Entry type resource - Arguments and flags that define the Dataplex entry type
you want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry_type` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY_TYPE`**:
ID of the entry type or fully qualified identifier for the entry type.
To set the `entry_type` attribute:

- provide the argument `entry_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `entry_type` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--description**:
Description of the Entry Type.

**--display-name**:
Display name of the Entry Type.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--platform**:
The platform that Entries of this type belongs to.

**--required-aspects**:
Required aspect type for the entry type.

**--system**:
The system that Entries of this type belongs to.

**--type-aliases**:
Indicates the class this Entry Type belongs to.

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
gcloud alpha dataplex entry-types create
```