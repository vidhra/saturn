# gcloud domains registrations register  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register)*

**NAME**

: **gcloud domains registrations register - register a new domain**

**SYNOPSIS**

: **`gcloud domains registrations register` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#REGISTRATION)` [`[--contact-data-from-file](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--contact-data-from-file)`=`CONTACT_DATA_FILE_NAME`] [`[--contact-privacy](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--contact-privacy)`=`CONTACT_PRIVACY`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--validate-only)`] [`[--cloud-dns-zone](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--cloud-dns-zone)`=`CLOUD_DNS_ZONE`     | `[--name-servers](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--name-servers)`=`NAME_SERVER`,…,[…]     | `[--use-google-domains-dns](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--use-google-domains-dns)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--async)`] [`[--disable-dnssec](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--disable-dnssec)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--labels)`=[`KEY`=`VALUE`,…]] [`[--notices](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--notices)`=[`NOTICE`,…]] [`[--yearly-price](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#--yearly-price)`=`YEARLY_PRICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/register#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Cloud Domains registration resource by registering a new domain.
The new resource's ID will be equal to the domain name.
After this command executes, the resource will be in state REGISTRATION_PENDING.
The registration process should complete in less than 5 minutes. After that the
resource will be in state ACTIVE. In rare cases this process can take much
longer due, for example, to a downtime of the domain registry.
Also in rare cases, the domain may end up in state REGISTRATION_FAILED. In that
case, delete the registration resource and try again.
When using Cloud DNS Zone DNSSEC will be enabled by default whenever the Zone is
DNSSEC signed. You can choose to not enable DNSSEC by using the --disable-dnssec
flag.

**EXAMPLES**

: To register ``example.com`` interactively, run:

```
gcloud domains registrations register example.com
```

To register ``example.com`` using contact data
from a YAML file ``contacts.yaml``, run:

```
gcloud domains registrations register example.com --contact-data-from-file=contacts.yaml
```

To register ``example.com`` with interactive
prompts disabled, provide --contact-data-from-file, --contact-privacy,
--yearly-price flags and one of the flags for setting authoritative name
servers. Sometimes also --notices flag is required. For example, run:

```
gcloud domains registrations register example.com --contact-data-from-file=contacts.yaml --contact-privacy=private-contact-data --yearly-price="12.00 USD" --cloud-dns-zone=example-com --quiet
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain name to register. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

: **--contact-data-from-file**:
A YAML file containing the contact data for the domain's three contacts:
registrant, admin, and technical.
The file can either specify a single set of contact data with label
'allContacts', or three separate sets of contact data with labels 'adminContact'
and 'technicalContact'.
Each contact data must contain values for all required fields: email,
phoneNumber and postalAddress in google.type.PostalAddress format.
For more guidance on how to specify postalAddress, please see: [https://support.google.com/business/answer/6397478](https://support.google.com/business/answer/6397478)
Examples of file contents:

```
allContacts:
  email: 'example@example.com'
  phoneNumber: '+1.8005550123'
  postalAddress:
    regionCode: 'US'
    postalCode: '94043'
    administrativeArea: 'CA'
    locality: 'Mountain View'
    addressLines: ['1600 Amphitheatre Pkwy']
    recipients: ['Jane Doe']
```

```
registrantContact:
  email: 'registrant@example.com'
  phoneNumber: '+1.8005550123'
  postalAddress:
    regionCode: 'US'
    postalCode: '94043'
    administrativeArea: 'CA'
    locality: 'Mountain View'
    addressLines: ['1600 Amphitheatre Pkwy']
    recipients: ['Registrant Jane Doe']
adminContact:
  email: 'admin@example.com'
  phoneNumber: '+1.8005550123'
  postalAddress:
    regionCode: 'US'
    postalCode: '94043'
    administrativeArea: 'CA'
    locality: 'Mountain View'
    addressLines: ['1600 Amphitheatre Pkwy']
    recipients: ['Admin Jane Doe']
technicalContact:
  email: 'technical@example.com'
  phoneNumber: '+1.8005550123'
  postalAddress:
    regionCode: 'US'
    postalCode: '94043'
    administrativeArea: 'CA'
    locality: 'Mountain View'
    addressLines: ['1600 Amphitheatre Pkwy']
    recipients: ['Technic Jane Doe']
```

**--contact-privacy**:
The contact privacy mode to use. Supported privacy modes depend on the domain.
`CONTACT_PRIVACY` must be one of:

**`private-contact-data`**:
(DEPRECATED) Your contact info won't be available to the public. To help protect
your info and prevent spam, a third party provides alternate (proxy) contact
info for your domain in the public directory at no extra cost. They will forward
received messages to you. The private-contact-data option is deprecated; See [https://cloud.google.com/domains/docs/deprecations/feature-deprecations](https://cloud.google.com/domains/docs/deprecations/feature-deprecations).

**`public-contact-data`**:
All the data from contact config is publicly available. To set this value, you
must also pass the --notices flag with value public-contact-data-acknowledgement
or agree to the notice interactively.

**`redacted-contact-data`**:
Limited personal information will be available to the public. The actual
information redacted depends on the domain. For more information see [https://support.google.com/domains/answer/3251242](https://support.google.com/domains/answer/3251242).

**--validate-only**:
Don't actually create registration. Only validate arguments.

**--cloud-dns-zone**

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--disable-dnssec**:
Use this flag to disable DNSSEC, or to skip enabling it when switching to a
Cloud DNS Zone or Google Domains nameservers.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--notices**:
Notices about special properties of certain domains or contacts.
`NOTICE` must be one of:

**`public-contact-data-acknowledgement`**:
By sending this notice you acknowledge that using public-contact-data contact
privacy makes all the data from contact config publicly available.

**`hsts-preloaded`**:
By sending this notice you acknowledge that the domain is preloaded on the HTTP
Strict Transport Security list in browsers. Serving a website on such domain
will require an SSL certificate. See [https://support.google.com/domains/answer/7638036](https://support.google.com/domains/answer/7638036)
for details.

**--yearly-price**:
Accept the domain's yearly price in the interactive flow or by using this flag.
Use a number followed by a currency code, for example, "12.00 USD". Get the
price using the get-register-parameters command.

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
gcloud alpha domains registrations register
```

```
gcloud beta domains registrations register
```