# gcloud privateca templates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update)*

**NAME**

: **gcloud privateca templates update - update a certificate template**

**SYNOPSIS**

: **`gcloud privateca templates update` (`[CERTIFICATE_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#CERTIFICATE_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--location)`=`LOCATION`) [`[--copy-sans](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--copy-sans)`] [`[--copy-subject](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--copy-subject)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--description)`=`DESCRIPTION`] [`[--identity-cel-expression](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--identity-cel-expression)`=`IDENTITY_CEL_EXPRESSION`] [`[--predefined-values-file](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--predefined-values-file)`=`PREDEFINED_VALUES_FILE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--remove-labels)`=[`KEY`,…]] [`[--copy-all-requested-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--copy-all-requested-extensions)`     | `[--copy-extensions-by-oid](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--copy-extensions-by-oid)`=[`OBJECT_ID`,…]     | `[--drop-oid-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--drop-oid-extensions)` `[--copy-known-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--copy-known-extensions)`=[`KNOWN_EXTENSIONS`,…]     | `[--drop-known-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#--drop-known-extensions)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a certificate template.

**EXAMPLES**

: To update a template named "dns-restricted" with new default x509 extensions:

```
gcloud privateca templates update dns-restricted --location=us-west1 --predefined-values-file=x509_parameters.yaml
```

To update a template named "dns-restricted" to allow requestors to specify
subject:

```
gcloud privateca templates update dns-restricted --location=us-west1 --copy-subject
```

To update a template named "dns-restricted" with allowed extension
'base-key-usage' to allow requestors to specify additional x509 extension
'extended-key-usage':

```
gcloud privateca templates update dns-restricted --location=us-west1 --copy-known-extensions=base-key-usage,extended-key-usage
```

To update a template named "mtls-restricted" with allowed OID '1.1' to allow
requestors to specify alternative OIDS '2.2,3.3':

```
gcloud privateca templates update mtls-restricted --location=us-west1 --copy-extensions-by-oid=2.2,3.3
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE TEMPLATE resource - The template to update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_TEMPLATE`**:
ID of the CERTIFICATE_TEMPLATE or fully qualified identifier for the
CERTIFICATE_TEMPLATE.
To set the `certificate template` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_TEMPLATE.
To set the `location` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.**

**FLAGS**

: **--copy-sans**:
If this is specified, the Subject Alternative Name extension from the
certificate request will be copied into the signed certificate. Specify
--no-copy-sans to drop any caller-specified SANs in the certificate request.

**--copy-subject**:
If this is specified, the Subject from the certificate request will be copied
into the signed certificate. Specify --no-copy-subject to drop any
caller-specified subjects from the certificate request.

**--description**:
A text description for the Certificate Template.

**--identity-cel-expression**:
A CEL expression that will be evaluated against the identity in the certificate
before it is issued, and returns a boolean signifying whether the request should
be allowed.

**--predefined-values-file**:
A YAML file describing any predefined X.509 values set by this template. The
provided extensions will be copied over to any certificate requests that use
this template, taking precedent over any allowed extensions in the certificate
request. The format of this file should be a YAML representation of the
X509Parameters message, which is defined here: [https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters](https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters).
Some examples can be found here: [https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template](https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template)

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--copy-all-requested-extensions**

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