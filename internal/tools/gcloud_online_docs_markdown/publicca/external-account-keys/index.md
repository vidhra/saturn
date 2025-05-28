# gcloud publicca external-account-keys  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys)*

**NAME**

: **gcloud publicca external-account-keys - create ACME external account binding keys**

**SYNOPSIS**

: **`gcloud publicca external-account-keys` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud publicca external-account-keys lets you create an external account key
associated with Google Trust Services' publicly trusted certificate authority.
The external account key will be associated with the Cloud project and it may be
bound to an Automatic Certificate Management Environment (ACME) account
following RFC 8555.
See [https://tools.ietf.org/html/rfc8555#section-7.3.4](https://tools.ietf.org/html/rfc8555#section-7.3.4)
for more details.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys/create)`**:
Create a new external account key.

**NOTES**

: These variants are also available:

```
gcloud alpha publicca external-account-keys
```

```
gcloud beta publicca external-account-keys
```