# gcloud domains registrations google-domains-dns get-forwarding-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/get-forwarding-config](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/get-forwarding-config)*

**NAME**

: **gcloud domains registrations google-domains-dns get-forwarding-config - get forwarding configuration of a specific Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations google-domains-dns get-forwarding-config` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/get-forwarding-config#REGISTRATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/google-domains-dns/get-forwarding-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get forwarding configuration (deprecated) of a specific registration.

**EXAMPLES**

: To get forwarding configuration of
``example.com``, run:

```
gcloud domains registrations google-domains-dns get-forwarding-config example.com
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to get the forwarding config
for. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- location is always global.

This must be specified.

**`REGISTRATION`**:
ID of the registration or fully qualified identifier for the registration.
To set the `registration` attribute:

- provide the argument `registration` on the command line.**

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
gcloud alpha domains registrations google-domains-dns get-forwarding-config
```

```
gcloud beta domains registrations google-domains-dns get-forwarding-config
```