# update-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pca-connector-ad/update-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pca-connector-ad/update-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pca-connector-ad](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pca-connector-ad/index.html#cli-aws-pca-connector-ad) ]

# update-template

## Description

Update template configuration to define the information included in certificates.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pca-connector-ad-2018-05-10/UpdateTemplate)

## Synopsis

```
update-template
[--definition <value>]
[--reenroll-all-certificate-holders | --no-reenroll-all-certificate-holders]
--template-arn <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--definition` (tagged union structure)

Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `TemplateV2`, `TemplateV3`, `TemplateV4`.

TemplateV2 -> (structure)

Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

CertificateValidity -> (structure)

Certificate validity describes the validity and renewal periods of a certificate.

RenewalPeriod -> (structure)

Renewal period is the period of time before certificate expiration when a new certificate will be requested.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

ValidityPeriod -> (structure)

Information describing the end of the validity period of the certificate. This parameter sets the âNot Afterâ date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

EnrollmentFlags -> (structure)

Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.

EnableKeyReuseOnNtTokenKeysetStorageFull -> (boolean)

Allow renewal using the same key.

IncludeSymmetricAlgorithms -> (boolean)

Include symmetric algorithms allowed by the subject.

NoSecurityExtension -> (boolean)

This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

RemoveInvalidCertificateFromPersonalStore -> (boolean)

Delete expired or revoked certificates instead of archiving them.

UserInteractionRequired -> (boolean)

Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

Extensions -> (structure)

Extensions describe the key usage extensions and application policies for a template.

ApplicationPolicies -> (structure)

Application policies specify what the certificate is used for and its purpose.

Critical -> (boolean)

Marks the application policy extension as critical.

Policies -> (list)

Application policies describe what the certificate can be used for.

(tagged union structure)

Application policies describe what the certificate can be used for.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PolicyObjectIdentifier`, `PolicyType`.

PolicyObjectIdentifier -> (string)

The object identifier (OID) of an application policy.

PolicyType -> (string)

The type of application policy

KeyUsage -> (structure)

The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.

Critical -> (boolean)

Sets the key usage extension to critical.

UsageFlags -> (structure)

The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

DataEncipherment -> (boolean)

DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.

DigitalSignature -> (boolean)

The digitalSignature is asserted when the subject public key is used for verifying digital signatures.

KeyAgreement -> (boolean)

KeyAgreement is asserted when the subject public key is used for key agreement.

KeyEncipherment -> (boolean)

KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.

NonRepudiation -> (boolean)

NonRepudiation is asserted when the subject public key is used to verify digital signatures.

GeneralFlags -> (structure)

General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

AutoEnrollment -> (boolean)

Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.

MachineType -> (boolean)

Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users.

PrivateKeyAttributes -> (structure)

Private key attributes allow you to specify the minimal key length, key spec, and cryptographic providers for the private key of a certificate for v2 templates. V2 templates allow you to use Legacy Cryptographic Service Providers.

CryptoProviders -> (list)

Defines the cryptographic providers used to generate the private key.

(string)

KeySpec -> (string)

Defines the purpose of the private key. Set it to âKEY_EXCHANGEâ or âSIGNATUREâ value.

MinimalKeyLength -> (integer)

Set the minimum key length of the private key.

PrivateKeyFlags -> (structure)

Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.

ClientVersion -> (string)

Defines the minimum client compatibility.

ExportableKey -> (boolean)

Allows the private key to be exported.

StrongKeyProtectionRequired -> (boolean)

Require user input when using the private key for enrollment.

SubjectNameFlags -> (structure)

Subject name flags describe the subject name and subject alternate name that is included in a certificate.

RequireCommonName -> (boolean)

Include the common name in the subject name.

RequireDirectoryPath -> (boolean)

Include the directory path in the subject name.

RequireDnsAsCn -> (boolean)

Include the DNS as common name in the subject name.

RequireEmail -> (boolean)

Include the subjectâs email in the subject name.

SanRequireDirectoryGuid -> (boolean)

Include the globally unique identifier (GUID) in the subject alternate name.

SanRequireDns -> (boolean)

Include the DNS in the subject alternate name.

SanRequireDomainDns -> (boolean)

Include the domain DNS in the subject alternate name.

SanRequireEmail -> (boolean)

Include the subjectâs email in the subject alternate name.

SanRequireSpn -> (boolean)

Include the service principal name (SPN) in the subject alternate name.

SanRequireUpn -> (boolean)

Include the user principal name (UPN) in the subject alternate name.

SupersededTemplates -> (list)

List of templates in Active Directory that are superseded by this template.

(string)

TemplateV3 -> (structure)

Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

CertificateValidity -> (structure)

Certificate validity describes the validity and renewal periods of a certificate.

RenewalPeriod -> (structure)

Renewal period is the period of time before certificate expiration when a new certificate will be requested.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

ValidityPeriod -> (structure)

Information describing the end of the validity period of the certificate. This parameter sets the âNot Afterâ date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

EnrollmentFlags -> (structure)

Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.

EnableKeyReuseOnNtTokenKeysetStorageFull -> (boolean)

Allow renewal using the same key.

IncludeSymmetricAlgorithms -> (boolean)

Include symmetric algorithms allowed by the subject.

NoSecurityExtension -> (boolean)

This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

RemoveInvalidCertificateFromPersonalStore -> (boolean)

Delete expired or revoked certificates instead of archiving them.

UserInteractionRequired -> (boolean)

Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

Extensions -> (structure)

Extensions describe the key usage extensions and application policies for a template.

ApplicationPolicies -> (structure)

Application policies specify what the certificate is used for and its purpose.

Critical -> (boolean)

Marks the application policy extension as critical.

Policies -> (list)

Application policies describe what the certificate can be used for.

(tagged union structure)

Application policies describe what the certificate can be used for.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PolicyObjectIdentifier`, `PolicyType`.

