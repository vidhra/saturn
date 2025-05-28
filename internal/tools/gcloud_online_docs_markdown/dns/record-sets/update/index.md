# gcloud dns record-sets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update)*

**NAME**

: **gcloud dns record-sets update - updates a record-set in a managed-zone**

**SYNOPSIS**

: **`gcloud dns record-sets update` `[DNS_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#DNS_NAME)` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#ZONE)` (`[--rrdatas](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--rrdatas)`=[`RRDATA`,…]     | [`[--routing-policy-type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-type)`=`ROUTING_POLICY_TYPE` (`[--routing-policy-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-data)`=`ROUTING_POLICY_DATA` | `[--routing-policy-item](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-item)`=[`ROUTING_POLICY_ITEM`,…] | [`[--routing-policy-backup-data-type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-backup-data-type)`=`ROUTING_POLICY_BACKUP_DATA_TYPE` `[--routing-policy-primary-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-primary-data)`=`ROUTING_POLICY_PRIMARY_DATA` (`[--routing-policy-backup-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-backup-data)`=`ROUTING_POLICY_BACKUP_DATA` | `[--routing-policy-backup-item](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--routing-policy-backup-item)`=[`ROUTING_POLICY_BACKUP_ITEM`,…]) : `[--backup-data-trickle-ratio](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--backup-data-trickle-ratio)`=`BACKUP_DATA_TRICKLE_RATIO`]) : `[--enable-geo-fencing](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--enable-geo-fencing)` `[--enable-health-checking](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--enable-health-checking)` | `[--health-check](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--health-check)`=`HEALTH_CHECK`]) [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--location)`=`LOCATION`] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#--ttl)`=`TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates a record-set contained within the specified managed-zone.

**EXAMPLES**

: To update a record-set with dnsName foo.bar.com., record type A to have rrdata
[1.2.3.4, 9.8.7.6] and ttl 60 in my_zone, run:

```
gcloud dns record-sets update foo.bar.com. --rrdatas=1.2.3.4,9.8.7.6 --type=A --ttl=60 --zone=my_zone
```

To update a record-set with dnsName foo.bar.com., record type A to have rrdata
[1.2.3.4, 9.8.7.6] and ttl 60 in my_zone that is located in us-east1-a, run:

```
gcloud dns record-sets update foo.bar.com. --rrdatas=1.2.3.4,9.8.7.6 --type=A --ttl=60 --zone=my_zone --location=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`DNS_NAME`**:
DNS or domain name of the record-set.

**REQUIRED FLAGS**

: **--type**:
DNS record type of the record-set (e.g. A, AAAA, MX etc.).

**--zone**:
Name of the managed zone whose record sets you want to manage.

**--rrdatas**

**OPTIONAL FLAGS**

: **--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**--ttl**:
TTL (time to live) for the record-set.

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
gcloud alpha dns record-sets update
```

```
gcloud beta dns record-sets update
```