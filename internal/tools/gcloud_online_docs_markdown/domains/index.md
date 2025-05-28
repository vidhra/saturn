# gcloud domains  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains](https://cloud.google.com/sdk/gcloud/reference/domains)*

**NAME**

: **gcloud domains - manage domains for your Google Cloud projects**

**SYNOPSIS**

: **`gcloud domains` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/domains#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/domains#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud domains command group lets you view and manage your custom domains
for use across Google projects.

**EXAMPLES**

: To verify a domain you own, run:

```
gcloud domains verify example.com
```

To list your verified domains, run:

```
gcloud domains list-user-verified
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[registrations](https://cloud.google.com/sdk/gcloud/reference/domains/registrations)`**:
Manage Cloud Domains registrations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list-user-verified](https://cloud.google.com/sdk/gcloud/reference/domains/list-user-verified)`**:
Lists the user's verified domains.

**`[verify](https://cloud.google.com/sdk/gcloud/reference/domains/verify)`**:
Verifies a domain via an in-browser workflow.

**NOTES**

: These variants are also available:

```
gcloud alpha domains
```

```
gcloud beta domains
```