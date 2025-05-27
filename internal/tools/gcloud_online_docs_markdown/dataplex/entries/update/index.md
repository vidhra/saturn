# gcloud dataplex entries update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update)*

**NAME**

: **gcloud dataplex entries update - update a Dataplex Entry**

**SYNOPSIS**

: **`gcloud dataplex entries update` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--location)`=`LOCATION`) [`[--remove-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--remove-aspects)`=[`ASPECT_TYPE`@`[PATH](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#PATH)`,…]] [`[--update-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--update-aspects)`=`YAML_OR_JSON_FILE`] [`[--clear-fully-qualified-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-fully-qualified-name)`     | `[--fully-qualified-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--fully-qualified-name)`=`FULLY_QUALIFIED_NAME`] [`[--entry-source-update-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-update-time)`=`DATE_TIME` : `[--clear-entry-source-create-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-create-time)`     | `[--entry-source-create-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-create-time)`=`DATE_TIME` `[--clear-entry-source-description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-description)`     | `[--entry-source-description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-description)`=`DESCRIPTION` `[--clear-entry-source-display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-display-name)`     | `[--entry-source-display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-display-name)`=`DISPLAY_NAME` `[--clear-entry-source-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-labels)`     | `[--entry-source-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-labels)`=[`KEY`=`VALUE`,…] `[--clear-entry-source-platform](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-platform)`     | `[--entry-source-platform](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-platform)`=`PLATFORM_NAME` `[--clear-entry-source-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-resource)`     | `[--entry-source-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-resource)`=`RESOURCE` `[--clear-entry-source-system](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--clear-entry-source-system)`     | `[--entry-source-system](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#--entry-source-system)`=`SYSTEM_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update specified fields in a given Dataplex Entry.

**EXAMPLES**

: To update fully qualified name (FQN) of an entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --fully-qualified-name='custom:a.b.c'
```

To update description of an entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --entry-source-description='Updated description' --entry-source-update-time='1998-09-04T12:00:00-0700'
```

To clear the description of an entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --clear-entry-source-description --entry-source-update-time='1998-09-04T12:00:00-0700'
```

To add or update aspects from the YAML/JSON file, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --update-aspects=path-to-a-file-with-aspects.json
```

To remove all aspects of type
`test-project.us-central1.some-aspect-type` from the entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --remove-aspects='test-project.us-central1.some-aspect-type@*'
```

To remove all aspects on path `Schema.column1` from the entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --remove-aspects='*@Schema.column1'
```

To remove exact aspects
`test-project.us-central1.some-aspect-type@Schema.column1` and
`test-project.us-central1.some-aspect-type2@Schema.column2` from the
entry, run:

```
gcloud dataplex entries update entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --remove-aspects=test-project.us-central1.some-aspect-type@Schema.column1,test-project.us-central2.some-aspect-type@Schema.column2
```

**POSITIONAL ARGUMENTS**

: **Entry resource - Arguments and flags that define the Dataplex Entry you want to
reference. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY`**:
ID of the entry or fully qualified identifier for the entry.
To set the `entry` attribute:

- provide the argument `entry` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--entry-group**:
Entry group containing Dataplex Entries.
To set the `entry-group` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--entry-group` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--remove-aspects**:
List of Aspect keys, identifying Aspects to remove from the entry.
Keys are in the format ``ASPECT_TYPE@PATH``, or
just ``ASPECT_TYPE``, if the Aspect is attached
to an entry itself rather than to a specific column defined in the schema.
``ASPECT_TYPE`` is expected to be in a format
``PROJECT_ID.LOCATION.ASPECT_TYPE_ID`` or a
wildcard `*`, which targets all aspect types.
``PATH`` can be either empty (which means a
'root' path, such that Aspect is attached to the entry itself), point to a
specific column defined in the schema (for example:
`Schema.some_column`) or a wildcard `*` (target all
paths).
``ASPECT_TYPE`` and
``PATH`` cannot be both specified as wildcards
`*`.
If both `--update-aspects` and `--remove-aspects` flags
are specified, and the same aspect key is used in both flags, then
`--update-aspects` takes precedence, and such an aspect will be
updated and not removed.

**--update-aspects**:
Path to a YAML or JSON file containing Aspects to add or update.
When this flag is specified, only Aspects referenced in the file are going to be
added or updated. Specifying this flag does not remove any Aspects from the
entry. In other words, specifying this flag will not lead to a full replacement
of Aspects with a contents of the provided file.
Content of the file contains a map, where keys are in the format
``ASPECT_TYPE@PATH``, or just
``ASPECT_TYPE``, if the Aspect is attached to
an entry itself rather than to a specific column defined in the schema.
Values in the map represent Aspect's content, which must conform to a template
defined for a given ``ASPECT_TYPE``. Each
Aspect will be replaced fully by the provided content. That means data in the
Aspect will be replaced and not merged with existing contents of that Aspect in
the Entry.
``ASPECT_TYPE`` is expected to be in a format
``PROJECT_ID.LOCATION.ASPECT_TYPE_ID``.
``PATH`` can be either empty (which means a
'root' path, such that Aspect is attached to the entry itself) or point to a
specific column defined in the schema. For example:
`Schema.some_column`.
Example YAML format:

```
project-id1.us-central1.my-aspect-type1:
    data:
      aspectField1: someValue
      aspectField2: someOtherValue
  project-id2.us-central1.my-aspect-type2@Schema.column1:
    data:
      aspectField3: someValue3
```

Example JSON format:

```
{
    "project-id1.us-central1.my-aspect-type1": {
      "data": {
        "aspectField1": "someValue",
        "aspectField2": "someOtherValue"
      }
    },
    "project-id2.us-central1.my-aspect-type2@Schema.column1": {
      "data": {
        "aspectField3": "someValue3"
      }
    }
  }
```

If both `--update-aspects` and `--remove-aspects` flags
are specified, and the same aspect key is used in both flags, then
`--update-aspects` takes precedence, and such an aspect will be
updated and not removed.

**--clear-fully-qualified-name**

**Source system related information for an entry. If any of the entry source
fields are specified, then ``--entry-source-update-time`must be specified
as well.

**--entry-source-update-time**:
The update date and time of the resource in the source system.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--clear-entry-source-create-time**

**--clear-entry-source-description**

**--clear-entry-source-display-name**

**--clear-entry-source-labels**`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.`**

**At most one of these can be specified:

**--clear-entry-source-platform**:
Clear the value for the platform field in the Entry Source.

**--entry-source-platform**:
The platform containing the source system.**

**At most one of these can be specified:

**--clear-entry-source-resource**:
Clear the value for the resource field in the Entry Source.

**--entry-source-resource**:
The name of the resource in the source system.**

**At most one of these can be specified:

**--clear-entry-source-system**:
Clear the value for the system field in the Entry Source.

**--entry-source-system**:
The name of the source system.**