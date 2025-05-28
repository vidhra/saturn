# gcloud dns managed-zones update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update)*

**NAME**

: **gcloud dns managed-zones update - update an existing Cloud DNS managed-zone**

**SYNOPSIS**

: **`gcloud dns managed-zones update` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#ZONE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--async)`] [`[--denial-of-existence](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--denial-of-existence)`=`DENIAL_OF_EXISTENCE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--description)`=`DESCRIPTION`] [`[--dnssec-state](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--dnssec-state)`=`DNSSEC_STATE`] [`[--forwarding-targets](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--forwarding-targets)`=[`IP_ADDRESSES`,…]] [`[--gkeclusters](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--gkeclusters)`=[`GKECLUSTERS`,…]] [`[--ksk-algorithm](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--ksk-algorithm)`=`KSK_ALGORITHM`] [`[--ksk-key-length](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--ksk-key-length)`=`KSK_KEY_LENGTH`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--location)`=`LOCATION`] [`[--[no-]log-dns-queries](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--[no-]log-dns-queries)`] [`[--managed-reverse-lookup](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--managed-reverse-lookup)`] [`[--networks](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--networks)`=[`NETWORK`,…]] [`[--private-forwarding-targets](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--private-forwarding-targets)`=[`IP_ADDRESSES`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--zsk-algorithm](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--zsk-algorithm)`=`ZSK_ALGORITHM`] [`[--zsk-key-length](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--zsk-key-length)`=`ZSK_KEY_LENGTH`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--remove-labels)`=[`KEY`,…]] [`[--target-network](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--target-network)`=`TARGET_NETWORK` `[--target-project](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#--target-project)`=`TARGET_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing Cloud DNS managed-zone.

**EXAMPLES**

: To change the description of a managed-zone, run:

```
gcloud dns managed-zones update my-zone --description="Hello, world!"
```

To change the description of a zonal managed-zone in us-east1-a, run:

```
gcloud dns managed-zones update my-zone --description="Hello, world!" --location=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **Zone resource - The name of the managed-zone to be updated. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zone or fully qualified identifier for the zone.
To set the `zone` attribute:

- provide the argument `zone` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--denial-of-existence**:
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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--zsk-algorithm**:
String mnemonic specifying the DNSSEC algorithm of the key-signing key. Requires
DNSSEC enabled. `ZSK_ALGORITHM` must be one of:
`ecdsap256sha256`, `ecdsap384sha384`,
`rsasha1`, `rsasha256`, `rsasha512`.

**--zsk-key-length**:
Length of the zone-signing key in bits. Requires DNSSEC enabled.

**--clear-labels**

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
gcloud alpha dns managed-zones update
```

```
gcloud beta dns managed-zones update
```