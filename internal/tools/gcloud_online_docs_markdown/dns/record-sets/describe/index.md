# gcloud dns record-sets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe)*

**NAME**

: **gcloud dns record-sets describe - describe a record-set in a managed-zone**

**SYNOPSIS**

: **`gcloud dns record-sets describe` `[DNS_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#DNS_NAME)` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#ZONE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command describes a record-set contained within the specified managed-zone.

**EXAMPLES**

: To describe a record-set with dnsName foo.bar.com. and record type A, rrdata
run:

```
gcloud dns record-sets describe foo.bar.com. --type=A --zone=my_zone
```

**POSITIONAL ARGUMENTS**

: **`DNS_NAME`**:
DNS or domain name of the record-set.

**REQUIRED FLAGS**

: **--type**:
DNS record type of the record-set (e.g. A, AAAA, MX etc.).

**--zone**:
Name of the managed zone whose record sets you want to manage.

**OPTIONAL FLAGS**

: **--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

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
gcloud alpha dns record-sets describe
```

```
gcloud beta dns record-sets describe
```