# gcloud domains registrations configure contacts  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts)*

**NAME**

: **gcloud domains registrations configure contacts - configure contact settings of a Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations configure contacts` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#REGISTRATION)` [`[--contact-data-from-file](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#--contact-data-from-file)`=`CONTACT_DATA_FILE_NAME`] [`[--contact-privacy](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#--contact-privacy)`=`CONTACT_PRIVACY`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#--validate-only)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#--async)`] [`[--notices](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#--notices)`=[`NOTICE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Configure registration's contact settings: email, phone number, postal address
and also contact privacy.
In some cases such changes have to be confirmed through an email sent to the
registrant before they take effect. In order to resend the email, execute this
command again.
NOTE: Please consider carefully any changes to contact privacy settings when
changing from "redacted-contact-data" to "public-contact-data." There may be a
delay in reflecting updates you make to registrant contact information such that
any changes you make to contact privacy (including from "redacted-contact-data"
to "public-contact-data") will be applied without delay but changes to
registrant contact information may take a limited time to be publicized. This
means that changes to contact privacy from "redacted-contact-data" to
"public-contact-data" may make the previous registrant contact data public until
the modified registrant contact details are published.

**EXAMPLES**

: To start an interactive flow to configure contact settings for
``example.com``, run:

```
gcloud domains registrations configure contacts example.com
```

To enable contact privacy for ``example.com``,
run:

```
gcloud domains registrations configure contacts example.com --contact-privacy=private-contact-data
```

To change contact data for ``example.com``
according to information from a YAML file
``contacts.yaml``, run:

```
gcloud domains registrations configure contacts example.com --contact-data-from-file=contacts.yaml
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to configure contact settings
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

**COMMONLY USED FLAGS**

: **--contact-data-from-file**:
A YAML file containing the contact data for the domain's three contacts:
registrant, admin, and technical.
The file can either specify a single set of contact data with label
'allContacts', or three separate sets of contact data with labels 'adminContact'
and 'technicalContact'.
If 'registrantContact', 'adminContact' or 'technicalContact' labels are used
then only the specified contacts are updated.
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
Don't actually configure contact settings of the registration. Only validate
arguments.

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--notices**:
Notices about special properties of contacts. `NOTICE`
must be (only one value is supported):

**`public-contact-data-acknowledgement`**:
By sending this notice you acknowledge that using public-contact-data contact
privacy makes all the data from contact config publicly available.

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
gcloud alpha domains registrations configure contacts
```

```
gcloud beta domains registrations configure contacts
```