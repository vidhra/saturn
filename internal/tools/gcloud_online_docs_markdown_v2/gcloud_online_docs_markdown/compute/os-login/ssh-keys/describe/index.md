# gcloud compute os-login ssh-keys describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe)*

**NAME**

: **gcloud compute os-login ssh-keys describe - describe an SSH Public Key from an OS Login Profile**

**SYNOPSIS**

: **`gcloud compute os-login ssh-keys describe` (`[--key](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe#--key)`=`KEY`     | `[--key-file](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe#--key-file)`=`KEY_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute os-login ssh-keys describe` accepts either a string
containing an SSH Public Key or a filename for an SSH Public key and displays
that key from the user's OS Login Profile. The key value used can either be the
full SSH key or the OS Login fingerprint for that key.

**EXAMPLES**

: To show all of the information for the key stored in your OS Login profile that
matches the key in `/home/user/.ssh/id_rsa.pub`, run:

```
gcloud compute os-login ssh-keys describe --key-file=/home/user/.ssh/id_rsa.pub
```

To show all of the information about the key with a fingerprint of
'e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52', run:

```
gcloud compute os-login ssh-keys describe --key='e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52'
```

**REQUIRED FLAGS**

: **--key**

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
gcloud alpha compute os-login ssh-keys describe
```

```
gcloud beta compute os-login ssh-keys describe
```