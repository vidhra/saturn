# gcloud dns  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns](https://cloud.google.com/sdk/gcloud/reference/dns)*

**NAME**

: **gcloud dns - manage your Cloud DNS managed-zones and record-sets**

**SYNOPSIS**

: **`gcloud dns` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dns#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud dns command group lets you create and manage DNS zones and their
associated records on Google Cloud DNS.
Cloud DNS is a scalable, reliable and managed authoritative DNS service running
on the same infrastructure as Google. It has low latency, high availability and
is a cost-effective way to make your applications and services available to your
users.
More information on Cloud DNS can be found here: [https://cloud.google.com/dns](https://cloud.google.com/dns) and
detailed documentation can be found here: [https://cloud.google.com/dns/docs/](https://cloud.google.com/dns/docs/)

**EXAMPLES**

: To see how to create and maintain managed-zones, run:

```
gcloud dns managed-zones --help
```

To see how to maintain the record-sets within a managed-zone, run:

```
gcloud dns record-sets --help
```

To display Cloud DNS related information for your project, run:

```
gcloud dns project-info describe --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[dns-keys](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys)`**:
Manage Cloud DNS DNSKEY records.

**`[managed-zones](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones)`**:
Manage your Cloud DNS managed-zones.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/dns/operations)`**:
Manage your Cloud DNS operations.

**`[policies](https://cloud.google.com/sdk/gcloud/reference/dns/policies)`**:
Manage your Cloud DNS policies.

**`[project-info](https://cloud.google.com/sdk/gcloud/reference/dns/project-info)`**:
View Cloud DNS related information for a project.

**`[record-sets](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets)`**:
Manage the record-sets within your managed-zones.

**`[response-policies](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies)`**:
Manage your Cloud DNS response policy.

**NOTES**

: These variants are also available:

```
gcloud alpha dns
```

```
gcloud beta dns
```