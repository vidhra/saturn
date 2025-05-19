# gcloud alpha compute firewall-policies rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create)*

**NAME**

: **gcloud alpha compute firewall-policies rules create - creates a Compute Engine firewall policy rule**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies rules create` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#PRIORITY)` `[--action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--action)`=`ACTION` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--firewall-policy)`=`FIREWALL_POLICY` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--description)`=`DESCRIPTION`] [`[--dest-address-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-address-groups)`=[`DEST_ADDRESS_GROUPS`,…]] [`[--dest-fqdns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-fqdns)`=[`DEST_FQDNS`,…]] [`[--dest-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-ip-ranges)`=[`DEST_IP_RANGE`,…]] [`[--dest-network-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-network-type)`=`DEST_NETWORK_TYPE`] [`[--dest-region-codes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-region-codes)`=[`DEST_REGION_CODES`,…]] [`[--dest-threat-intelligence](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--dest-threat-intelligence)`=[`DEST_THREAT_INTELLIGENCE_LISTS`,…]] [`[--direction](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--direction)`=`DIRECTION`] [`[--[no-]disabled](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--[no-]disabled)`] [`[--[no-]enable-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--[no-]enable-logging)`] [`[--layer4-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--layer4-configs)`=[`LAYER4_CONFIG`,…]] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--organization)`=`ORGANIZATION`] [`[--security-profile-group](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--security-profile-group)`=`SECURITY_PROFILE_GROUP`] [`[--src-address-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-address-groups)`=[`SOURCE_ADDRESS_GROUPS`,…]] [`[--src-fqdns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-fqdns)`=[`SOURCE_FQDNS`,…]] [`[--src-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-ip-ranges)`=[`SRC_IP_RANGE`,…]] [`[--src-network-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-network-type)`=`SRC_NETWORK_TYPE`] [`[--src-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-networks)`=[`SRC_NETWORKS`,…]] [`[--src-region-codes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-region-codes)`=[`SOURCE_REGION_CODES`,…]] [`[--src-secure-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-secure-tags)`=[`SOURCE_SECURE_TAGS`,…]] [`[--src-threat-intelligence](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--src-threat-intelligence)`=[`SOURCE_THREAT_INTELLIGENCE_LISTS`,…]] [`[--target-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--target-resources)`=[`TARGET_RESOURCES`,…]] [`[--target-secure-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--target-secure-tags)`=[`TARGET_SECURE_TAGS`,…]] [`[--target-service-accounts](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--target-service-accounts)`=[`TARGET_SERVICE_ACCOUNTS`,…]] [`[--[no-]tls-inspect](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#--[no-]tls-inspect)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-policies rules
create` is used to create organization firewall policy rules.

**EXAMPLES**

: To create a rule with priority ``10" in an organization firewall policy with ID
``123456789", run:

```
gcloud alpha compute firewall-policies rules create 10 --firewall-policy=123456789 --action=allow --description=example-rule
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the firewall policy rule to create.

**REQUIRED FLAGS**

: **--action**:
Action to take if the request matches the match condition.
`ACTION` must be one of: `allow`,
`deny`, `goto_next`,
`apply_security_profile_group`.

**--firewall-policy**:
Short name of the firewall policy into which the rule should be inserted.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the rule.

**--dest-address-groups**:
Destination address groups to match for this rule. Can only be specified if
DIRECTION is egress.

**--dest-fqdns**:
Destination FQDNs to match for this rule. Can only be specified if DIRECTION is
`egress`.

**--dest-ip-ranges**:
Destination IP ranges to match for this rule.

**--dest-network-type**:
Use this flag to indicate that the rule should match internet or non-internet
traffic. It applies to destination traffic for egress rules. Valid values are
INTERNET and NON_INTERNET. Use empty string to clear the field.

**--dest-region-codes**:
Destination Region Code to match for this rule. Can only be specified if
DIRECTION is `egress`. Cannot be specified when the source network
type is NON_INTERNET.

**--dest-threat-intelligence**:
Destination Threat Intelligence lists to match for this rule. Can only be
specified if DIRECTION is `egress`. Cannot be specified when source
network type is NON_INTERNET. The available lists can be found here: [https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy](https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy).

**--direction**:
Direction of the traffic the rule is applied. The default is to apply on
incoming traffic. `DIRECTION` must be one of:
`INGRESS`, `EGRESS`.

**--[no-]disabled**:
Use this flag to disable the rule. Disabled rules will not affect traffic. Use
`--disabled` to enable and `--no-disabled` to disable.

**--[no-]enable-logging**:
Use this flag to enable logging of connections that allowed or denied by this
rule. Use `--enable-logging` to enable and
`--no-enable-logging` to disable.

**--layer4-configs**:
A list of destination protocols and ports to which the firewall rule will apply.

**--organization**:
Organization which the organization firewall policy belongs to. Must be set if
FIREWALL_POLICY is short name.

**--security-profile-group**:
An org-based security profile group to be used with apply_security_profile_group
action. Allowed formats are: a)
http(s)://<namespace>/<api>/organizations/<org_id>/locations/global/securityProfileGroups/<profile>
b)
(//)<namespace>/organizations/<org_id>/locations/global/securityProfileGroups/<profile>
c) <profile>. In case "c" `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI will create a reference
matching format "a", but to make it work
CLOUDSDK_API_ENDPOINT_OVERRIDES_NETWORKSECURITY property must be set. In order
to set this property, please run the command `gcloud config set
api_endpoint_overrides/networksecurity https://<namespace>/`.

