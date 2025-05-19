# gcloud alpha anthos config controller update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update)*

**NAME**

: **gcloud alpha anthos config controller update - update an Anthos Config Controller instance**

**SYNOPSIS**

: **`gcloud alpha anthos config controller update` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#--async)`] [`[--experimental-features](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#--experimental-features)`=[`FEATURE`,…]] [`[--man-block](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#--man-block)`=`MAN_BLOCK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an Anthos Config Controller instance.

**EXAMPLES**

: To update the master authorized network for an existing Anthos Config Controller
instance, run:

```
gcloud alpha anthos config controller update sample-instance --man-block=MAN_BLOCK
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The identifier for a Config Controller instance. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the instance or fully qualified identifier for the instance.
To set the `name` attribute:

- provide the argument `name` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the Config Controller instance location. Currently, only
``us-central1``,
``us-east1``,
``us-east4``,
``us-east5``,
``us-west2``,
``northamerica-northeast1``,
``northamerica-northeast2``,
``europe-north1``,
``europe-west1``,
``europe-west3``,
``europe-west6``,
``australia-southeast1``,
``australia-southeast2``,
``asia-northeast1``,
``asia-northeast2`` and
``asia-southeast1`` are supported.
To set the `location` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--experimental-features**:
Enable experimental features. It can only be enabled in ALPHA version.

**--man-block**:
Master Authorized Network. Allows access to the Kubernetes control plane from
this block. Defaults to '0.0.0.0/0' if flag is not provided.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.