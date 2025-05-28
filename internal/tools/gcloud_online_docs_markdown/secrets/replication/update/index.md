# gcloud secrets replication update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update)*

**NAME**

: **gcloud secrets replication update - update a secret replica's metadata**

**SYNOPSIS**

: **`gcloud secrets replication update` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update#SECRET)` [`[--remove-cmek](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update#--remove-cmek)`     | `[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update#--location)`=`REPLICA-LOCATION` `[--set-kms-key](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update#--set-kms-key)`=`SET-KMS-KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a secret replica's metadata (e.g. cmek policy). This command will return
an error if given a secret that does not exist or if given a location that the
given secret doesn't exist in.
The --remove-kms-key flag is only valid for Secrets that have an automatic
replication policy or exist in a single location. To remove keys from a Secret
with multiple user managed replicas, please use the set-replication command.

**EXAMPLES**

: To remove CMEK from a secret called 'my-secret', run:

```
gcloud secrets replication update my-secret --remove-cmek
```

To set the CMEK key on an automatic secret called my-secret to a specified KMS
key, run:

```
$gcloud secrets replication update my-secret
--set-kms-key=projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key
```

To set the CMEK key on a secret called my-secret to a specified KMS key in a
specified location in its replication, run:

```
$gcloud secrets replication update my-secret
--set-kms-key=projects/my-project/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key
--location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Secret resource - The secret to update. This represents a Cloud resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `SECRET` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SECRET`**:
ID of the secret or fully qualified identifier for the secret.
To set the `secret` attribute:

- provide the argument `SECRET` on the command line.**

**FLAGS**

: **--remove-cmek**

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
gcloud beta secrets replication update
```