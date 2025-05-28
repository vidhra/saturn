# gcloud privateca subordinates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update)*

**NAME**

: **gcloud privateca subordinates update - update an existing subordinate certificate authority**

**SYNOPSIS**

: **`gcloud privateca subordinates update` (`[CERTIFICATE_AUTHORITY](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#CERTIFICATE_AUTHORITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--location)`=`LOCATION` `[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--pool)`=`POOL`) [`[--pem-chain](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--pem-chain)`=`PEM_CHAIN`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update labels on a subordinate CA:

```
gcloud privateca subordinates update server-tls-1 --pool=my-pool --location=us-west1 --update-labels=foo=bar
```

To update the CA certificate chain for a subordinate CA:

```
gcloud privateca subordinates update server-tls-1 --pool=my-pool --location=us-west1 --pem-chain=pem_chain.txt
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE AUTHORITY resource - The certificate authority to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_AUTHORITY`**:
ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the
CERTIFICATE_AUTHORITY.
To set the `certificate_authority` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_AUTHORITY.
To set the `location` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

**--pool**:
The parent CA Pool of the CERTIFICATE_AUTHORITY.
To set the `pool` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--pool` on the command line.**

**FLAGS**

: **--pem-chain**:
A file containing a list of PEM-encoded certificates that represent the issuing
chain of this CA.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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