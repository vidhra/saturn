# gcloud network-security gateway-security-policies rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete)*

**NAME**

: **gcloud network-security gateway-security-policies rules delete - delete Gateway Security Policy Rule**

**SYNOPSIS**

: **`gcloud network-security gateway-security-policies rules delete` (`[GATEWAY_SECURITY_POLICY_RULE](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete#GATEWAY_SECURITY_POLICY_RULE)` : `[--gateway-security-policy](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete#--gateway-security-policy)`=`GATEWAY_SECURITY_POLICY` `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified Gateway Security Policy Rule.

**EXAMPLES**

: To delete a Gateway Security Policy Rule called 'my-rule', run:

```
gcloud network-security gateway-security-policies rules delete my-rule --location={region} --gateway-security-policy={policy-name}
```

**POSITIONAL ARGUMENTS**

: **Gateway security policy rule resource - Name of the Gateway Security Policy Rule
you want to delete. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `gateway_security_policy_rule` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GATEWAY_SECURITY_POLICY_RULE`**:
ID of the gateway security policy rule or fully qualified identifier for the
gateway security policy rule.
To set the `gateway_security_policy_rule` attribute:

- provide the argument `gateway_security_policy_rule` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--gateway-security-policy**:
Id of the gateway security policy.
To set the `gateway-security-policy` attribute:

- provide the argument `gateway_security_policy_rule` on the command
line with a fully specified name;
- provide the argument `--gateway-security-policy` on the command line.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `gateway_security_policy_rule` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `networksecurity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-security gateway-security-policies rules delete
```

```
gcloud beta network-security gateway-security-policies rules delete
```