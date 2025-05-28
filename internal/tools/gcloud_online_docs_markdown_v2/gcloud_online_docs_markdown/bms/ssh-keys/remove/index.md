# gcloud bms ssh-keys remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/remove](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/remove)*

**NAME**

: **gcloud bms ssh-keys remove - remove an SSH key in Bare Metal Solution given its name**

**SYNOPSIS**

: **`gcloud bms ssh-keys remove` `[SSH_KEY](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/remove#SSH_KEY)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove an SSH key in Bare Metal Solution given its name.

**EXAMPLES**

: To remove an SSH key called ``my-ssh-key`` run:

```
gcloud bms ssh-keys remove my-ssh-key
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
gcloud alpha bms ssh-keys remove
```