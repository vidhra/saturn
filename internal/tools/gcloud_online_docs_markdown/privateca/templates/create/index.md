# gcloud privateca templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create)*

**NAME**

: **gcloud privateca templates create - create a new certificate template**

**SYNOPSIS**

: **`gcloud privateca templates create` (`[CERTIFICATE_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#CERTIFICATE_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--location)`=`LOCATION`) `[--copy-sans](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--copy-sans)` `[--copy-subject](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--copy-subject)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--description)`=`DESCRIPTION`] [`[--identity-cel-expression](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--identity-cel-expression)`=`IDENTITY_CEL_EXPRESSION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--maximum-lifetime](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--maximum-lifetime)`=`MAXIMUM_LIFETIME`] [`[--predefined-values-file](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--predefined-values-file)`=`PREDEFINED_VALUES_FILE`] [`[--copy-all-requested-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--copy-all-requested-extensions)`     | `[--copy-extensions-by-oid](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--copy-extensions-by-oid)`=[`OBJECT_ID`,…] `[--copy-known-extensions](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#--copy-known-extensions)`=[`KNOWN_EXTENSIONS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a certificate template that enforces policy restrictions on certificate
requestors. Using a certificate template, you can define restrictions on the
kinds of Subjects/SANs and x509 extensions allowed from certificate requestors
as well as a default set of x509 extensions that should be applied to all
certificates using that template. These templates can be binded to IAM
identities such that certain groups of requestors must use particular templates,
allowing for fine-grained policy enforcements based on identity.
For more information and examples, see [https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template](https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template).

**EXAMPLES**

: To create a template that prohibits any x509 extension from a requester, but
permits custom subjects/SANs and defines the default x509 extensions, run:

```
gcloud privateca templates create restricted-template --location=us-west1 --copy-subject --copy-sans --predefined-values-file=x509_parameters.yaml
```

To create a template that allows requesters to specify only DNS names from
requesters, use a custom CEL expression with a SAN only restriction:

```
gcloud privateca templates create dns-only-template --location=us-west1 --description="Restricts certificates to DNS SANs." --no-copy-subject --copy-sans --identity-cel-expression="subject_alt_names.all(san, san.type == DNS)"
```

To create a template that permits a requestor to specify extensions by OIDs, and
subjects (but not SANs), with default x509 exensions:

```
gcloud privateca templates create mtls-only-extensions --location=us-west1 --copy-subject --no-copy-sans --predefined-values-file=mtls_cert_exts.yaml --copy-extensions-by-oid=1.3.6.1.5.5.7.3.2,1.3.6.1.5.5.7.3.1
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE TEMPLATE resource - The template to create. The arguments in this
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

**REQUIRED FLAGS**

: **--copy-sans**:
If this is specified, the Subject Alternative Name extension from the
certificate request will be copied into the signed certificate. Specify
--no-copy-sans to drop any caller-specified SANs in the certificate request.

**--copy-subject**:
If this is specified, the Subject from the certificate request will be copied
into the signed certificate. Specify --no-copy-subject to drop any
caller-specified subjects from the certificate request.

**OPTIONAL FLAGS**

: **--description**:
A text description for the Certificate Template.

**--identity-cel-expression**:
A CEL expression that will be evaluated against the identity in the certificate
before it is issued, and returns a boolean signifying whether the request should
be allowed.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--maximum-lifetime**:
If this is set, then issued certificate's lifetime will be truncated to the
value provided. If the issuing CaPool's IssuancePolicy specifies a maximum
lifetime the minimum of the two durations will be the maximum lifetime for the
issued certificate. Note that if the issuing CertificateAuthority expires before
a Certificate's requested maximum_lifetime, the effective lifetime will be
explicitly truncated to match it.

**--predefined-values-file**:
A YAML file describing any predefined X.509 values set by this template. The
provided extensions will be copied over to any certificate requests that use
this template, taking precedent over any allowed extensions in the certificate
request. The format of this file should be a YAML representation of the
X509Parameters message, which is defined here: [https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters](https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters).
Some examples can be found here: [https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template](https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template)

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