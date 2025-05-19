# gcloud bms ssh-keys add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add)*

**NAME**

: **gcloud bms ssh-keys add - add a public SSH key to the project in Bare Metal Solution**

**SYNOPSIS**

: **`gcloud bms ssh-keys add` `[SSH_KEY](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add#SSH_KEY)` (`[--key](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add#--key)`=`KEY`     | `[--key-file](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add#--key-file)`=`KEY_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add a public SSH key to the project in Bare Metal Solution.

**EXAMPLES**

: To add an SSH key called ``my-ssh-key`` in
project ``my-project`` with a public key
``ABC6695``

```
gcloud bms ssh-keys add my-ssh-key --project=my-project --key=ABC6695
```

To add an SSH key called ``my-ssh-key`` in
project ``my-project`` with a public key stored
in /home/user/.ssh/id_rsa.pub

```
gcloud bms ssh-keys add my-ssh-key --project=my-project --key-file=/home/user/.ssh/id_rsa.pub
```

**POSITIONAL ARGUMENTS**

: **SSH key resource - ssh_key. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `ssh_key` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `ssh_key` on the command line with a fully
specified name;
- global is the only supported location.

This must be specified.

**`SSH_KEY`**:
ID of the SSH key or fully qualified identifier for the SSH key.
To set the `ssh_key` attribute:

- provide the argument `ssh_key` on the command line.**

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

: This variant is also available:

```
gcloud alpha bms ssh-keys add
```