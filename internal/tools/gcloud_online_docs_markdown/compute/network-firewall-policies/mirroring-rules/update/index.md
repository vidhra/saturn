# gcloud compute network-firewall-policies mirroring-rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update)*

**NAME**

: **gcloud compute network-firewall-policies mirroring-rules update - updates a Compute Engine network firewall policy packet mirroring rule**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies mirroring-rules update` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#PRIORITY)` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--firewall-policy)`=`FIREWALL_POLICY` `[--global-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--global-firewall-policy)` [`[--action](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--action)`=`ACTION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--description)`=`DESCRIPTION`] [`[--dest-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--dest-ip-ranges)`=[`DEST_IP_RANGE`,…]] [`[--direction](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--direction)`=`DIRECTION`] [`[--[no-]disabled](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--[no-]disabled)`] [`[--layer4-configs](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--layer4-configs)`=[`LAYER4_CONFIG`,…]] [`[--new-priority](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--new-priority)`=`NEW_PRIORITY`] [`[--security-profile-group](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--security-profile-group)`=`SECURITY_PROFILE_GROUP`] [`[--src-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--src-ip-ranges)`=[`SRC_IP_RANGE`,…]] [`[--target-secure-tags](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#--target-secure-tags)`=[`TARGET_SECURE_TAGS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies mirroring-rules update` is
used to update network firewall policy packet mirroring rules.

**EXAMPLES**

: To update a rule with priority ``10`` in a
global network firewall policy with name
``my-policy`` to change the action to
``mirror`` and description to
``new example rule``, run:

```
gcloud compute network-firewall-policies mirroring-rules update 10 --firewall-policy=my-policy --action=mirror --description="new example rule"
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the rule to be updated. Valid in [0, 65535].

**REQUIRED FLAGS**

: **--firewall-policy**:
Firewall policy ID with which to update rule.

**--global-firewall-policy**:
Use this flag to indicate that firewall policy is global.

**OPTIONAL FLAGS**

: **--action**:
Action to take if the request matches the match condition.
`ACTION` must be one of: `mirror`,
`do_not_mirror`, `goto_next`.

**--description**:
An optional, textual description for the rule.

**--dest-ip-ranges**:
Destination IP ranges to match for this rule.

**--direction**:
Direction of the traffic the rule is applied. The default is to apply on
incoming traffic. `DIRECTION` must be one of:
`INGRESS`, `EGRESS`.

**--[no-]disabled**:
Use this flag to disable the rule. Disabled rules will not affect traffic. Use
`--disabled` to enable and `--no-disabled` to disable.

**--layer4-configs**:
A list of destination protocols and ports to which the firewall rule will apply.

**--new-priority**:
New priority for the rule to update. Valid in [0, 65535].

**--security-profile-group**:
A security profile group to be used with mirror action.

**--src-ip-ranges**:
A list of IP address blocks that are allowed to make inbound connections that
match the firewall rule to the instances on the network. The IP address blocks
must be specified in CIDR format: [http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing.Either](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing.Either)
--src-ip-ranges or --src-secure-tags must be specified for INGRESS traffic. If
both --src-ip-ranges and --src-secure-tags are specified, the rule matches if
either the range of the source matches --src-ip-ranges or the secure tag of the
source matches --src-secure-tags.Multiple IP address blocks can be specified if
they are separated by commas.

**--target-secure-tags**:
An optional, list of target secure tags with a name of the format tagValues/ or
full namespaced name

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
gcloud alpha compute network-firewall-policies mirroring-rules update
```

```
gcloud beta compute network-firewall-policies mirroring-rules update
```