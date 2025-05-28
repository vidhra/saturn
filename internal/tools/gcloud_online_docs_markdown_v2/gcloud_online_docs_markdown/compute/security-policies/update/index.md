# gcloud compute security-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update)*

**NAME**

: **gcloud compute security-policies update - update a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--description)`=`DESCRIPTION`] [`[--enable-layer7-ddos-defense](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--enable-layer7-ddos-defense)`] [`[--json-custom-content-types](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--json-custom-content-types)`=[`CONTENT_TYPE`,…]] [`[--json-parsing](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--json-parsing)`=`JSON_PARSING`] [`[--layer7-ddos-defense-rule-visibility](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--layer7-ddos-defense-rule-visibility)`=`VISIBILITY_TYPE`] [`[--log-level](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--log-level)`=`LOG_LEVEL`] [`[--network-ddos-protection](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--network-ddos-protection)`=`NETWORK_DDOS_PROTECTION`] [`[--recaptcha-redirect-site-key](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--recaptcha-redirect-site-key)`=`RECAPTCHA_REDIRECT_SITE_KEY`] [`[--user-ip-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--user-ip-request-headers)`=[`USER_IP_REQUEST_HEADER`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies update` is used to update security
policies.

**EXAMPLES**

: To update the description run this:

```
gcloud compute security-policies update SECURITY_POLICY --description='new description'
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to update.

**FLAGS**

: **--description**:
An optional, textual description for the security policy.

**--enable-layer7-ddos-defense**:
Whether to enable Cloud Armor Layer 7 DDoS Defense Adaptive Protection.

**--json-custom-content-types**:
A comma-separated list of custom Content-Type header values to apply JSON
parsing for preconfigured WAF rules. Only applicable when JSON parsing is
enabled, like ``--json-parsing=STANDARD``. When
configuring a Content-Type header value, only the type/subtype needs to be
specified, and the parameters should be excluded.

**--json-parsing**:
The JSON parsing behavior for this rule. Must be one of the following values:
[DISABLED, STANDARD, STANDARD_WITH_GRAPHQL].
`JSON_PARSING` must be one of: `DISABLED`,
`STANDARD`, `STANDARD_WITH_GRAPHQL`.

**--layer7-ddos-defense-rule-visibility**:
The visibility type indicates whether the rules are opaque or transparent.
`VISIBILITY_TYPE` must be one of: `STANDARD`,
`PREMIUM`.

**--log-level**:
The level of detail to display for WAF logging.
`LOG_LEVEL` must be one of: `NORMAL`,
`VERBOSE`.

**--network-ddos-protection**:
The DDoS protection level for network load balancing and instances with external
IPs. `NETWORK_DDOS_PROTECTION` must be one of:
`STANDARD`, `ADVANCED`, `ADVANCED_PREVIEW`.

**--recaptcha-redirect-site-key**:
The reCAPTCHA site key to be used for rules using the
``redirect`` action and the
``google-recaptcha`` redirect type under the
security policy.

**--user-ip-request-headers**:
A comma-separated list of request header names to use for resolving the caller's
user IP address.

**--global**

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
gcloud alpha compute security-policies update
```

```
gcloud beta compute security-policies update
```