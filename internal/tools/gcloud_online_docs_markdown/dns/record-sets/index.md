# gcloud dns record-sets  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets)*

**NAME**

: **gcloud dns record-sets - manage the record-sets within your managed-zones**

**SYNOPSIS**

: **`gcloud dns record-sets` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage the record-sets within your managed-zones.

**EXAMPLES**

: To import record-sets from a BIND zone file, run:

```
gcloud dns record-sets import --zone=MANAGED_ZONE --zone-file-format ZONE_FILE
```

To export record-sets in yaml format, run:

```
gcloud dns record-sets export --zone=MANAGED_ZONE
```

To see how to make scriptable changes to your record-sets through transactions,
run:

```
gcloud dns record-sets transaction --help
```

To list all changes, run:

```
gcloud dns record-sets changes list --zone=MANAGED_ZONE
```

To see change details, run:

```
gcloud dns record-sets changes describe CHANGE_ID --zone=MANAGED_ZONE
```

To see the list of all record-sets, run:

```
gcloud dns record-sets list --zone=MANAGED_ZONE
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[changes](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes)`**:
View details about changes to your Cloud DNS record-sets.

**`[transaction](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction)`**:
Make scriptable and transactional changes to your record-sets.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create)`**:
Creates a record-set in a managed-zone.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete)`**:
Delete a record-set in a managed-zone.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe)`**:
Describe a record-set in a managed-zone.

**`[export](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export)`**:
Export your record-sets into a file.

**`[import](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import)`**:
Import record-sets into your managed-zone.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/list)`**:
View the list of record-sets in a managed-zone.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update)`**:
Updates a record-set in a managed-zone.

**NOTES**

: These variants are also available:

```
gcloud alpha dns record-sets
```

```
gcloud beta dns record-sets
```