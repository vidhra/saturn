# gcloud dns managed-zones create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create)*

**NAME**

: **gcloud dns managed-zones create - create a Cloud DNS managed-zone**

**SYNOPSIS**

: **`gcloud dns managed-zones create` `[ZONE_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#ZONE_NAME)` `[--dns-name](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--dns-name)`=`DNS_NAME` [`[--denial-of-existence](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--denial-of-existence)`=`DENIAL_OF_EXISTENCE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--description)`=`DESCRIPTION`] [`[--dnssec-state](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--dnssec-state)`=`DNSSEC_STATE`] [`[--forwarding-targets](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--forwarding-targets)`=[`IP_ADDRESSES`,…]] [`[--gkeclusters](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--gkeclusters)`=[`GKECLUSTERS`,…]] [`[--ksk-algorithm](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--ksk-algorithm)`=`KSK_ALGORITHM`] [`[--ksk-key-length](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--ksk-key-length)`=`KSK_KEY_LENGTH`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--location)`=`LOCATION`] [`[--[no-]log-dns-queries](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--[no-]log-dns-queries)`] [`[--managed-reverse-lookup](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--managed-reverse-lookup)`] [`[--networks](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--networks)`=[`NETWORK`,…]] [`[--private-forwarding-targets](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--private-forwarding-targets)`=[`IP_ADDRESSES`,…]] [`[--service-directory-namespace](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--service-directory-namespace)`=`SERVICE_DIRECTORY_NAMESPACE`] [`[--visibility](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--visibility)`=`VISIBILITY`; default="public"] [`[--zsk-algorithm](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--zsk-algorithm)`=`ZSK_ALGORITHM`] [`[--zsk-key-length](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--zsk-key-length)`=`ZSK_KEY_LENGTH`] [`[--target-network](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--target-network)`=`TARGET_NETWORK` `[--target-project](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#--target-project)`=`TARGET_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a Cloud DNS managed-zone.

**EXAMPLES**

: To create a managed-zone, run:

```
gcloud dns managed-zones create my-zone --dns-name=my.zone.com. --description="My zone!"
```

To create a managed-zone with DNSSEC, run:

```
gcloud dns managed-zones create my-zone-2 --description="Signed Zone" --dns-name=myzone.example --dnssec-state=on
```

```
To create a zonal managed-zone scoped to a GKE Cluster in us-east1-a, run:
```

```
gcloud dns managed-zones create my-zonal-zone --description="Signed Zone" --dns-name=cluster.local --visibility=private --gkeclusters=cluster1 --location=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`ZONE_NAME`**:
The name of the managed-zone to be created.

**REQUIRED FLAGS**

: **--dns-name**:
The DNS name suffix that will be managed with the created zone.

**OPTIONAL FLAGS**

: **--denial-of-existence**:
Requires DNSSEC enabled. `DENIAL_OF_EXISTENCE` must be one
of: `nsec`, `nsec3`.

**--description**:
Short description for the managed zone.

**--dnssec-state**:
The DNSSEC state for this managed zone. `DNSSEC_STATE`
must be one of:

**`off`**:
Disable DNSSEC for the managed zone.

**`on`**:
Enable DNSSEC for the managed zone.

**`transfer`**:
Enable DNSSEC and allow transferring a signed zone in or out.

**--forwarding-targets**:
List of IPv4 addresses that the zone will forward queries to. Ignored for
`public` visibility. Non-RFC1918 addresses will forward to the target
through the Internet. RFC1918 addresses will forward through the VPC.

**--gkeclusters**:
List of GKE clusters that the zone should be visible in if the zone visibility
is [private].

**--ksk-algorithm**:
String mnemonic specifying the DNSSEC algorithm of the key-signing key. Requires
DNSSEC enabled. `KSK_ALGORITHM` must be one of:
`ecdsap256sha256`, `ecdsap384sha384`,
`rsasha1`, `rsasha256`, `rsasha512`.

**--ksk-key-length**:
Length of the key-signing key in bits. Requires DNSSEC enabled.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**--[no-]log-dns-queries**:
Specifies whether to enable query logging. Defaults to False. Use
`--log-dns-queries` to enable and `--no-log-dns-queries`
to disable.

**--managed-reverse-lookup**:
Specifies whether this zone is a managed reverse lookup zone, required for Cloud
DNS to correctly resolve Non-RFC1918 PTR records.

**--networks**:
List of networks that the zone should be visible in if the zone visibility is
[private].

**--private-forwarding-targets**:
List of IPv4 addresses that the zone will forward queries to. Ignored for
`public` visibility. All addresses specified for this parameter will
be reached through the VPC.

**--service-directory-namespace**:
The fully qualified URL of the service directory namespace that should be
associated with the zone. Ignored for `public` visibility zones.

**--visibility**:
Visibility of the zone. Public zones are visible to the public internet. Private
zones are only visible in your internal networks denoted by the
`--networks` flag. `VISIBILITY` must be one of:
`public`, `private`.

**--zsk-algorithm**:
String mnemonic specifying the DNSSEC algorithm of the key-signing key. Requires
DNSSEC enabled. `ZSK_ALGORITHM` must be one of:
`ecdsap256sha256`, `ecdsap384sha384`,
`rsasha1`, `rsasha256`, `rsasha512`.

**--zsk-key-length**:
Length of the zone-signing key in bits. Requires DNSSEC enabled.

**--target-network**:
Network ID of the Google Compute Engine private network to forward queries to.

**--target-project**:
Project ID of the Google Compute Engine private network to forward queries to.

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
gcloud alpha dns managed-zones create
```

```
gcloud beta dns managed-zones create
```