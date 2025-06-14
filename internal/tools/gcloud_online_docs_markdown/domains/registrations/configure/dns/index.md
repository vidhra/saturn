# gcloud domains registrations configure dns  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns)*

**NAME**

: **gcloud domains registrations configure dns - configure DNS settings of a Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations configure dns` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#REGISTRATION)` [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--validate-only)`] [`[--cloud-dns-zone](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--cloud-dns-zone)`=`CLOUD_DNS_ZONE`     | `[--dns-settings-from-file](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--dns-settings-from-file)`=`DNS_SETTINGS_FILE_NAME`     | `[--name-servers](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--name-servers)`=`NAME_SERVER`,…,[…]     | `[--use-google-domains-dns](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--use-google-domains-dns)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--async)`] [`[--disable-dnssec](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--disable-dnssec)`] [`[--unsafe-dns-update](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#--unsafe-dns-update)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Configure DNS settings of a Cloud Domains registration.
In most cases, this command is used for changing the authoritative name servers
and DNSSEC options for the given domain. However, advanced options like glue
records are available.

**EXAMPLES**

: To start an interactive flow to configure DNS settings for
``example.com``, run:

```
gcloud domains registrations configure dns example.com
```

To use Cloud DNS managed-zone ``example-zone``
for ``example.com``, run:

```
gcloud domains registrations configure dns example.com --cloud-dns-zone=example-zone
```

DNSSEC will not be enabled as it may not be safe to enable it (e.g. when the
Cloud DNS managed-zone was signed less than 24h ago).
To use a signed Cloud DNS managed-zone
``example-zone`` for
``example.com`` and enable DNSSEC, run:

```
gcloud domains registrations configure dns example.com --cloud-dns-zone=example-zone --no-disable-dnssec
```

To change DNS settings for ``example.com``
according to information from a YAML file
``dns_settings.yaml``, run:

```
gcloud domains registrations configure dns example.com --dns-settings-from-file=dns_settings.yaml
```

To disable DNSSEC, run:

```
gcloud domains registrations configure dns example.com --disable-dnssec
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to configure DNS settings for.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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

**COMMONLY USED FLAGS**

: **--validate-only**:
Don't actually configure DNS settings of the registration. Only validate
arguments.

**Set the authoritative name servers for the given domain.

```
Warning: Do not change name servers if ds_records is non-empty.
Clear ds_records first by calling this command with the
--disable-dnssec flag, and wait 24 hours before changing
name servers. Otherwise your domain may stop serving.
```**

At most one of these can be specified:

**--cloud-dns-zone**:
The name of the Cloud DNS managed-zone to set as the name server for the domain.
If it's in the same project, you can use short name. If not, use the full
resource name, e.g.:
--cloud-dns-zone=projects/example-project/managedZones/example-zone.

**--dns-settings-from-file**:
A YAML file containing the required DNS settings. If specified, its content will
replace the values currently used in the registration resource. If the file is
missing some of the dns_settings fields, those fields will be cleared.
Examples of file contents:

```
googleDomainsDns:
  dsState: DS_RECORDS_PUBLISHED
glueRecords:
- hostName: ns1.example.com
  ipv4Addresses:
  - 8.8.8.8
- hostName: ns2.example.com
  ipv4Addresses:
  - 8.8.8.8
```

```
customDns:
  nameServers:
  - new.ns1.com
  - new.ns2.com
  dsRecords:
  - keyTag: 24
    algorithm: RSASHA1
    digestType: SHA256
    digest: 2e1cfa82b035c26cbbbdae632cea070514eb8b773f616aaeaf668e2f0be8f10d
  - keyTag: 42
    algorithm: RSASHA1
    digestType: SHA256
    digest: 2e1cfa82bf35c26cbbbdae632cea070514eb8b773f616aaeaf668e2f0be8f10d
```

**--name-servers**:
List of DNS name servers for the domain.

**--use-google-domains-dns**:
(DEPRECATED) Use free name servers provided by Google Domains.
The --use-google-domains-dns option is deprecated; See [https://cloud.google.com/domains/docs/deprecations/feature-deprecations](https://cloud.google.com/domains/docs/deprecations/feature-deprecations).

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--disable-dnssec**:
Use this flag to disable DNSSEC, or to skip enabling it when switching to a
Cloud DNS Zone or Google Domains nameservers.

**--unsafe-dns-update**:
(DEPRECATED) Use this flag to allow DNS changes that may make your domain stop
serving.
The --unsafe-dns-update option is deprecated. To complete an unsafe DNS
operation first disable DNSSEC, then change name servers, then (optionally)
enable DNSSEC.

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
gcloud alpha domains registrations configure dns
```

```
gcloud beta domains registrations configure dns
```