# gcloud dns record-sets changes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes)*

**NAME**

: **gcloud dns record-sets changes - view details about changes to your Cloud DNS record-sets**

**SYNOPSIS**

: **`gcloud dns record-sets changes` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: View details about changes to your Cloud DNS record-sets.

**EXAMPLES**

: To view the details of a particular change, run:

```
gcloud dns record-sets changes describe CHANGE_ID --zone=MANAGED_ZONE
```

To view the list of all changes, run:

```
gcloud dns record-sets changes list --zone=MANAGED_ZONE
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/describe)`**:
View the details of a change.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/list)`**:
View the list of changes that have been made to your record-sets.

**NOTES**

: These variants are also available:

```
gcloud alpha dns record-sets changes
```

```
gcloud beta dns record-sets changes
```