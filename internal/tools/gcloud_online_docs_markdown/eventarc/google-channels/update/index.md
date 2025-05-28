# gcloud eventarc google-channels update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update)*

**NAME**

: **gcloud eventarc google-channels update - update an Eventarc Google channel**

**SYNOPSIS**

: **`gcloud eventarc google-channels update` [`[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--location)`=`LOCATION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-crypto-key](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--clear-crypto-key)`     | `[--crypto-key](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--crypto-key)`=`CRYPTO_KEY`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Eventarc Google channel.

**EXAMPLES**

: To update the Google channel in location `us-central1`, run:

```
gcloud eventarc google-channels update --location=us-central1
```

To configure the Google channel in location `us-central1` with a
Cloud KMS CryptoKey, run:

```
gcloud eventarc google-channels update --location=us-central1 --crypto-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY
```

**FLAGS**

: **Location resource - The location of the Google Channel. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `eventarc/location` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

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