# gcloud dataplex lakes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update)*

**NAME**

: **gcloud dataplex lakes update - update a Dataplex lake resource**

**SYNOPSIS**

: **`gcloud dataplex lakes update` (`[LAKE](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#LAKE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--metastore-service)`=`METASTORE_SERVICE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex lake resource.

**EXAMPLES**

: To update a Dataplex Lake `test-lake` in location
`us-central1` to have the display name
`first-dataplex-lake` and metastore service
`projects/test-lake/locations/us-central1/service/test-service`, run:

```
gcloud dataplex lakes update test-lake --location=us-central1 --display-name="first-dataplex-lake" --metastore-service="projects/test-lake/locations/us-central1/service/test-service"
```

**POSITIONAL ARGUMENTS**

: **Lakes resource - Arguments and flags that define the Dataplex lake you want to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `lake` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`LAKE`**:
ID of the lakes or fully qualified identifier for the lakes.
To set the `lake` attribute:

- provide the argument `lake` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `lake` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the lake

**--display-name**:
Display Name

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--metastore-service**

**--validate-only**:
Validate the update action, but don't actually perform it.

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
gcloud alpha dataplex lakes update
```