# gcloud domains registrations google-domains-dns export-dns-record-sets  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets)*

**NAME**

: **gcloud domains registrations google-domains-dns export-dns-record-sets - export your registration's Google Domains DNS zone's record-sets into a file**

**SYNOPSIS**

: **`gcloud domains registrations google-domains-dns export-dns-record-sets` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets#REGISTRATION)` `[--records-file](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets#--records-file)`=`RECORDS_FILE` [`[--zone-file-format](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets#--zone-file-format)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/export-dns-record-sets#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export your registration's Google Domains DNS (deprecated) zone's record-sets
into a file. The formats you can export to are YAML records format (default) and
BIND zone file format.

**EXAMPLES**

: To export DNS record-sets of ``example.com``
into a YAML file, run:

```
gcloud domains registrations google-domains-dns export-dns-record-sets example.com --records-file=records.yaml
```

To export DNS record-sets of ``example.com``
into a BIND zone formatted file, run:

```
gcloud domains registrations google-domains-dns export-dns-record-sets example.com --records-file=records.zonefile --zone-file-format
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to get the DNS records for. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- location is always global.

This must be specified.

**`REGISTRATION`**:
ID of the registration or fully qualified identifier for the registration.
To set the `registration` attribute:

- provide the argument `registration` on the command line.**

**REQUIRED FLAGS**

: **--records-file**:
File to which record-sets should be exported.

**OPTIONAL FLAGS**

: **--zone-file-format**:
Indicates that records-file should be in the zone file format. When using this
flag, expect the record-set to be exported to a BIND zone formatted file. If you
omit this flag, the record-set is exported into a YAML formatted records file.
Note, this format flag determines the format of the output recorded in the
records-file; it is different from the global `--format` flag which
affects console output alone.

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
gcloud alpha domains registrations google-domains-dns export-dns-record-sets
```

```
gcloud beta domains registrations google-domains-dns export-dns-record-sets
```