# gcloud dataplex entries create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create)*

**NAME**

: **gcloud dataplex entries create - create a Dataplex Entry resource**

**SYNOPSIS**

: **`gcloud dataplex entries create` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--location)`=`LOCATION`) (`[--entry-type](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-type)`=`ENTRY_TYPE` : `[--entry-type-location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-type-location)`=`ENTRY_TYPE_LOCATION` `[--entry-type-project](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-type-project)`=`ENTRY_TYPE_PROJECT`) [`[--aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--aspects)`=`YAML_OR_JSON_FILE`] [`[--fully-qualified-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--fully-qualified-name)`=`FULLY_QUALIFIED_NAME`] [`[--parent-entry](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--parent-entry)`=`PARENT_ENTRY`] [`[--entry-source-ancestors](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-ancestors)`=[`ANCESTORS`,…] `[--entry-source-create-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-create-time)`=`DATE_TIME` `[--entry-source-description](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-description)`=`DESCRIPTION` `[--entry-source-display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-display-name)`=`DISPLAY_NAME` `[--entry-source-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-labels)`=[`KEY`=`VALUE`,…] `[--entry-source-platform](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-platform)`=`PLATFORM_NAME` `[--entry-source-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-resource)`=`RESOURCE` `[--entry-source-system](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-system)`=`SYSTEM_NAME` `[--entry-source-update-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#--entry-source-update-time)`=`DATE_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Dataplex Entry resource.

**EXAMPLES**

: To create a Dataplex entry with name `my-dataplex-entry` in location
`us-central1` in entry group `my-entry-group` and with
entry type projects/my-project/locations/us-central1/entryTypes/my-type, run:

```
gcloud dataplex entries create my-dataplex-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type
```

To create a Dataplex Entry with name `my-child-entry` and set its
parent to an existing entry `my-parent-entry`, run:

```
gcloud dataplex entries create my-child-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --parent-entry projects/my-project/locations/us-central1/entryGroups/my-entry-group/entries/my-parent-entry
```

To create a Dataplex Entry with its description, display name, ancestors, labels
and timestamps populated in its EntrySource, run:

```
gcloud dataplex entries create my-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --entry-source-description 'This is a description of the Entry.' --entry-source-display-name 'display name' --entry-source-ancestors '{"type":"projects/my-project/locations/us-central1/entryTypes/some-type",
 "name":"projects/my-project/locations/us-central1/entryGroups/my-en\
try-group/entries/ancestor-entry"},
 {"type":"projects/my-project/locations/us-central1/entryTypes/anoth\
er-type",
 "name":"projects/my-project/locations/us-central1/entryGroups/my-en\
try-group/entries/another-ancestor-entry"}' \
    --entry-source-labels key1=value1,key2=value2 \
    --entry-source-create-time 2024-01-01T09:39:25.160173Z \
    --entry-source-update-time 2024-01-01T09:39:25.160173Z
```

To create a Dataplex Entry reading its aspects from a YAML file, run:

```
gcloud dataplex entries create my-entry --location=us-central1 --entry_group=my-entry-group --entry-type projects/my-project/locations/us-central1/entryTypes/my-type --aspects aspects.yaml
```

The file containing the aspects has the following format:

```
my-project.us-central1.my-aspect-type:
  aspectType: my-project.us-central1.my-aspect-type
  createTime: "2024-01-01T09:39:25.160173Z"
  updateTime: "2024-01-01T09:39:25.160173Z"
  data:
    {}
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

**REQUIRED FLAGS**

: **--entry-type**

**OPTIONAL FLAGS**

: **--aspects**:
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

**--fully-qualified-name**:
A name for the entry that can reference it in an external system. The maximum
size of the field is 4000 characters.

**Entry resource - Arguments and flags that define the parent Entry you want to
reference. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--parent-entry` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--parent-entry` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

To set the `entry_group` attribute:

- provide the argument `--parent-entry` on the command line with a
fully specified name;
- provide the argument `--entry_group` on the command line.

**--parent-entry**:
ID of the entry or fully qualified identifier for the entry.
To set the `entry` attribute:

- provide the argument `--parent-entry` on the command line.**

**Source system related information for an entry. If any of the entry source
fields are specified, then ``--entry-source-update-time`must be specified
as well.

**--entry-source-ancestors**:
Information about individual items in the hierarchy of an Entry.

**--entry-source-create-time**:
The creation date and time of the resource in the source system.

**--entry-source-description**:
Description of the Entry.

**--entry-source-display-name**:
User friendly display name.

**--entry-source-labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.`**

**`--entry-source-platform`=`PLATFORM_NAME`**

: The platform containing the source system.

**`--entry-source-resource`=`RESOURCE`**

: The name of the resource in the source system.

**`--entry-source-system`=`SYSTEM_NAME`**

: The name of the source system.

**`--entry-source-update-time`=`DATE_TIME`**

: The update date and time of the resource in the source system.