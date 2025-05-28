# gcloud recaptcha keys add-ip-override  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override)*

**NAME**

: **gcloud recaptcha keys add-ip-override - add an IP override to a key**

**SYNOPSIS**

: **`gcloud recaptcha keys add-ip-override` `[KEY](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override#KEY)` `[--ip](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override#--ip)`=`IP` `[--override](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override#--override)`=`OVERRIDE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/keys/add-ip-override#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IP override to a key.

**EXAMPLES**

: ```
gcloud recaptcha keys add-ip-override test-key --ip=1.2.3.4 --override=allow
```

**POSITIONAL ARGUMENTS**

: **Key resource - The reCAPTCHA key to add the IP override to. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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

**REQUIRED FLAGS**

: **--ip**:
IP address to override for the key.

**--override**:
If set to allow, the IP address/CIDR range will be allowlisted for the key.
`OVERRIDE` must be one of: `allow`,
`override-type-unspecified`.

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
gcloud alpha recaptcha keys add-ip-override
```