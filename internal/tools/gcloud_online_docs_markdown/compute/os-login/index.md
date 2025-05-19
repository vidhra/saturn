# gcloud compute os-login  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-login](https://cloud.google.com/sdk/gcloud/reference/compute/os-login)*

**NAME**

: **gcloud compute os-login - create and manipulate Compute Engine OS Login resources**

**SYNOPSIS**

: **`gcloud compute os-login` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/os-login#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/os-login#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-login#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud oslogin command group lets you manage your OS Login profile.
OS Login profiles can be used to store information such as Posix account
information and SSH keys used for cloud products such as Compute Engine.
For more information about OS Login, see the [OS Login documentation](https://cloud.google.com/compute/docs/oslogin).
See also: [OS Login
API](https://cloud.google.com/compute/docs/oslogin/rest/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[ssh-keys](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys)`**:
List, add, update, and remove OS Login SSH Keys.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe-profile](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile)`**:
Describe the OS Login profile for the current user.

**`[remove-profile](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/remove-profile)`**:
Remove the posix account information for the current user.

**NOTES**

: These variants are also available:

```
gcloud alpha compute os-login
```

```
gcloud beta compute os-login
```