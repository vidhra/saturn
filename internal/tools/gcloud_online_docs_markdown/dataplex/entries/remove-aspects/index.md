# gcloud dataplex entries remove-aspects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects)*

**NAME**

: **gcloud dataplex entries remove-aspects - remove aspects from a Dataplex Entry**

**SYNOPSIS**

: **`gcloud dataplex entries remove-aspects` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#--location)`=`LOCATION`) `[--keys](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#--keys)`=[`ASPECT_TYPE`@`[PATH](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#PATH)`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/remove-aspects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove aspects from a Dataplex Entry.

**EXAMPLES**

: To remove all aspects of type
`test-project.us-central1.some-aspect-type` from the entry, run:

```
gcloud dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys='test-project.us-central1.some-aspect-type@*'
```

To remove all aspects on path `Schema.column1` from the entry, run:

```
gcloud dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys='*@Schema.column1'
```

To remove exact aspects
`test-project.us-central1.some-aspect-type@Schema.column1` and
`test-project.us-central1.some-aspect-type2@Schema.column2` from the
entry, run:

```
gcloud dataplex entries remove-aspects entry1 --project=test-project --location=us-central1 --entry-group entry-group1 --keys=test-project.us-central1.some-aspect-type@Schema.column1,test-project.us-central2.some-aspect-type@Schema.column2
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

: **--keys**:
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
gcloud alpha dataplex entries remove-aspects
```