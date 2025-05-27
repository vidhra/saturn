# gcloud dataplex entries update-aspects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects)*

**NAME**

: **gcloud dataplex entries update-aspects - add or update aspects for a Dataplex Entry**

**SYNOPSIS**

: **`gcloud dataplex entries update-aspects` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects#--location)`=`LOCATION`) `[--aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects#--aspects)`=`YAML_OR_JSON_FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add or update aspects for a Dataplex Entry.

**EXAMPLES**

: To add or update aspects for the Dataplex entry `entry1` within the
entry group `entry-group1` in location `us-central1` from
the YAML/JSON file, run:

```
gcloud dataplex entries update-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --aspects=path-to-a-file-with-aspects.json
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
gcloud alpha dataplex entries update-aspects
```