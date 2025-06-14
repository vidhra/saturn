# gcloud filestore operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel)*

**NAME**

: **gcloud filestore operations cancel - cancel a Filestore operation**

**SYNOPSIS**

: **`gcloud filestore operations cancel` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel#OPERATION)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel#--zone)`=`ZONE`) [`[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancels a Filestore operation. The server makes a best effort to cancel the
operation, but success is not guaranteed. Clients can use the `filestore
operations describe` command to check whether the cancellation succeeded
or not.

**EXAMPLES**

: To cancel a Filestore operation named ``NAME" in the ``us-central1-c" zone, run:

```
gcloud filestore operations cancel NAME --zone=us-central1-c
```

To cancel a Filestore operation named ``NAME" in the ``us-central1" region, run:

```
gcloud filestore operations cancel NAME --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The operation to cancel. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The zone of the operation.
To set the `zone` attribute:

- provide the argument `operation` on the command line with a fully
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
gcloud alpha filestore operations cancel
```

```
gcloud beta filestore operations cancel
```