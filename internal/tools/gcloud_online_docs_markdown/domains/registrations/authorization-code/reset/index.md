# gcloud domains registrations authorization-code reset  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/authorization-code/reset](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/authorization-code/reset)*

**NAME**

: **gcloud domains registrations authorization-code reset - resets authorization code of a specific Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations authorization-code reset` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/authorization-code/reset#REGISTRATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/authorization-code/reset#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resets authorization code of a specific registration.
You can call this API only after 60 days have elapsed since initial
registration.

**EXAMPLES**

: To reset authorization code of ``example.com``,
run:

```
gcloud domains registrations authorization-code reset example.com
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to reset authorization code for.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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
gcloud alpha domains registrations authorization-code reset
```

```
gcloud beta domains registrations authorization-code reset
```