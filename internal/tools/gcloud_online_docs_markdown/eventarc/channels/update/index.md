# gcloud eventarc channels update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update)*

**NAME**

: **gcloud eventarc channels update - update an Eventarc channel**

**SYNOPSIS**

: **`gcloud eventarc channels update` (`[CHANNEL](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#CHANNEL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-crypto-key](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--clear-crypto-key)`     | `[--crypto-key](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--crypto-key)`=`CRYPTO_KEY`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Eventarc channel.

**EXAMPLES**

: To update the channel `my-channel` in location
`us-central1`, run:

```
gcloud eventarc channels update my-channel --location=us-central1
```

To configure the channel `my-channel` in location
`us-central1` with a Cloud KMS CryptoKey, run:

```
gcloud eventarc channels update my-channel --location=us-central1 --crypto-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY
```

**POSITIONAL ARGUMENTS**

: **Channel resource - Channel to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `channel` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CHANNEL`**:
ID of the channel or fully qualified identifier for the channel.
To set the `channel` attribute:

- provide the argument `channel` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the Eventarc channel, which should be either
``global`` or one of the supported regions.
Alternatively, set the [eventarc/location] property.
To set the `location` attribute:

- provide the argument `channel` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-crypto-key**

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