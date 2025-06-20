# gcloud recaptcha keys migrate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/migrate](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/migrate)*

**NAME**

: **gcloud recaptcha keys migrate - migrate a key to reCAPTCHA Enterprise**

**SYNOPSIS**

: **`gcloud recaptcha keys migrate` `[KEY](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/migrate#KEY)` [`[--skip-billing-check](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/migrate#--skip-billing-check)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/migrate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Migrate a key from reCAPTCHA to reCAPTCHA Enterprise.

**EXAMPLES**

: To migrate a key from reCAPTCHA to reCAPTCHA Enterprise, run:

```
gcloud recaptcha keys migrate test-key
```

**POSITIONAL ARGUMENTS**

: **Key resource - The reCAPTCHA key to migrate. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.**

**FLAGS**

: **--skip-billing-check**:
If true, skips the billing check. If your usage of reCAPTCHA is under the free
quota, you can safely skip the billing check.

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
gcloud alpha recaptcha keys migrate
```