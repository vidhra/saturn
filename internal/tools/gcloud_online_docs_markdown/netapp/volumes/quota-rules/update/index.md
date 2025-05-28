# gcloud netapp volumes quota-rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update)*

**NAME**

: **gcloud netapp volumes quota-rules update - update a Cloud NetApp Volume QuotaRule**

**SYNOPSIS**

: **`gcloud netapp volumes quota-rules update` (`[QUOTA_RULE](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#QUOTA_RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--description)`=`DESCRIPTION`] [`[--disk-limit-mib](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--disk-limit-mib)`=`DISK_LIMIT_MIB`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--volume)`=`VOLUME`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud NetApp Volume QuotaRule and its specified parameters.

**EXAMPLES**

: The following command updates a QuotaRule named NAME and its specified
parameters:

```
gcloud netapp volumes quota-rules update NAME --location=us-central1 --description="new" --disk-limit-mib=100 --update-labels=key2=val2 --volume=vol1
```

**POSITIONAL ARGUMENTS**

: **Quota rule resource - The Quota rule to update. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `volume` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--volume` on the command line.

This must be specified.

**`QUOTA_RULE`**:
ID of the quota_rule or fully qualified identifier for the quota_rule.
To set the `quota_rule` attribute:

- provide the argument `quota_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the quota_rule.
To set the `location` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud NetApp Quota rule

**--disk-limit-mib**:
The disk limit in MiB for the quota rule.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Volume resource - The volume for which quota rule applies. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.**

**--clear-labels**

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
gcloud beta netapp volumes quota-rules update
```