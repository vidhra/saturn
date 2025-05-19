# gcloud alpha access-context-manager levels  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels)*

**NAME**

: **gcloud alpha access-context-manager levels - manage Access Context Manager levels**

**SYNOPSIS**

: **`gcloud alpha access-context-manager levels` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` An access level is a classification of requests based on
raw attributes of that request (e.g. IP address, device identity, time of day,
etc.).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[conditions](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions)`**:
`(ALPHA)` Manage Access Context Manager level conditions.

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/config)`**:
`(ALPHA)` Manage Access Context Manager access level configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/create)`**:
`(ALPHA)` Create a new access level.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/delete)`**:
`(ALPHA)` Delete an access level.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/describe)`**:
`(ALPHA)` Show details about an access level.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/list)`**:
`(ALPHA)` List access levels.

**`[replace-all](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/replace-all)`**:
`(ALPHA)` Replace all existing access levels.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/update)`**:
`(ALPHA)`

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager levels
```

```
gcloud beta access-context-manager levels
```