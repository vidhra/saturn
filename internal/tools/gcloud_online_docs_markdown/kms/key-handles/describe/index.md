# gcloud kms key-handles describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/describe](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/describe)*

**NAME**

: **gcloud kms key-handles describe - get metadata for a KeyHandle**

**SYNOPSIS**

: **`gcloud kms key-handles describe` (`[KEY_HANDLE](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/describe#KEY_HANDLE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get metadata for a KeyHandle.

**EXAMPLES**

: The following command gets metadata for a KeyHandle named
`my-key-handle` in the locations `us-central1`.

```
gcloud kms key-handles describe my-key-handle --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Key handle resource - The KeyHandle to get metadata for. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key_handle` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KEY_HANDLE`**:
ID of the key handle or fully qualified identifier for the key handle.
To set the `key_handle` attribute:

- provide the argument `key_handle` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the resource.
To set the `location` attribute:

- provide the argument `key_handle` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `cloudkms/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/kms/](https://cloud.google.com/kms/)

**NOTES**

: These variants are also available:

```
gcloud alpha kms key-handles describe
```

```
gcloud beta kms key-handles describe
```