PolicyObjectIdentifier -> (string)

The object identifier (OID) of an application policy.

PolicyType -> (string)

The type of application policy

KeyUsage -> (structure)

The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.

Critical -> (boolean)

Sets the key usage extension to critical.

UsageFlags -> (structure)

The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

DataEncipherment -> (boolean)

DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.

DigitalSignature -> (boolean)

The digitalSignature is asserted when the subject public key is used for verifying digital signatures.

KeyAgreement -> (boolean)

KeyAgreement is asserted when the subject public key is used for key agreement.

KeyEncipherment -> (boolean)

KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.

NonRepudiation -> (boolean)

NonRepudiation is asserted when the subject public key is used to verify digital signatures.

GeneralFlags -> (structure)

General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

AutoEnrollment -> (boolean)

Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.

MachineType -> (boolean)

Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users

HashAlgorithm -> (string)

Specifies the hash algorithm used to hash the private key.

PrivateKeyAttributes -> (structure)

Private key attributes allow you to specify the algorithm, minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v3 templates. V3 templates allow you to use Key Storage Providers.

Algorithm -> (string)

Defines the algorithm used to generate the private key.

CryptoProviders -> (list)

Defines the cryptographic providers used to generate the private key.

(string)

KeySpec -> (string)

Defines the purpose of the private key. Set it to âKEY_EXCHANGEâ or âSIGNATUREâ value.

KeyUsageProperty -> (tagged union structure)

