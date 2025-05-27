# gcloud dataplex lakes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create)*

**NAME**

: **gcloud dataplex lakes create - create a Dataplex lake resource**

**SYNOPSIS**

: **`gcloud dataplex lakes create` (`[LAKE](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#LAKE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--metastore-service](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--metastore-service)`=`METASTORE_SERVICE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A lake is a centralized repository for managing data across the organization,
where enterprise data is distributed across many cloud projects, and stored in a
variety of storage services, such as Google Cloud Storage and BigQuery. A lake
provides data admins with tools to organize, secure and manage their data at
scale, and provides data scientists and data engineers an integrated experience
to easily search, discover, analyze and transform data and associated metadata.
The Lake ID will be used to generate names such as database and dataset names
when publishing metadata to Hive Metastore and BigQuery. The Lake id must follow
these rules:

- Must contain only lowercase letters, numbers, and hyphens.
- Must start with a letter.
- Must end with a number or a letter.
- Must be between 1-63 characters.
- Must be unique within the customer project / location.

**EXAMPLES**

: To create a Dataplex lake with name `my-dataplex-lake` in location
`us-central1`, run:

```
gcloud dataplex lakes create my-dataplex-lake --location=us-central
```

To create a Dataplex lake with name `my-dataplex-lake` in location
`us-central1` with metastore service `service-123abc`
attached, run:

```
gcloud dataplex lakes create my-dataplex-lake --location=us-central --metastore-service=projects/my-project/services/service-123abc
```

**POSITIONAL ARGUMENTS**

: **Lakes resource - Arguments and flags that define the Dataplex lake you want to
create. The arguments in this group can be used to specify the attributes of
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
Description of the lake.

**--display-name**:
Display name of the lake.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--metastore-service**

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
gcloud alpha dataplex lakes create
```