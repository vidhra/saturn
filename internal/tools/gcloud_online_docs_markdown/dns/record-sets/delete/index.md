# gcloud dns record-sets delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete)*

**NAME**

: **gcloud dns record-sets delete - delete a record-set in a managed-zone**

**SYNOPSIS**

: **`gcloud dns record-sets delete` `[DNS_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#DNS_NAME)` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#ZONE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes a record-set contained within the specified managed-zone.

**EXAMPLES**

: To delete a record-set with dnsName foo.bar.com. and record type A, rrdata run:

```
gcloud dns record-sets delete foo.bar.com. --type=A --zone=my_zone
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
gcloud alpha dns record-sets delete
```

```
gcloud beta dns record-sets delete
```