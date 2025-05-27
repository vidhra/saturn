# gcloud dataplex content create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create)*

**NAME**

: **gcloud dataplex content create - creating a content**

**SYNOPSIS**

: **`gcloud dataplex content create` `[--data-text](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--data-text)`=`DATA_TEXT` `[--path](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--path)`=`PATH` (`[--kernel-type](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--kernel-type)`=`KERNEL_TYPE`     | `[--query-engine](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--query-engine)`=`QUERY_ENGINE`) (`[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--lake)`=`LAKE` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/content/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creating a content.

**EXAMPLES**

: To create a Dataplex content `test-content` of type notebook within
lake `test-lake` in location `us-central1`.

```
gcloud dataplex content create --project=test-project --location=us-central1 --lake=test-lake --kernel-type=PYTHON3 --data-text='' --path='test-content'
```

**REQUIRED FLAGS**

: **--data-text**:
Content data in string format

**--path**:
The path for the Content file, represented as directory structure

**--kernel-type**

**Lakes resource - Arguments and flags that define the Dataplex lake you want to
create a Content to. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--lake` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--lake**:
ID of the lakes or fully qualified identifier for the lakes.
To set the `lake` attribute:

- provide the argument `--lake` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `--lake` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**OPTIONAL FLAGS**

: **--description**:
Description of the Content

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
Validate the create action, but don't actually perform it.

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
gcloud alpha dataplex content create
```