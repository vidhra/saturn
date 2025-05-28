# gcloud alpha access-context-manager levels conditions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions)*

**NAME**

: **gcloud alpha access-context-manager levels conditions - manage Access Context Manager level conditions**

**SYNOPSIS**

: **`gcloud alpha access-context-manager levels conditions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` An access level is a classification of requests based on
raw attributes of that request (e.g. IP address, device identity, time of day,
etc.). These individual attributes are called conditions.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/conditions/list)`**:
`(ALPHA)` List conditions for an access level.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager levels conditions
```

```
gcloud beta access-context-manager levels conditions
```