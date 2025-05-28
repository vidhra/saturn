# gcloud metastore federations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update)*

**NAME**

: **gcloud metastore federations update - update a Dataproc Metastore federation**

**SYNOPSIS**

: **`gcloud metastore federations update` (`[FEDERATION](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#FEDERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--location)`=`LOCATION`) (`[--update-backends](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--update-backends)`=`RANK`=`BACKEND` `[--clear-backends](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--clear-backends)`     | `[--remove-backends](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--remove-backends)`=`RANK`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/federations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata and/or configuration parameters of a Dataproc Metastore
federation.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the update via:

```
gcloud metastore operations describe
```

**EXAMPLES**

: To update a Dataproc Metastore federation with the name
`my-metastore-federation` in location `us-central` with
two backends `dpms1` and `dpms2`, run:

```
gcloud metastore federations update my-metastore-federation --location=us-central1 --update-backends=1=dpms:dpms1,2=dpms:projects/my-project/locations/us-central1/services/dpms2
```

**POSITIONAL ARGUMENTS**

: **Federation resource - Arguments and flags that specify the Dataproc Metastore
federation you want to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `federation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FEDERATION`**:
ID of the federation or fully qualified identifier for the federation.
To set the `federation` attribute:

- provide the argument `federation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `federation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.**

**REQUIRED FLAGS**

: **--update-backends**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

**API REFERENCE**

: This command uses the `metastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataproc-metastore/docs](https://cloud.google.com/dataproc-metastore/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha metastore federations update
```

```
gcloud beta metastore federations update
```