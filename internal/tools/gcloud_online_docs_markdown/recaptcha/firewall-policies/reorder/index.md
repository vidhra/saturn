# gcloud recaptcha firewall-policies reorder  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/reorder](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/reorder)*

**NAME**

: **gcloud recaptcha firewall-policies reorder - reorder all Firewall Policies**

**SYNOPSIS**

: **`gcloud recaptcha firewall-policies reorder` `[--names](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/reorder#--names)`=[`NAMES`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/reorder#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Reorder all reCAPTCHA Firewall Policies.

**EXAMPLES**

: To reorder the list of reCAPTCHA firewall policies, run:

```
gcloud recaptcha firewall-policies reorder --names=policy-name,policy-name,policy-name
```

**REQUIRED FLAGS**

: **--names**:
Names of all firewall policies in desired order.

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

: This command uses the `recaptchaenterprise/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/recaptcha-enterprise/](https://cloud.google.com/recaptcha-enterprise/)

**NOTES**

: This variant is also available:

```
gcloud alpha recaptcha firewall-policies reorder
```