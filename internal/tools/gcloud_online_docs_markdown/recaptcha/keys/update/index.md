# gcloud recaptcha keys update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update)*

**NAME**

: **gcloud recaptcha keys update - update a Key**

**SYNOPSIS**

: **`gcloud recaptcha keys update` `[KEY](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#KEY)` [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--express](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--express)`     | `[--android](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--android)` (`[--allow-all-package-names](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--allow-all-package-names)` | `[--package-names](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--package-names)`=[`PACKAGE_NAMES`,…])     | [`[--ios](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--ios)` : `[--allow-all-bundle-ids](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--allow-all-bundle-ids)` | `[--bundle-ids](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--bundle-ids)`=[`BUNDLE_IDS`,…] `[--key-id](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--key-id)`=`KEY_ID` `[--private-key-file](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--private-key-file)`=`PATH_TO_FILE` `[--team-id](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--team-id)`=`TEAM_ID`]     | [`[--web](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--web)` : `[--allow-amp-traffic](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--allow-amp-traffic)` `[--security-preference](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--security-preference)`=`SECURITY_PREFERENCE` `[--allow-all-domains](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--allow-all-domains)` | `[--domains](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#--domains)`=[`DOMAINS`,…]]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a reCAPTCHA Key.

**EXAMPLES**

: To update the information of a reCAPTCHA key, run:

```
gcloud recaptcha keys update test-key --labels="foo=bar" --web --domains=test.com.mx
```

**POSITIONAL ARGUMENTS**

: **Key resource - The reCAPTCHA Key to update. This represents a Cloud resource.
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

: **--display-name**:
A human-readable name for the key. Typically a site or app name.

**--labels**:
List of label KEY=VALUE pairs to add.

**--express**

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
gcloud alpha recaptcha keys update
```