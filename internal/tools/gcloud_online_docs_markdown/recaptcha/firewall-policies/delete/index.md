# gcloud recaptcha firewall-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/delete](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/delete)*

**NAME**

: **gcloud recaptcha firewall-policies delete - delete one or more reCAPTCHA Firewall Policies**

**SYNOPSIS**

: **`gcloud recaptcha firewall-policies delete` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/delete#FIREWALL_POLICY)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete one or more reCAPTCHA Firewall Policies from a given cloud project.

**EXAMPLES**

: To delete a reCAPTCHA firewall policies, run:

```
gcloud recaptcha firewall-policies delete policy-id
```

**POSITIONAL ARGUMENTS**

: **Firewall policy resource - The reCAPTCHA firewall policy to delete. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `firewall_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FIREWALL_POLICY`**:
ID of the firewall_policy or fully qualified identifier for the firewall_policy.
To set the `firewall_policy` attribute:

- provide the argument `firewall_policy` on the command line.**

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
gcloud alpha recaptcha firewall-policies delete
```