# gcloud dns record-sets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create)*

**NAME**

: **gcloud dns record-sets create - creates a record-set in a managed-zone**

**SYNOPSIS**

: **`gcloud dns record-sets create` `[DNS_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#DNS_NAME)` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#ZONE)` (`[--rrdatas](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--rrdatas)`=[`RRDATA`,…]     | [`[--routing-policy-type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-type)`=`ROUTING_POLICY_TYPE` (`[--routing-policy-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-data)`=`ROUTING_POLICY_DATA` | `[--routing-policy-item](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-item)`=[`ROUTING_POLICY_ITEM`,…] | [`[--routing-policy-backup-data-type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-backup-data-type)`=`ROUTING_POLICY_BACKUP_DATA_TYPE` `[--routing-policy-primary-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-primary-data)`=`ROUTING_POLICY_PRIMARY_DATA` (`[--routing-policy-backup-data](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-backup-data)`=`ROUTING_POLICY_BACKUP_DATA` | `[--routing-policy-backup-item](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--routing-policy-backup-item)`=[`ROUTING_POLICY_BACKUP_ITEM`,…]) : `[--backup-data-trickle-ratio](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--backup-data-trickle-ratio)`=`BACKUP_DATA_TRICKLE_RATIO`]) : `[--enable-geo-fencing](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--enable-geo-fencing)` `[--enable-health-checking](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--enable-health-checking)` | `[--health-check](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--health-check)`=`HEALTH_CHECK`]) [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--location)`=`LOCATION`] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#--ttl)`=`TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a record-set contained within the specified managed-zone.

**EXAMPLES**

: To create a record-set with dnsName foo.bar.com., record type A, rrdata
[1.2.3.4, 9.8.7.6] and ttl 60 in my_zone run this:

```
gcloud dns record-sets create foo.bar.com. --rrdatas=1.2.3.4,9.8.7.6 --type=A --ttl=60 --zone=my_zone
```

To create a geo routed record-set with dnsName foo.bar.com., record type A,
routing_policy_data "us-centra1=1.2.3.4,2.3.4.5;us-west1=3.4.5.6,9.8.7.6" and
ttl 60 in my_zone.

```
gcloud dns record-sets create foo.bar.com. --routing_policy_data="us-centra1=1.2.3.4,2.3.4.5;us-west1=3.4.5.6,9.8.7.6" --routing_policy_type=GEO --type=A --ttl=60 --zone=my_zone --location=us-east1-a
```

To create a record-set with dnsName foo.bar.com., record type A, rrdata
[1.2.3.4, 9.8.7.6] and ttl 60 in my_zone in us-east1-a run this:

```
gcloud dns record-sets create us-east1-a.bar.com. --rrdatas=1.2.3.4,9.8.7.6 --type=A --ttl=60 --zone=my_zone --location=us-east1-a
```

To create a failover type health checked routed record-set with dnsName
foo.bar.com., record type A, primary routing data "config1", backup routing data
"us-centra1=1.2.3.4,2.3.4.5;us-west1=3.4.5.6,9.8.7.6", with a trickle traffic
ratio of 10% to the backup data, and ttl 60 in my_zone.

```
gcloud dns record-sets create foo.bar.com. --type=A --ttl=60 --zone=routing-policy-test --routing_policy_type=FAILOVER --routing-policy-primary-data='config1' --routing-policy-backup-data-type=GEO --routing-policy-backup-data='us-centra1=1.2.3.4,2.3.4.5;us-west1=3.4.5.6,9.8.7.6' --backup-data-trickle-ratio=0.1 --enable-health-checking --zone=my_zone
```

To create a geo fenced health checked routed record-set with dnsName
foo.bar.com., record type A, routing-policy-data
"us-centra1=config1,config2;us-west1=3.4.5.6,9.8.7.6", and ttl 60 in my_zone.

```
gcloud dns record-sets create foo.bar.com. --type=A --ttl=60 --zone=routing-policy-test --routing_policy_type=GEO --routing_policy_data='us-centra1=config1,config2;us-west1=3.4.5.6,9.8.7.6' --enable-health-checking --enable-geo-fencing --zone=my_zone
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
gcloud alpha dns record-sets create
```

```
gcloud beta dns record-sets create
```