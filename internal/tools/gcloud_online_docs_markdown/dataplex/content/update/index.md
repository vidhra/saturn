# gcloud dataplex content update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update)*

**NAME**

: **gcloud dataplex content update - update a Dataplex Content Resource with the given configurations**

**SYNOPSIS**

: **`gcloud dataplex content update` (`[CONTENT](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#CONTENT)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--location)`=`LOCATION`) [`[--data-text](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--data-text)`=`DATA_TEXT`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--path](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--path)`=`PATH`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--validate-only)`] [`[--kernel-type](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--kernel-type)`=`KERNEL_TYPE`     | `[--query-engine](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#--query-engine)`=`QUERY_ENGINE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex Content Resource with the given configurations.

**EXAMPLES**

: To update a Dataplex content `test-content` in project
`test-project` within lake `test-lake` in location
`us-central1` and change the description to `Updated
Description`, run:

```
gcloud dataplex content update test-content --project=test-project --location=us-central1 --lake=test-lake --description='Updated Description'
```

**POSITIONAL ARGUMENTS**

: **Content resource - The Content to Update a Content to. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `content` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONTENT`**:
ID of the content or fully qualified identifier for the content.
To set the `content` attribute:

- provide the argument `content` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `content` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `content` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--data-text**:
Content data in string format

**--description**:
Description of the Content

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--path**:
The path for the Content file, represented as directory structure

**--validate-only**:
Validate the update action, but don't actually perform it.

**--kernel-type**

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
gcloud alpha dataplex content update
```