# gcloud filestore instances describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe)*

**NAME**

: **gcloud filestore instances describe - show metadata for a Filestore instance**

**SYNOPSIS**

: **`gcloud filestore instances describe` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe#--zone)`=`ZONE`) [`[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe#--location)`=`LOCATION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show metadata for a Filestore instance.

**EXAMPLES**

: The following command shows the metadata for the Filestore instance named NAME
in us-central1-c.

```
gcloud filestore instances describe NAME --location=us-central1-c
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The instance to describe. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The zone of the instance.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- provide the argument `region` on the command line;
- provide the argument `location` on the command line;
- set the property `filestore/zone`;
- set the property `filestore/region`;
- set the property `filestore/location`.**

**FLAGS**

: **--location**:
Location of the Cloud Filestore instance/operation.

**--region**:
Region of the Cloud Filestore instance.

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

: These variants are also available:

```
gcloud alpha filestore instances describe
```

```
gcloud beta filestore instances describe
```