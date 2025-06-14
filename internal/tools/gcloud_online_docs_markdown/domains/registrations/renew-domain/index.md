# gcloud domains registrations renew-domain  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain)*

**NAME**

: **gcloud domains registrations renew-domain - renew a recently expired Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations renew-domain` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain#REGISTRATION)` [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain#--validate-only)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain#--async)`] [`[--yearly-price](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain#--yearly-price)`=`YEARLY_PRICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Use this method to renew domains that expired within the last 30 days. Renewing
your domain extends it for one year from the previous expiration date and you
are charged the yearly renewal price.

**EXAMPLES**

: To renew a registration for ``example.com``
interactively, run:

```
gcloud domains registrations renew-domain example.com
```

To renew ``example.com`` with interactive
prompts disabled, provide the --yearly-price flag. For example, run:

```
gcloud domains registrations renew-domain example.com --yearly-price="12.00 USD" --quiet
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to renew. This represents a
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

**COMMONLY USED FLAGS**

: **--validate-only**:
Don't actually renew registration. Only validate arguments.

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--yearly-price**:
Accept the domain's yearly price in the interactive flow or by using this flag.
Use a number followed by a currency code, for example, "12.00 USD". Get the
price by calling the renew-domain command without the --yearly-price flag.

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
gcloud alpha domains registrations renew-domain
```

```
gcloud beta domains registrations renew-domain
```