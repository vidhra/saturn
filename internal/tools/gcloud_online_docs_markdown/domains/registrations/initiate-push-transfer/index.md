# gcloud domains registrations initiate-push-transfer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer)*

**NAME**

: **gcloud domains registrations initiate-push-transfer - initiates the push transfer process**

**SYNOPSIS**

: **`gcloud domains registrations initiate-push-transfer` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer#REGISTRATION)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer#--async)`] [`[--tag](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer#--tag)`=`TAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Initiates the `Push Transfer` process to transfer the domain to
another registrar. The process might complete instantly or might require
confirmation or additional work. Check the emails sent to the email address of
the registrant. The process is aborted after a timeout if it's not completed.
This method is only supported for domains that have the
`REQUIRE_PUSH_TRANSFER` property in the list of
`domain_properties`. The domain must also be unlocked before it can
be transferred to a different registrar.

**EXAMPLES**

: To initiate a push transfer for
``example.co.uk``, run:

```
gcloud domains registrations initiate-push-transfer example.co.uk --tag=NEW_REGISTRY_TAG
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to transfer. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--tag**:
The Tag of the new registrar. Can be found at [https://nominet.uk/registrar-list/](https://nominet.uk/registrar-list/)

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
gcloud alpha domains registrations initiate-push-transfer
```

```
gcloud beta domains registrations initiate-push-transfer
```