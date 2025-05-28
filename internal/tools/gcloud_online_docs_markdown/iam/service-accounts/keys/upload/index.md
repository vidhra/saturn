# gcloud iam service-accounts keys upload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload)*

**NAME**

: **gcloud iam service-accounts keys upload - upload a public key for an IAM service account**

**SYNOPSIS**

: **`gcloud iam service-accounts keys upload` `[PUBLIC_KEY_FILE](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload#PUBLIC_KEY_FILE)` `[--iam-account](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload#--iam-account)`=`IAM_ACCOUNT` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upload a public key for an IAM service account.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: The following command uploads a public key certificate to a service account:
```
gcloud iam service-accounts keys upload test_data/public_key.cert --iam-account=my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`PUBLIC_KEY_FILE`**:
Path of the file containing the public key. Note that only public key data in
the format of RSA_X509_PEM is supported. See [https://cloud.google.com/iot/docs/concepts/device-security#public_key_format](https://cloud.google.com/iot/docs/concepts/device-security#public_key_format)
for more information.

**REQUIRED FLAGS**

: **IamAccount resource - The service account for which to upload a key. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--iam-account` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--iam-account**:
ID of the iamAccount or fully qualified identifier for the iamAccount.
To set the `iam-account` attribute:

- provide the argument `--iam-account` on the command line.**

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts keys upload
```

```
gcloud beta iam service-accounts keys upload
```