The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PropertyFlags`, `PropertyType`.

PropertyFlags -> (structure)

You can specify key usage for encryption, key agreement, and signature. You can use property flags or property type but not both.

Decrypt -> (boolean)

Allows key for encryption and decryption.

KeyAgreement -> (boolean)

Allows key exchange without encryption.

Sign -> (boolean)

Allow key use for digital signature.

PropertyType -> (string)

You can specify all key usages using property type ALL. You can use property type or property flags but not both.

MinimalKeyLength -> (integer)

Set the minimum key length of the private key.

PrivateKeyFlags -> (structure)

Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.

ClientVersion -> (string)

Defines the minimum client compatibility.

ExportableKey -> (boolean)

Allows the private key to be exported.

RequireAlternateSignatureAlgorithm -> (boolean)

Reguires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.

StrongKeyProtectionRequired -> (boolean)

Requirer user input when using the private key for enrollment.

SubjectNameFlags -> (structure)

Subject name flags describe the subject name and subject alternate name that is included in a certificate.

RequireCommonName -> (boolean)

Include the common name in the subject name.

RequireDirectoryPath -> (boolean)

Include the directory path in the subject name.

RequireDnsAsCn -> (boolean)

Include the DNS as common name in the subject name.

RequireEmail -> (boolean)

Include the subjectâs email in the subject name.

SanRequireDirectoryGuid -> (boolean)

Include the globally unique identifier (GUID) in the subject alternate name.

SanRequireDns -> (boolean)

Include the DNS in the subject alternate name.

SanRequireDomainDns -> (boolean)

Include the domain DNS in the subject alternate name.

SanRequireEmail -> (boolean)

Include the subjectâs email in the subject alternate name.

SanRequireSpn -> (boolean)

Include the service principal name (SPN) in the subject alternate name.

SanRequireUpn -> (boolean)

Include the user principal name (UPN) in the subject alternate name.

SupersededTemplates -> (list)

List of templates in Active Directory that are superseded by this template.

(string)

TemplateV4 -> (structure)

Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

CertificateValidity -> (structure)

Certificate validity describes the validity and renewal periods of a certificate.

RenewalPeriod -> (structure)

Renewal period is the period of time before certificate expiration when a new certificate will be requested.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

ValidityPeriod -> (structure)

Information describing the end of the validity period of the certificate. This parameter sets the âNot Afterâ date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

Period -> (long)

The numeric value for the validity period.

PeriodType -> (string)

The unit of time. You can select hours, days, weeks, months, and years.

EnrollmentFlags -> (structure)

Enrollment flags describe the enrollment settings for certificates using the existing private key and deleting expired or revoked certificates.

EnableKeyReuseOnNtTokenKeysetStorageFull -> (boolean)

Allow renewal using the same key.

IncludeSymmetricAlgorithms -> (boolean)

Include symmetric algorithms allowed by the subject.

NoSecurityExtension -> (boolean)

This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

RemoveInvalidCertificateFromPersonalStore -> (boolean)

Delete expired or revoked certificates instead of archiving them.

UserInteractionRequired -> (boolean)

Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

Extensions -> (structure)

Extensions describe the key usage extensions and application policies for a template.

ApplicationPolicies -> (structure)

Application policies specify what the certificate is used for and its purpose.

Critical -> (boolean)

Marks the application policy extension as critical.

Policies -> (list)

Application policies describe what the certificate can be used for.

(tagged union structure)

Application policies describe what the certificate can be used for.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PolicyObjectIdentifier`, `PolicyType`.

PolicyObjectIdentifier -> (string)

The object identifier (OID) of an application policy.

PolicyType -> (string)

The type of application policy

KeyUsage -> (structure)

The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.

Critical -> (boolean)

Sets the key usage extension to critical.

UsageFlags -> (structure)

The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

DataEncipherment -> (boolean)

DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.

DigitalSignature -> (boolean)

The digitalSignature is asserted when the subject public key is used for verifying digital signatures.

KeyAgreement -> (boolean)

KeyAgreement is asserted when the subject public key is used for key agreement.

KeyEncipherment -> (boolean)

KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.

NonRepudiation -> (boolean)

NonRepudiation is asserted when the subject public key is used to verify digital signatures.

GeneralFlags -> (structure)

General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

AutoEnrollment -> (boolean)

Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.

MachineType -> (boolean)

Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users

HashAlgorithm -> (string)

Specifies the hash algorithm used to hash the private key. Hash algorithm can only be specified when using Key Storage Providers.

PrivateKeyAttributes -> (structure)

