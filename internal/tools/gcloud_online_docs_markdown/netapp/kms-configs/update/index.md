# gcloud netapp kms-configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update)*

**NAME**

: **gcloud netapp kms-configs update - update a Cloud NetApp Volumes KMS Config**

**SYNOPSIS**

: **`gcloud netapp kms-configs update` (`[KMS_CONFIG](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#KMS_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--remove-labels)`=[`KEY`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a KMS (Key Management System) Config.

**EXAMPLES**

: The following command updates a KMS Config instance named KMS_CONFIG with all
possible arguments:

```
gcloud netapp kms-configs update KMS_CONFIG --location=us-central1 --kms-location=europe-southwest1 --kms-project=new-kms-project --kms-keyring=kms-keyring2 --kms-key=crypto-key2
```

To update a KMS Config named KMS_CONFIG asynchronously, run the following
command:

```
gcloud netapp kms-configs update KMS_CONFIG --async --location=us-central1 --kms-location=europe-southwest1 --kms-project=new-kms-project --kms-keyring=kms-keyring2 --kms-key=crypto-key2
```

**POSITIONAL ARGUMENTS**

: **Kms config resource - The KMS Config to update The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud NetApp KMS Config

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--kms-key**

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
gcloud beta netapp kms-configs update
```