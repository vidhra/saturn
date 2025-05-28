# gcloud alpha compute firewall-policies mirroring-rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create)*

**NAME**

: **gcloud alpha compute firewall-policies mirroring-rules create - creates a Compute Engine firewall policy packet mirroring rule**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies mirroring-rules create` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#PRIORITY)` `[--action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--action)`=`ACTION` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--firewall-policy)`=`FIREWALL_POLICY` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--description)`=`DESCRIPTION`] [`[--dest-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--dest-ip-ranges)`=[`DEST_IP_RANGE`,…]] [`[--direction](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--direction)`=`DIRECTION`] [`[--[no-]disabled](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--[no-]disabled)`] [`[--layer4-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--layer4-configs)`=[`LAYER4_CONFIG`,…]] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--organization)`=`ORGANIZATION`] [`[--security-profile-group](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--security-profile-group)`=`SECURITY_PROFILE_GROUP`] [`[--src-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--src-ip-ranges)`=[`SRC_IP_RANGE`,…]] [`[--target-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#--target-resources)`=[`TARGET_RESOURCES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-policies
mirroring-rules create` is used to create organization firewall policy
packet mirroring rules.

**EXAMPLES**

: To create a packet mirroring rule with priority ``10" in an organization
firewall policy with ID ``123456789", run:

```
gcloud alpha compute firewall-policies mirroring-rules create 10 --firewall-policy=123456789 --action=mirror --security-profile-group=organizations/123/locations/global/securityProfileGroups/custom-security-profile-group --description=example-rule
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the firewall policy rule to create.

**REQUIRED FLAGS**

: **--action**:
Action to take if the request matches the match condition.
`ACTION` must be one of: `mirror`,
`do_not_mirror`, `goto_next`.

**--firewall-policy**:
Short name of the firewall policy into which the rule should be inserted.

**OPTIONAL FLAGS**

: **--description**:
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

**--organization**:
Organization which the organization firewall policy belongs to. Must be set if
FIREWALL_POLICY is short name.

**--security-profile-group**:
An org-based security profile group to be used with mirror action. Allowed
formats are: a)
http(s)://<namespace>/<api>/organizations/<org_id>/locations/global/securityProfileGroups/<profile>
b)
(//)<namespace>/organizations/<org_id>/locations/global/securityProfileGroups/<profile>
c) <profile>. In case "c" `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI will create a reference
matching format "a", but to make it work
CLOUDSDK_API_ENDPOINT_OVERRIDES_NETWORKSECURITY property must be set. In order
to set this property, please run the command `gcloud config set
api_endpoint_overrides/networksecurity https://<namespace>/`.

**--src-ip-ranges**:
Source IP ranges to match for this rule.

**--target-resources**:
List of URLs of target resources to which the rule is applied.

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
allowlist. This variant is also available:

```
gcloud beta compute firewall-policies mirroring-rules create
```