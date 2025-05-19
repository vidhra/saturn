# gcloud alpha compute addresses  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses)*

**NAME**

: **gcloud alpha compute addresses - read and manipulate Compute Engine addresses**

**SYNOPSIS**

: **`gcloud alpha compute addresses` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate Compute Engine addresses.
For more information about addresses, see the [addresses
documentation](https://cloud.google.com/compute/docs/ip-addresses/).
See also: [Addresses
API](https://cloud.google.com/compute/docs/reference/rest/v1/addresses).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/config)`**:
`(ALPHA)` Manage Compute Engine address configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/create)`**:
`(ALPHA)` Reserve IP addresses.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete)`**:
`(ALPHA)` Release reserved IP addresses.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/describe)`**:
`(ALPHA)` Display detailed information about a reserved static
address.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/list)`**:
`(ALPHA)` List addresses.

**`[move](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/move)`**:
`(ALPHA)` Move an address to another project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update)`**:
`(ALPHA)` Update a Compute Engine address.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute addresses
```

```
gcloud beta compute addresses
```