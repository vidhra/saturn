# gcloud recaptcha keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create)*

**NAME**

: **gcloud recaptcha keys create - create a Key**

**SYNOPSIS**

: **`gcloud recaptcha keys create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--display-name)`=`DISPLAY_NAME` (`[--express](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--express)`     | [`[--android](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--android)` (`[--allow-all-package-names](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--allow-all-package-names)` | `[--package-names](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--package-names)`=[`PACKAGE_NAMES`,…]) : `[--support-non-google-app-store-distribution](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--support-non-google-app-store-distribution)`]     | [`[--ios](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--ios)` (`[--allow-all-bundle-ids](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--allow-all-bundle-ids)` | `[--bundle-ids](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--bundle-ids)`=[`BUNDLE_IDS`,…]) : `[--key-id](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--key-id)`=`KEY_ID` `[--private-key-file](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--private-key-file)`=`PATH_TO_FILE` `[--team-id](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--team-id)`=`TEAM_ID`]     | [`[--web](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--web)` (`[--allow-all-domains](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--allow-all-domains)` | `[--domains](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--domains)`=[`DOMAINS`,…]) : `[--allow-amp-traffic](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--allow-amp-traffic)` `[--integration-type](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--integration-type)`=`INTEGRATION_TYPE` `[--security-preference](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--security-preference)`=`SECURITY_PREFERENCE` `[--testing-challenge](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--testing-challenge)`=`TESTING_CHALLENGE`]) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--testing-score](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--testing-score)`=`TESTING_SCORE`] [`[--waf-service](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--waf-service)`=`WAF_SERVICE` : `[--waf-feature](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#--waf-feature)`=`WAF_FEATURE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a reCAPTCHA Key.

**EXAMPLES**

: To create a new reCAPTCHA key for websites showing no CAPTCHA challenge, run:

```
gcloud recaptcha keys create --display-name=test-key-name --web --allow-all-domains --integration-type=score
```

**REQUIRED FLAGS**

: **--display-name**:
A human-readable name for the key. Typically a site or app name.

**--express**

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--testing-score**:
If set, all assessments for this key will return this score. Must be between 0
(likely not legitimate) and 1 (likely legitimate) inclusive.

**--waf-service**

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
gcloud alpha recaptcha keys create
```