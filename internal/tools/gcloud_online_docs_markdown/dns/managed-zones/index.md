# gcloud dns managed-zones  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones)*

**NAME**

: **gcloud dns managed-zones - manage your Cloud DNS managed-zones**

**SYNOPSIS**

: **`gcloud dns managed-zones` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage your Cloud DNS managed-zones. See [Managing Zones](https://cloud.google.com/dns/zones/) for details.

**EXAMPLES**

: To create a managed-zone, run:

```
gcloud dns managed-zones create my-zone --description="My Zone" --dns-name="my.zone.com."
```

To delete a managed-zone, run:

```
gcloud dns managed-zones delete my-zone
```

To view the details of a managed-zone, run:

```
gcloud dns managed-zones describe my-zone
```

To see the list of all managed-zones, run:

```
gcloud dns managed-zones list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create)`**:
Create a Cloud DNS managed-zone.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete)`**:
Delete an empty Cloud DNS managed-zone.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe)`**:
View the details of a Cloud DNS managed-zone.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/get-iam-policy)`**:
Get the IAM policy for a Cloud DNS managed-zone.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list)`**:
View the list of all your managed-zones.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy)`**:
Set the IAM policy for a Cloud DNS managed-zone.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update)`**:
Update an existing Cloud DNS managed-zone.

**NOTES**

: These variants are also available:

```
gcloud alpha dns managed-zones
```

```
gcloud beta dns managed-zones
```