**--src-address-groups**:
Source address groups to match for this rule. Can only be specified if DIRECTION
is ingress.

**--src-fqdns**:
Source FQDNs to match for this rule. Can only be specified if DIRECTION is
`ingress`.

**--src-ip-ranges**:
Source IP ranges to match for this rule.

**--src-network-type**:
Use this flag to indicate that the rule should match internet, non-internet
traffic or traffic coming from the network specified by --src-network. It
applies to ingress rules. Valid values are INTERNET, NON_INTERNET, VPC_NETWORKS
and INTRA_VPC. Use empty string to clear the field.

**--src-networks**:
The source VPC networks to match for this rule. It can only be specified when
--src-network-type is VPC_NETWORKS. It applies to ingress rules. It accepts full
or partial URLs.

**--src-region-codes**:
Source Region Code to match for this rule. Can only be specified if DIRECTION is
`ingress`. Cannot be specified when the source network type is
NON_INTERNET, VPC_NETWORK or INTRA_VPC.

**--src-secure-tags**:
A list of instance secure tags indicating the set of instances on the network to
which the rule applies if all other fields match. Either --src-ip-ranges or
--src-secure-tags must be specified for ingress traffic. If both --src-ip-ranges
and --src-secure-tags are specified, an inbound connection is allowed if either
the range of the source matches --src-ip-ranges or the tag of the source matches
--src-secure-tags. Secure Tags can be assigned to instances during instance
creation.

**--src-threat-intelligence**:
Source Threat Intelligence lists to match for this rule. Can only be specified
if DIRECTION is `ingress`. Cannot be specified when the source
network type is NON_INTERNET, VPC_NETWORK or INTRA_VPC. The available lists can
be found here: [https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy](https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy).

**--target-resources**:
List of URLs of target resources to which the rule is applied.

**--target-secure-tags**:
An optional, list of target secure tags with a name of the format tagValues/ or
full namespaced name

**--target-service-accounts**:
List of target service accounts for the rule.

**--[no-]tls-inspect**:
Use this flag to indicate whether TLS traffic should be inspected using the TLS
inspection policy when the security profile group is applied. Default: no TLS
inspection. Use `--tls-inspect` to enable and
`--no-tls-inspect` to disable.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute firewall-policies rules create
```

```
gcloud beta compute firewall-policies rules create
```