# gcloud dataplex entry-types update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update)*

**NAME**

: **gcloud dataplex entry-types update - update a Dataplex Entry Type**

**SYNOPSIS**

: **`gcloud dataplex entry-types update` (`[ENTRY_TYPE](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#ENTRY_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--etag)`=`ETAG`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--platform](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--platform)`=`PLATFORM`] [`[--required-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--required-aspects)`=[`type`=`TYPE`]] [`[--system](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--system)`=`SYSTEM`] [`[--type-aliases](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--type-aliases)`=[`TYPE_ALIASES`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex Entry Type.

**EXAMPLES**

: To update Entry Type `test-entry-type` in project
`test-project` at location `us-central1`, with description
`updated description` and display name `updated display
name`, run:

```
gcloud dataplex entry-types update test-entry-type --location=us-central1 --project=test-project --description='updated description' --display-name='updated display name'
```

**POSITIONAL ARGUMENTS**

: **Entry type resource - Arguments and flags that define the Dataplex entry type
you want to update. The arguments in this group can be used to specify the
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

**--etag**:
etag value for particular Entry Type.

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
gcloud alpha dataplex entry-types update
```