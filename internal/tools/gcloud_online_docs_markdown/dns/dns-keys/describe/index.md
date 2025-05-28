# gcloud dns dns-keys describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe)*

**NAME**

: **gcloud dns dns-keys describe - show details about a DNS key resource**

**SYNOPSIS**

: **`gcloud dns dns-keys describe` `KEY-ID` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/dns-keys/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the details of a single DNS key resource.

**EXAMPLES**

: To show details about a DNS key resource with ID 3 in a managed zone
`my_zone`, run:

```
gcloud dns dns-keys describe --zone=my_zone 3
```

To get the DS record corresponding for the DNSKEY record from the previous
example, run (the DNSKEY record must be for a key-signing key):

```
gcloud dns dns-keys describe --zone=my_zone 3 --format='value(ds_record())'
```

**POSITIONAL ARGUMENTS**

: **`KEY-ID`**:
The DNS key identifier.

**REQUIRED FLAGS**

: **--zone**:
The name of the managed-zone the DNSKEY record belongs to

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

: These variants are also available:

```
gcloud alpha dns dns-keys describe
```

```
gcloud beta dns dns-keys describe
```