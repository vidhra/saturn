# gcloud compute os-login ssh-keys update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update)*

**NAME**

: **gcloud compute os-login ssh-keys update - update an SSH public key in an OS Login profile**

**SYNOPSIS**

: **`gcloud compute os-login ssh-keys update` `[--ttl](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update#--ttl)`=`TTL` (`[--key](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update#--key)`=`KEY`     | `[--key-file](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update#--key-file)`=`KEY_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute os-login ssh-keys update` accepts either a string
containing an SSH public key or a filename for an SSH public key, and updates
the key in the user's OS Login profile. Currently, only the expiration time,
``--ttl``, can be updated.

**EXAMPLES**

: To update the SSH public key found in `/home/user/.ssh/id_rsa.pub`
with an expiration time of one week from now, run:

```
gcloud compute os-login ssh-keys update --ttl=7d --key-file=/home/user/.ssh/id_rsa.pub
```

To update the SSH public key with a fingerprint of
'e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52' and an
expiration time of five years from now, run:

```
gcloud compute os-login ssh-keys update --ttl=5y --key='e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52'
```

**REQUIRED FLAGS**

: **--ttl**:
The amount of time before the SSH key expires. For example, specifying
``30m`` will set the expiration time on the SSH
key for 30 minutes from the current time. A value of 0 will result in no
expiration time. See $ [gcloud
topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.

**--key**

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
gcloud alpha compute os-login ssh-keys update
```

```
gcloud beta compute os-login ssh-keys update
```