Private key attributes allow you to specify the minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v4 templates. V4 templates allow you to use either Key Storage Providers or Legacy Cryptographic Service Providers. You specify the cryptography provider category in private key flags.

Algorithm -> (string)

Defines the algorithm used to generate the private key.

CryptoProviders -> (list)

Defines the cryptographic providers used to generate the private key.

(string)

KeySpec -> (string)

Defines the purpose of the private key. Set it to âKEY_EXCHANGEâ or âSIGNATUREâ value.

KeyUsageProperty -> (tagged union structure)

The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PropertyFlags`, `PropertyType`.

PropertyFlags -> (structure)

You can specify key usage for encryption, key agreement, and signature. You can use property flags or property type but not both.

Decrypt -> (boolean)

Allows key for encryption and decryption.

KeyAgreement -> (boolean)

Allows key exchange without encryption.

Sign -> (boolean)

Allow key use for digital signature.

PropertyType -> (string)

You can specify all key usages using property type ALL. You can use property type or property flags but not both.

MinimalKeyLength -> (integer)

Set the minimum key length of the private key.

PrivateKeyFlags -> (structure)

Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.

ClientVersion -> (string)

Defines the minimum client compatibility.

ExportableKey -> (boolean)

Allows the private key to be exported.

RequireAlternateSignatureAlgorithm -> (boolean)

Requires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.

RequireSameKeyRenewal -> (boolean)

Renew certificate using the same private key.

StrongKeyProtectionRequired -> (boolean)

Require user input when using the private key for enrollment.

UseLegacyProvider -> (boolean)

Specifies the cryptographic service provider category used to generate private keys. Set to TRUE to use Legacy Cryptographic Service Providers and FALSE to use Key Storage Providers.

SubjectNameFlags -> (structure)

Subject name flags describe the subject name and subject alternate name that is included in a certificate.

RequireCommonName -> (boolean)

Include the common name in the subject name.

RequireDirectoryPath -> (boolean)

Include the directory path in the subject name.

RequireDnsAsCn -> (boolean)

Include the DNS as common name in the subject name.

RequireEmail -> (boolean)

Include the subjectâs email in the subject name.

SanRequireDirectoryGuid -> (boolean)

Include the globally unique identifier (GUID) in the subject alternate name.

SanRequireDns -> (boolean)

Include the DNS in the subject alternate name.

SanRequireDomainDns -> (boolean)

Include the domain DNS in the subject alternate name.

SanRequireEmail -> (boolean)

Include the subjectâs email in the subject alternate name.

SanRequireSpn -> (boolean)

Include the service principal name (SPN) in the subject alternate name.

SanRequireUpn -> (boolean)

Include the user principal name (UPN) in the subject alternate name.

SupersededTemplates -> (list)

List of templates in Active Directory that are superseded by this template.

(string)

JSON Syntax:

```
{
  "TemplateV2": {
    "CertificateValidity": {
      "RenewalPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      },
      "ValidityPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      }
    },
    "EnrollmentFlags": {
      "EnableKeyReuseOnNtTokenKeysetStorageFull": true|false,
      "IncludeSymmetricAlgorithms": true|false,
      "NoSecurityExtension": true|false,
      "RemoveInvalidCertificateFromPersonalStore": true|false,
      "UserInteractionRequired": true|false
    },
    "Extensions": {
      "ApplicationPolicies": {
        "Critical": true|false,
        "Policies": [
          {
            "PolicyObjectIdentifier": "string",
            "PolicyType": "ALL_APPLICATION_POLICIES"|"ANY_PURPOSE"|"ATTESTATION_IDENTITY_KEY_CERTIFICATE"|"CERTIFICATE_REQUEST_AGENT"|"CLIENT_AUTHENTICATION"|"CODE_SIGNING"|"CTL_USAGE"|"DIGITAL_RIGHTS"|"DIRECTORY_SERVICE_EMAIL_REPLICATION"|"DISALLOWED_LIST"|"DNS_SERVER_TRUST"|"DOCUMENT_ENCRYPTION"|"DOCUMENT_SIGNING"|"DYNAMIC_CODE_GENERATOR"|"EARLY_LAUNCH_ANTIMALWARE_DRIVER"|"EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"ENCLAVE"|"ENCRYPTING_FILE_SYSTEM"|"ENDORSEMENT_KEY_CERTIFICATE"|"FILE_RECOVERY"|"HAL_EXTENSION"|"IP_SECURITY_END_SYSTEM"|"IP_SECURITY_IKE_INTERMEDIATE"|"IP_SECURITY_TUNNEL_TERMINATION"|"IP_SECURITY_USER"|"ISOLATED_USER_MODE"|"KDC_AUTHENTICATION"|"KERNEL_MODE_CODE_SIGNING"|"KEY_PACK_LICENSES"|"KEY_RECOVERY"|"KEY_RECOVERY_AGENT"|"LICENSE_SERVER_VERIFICATION"|"LIFETIME_SIGNING"|"MICROSOFT_PUBLISHER"|"MICROSOFT_TIME_STAMPING"|"MICROSOFT_TRUST_LIST_SIGNING"|"OCSP_SIGNING"|"OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"PLATFORM_CERTIFICATE"|"PREVIEW_BUILD_SIGNING"|"PRIVATE_KEY_ARCHIVAL"|"PROTECTED_PROCESS_LIGHT_VERIFICATION"|"PROTECTED_PROCESS_VERIFICATION"|"QUALIFIED_SUBORDINATION"|"REVOKED_LIST_SIGNER"|"ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION"|"ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION"|"ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL"|"ROOT_LIST_SIGNER"|"SECURE_EMAIL"|"SERVER_AUTHENTICATION"|"SMART_CARD_LOGIN"|"SPC_ENCRYPTED_DIGEST_RETRY_COUNT"|"SPC_RELAXED_PE_MARKER_CHECK"|"TIME_STAMPING"|"WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_VERIFICATION"|"WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION"|"WINDOWS_KITS_COMPONENT"|"WINDOWS_RT_VERIFICATION"|"WINDOWS_SOFTWARE_EXTENSION_VERIFICATION"|"WINDOWS_STORE"|"WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"WINDOWS_TCB_COMPONENT"|"WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT"|"WINDOWS_UPDATE"
          }
          ...
        ]
      },
      "KeyUsage": {
        "Critical": true|false,
        "UsageFlags": {
          "DataEncipherment": true|false,
          "DigitalSignature": true|false,
          "KeyAgreement": true|false,
          "KeyEncipherment": true|false,
          "NonRepudiation": true|false
        }
      }
    },
    "GeneralFlags": {
      "AutoEnrollment": true|false,
      "MachineType": true|false
    },
    "PrivateKeyAttributes": {
      "CryptoProviders": ["string", ...],
      "KeySpec": "KEY_EXCHANGE"|"SIGNATURE",
      "MinimalKeyLength": integer
    },
    "PrivateKeyFlags": {
      "ClientVersion": "WINDOWS_SERVER_2003"|"WINDOWS_SERVER_2008"|"WINDOWS_SERVER_2008_R2"|"WINDOWS_SERVER_2012"|"WINDOWS_SERVER_2012_R2"|"WINDOWS_SERVER_2016",
      "ExportableKey": true|false,
      "StrongKeyProtectionRequired": true|false
    },
    "SubjectNameFlags": {
      "RequireCommonName": true|false,
      "RequireDirectoryPath": true|false,
      "RequireDnsAsCn": true|false,
      "RequireEmail": true|false,
      "SanRequireDirectoryGuid": true|false,
      "SanRequireDns": true|false,
      "SanRequireDomainDns": true|false,
      "SanRequireEmail": true|false,
      "SanRequireSpn": true|false,
      "SanRequireUpn": true|false
    },
    "SupersededTemplates": ["string", ...]
  },
  "TemplateV3": {
    "CertificateValidity": {
      "RenewalPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      },
      "ValidityPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      }
    },
    "EnrollmentFlags": {
      "EnableKeyReuseOnNtTokenKeysetStorageFull": true|false,
      "IncludeSymmetricAlgorithms": true|false,
      "NoSecurityExtension": true|false,
      "RemoveInvalidCertificateFromPersonalStore": true|false,
      "UserInteractionRequired": true|false
    },
    "Extensions": {
      "ApplicationPolicies": {
        "Critical": true|false,
        "Policies": [
          {
            "PolicyObjectIdentifier": "string",
            "PolicyType": "ALL_APPLICATION_POLICIES"|"ANY_PURPOSE"|"ATTESTATION_IDENTITY_KEY_CERTIFICATE"|"CERTIFICATE_REQUEST_AGENT"|"CLIENT_AUTHENTICATION"|"CODE_SIGNING"|"CTL_USAGE"|"DIGITAL_RIGHTS"|"DIRECTORY_SERVICE_EMAIL_REPLICATION"|"DISALLOWED_LIST"|"DNS_SERVER_TRUST"|"DOCUMENT_ENCRYPTION"|"DOCUMENT_SIGNING"|"DYNAMIC_CODE_GENERATOR"|"EARLY_LAUNCH_ANTIMALWARE_DRIVER"|"EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"ENCLAVE"|"ENCRYPTING_FILE_SYSTEM"|"ENDORSEMENT_KEY_CERTIFICATE"|"FILE_RECOVERY"|"HAL_EXTENSION"|"IP_SECURITY_END_SYSTEM"|"IP_SECURITY_IKE_INTERMEDIATE"|"IP_SECURITY_TUNNEL_TERMINATION"|"IP_SECURITY_USER"|"ISOLATED_USER_MODE"|"KDC_AUTHENTICATION"|"KERNEL_MODE_CODE_SIGNING"|"KEY_PACK_LICENSES"|"KEY_RECOVERY"|"KEY_RECOVERY_AGENT"|"LICENSE_SERVER_VERIFICATION"|"LIFETIME_SIGNING"|"MICROSOFT_PUBLISHER"|"MICROSOFT_TIME_STAMPING"|"MICROSOFT_TRUST_LIST_SIGNING"|"OCSP_SIGNING"|"OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"PLATFORM_CERTIFICATE"|"PREVIEW_BUILD_SIGNING"|"PRIVATE_KEY_ARCHIVAL"|"PROTECTED_PROCESS_LIGHT_VERIFICATION"|"PROTECTED_PROCESS_VERIFICATION"|"QUALIFIED_SUBORDINATION"|"REVOKED_LIST_SIGNER"|"ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION"|"ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION"|"ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL"|"ROOT_LIST_SIGNER"|"SECURE_EMAIL"|"SERVER_AUTHENTICATION"|"SMART_CARD_LOGIN"|"SPC_ENCRYPTED_DIGEST_RETRY_COUNT"|"SPC_RELAXED_PE_MARKER_CHECK"|"TIME_STAMPING"|"WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_VERIFICATION"|"WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION"|"WINDOWS_KITS_COMPONENT"|"WINDOWS_RT_VERIFICATION"|"WINDOWS_SOFTWARE_EXTENSION_VERIFICATION"|"WINDOWS_STORE"|"WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"WINDOWS_TCB_COMPONENT"|"WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT"|"WINDOWS_UPDATE"
          }
          ...
        ]
      },
      "KeyUsage": {
        "Critical": true|false,
        "UsageFlags": {
          "DataEncipherment": true|false,
          "DigitalSignature": true|false,
          "KeyAgreement": true|false,
          "KeyEncipherment": true|false,
          "NonRepudiation": true|false
        }
      }
    },
    "GeneralFlags": {
      "AutoEnrollment": true|false,
      "MachineType": true|false
    },
    "HashAlgorithm": "SHA256"|"SHA384"|"SHA512",
    "PrivateKeyAttributes": {
      "Algorithm": "RSA"|"ECDH_P256"|"ECDH_P384"|"ECDH_P521",
      "CryptoProviders": ["string", ...],
      "KeySpec": "KEY_EXCHANGE"|"SIGNATURE",
      "KeyUsageProperty": {
        "PropertyFlags": {
          "Decrypt": true|false,
          "KeyAgreement": true|false,
          "Sign": true|false
        },
        "PropertyType": "ALL"
      },
      "MinimalKeyLength": integer
    },
    "PrivateKeyFlags": {
      "ClientVersion": "WINDOWS_SERVER_2008"|"WINDOWS_SERVER_2008_R2"|"WINDOWS_SERVER_2012"|"WINDOWS_SERVER_2012_R2"|"WINDOWS_SERVER_2016",
      "ExportableKey": true|false,
      "RequireAlternateSignatureAlgorithm": true|false,
      "StrongKeyProtectionRequired": true|false
    },
    "SubjectNameFlags": {
      "RequireCommonName": true|false,
      "RequireDirectoryPath": true|false,
      "RequireDnsAsCn": true|false,
      "RequireEmail": true|false,
      "SanRequireDirectoryGuid": true|false,
      "SanRequireDns": true|false,
      "SanRequireDomainDns": true|false,
      "SanRequireEmail": true|false,
      "SanRequireSpn": true|false,
      "SanRequireUpn": true|false
    },
    "SupersededTemplates": ["string", ...]
  },
  "TemplateV4": {
    "CertificateValidity": {
      "RenewalPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      },
      "ValidityPeriod": {
        "Period": long,
        "PeriodType": "HOURS"|"DAYS"|"WEEKS"|"MONTHS"|"YEARS"
      }
    },
    "EnrollmentFlags": {
      "EnableKeyReuseOnNtTokenKeysetStorageFull": true|false,
      "IncludeSymmetricAlgorithms": true|false,
      "NoSecurityExtension": true|false,
      "RemoveInvalidCertificateFromPersonalStore": true|false,
      "UserInteractionRequired": true|false
    },
    "Extensions": {
      "ApplicationPolicies": {
        "Critical": true|false,
        "Policies": [
          {
            "PolicyObjectIdentifier": "string",
            "PolicyType": "ALL_APPLICATION_POLICIES"|"ANY_PURPOSE"|"ATTESTATION_IDENTITY_KEY_CERTIFICATE"|"CERTIFICATE_REQUEST_AGENT"|"CLIENT_AUTHENTICATION"|"CODE_SIGNING"|"CTL_USAGE"|"DIGITAL_RIGHTS"|"DIRECTORY_SERVICE_EMAIL_REPLICATION"|"DISALLOWED_LIST"|"DNS_SERVER_TRUST"|"DOCUMENT_ENCRYPTION"|"DOCUMENT_SIGNING"|"DYNAMIC_CODE_GENERATOR"|"EARLY_LAUNCH_ANTIMALWARE_DRIVER"|"EMBEDDED_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"ENCLAVE"|"ENCRYPTING_FILE_SYSTEM"|"ENDORSEMENT_KEY_CERTIFICATE"|"FILE_RECOVERY"|"HAL_EXTENSION"|"IP_SECURITY_END_SYSTEM"|"IP_SECURITY_IKE_INTERMEDIATE"|"IP_SECURITY_TUNNEL_TERMINATION"|"IP_SECURITY_USER"|"ISOLATED_USER_MODE"|"KDC_AUTHENTICATION"|"KERNEL_MODE_CODE_SIGNING"|"KEY_PACK_LICENSES"|"KEY_RECOVERY"|"KEY_RECOVERY_AGENT"|"LICENSE_SERVER_VERIFICATION"|"LIFETIME_SIGNING"|"MICROSOFT_PUBLISHER"|"MICROSOFT_TIME_STAMPING"|"MICROSOFT_TRUST_LIST_SIGNING"|"OCSP_SIGNING"|"OEM_WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"PLATFORM_CERTIFICATE"|"PREVIEW_BUILD_SIGNING"|"PRIVATE_KEY_ARCHIVAL"|"PROTECTED_PROCESS_LIGHT_VERIFICATION"|"PROTECTED_PROCESS_VERIFICATION"|"QUALIFIED_SUBORDINATION"|"REVOKED_LIST_SIGNER"|"ROOT_PROGRAM_AUTO_UPDATE_CA_REVOCATION"|"ROOT_PROGRAM_AUTO_UPDATE_END_REVOCATION"|"ROOT_PROGRAM_NO_OSCP_FAILOVER_TO_CRL"|"ROOT_LIST_SIGNER"|"SECURE_EMAIL"|"SERVER_AUTHENTICATION"|"SMART_CARD_LOGIN"|"SPC_ENCRYPTED_DIGEST_RETRY_COUNT"|"SPC_RELAXED_PE_MARKER_CHECK"|"TIME_STAMPING"|"WINDOWS_HARDWARE_DRIVER_ATTESTED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_EXTENDED_VERIFICATION"|"WINDOWS_HARDWARE_DRIVER_VERIFICATION"|"WINDOWS_HELLO_RECOVERY_KEY_ENCRYPTION"|"WINDOWS_KITS_COMPONENT"|"WINDOWS_RT_VERIFICATION"|"WINDOWS_SOFTWARE_EXTENSION_VERIFICATION"|"WINDOWS_STORE"|"WINDOWS_SYSTEM_COMPONENT_VERIFICATION"|"WINDOWS_TCB_COMPONENT"|"WINDOWS_THIRD_PARTY_APPLICATION_COMPONENT"|"WINDOWS_UPDATE"
          }
          ...
        ]
      },
      "KeyUsage": {
        "Critical": true|false,
        "UsageFlags": {
          "DataEncipherment": true|false,
          "DigitalSignature": true|false,
          "KeyAgreement": true|false,
          "KeyEncipherment": true|false,
          "NonRepudiation": true|false
        }
      }
    },
    "GeneralFlags": {
      "AutoEnrollment": true|false,
      "MachineType": true|false
    },
    "HashAlgorithm": "SHA256"|"SHA384"|"SHA512",
    "PrivateKeyAttributes": {
      "Algorithm": "RSA"|"ECDH_P256"|"ECDH_P384"|"ECDH_P521",
      "CryptoProviders": ["string", ...],
      "KeySpec": "KEY_EXCHANGE"|"SIGNATURE",
      "KeyUsageProperty": {
        "PropertyFlags": {
          "Decrypt": true|false,
          "KeyAgreement": true|false,
          "Sign": true|false
        },
        "PropertyType": "ALL"
      },
      "MinimalKeyLength": integer
    },
    "PrivateKeyFlags": {
      "ClientVersion": "WINDOWS_SERVER_2012"|"WINDOWS_SERVER_2012_R2"|"WINDOWS_SERVER_2016",
      "ExportableKey": true|false,
      "RequireAlternateSignatureAlgorithm": true|false,
      "RequireSameKeyRenewal": true|false,
      "StrongKeyProtectionRequired": true|false,
      "UseLegacyProvider": true|false
    },
    "SubjectNameFlags": {
      "RequireCommonName": true|false,
      "RequireDirectoryPath": true|false,
      "RequireDnsAsCn": true|false,
      "RequireEmail": true|false,
      "SanRequireDirectoryGuid": true|false,
      "SanRequireDns": true|false,
      "SanRequireDomainDns": true|false,
      "SanRequireEmail": true|false,
      "SanRequireSpn": true|false,
      "SanRequireUpn": true|false
    },
    "SupersededTemplates": ["string", ...]
  }
}
```

`--reenroll-all-certificate-holders` | `--no-reenroll-all-certificate-holders` (boolean)

This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.

`--template-arn` (string)

The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html) .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

None