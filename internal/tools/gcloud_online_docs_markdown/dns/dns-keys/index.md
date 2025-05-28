# gcloud dns dns-keys  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys)*

**NAME**

: **gcloud dns dns-keys - manage Cloud DNS DNSKEY records**

**SYNOPSIS**

: **`gcloud dns dns-keys` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The commands in this group manage Cloud DNS DNS key resources. A DNS key
resource represents a cryptographic signing key for use in DNSSEC; a DNSKEY
record contains a public key used for digitally signing zone data.
For more information, including instructions for managing and using DNS keys,
see the [documentation for
DNSSEC](https://cloud.google.com/dns/dnssec).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe)`**:
Show details about a DNS key resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/list)`**:
List DNS key resources.

**NOTES**

: These variants are also available:

```
gcloud alpha dns dns-keys
```

```
gcloud beta dns dns-keys
```