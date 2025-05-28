# gcloud netapp kms-configs verify  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify)*

**NAME**

: **gcloud netapp kms-configs verify - verify that the Cloud NetApp Volumes KMS Config is reachable**

**SYNOPSIS**

: **`gcloud netapp kms-configs verify` (`[KMS_CONFIG](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify#KMS_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Verifies that the Cloud NetApp Volumes KMS (Key Management System) Config is
reachable.

**EXAMPLES**

: The following command verifies that the KMS Config instance named KMS_CONFIG is
reachable using specified location.

```
gcloud netapp kms-configs verify KMS_CONFIG --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Kms config resource - The KMS Config used to verify The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `kms_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KMS_CONFIG`**:
ID of the kms_config or fully qualified identifier for the kms_config.
To set the `kms_config` attribute:

- provide the argument `kms_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the kms_config.
To set the `location` attribute:

- provide the argument `kms_config` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

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
gcloud beta netapp kms-configs verify
```