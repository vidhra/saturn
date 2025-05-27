# gcloud dataplex entry-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create)*

**NAME**

: **gcloud dataplex entry-groups create - create a Dataplex Entry Group**

**SYNOPSIS**

: **`gcloud dataplex entry-groups create` (`[ENTRY_GROUP](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#ENTRY_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Entry Group acts as a logical container used to organize Entries.

**EXAMPLES**

: To create Entry Group `test-entry-group` in project
`test-dataplex` at location `us-central1`, with
description `test description` and displayName `test display
name`, run:

```
gcloud dataplex entry-groups create test-entry-group --location=us-central1 --project=test-project --description='test description' --display-name='test display name'
```

**POSITIONAL ARGUMENTS**

: **Entry group resource - Arguments and flags that define the Dataplex entry group
you want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry_group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY_GROUP`**:
ID of the entry group or fully qualified identifier for the entry group.
To set the `entry_group` attribute:

- provide the argument `entry_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `entry_group` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--description**:
Description of the Entry Group.

**--display-name**:
Display name of the Entry Group.

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
gcloud alpha dataplex entry-groups create
```