# transfer-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/index.html#cli-aws-route53domains) ]

# transfer-domain

## Description

Transfers a domain from another registrar to Amazon Route 53.

For more information about transferring domains, see the following topics:

- For transfer requirements, a detailed procedure, and information about viewing the status of a domain that youâre transferring to Route 53, see [Transferring Registration for a Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html) in the *Amazon Route 53 Developer Guide* .
- For information about how to transfer a domain from one Amazon Web Services account to another, see [TransferDomainToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html) .
- For information about how to transfer a domain to another domain registrar, see [Transferring a Domain from Amazon Route 53 to Another Registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html) in the *Amazon Route 53 Developer Guide* .

### Warning

During the transfer of any country code top-level domains (ccTLDs) to Route 53, except for .cc and .tv, updates to the owner contact are ignored and the owner contact data from the registry is used. You can update the owner contact after the transfer is complete. For more information, see [UpdateDomainContact](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html) .

If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you transfer your DNS service to Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.

### Warning

If the registrar for your domain is also the DNS service provider for the domain and you donât transfer DNS service to another provider, your website, email, and the web applications associated with the domain might become unavailable.

If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesnât complete successfully, the domain registrant will be notified by email.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/TransferDomain)

## Synopsis

```
transfer-domain
--domain-name <value>
[--idn-lang-code <value>]
--duration-in-years <value>
[--nameservers <value>]
[--auth-code <value>]
[--auto-renew | --no-auto-renew]
--admin-contact <value>
--registrant-contact <value>
--tech-contact <value>
[--privacy-protect-admin-contact | --no-privacy-protect-admin-contact]
[--privacy-protect-registrant-contact | --no-privacy-protect-registrant-contact]
[--privacy-protect-tech-contact | --no-privacy-protect-tech-contact]
[--billing-contact <value>]
[--privacy-protect-billing-contact | --no-privacy-protect-billing-contact]
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

`--domain-name` (string)

The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide* .

The domain name can contain only the following characters:

- Letters a through z. Domain names are not case sensitive.
- Numbers 0 through 9.
- Hyphen (-). You canât specify a hyphen at the beginning or end of a label.
- Period (.) to separate the labels in the name, such as the `.` in `example.com` .

`--idn-lang-code` (string)

Reserved for future use.

`--duration-in-years` (integer)

The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.

Default: 1

`--nameservers` (list)

Contains details for the host and glue IP addresses.

(structure)

Name server includes the following elements.

Name -> (string)

The fully qualified host name of the name server.

Constraint: Maximum 255 characters

GlueIps -> (list)

Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.

Constraints: The list can contain only one IPv4 and one IPv6 address.

(string)

Shorthand Syntax:

```
Name=string,GlueIps=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "GlueIps": ["string", ...]
  }
  ...
]
```

`--auth-code` (string)

The authorization code for the domain. You get this value from the current registrar.

`--auto-renew` | `--no-auto-renew` (boolean)

Indicates whether the domain will be automatically renewed (true) or not (false). Auto renewal only takes effect after the account is charged.

Default: true

`--admin-contact` (structure)

Provides detailed contact information.

FirstName -> (string)

First name of contact.

LastName -> (string)

Last name of contact.

ContactType -> (string)

Indicates whether the contact is a person, company, association, or public organization. Note the following:

- If you specify a value other than `PERSON` , you must also specify a value for `OrganizationName` .
- For some TLDs, the privacy protection available depends on the value that you specify for `Contact Type` . For the privacy protection settings for your TLD, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*
- For .es domains, the value of `ContactType` must be `PERSON` for all three contacts.

OrganizationName -> (string)

Name of the organization for contact types other than `PERSON` .

AddressLine1 -> (string)

First line of the contactâs address.

AddressLine2 -> (string)

Second line of contactâs address, if any.

City -> (string)

The city of the contactâs address.

State -> (string)

The state or province of the contactâs city.

CountryCode -> (string)

Code for the country of the contactâs address.

ZipCode -> (string)

The zip or postal code of the contactâs address.

PhoneNumber -> (string)

The phone number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code>]â. For example, a US phone number might appear as `"+1.1234567890"` .

Email -> (string)

Email address of the contact.

Fax -> (string)

Fax number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code]â. For example, a US phone number might appear as `"+1.1234567890"` .

ExtraParams -> (list)

A list of name-value pairs for parameters required by certain top-level domains.

(structure)

ExtraParam includes the following elements.

Name -> (string)

The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

- `AU_ID_NUMBER`
- `AU_ID_TYPE`   Valid values include the following:

- `ABN` (Australian business number)
- `ACN` (Australian company number)
- `TM` (Trademark number)

.ca
- `BRAND_NUMBER`
- `CA_BUSINESS_ENTITY_TYPE`   Valid values include the following:

- `BANK` (Bank)
- `COMMERCIAL_COMPANY` (Commercial company)
- `COMPANY` (Company)
- `COOPERATION` (Cooperation)
- `COOPERATIVE` (Cooperative)
- `COOPRIX` (Cooprix)
- `CORP` (Corporation)
- `CREDIT_UNION` (Credit union)
- `FOMIA` (Federation of mutual insurance associations)
- `INC` (Incorporated)
- `LTD` (Limited)
- `LTEE` (LimitÃ©e)
- `LLC` (Limited liability corporation)
- `LLP` (Limited liability partnership)
- `LTE` (Lte.)
- `MBA` (Mutual benefit association)
- `MIC` (Mutual insurance company)
- `NFP` (Not-for-profit corporation)
- `SA` (S.A.)
- `SAVINGS_COMPANY` (Savings company)
- `SAVINGS_UNION` (Savings union)
- `SARL` (SociÃ©tÃ© Ã  responsabilitÃ© limitÃ©e)
- `TRUST` (Trust)
- `ULC` (Unlimited liability corporation)
- `CA_LEGAL_TYPE`   When `ContactType` is `PERSON` , valid values include the following:

- `ABO` (Aboriginal Peoples indigenous to Canada)
- `CCT` (Canadian citizen)
- `LGR` (Legal Representative of a Canadian Citizen or Permanent Resident)
- `RES` (Permanent resident of Canada)

When `ContactType` is a value other than `PERSON` , valid values include the following:

- `ASS` (Canadian unincorporated association)
- `CCO` (Canadian corporation)
- `EDU` (Canadian educational institution)
- `GOV` (Government or government entity in Canada)
- `HOP` (Canadian Hospital)
- `INB` (Indian Band recognized by the Indian Act of Canada)
- `LAM` (Canadian Library, Archive, or Museum)
- `MAJ` (Her/His Majesty the Queen/King)
- `OMK` (Official mark registered in Canada)
- `PLT` (Canadian Political Party)
- `PRT` (Partnership Registered in Canada)
- `TDM` (Trademark registered in Canada)
- `TRD` (Canadian Trade Union)
- `TRS` (Trust established in Canada)

.es

- `ES_IDENTIFICATION`   The value of `ES_IDENTIFICATION` depends on the following values:
- The value of `ES_LEGAL_FORM`
- The value of `ES_IDENTIFICATION_TYPE`

**If ``ES_LEGAL_FORM`` is any value other than ``INDIVIDUAL`` :**

- Specify 1 letter + 8 numbers (CIF [Certificado de IdentificaciÃ³n Fiscal])
- Example: B12345678

**If ``ES_LEGAL_FORM`` is ``INDIVIDUAL`` , the value that you specify for ``ES_IDENTIFICATION`` depends on the value of ``ES_IDENTIFICATION_TYPE`` :**

- If `ES_IDENTIFICATION_TYPE` is `DNI_AND_NIF` (for Spanish contacts):
- Specify 8 numbers + 1 letter (DNI [Documento Nacional de Identidad], NIF [NÃºmero de IdentificaciÃ³n Fiscal])
- Example: 12345678M
- If `ES_IDENTIFICATION_TYPE` is `NIE` (for foreigners with legal residence):
- Specify 1 letter + 7 numbers + 1 letter ( NIE [NÃºmero de Identidad de Extranjero])
- Example: Y1234567X
- If `ES_IDENTIFICATION_TYPE` is `OTHER` (for contacts outside of Spain):
- Specify a passport number, drivers license number, or national identity card number

- `ES_IDENTIFICATION_TYPE`   Valid values include the following:

- `DNI_AND_NIF` (For Spanish contacts)
- `NIE` (For foreigners with legal residence)
- `OTHER` (For contacts outside of Spain)
- `ES_LEGAL_FORM`   Valid values include the following:

- `ASSOCIATION`
- `CENTRAL_GOVERNMENT_BODY`
- `CIVIL_SOCIETY`
- `COMMUNITY_OF_OWNERS`
- `COMMUNITY_PROPERTY`
- `CONSULATE`
- `COOPERATIVE`
- `DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL`
- `ECONOMIC_INTEREST_GROUP`
- `EMBASSY`
- `ENTITY_MANAGING_NATURAL_AREAS`
- `FARM_PARTNERSHIP`
- `FOUNDATION`
- `GENERAL_AND_LIMITED_PARTNERSHIP`
- `GENERAL_PARTNERSHIP`
- `INDIVIDUAL`
- `LIMITED_COMPANY`
- `LOCAL_AUTHORITY`
- `LOCAL_PUBLIC_ENTITY`
- `MUTUAL_INSURANCE_COMPANY`
- `NATIONAL_PUBLIC_ENTITY`
- `ORDER_OR_RELIGIOUS_INSTITUTION`
- `OTHERS (Only for contacts outside of Spain)`
- `POLITICAL_PARTY`
- `PROFESSIONAL_ASSOCIATION`
- `PUBLIC_LAW_ASSOCIATION`
- `PUBLIC_LIMITED_COMPANY`
- `REGIONAL_GOVERNMENT_BODY`
- `REGIONAL_PUBLIC_ENTITY`
- `SAVINGS_BANK`
- `SPANISH_OFFICE`
- `SPORTS_ASSOCIATION`
- `SPORTS_FEDERATION`
- `SPORTS_LIMITED_COMPANY`
- `TEMPORARY_ALLIANCE_OF_ENTERPRISES`
- `TRADE_UNION`
- `WORKER_OWNED_COMPANY`
- `WORKER_OWNED_LIMITED_COMPANY`

.eu
- `EU_COUNTRY_OF_CITIZENSHIP`

.fi
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `FI_BUSINESS_NUMBER`
- `FI_ID_NUMBER`
- `FI_NATIONALITY`   Valid values include the following:

- `FINNISH`
- `NOT_FINNISH`
- `FI_ORGANIZATION_TYPE`   Valid values include the following:

- `COMPANY`
- `CORPORATION`
- `GOVERNMENT`
- `INSTITUTION`
- `POLITICAL_PARTY`
- `PUBLIC_COMMUNITY`
- `TOWNSHIP`

.it
- `IT_NATIONALITY`
- `IT_PIN`
- `IT_REGISTRANT_ENTITY_TYPE`   Valid values include the following:

- `FOREIGNERS`
- `FREELANCE_WORKERS` (Freelance workers and professionals)
- `ITALIAN_COMPANIES` (Italian companies and one-person companies)
- `NON_PROFIT_ORGANIZATIONS`
- `OTHER_SUBJECTS`
- `PUBLIC_ORGANIZATIONS`

.ru
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `RU_PASSPORT_DATA`

.se
- `BIRTH_COUNTRY`
- `SE_ID_NUMBER`

.sg
- `SG_ID_NUMBER`

.uk, .co.uk, .me.uk, and .org.uk
- `UK_CONTACT_TYPE`   Valid values include the following:

- `CRC` (UK Corporation by Royal Charter)
- `FCORP` (Non-UK Corporation)
- `FIND` (Non-UK Individual, representing self)
- `FOTHER` (Non-UK Entity that does not fit into any other category)
- `GOV` (UK Government Body)
- `IND` (UK Individual (representing self))
- `IP` (UK Industrial/Provident Registered Company)
- `LLP` (UK Limited Liability Partnership)
- `LTD` (UK Limited Company)
- `OTHER` (UK Entity that does not fit into any other category)
- `PLC` (UK Public Limited Company)
- `PTNR` (UK Partnership)
- `RCHAR` (UK Registered Charity)
- `SCH` (UK School)
- `STAT` (UK Statutory Body)
- `STRA` (UK Sole Trader)
- `UK_COMPANY_NUMBER`

In addition, many TLDs require a `VAT_NUMBER` .

Value -> (string)

The value that corresponds with the name of an extra parameter.

Shorthand Syntax:

```
FirstName=string,LastName=string,ContactType=string,OrganizationName=string,AddressLine1=string,AddressLine2=string,City=string,State=string,CountryCode=string,ZipCode=string,PhoneNumber=string,Email=string,Fax=string,ExtraParams=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "FirstName": "string",
  "LastName": "string",
  "ContactType": "PERSON"|"COMPANY"|"ASSOCIATION"|"PUBLIC_BODY"|"RESELLER",
  "OrganizationName": "string",
  "AddressLine1": "string",
  "AddressLine2": "string",
  "City": "string",
  "State": "string",
  "CountryCode": "AC"|"AD"|"AE"|"AF"|"AG"|"AI"|"AL"|"AM"|"AN"|"AO"|"AQ"|"AR"|"AS"|"AT"|"AU"|"AW"|"AX"|"AZ"|"BA"|"BB"|"BD"|"BE"|"BF"|"BG"|"BH"|"BI"|"BJ"|"BL"|"BM"|"BN"|"BO"|"BQ"|"BR"|"BS"|"BT"|"BV"|"BW"|"BY"|"BZ"|"CA"|"CC"|"CD"|"CF"|"CG"|"CH"|"CI"|"CK"|"CL"|"CM"|"CN"|"CO"|"CR"|"CU"|"CV"|"CW"|"CX"|"CY"|"CZ"|"DE"|"DJ"|"DK"|"DM"|"DO"|"DZ"|"EC"|"EE"|"EG"|"EH"|"ER"|"ES"|"ET"|"FI"|"FJ"|"FK"|"FM"|"FO"|"FR"|"GA"|"GB"|"GD"|"GE"|"GF"|"GG"|"GH"|"GI"|"GL"|"GM"|"GN"|"GP"|"GQ"|"GR"|"GS"|"GT"|"GU"|"GW"|"GY"|"HK"|"HM"|"HN"|"HR"|"HT"|"HU"|"ID"|"IE"|"IL"|"IM"|"IN"|"IO"|"IQ"|"IR"|"IS"|"IT"|"JE"|"JM"|"JO"|"JP"|"KE"|"KG"|"KH"|"KI"|"KM"|"KN"|"KP"|"KR"|"KW"|"KY"|"KZ"|"LA"|"LB"|"LC"|"LI"|"LK"|"LR"|"LS"|"LT"|"LU"|"LV"|"LY"|"MA"|"MC"|"MD"|"ME"|"MF"|"MG"|"MH"|"MK"|"ML"|"MM"|"MN"|"MO"|"MP"|"MQ"|"MR"|"MS"|"MT"|"MU"|"MV"|"MW"|"MX"|"MY"|"MZ"|"NA"|"NC"|"NE"|"NF"|"NG"|"NI"|"NL"|"NO"|"NP"|"NR"|"NU"|"NZ"|"OM"|"PA"|"PE"|"PF"|"PG"|"PH"|"PK"|"PL"|"PM"|"PN"|"PR"|"PS"|"PT"|"PW"|"PY"|"QA"|"RE"|"RO"|"RS"|"RU"|"RW"|"SA"|"SB"|"SC"|"SD"|"SE"|"SG"|"SH"|"SI"|"SJ"|"SK"|"SL"|"SM"|"SN"|"SO"|"SR"|"SS"|"ST"|"SV"|"SX"|"SY"|"SZ"|"TC"|"TD"|"TF"|"TG"|"TH"|"TJ"|"TK"|"TL"|"TM"|"TN"|"TO"|"TP"|"TR"|"TT"|"TV"|"TW"|"TZ"|"UA"|"UG"|"US"|"UY"|"UZ"|"VA"|"VC"|"VE"|"VG"|"VI"|"VN"|"VU"|"WF"|"WS"|"YE"|"YT"|"ZA"|"ZM"|"ZW",
  "ZipCode": "string",
  "PhoneNumber": "string",
  "Email": "string",
  "Fax": "string",
  "ExtraParams": [
    {
      "Name": "DUNS_NUMBER"|"BRAND_NUMBER"|"BIRTH_DEPARTMENT"|"BIRTH_DATE_IN_YYYY_MM_DD"|"BIRTH_COUNTRY"|"BIRTH_CITY"|"DOCUMENT_NUMBER"|"AU_ID_NUMBER"|"AU_ID_TYPE"|"CA_LEGAL_TYPE"|"CA_BUSINESS_ENTITY_TYPE"|"CA_LEGAL_REPRESENTATIVE"|"CA_LEGAL_REPRESENTATIVE_CAPACITY"|"ES_IDENTIFICATION"|"ES_IDENTIFICATION_TYPE"|"ES_LEGAL_FORM"|"FI_BUSINESS_NUMBER"|"FI_ID_NUMBER"|"FI_NATIONALITY"|"FI_ORGANIZATION_TYPE"|"IT_NATIONALITY"|"IT_PIN"|"IT_REGISTRANT_ENTITY_TYPE"|"RU_PASSPORT_DATA"|"SE_ID_NUMBER"|"SG_ID_NUMBER"|"VAT_NUMBER"|"UK_CONTACT_TYPE"|"UK_COMPANY_NUMBER"|"EU_COUNTRY_OF_CITIZENSHIP"|"AU_PRIORITY_TOKEN",
      "Value": "string"
    }
    ...
  ]
}
```

`--registrant-contact` (structure)

Provides detailed contact information.

FirstName -> (string)

First name of contact.

LastName -> (string)

Last name of contact.

ContactType -> (string)

Indicates whether the contact is a person, company, association, or public organization. Note the following:

- If you specify a value other than `PERSON` , you must also specify a value for `OrganizationName` .
- For some TLDs, the privacy protection available depends on the value that you specify for `Contact Type` . For the privacy protection settings for your TLD, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*
- For .es domains, the value of `ContactType` must be `PERSON` for all three contacts.

OrganizationName -> (string)

Name of the organization for contact types other than `PERSON` .

AddressLine1 -> (string)

First line of the contactâs address.

AddressLine2 -> (string)

Second line of contactâs address, if any.

City -> (string)

The city of the contactâs address.

State -> (string)

The state or province of the contactâs city.

CountryCode -> (string)

Code for the country of the contactâs address.

ZipCode -> (string)

The zip or postal code of the contactâs address.

PhoneNumber -> (string)

The phone number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code>]â. For example, a US phone number might appear as `"+1.1234567890"` .

Email -> (string)

Email address of the contact.

Fax -> (string)

Fax number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code]â. For example, a US phone number might appear as `"+1.1234567890"` .

ExtraParams -> (list)

A list of name-value pairs for parameters required by certain top-level domains.

(structure)

ExtraParam includes the following elements.

Name -> (string)

The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

- `AU_ID_NUMBER`
- `AU_ID_TYPE`   Valid values include the following:

- `ABN` (Australian business number)
- `ACN` (Australian company number)
- `TM` (Trademark number)

.ca
- `BRAND_NUMBER`
- `CA_BUSINESS_ENTITY_TYPE`   Valid values include the following:

- `BANK` (Bank)
- `COMMERCIAL_COMPANY` (Commercial company)
- `COMPANY` (Company)
- `COOPERATION` (Cooperation)
- `COOPERATIVE` (Cooperative)
- `COOPRIX` (Cooprix)
- `CORP` (Corporation)
- `CREDIT_UNION` (Credit union)
- `FOMIA` (Federation of mutual insurance associations)
- `INC` (Incorporated)
- `LTD` (Limited)
- `LTEE` (LimitÃ©e)
- `LLC` (Limited liability corporation)
- `LLP` (Limited liability partnership)
- `LTE` (Lte.)
- `MBA` (Mutual benefit association)
- `MIC` (Mutual insurance company)
- `NFP` (Not-for-profit corporation)
- `SA` (S.A.)
- `SAVINGS_COMPANY` (Savings company)
- `SAVINGS_UNION` (Savings union)
- `SARL` (SociÃ©tÃ© Ã  responsabilitÃ© limitÃ©e)
- `TRUST` (Trust)
- `ULC` (Unlimited liability corporation)
- `CA_LEGAL_TYPE`   When `ContactType` is `PERSON` , valid values include the following:

- `ABO` (Aboriginal Peoples indigenous to Canada)
- `CCT` (Canadian citizen)
- `LGR` (Legal Representative of a Canadian Citizen or Permanent Resident)
- `RES` (Permanent resident of Canada)

When `ContactType` is a value other than `PERSON` , valid values include the following:

- `ASS` (Canadian unincorporated association)
- `CCO` (Canadian corporation)
- `EDU` (Canadian educational institution)
- `GOV` (Government or government entity in Canada)
- `HOP` (Canadian Hospital)
- `INB` (Indian Band recognized by the Indian Act of Canada)
- `LAM` (Canadian Library, Archive, or Museum)
- `MAJ` (Her/His Majesty the Queen/King)
- `OMK` (Official mark registered in Canada)
- `PLT` (Canadian Political Party)
- `PRT` (Partnership Registered in Canada)
- `TDM` (Trademark registered in Canada)
- `TRD` (Canadian Trade Union)
- `TRS` (Trust established in Canada)

.es

- `ES_IDENTIFICATION`   The value of `ES_IDENTIFICATION` depends on the following values:
- The value of `ES_LEGAL_FORM`
- The value of `ES_IDENTIFICATION_TYPE`

**If ``ES_LEGAL_FORM`` is any value other than ``INDIVIDUAL`` :**

- Specify 1 letter + 8 numbers (CIF [Certificado de IdentificaciÃ³n Fiscal])
- Example: B12345678

**If ``ES_LEGAL_FORM`` is ``INDIVIDUAL`` , the value that you specify for ``ES_IDENTIFICATION`` depends on the value of ``ES_IDENTIFICATION_TYPE`` :**

- If `ES_IDENTIFICATION_TYPE` is `DNI_AND_NIF` (for Spanish contacts):
- Specify 8 numbers + 1 letter (DNI [Documento Nacional de Identidad], NIF [NÃºmero de IdentificaciÃ³n Fiscal])
- Example: 12345678M
- If `ES_IDENTIFICATION_TYPE` is `NIE` (for foreigners with legal residence):
- Specify 1 letter + 7 numbers + 1 letter ( NIE [NÃºmero de Identidad de Extranjero])
- Example: Y1234567X
- If `ES_IDENTIFICATION_TYPE` is `OTHER` (for contacts outside of Spain):
- Specify a passport number, drivers license number, or national identity card number

- `ES_IDENTIFICATION_TYPE`   Valid values include the following:

- `DNI_AND_NIF` (For Spanish contacts)
- `NIE` (For foreigners with legal residence)
- `OTHER` (For contacts outside of Spain)
- `ES_LEGAL_FORM`   Valid values include the following:

- `ASSOCIATION`
- `CENTRAL_GOVERNMENT_BODY`
- `CIVIL_SOCIETY`
- `COMMUNITY_OF_OWNERS`
- `COMMUNITY_PROPERTY`
- `CONSULATE`
- `COOPERATIVE`
- `DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL`
- `ECONOMIC_INTEREST_GROUP`
- `EMBASSY`
- `ENTITY_MANAGING_NATURAL_AREAS`
- `FARM_PARTNERSHIP`
- `FOUNDATION`
- `GENERAL_AND_LIMITED_PARTNERSHIP`
- `GENERAL_PARTNERSHIP`
- `INDIVIDUAL`
- `LIMITED_COMPANY`
- `LOCAL_AUTHORITY`
- `LOCAL_PUBLIC_ENTITY`
- `MUTUAL_INSURANCE_COMPANY`
- `NATIONAL_PUBLIC_ENTITY`
- `ORDER_OR_RELIGIOUS_INSTITUTION`
- `OTHERS (Only for contacts outside of Spain)`
- `POLITICAL_PARTY`
- `PROFESSIONAL_ASSOCIATION`
- `PUBLIC_LAW_ASSOCIATION`
- `PUBLIC_LIMITED_COMPANY`
- `REGIONAL_GOVERNMENT_BODY`
- `REGIONAL_PUBLIC_ENTITY`
- `SAVINGS_BANK`
- `SPANISH_OFFICE`
- `SPORTS_ASSOCIATION`
- `SPORTS_FEDERATION`
- `SPORTS_LIMITED_COMPANY`
- `TEMPORARY_ALLIANCE_OF_ENTERPRISES`
- `TRADE_UNION`
- `WORKER_OWNED_COMPANY`
- `WORKER_OWNED_LIMITED_COMPANY`

.eu
- `EU_COUNTRY_OF_CITIZENSHIP`

.fi
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `FI_BUSINESS_NUMBER`
- `FI_ID_NUMBER`
- `FI_NATIONALITY`   Valid values include the following:

- `FINNISH`
- `NOT_FINNISH`
- `FI_ORGANIZATION_TYPE`   Valid values include the following:

- `COMPANY`
- `CORPORATION`
- `GOVERNMENT`
- `INSTITUTION`
- `POLITICAL_PARTY`
- `PUBLIC_COMMUNITY`
- `TOWNSHIP`

.it
- `IT_NATIONALITY`
- `IT_PIN`
- `IT_REGISTRANT_ENTITY_TYPE`   Valid values include the following:

- `FOREIGNERS`
- `FREELANCE_WORKERS` (Freelance workers and professionals)
- `ITALIAN_COMPANIES` (Italian companies and one-person companies)
- `NON_PROFIT_ORGANIZATIONS`
- `OTHER_SUBJECTS`
- `PUBLIC_ORGANIZATIONS`

.ru
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `RU_PASSPORT_DATA`

.se
- `BIRTH_COUNTRY`
- `SE_ID_NUMBER`

.sg
- `SG_ID_NUMBER`

.uk, .co.uk, .me.uk, and .org.uk
- `UK_CONTACT_TYPE`   Valid values include the following:

- `CRC` (UK Corporation by Royal Charter)
- `FCORP` (Non-UK Corporation)
- `FIND` (Non-UK Individual, representing self)
- `FOTHER` (Non-UK Entity that does not fit into any other category)
- `GOV` (UK Government Body)
- `IND` (UK Individual (representing self))
- `IP` (UK Industrial/Provident Registered Company)
- `LLP` (UK Limited Liability Partnership)
- `LTD` (UK Limited Company)
- `OTHER` (UK Entity that does not fit into any other category)
- `PLC` (UK Public Limited Company)
- `PTNR` (UK Partnership)
- `RCHAR` (UK Registered Charity)
- `SCH` (UK School)
- `STAT` (UK Statutory Body)
- `STRA` (UK Sole Trader)
- `UK_COMPANY_NUMBER`

In addition, many TLDs require a `VAT_NUMBER` .

Value -> (string)

The value that corresponds with the name of an extra parameter.

Shorthand Syntax:

```
FirstName=string,LastName=string,ContactType=string,OrganizationName=string,AddressLine1=string,AddressLine2=string,City=string,State=string,CountryCode=string,ZipCode=string,PhoneNumber=string,Email=string,Fax=string,ExtraParams=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "FirstName": "string",
  "LastName": "string",
  "ContactType": "PERSON"|"COMPANY"|"ASSOCIATION"|"PUBLIC_BODY"|"RESELLER",
  "OrganizationName": "string",
  "AddressLine1": "string",
  "AddressLine2": "string",
  "City": "string",
  "State": "string",
  "CountryCode": "AC"|"AD"|"AE"|"AF"|"AG"|"AI"|"AL"|"AM"|"AN"|"AO"|"AQ"|"AR"|"AS"|"AT"|"AU"|"AW"|"AX"|"AZ"|"BA"|"BB"|"BD"|"BE"|"BF"|"BG"|"BH"|"BI"|"BJ"|"BL"|"BM"|"BN"|"BO"|"BQ"|"BR"|"BS"|"BT"|"BV"|"BW"|"BY"|"BZ"|"CA"|"CC"|"CD"|"CF"|"CG"|"CH"|"CI"|"CK"|"CL"|"CM"|"CN"|"CO"|"CR"|"CU"|"CV"|"CW"|"CX"|"CY"|"CZ"|"DE"|"DJ"|"DK"|"DM"|"DO"|"DZ"|"EC"|"EE"|"EG"|"EH"|"ER"|"ES"|"ET"|"FI"|"FJ"|"FK"|"FM"|"FO"|"FR"|"GA"|"GB"|"GD"|"GE"|"GF"|"GG"|"GH"|"GI"|"GL"|"GM"|"GN"|"GP"|"GQ"|"GR"|"GS"|"GT"|"GU"|"GW"|"GY"|"HK"|"HM"|"HN"|"HR"|"HT"|"HU"|"ID"|"IE"|"IL"|"IM"|"IN"|"IO"|"IQ"|"IR"|"IS"|"IT"|"JE"|"JM"|"JO"|"JP"|"KE"|"KG"|"KH"|"KI"|"KM"|"KN"|"KP"|"KR"|"KW"|"KY"|"KZ"|"LA"|"LB"|"LC"|"LI"|"LK"|"LR"|"LS"|"LT"|"LU"|"LV"|"LY"|"MA"|"MC"|"MD"|"ME"|"MF"|"MG"|"MH"|"MK"|"ML"|"MM"|"MN"|"MO"|"MP"|"MQ"|"MR"|"MS"|"MT"|"MU"|"MV"|"MW"|"MX"|"MY"|"MZ"|"NA"|"NC"|"NE"|"NF"|"NG"|"NI"|"NL"|"NO"|"NP"|"NR"|"NU"|"NZ"|"OM"|"PA"|"PE"|"PF"|"PG"|"PH"|"PK"|"PL"|"PM"|"PN"|"PR"|"PS"|"PT"|"PW"|"PY"|"QA"|"RE"|"RO"|"RS"|"RU"|"RW"|"SA"|"SB"|"SC"|"SD"|"SE"|"SG"|"SH"|"SI"|"SJ"|"SK"|"SL"|"SM"|"SN"|"SO"|"SR"|"SS"|"ST"|"SV"|"SX"|"SY"|"SZ"|"TC"|"TD"|"TF"|"TG"|"TH"|"TJ"|"TK"|"TL"|"TM"|"TN"|"TO"|"TP"|"TR"|"TT"|"TV"|"TW"|"TZ"|"UA"|"UG"|"US"|"UY"|"UZ"|"VA"|"VC"|"VE"|"VG"|"VI"|"VN"|"VU"|"WF"|"WS"|"YE"|"YT"|"ZA"|"ZM"|"ZW",
  "ZipCode": "string",
  "PhoneNumber": "string",
  "Email": "string",
  "Fax": "string",
  "ExtraParams": [
    {
      "Name": "DUNS_NUMBER"|"BRAND_NUMBER"|"BIRTH_DEPARTMENT"|"BIRTH_DATE_IN_YYYY_MM_DD"|"BIRTH_COUNTRY"|"BIRTH_CITY"|"DOCUMENT_NUMBER"|"AU_ID_NUMBER"|"AU_ID_TYPE"|"CA_LEGAL_TYPE"|"CA_BUSINESS_ENTITY_TYPE"|"CA_LEGAL_REPRESENTATIVE"|"CA_LEGAL_REPRESENTATIVE_CAPACITY"|"ES_IDENTIFICATION"|"ES_IDENTIFICATION_TYPE"|"ES_LEGAL_FORM"|"FI_BUSINESS_NUMBER"|"FI_ID_NUMBER"|"FI_NATIONALITY"|"FI_ORGANIZATION_TYPE"|"IT_NATIONALITY"|"IT_PIN"|"IT_REGISTRANT_ENTITY_TYPE"|"RU_PASSPORT_DATA"|"SE_ID_NUMBER"|"SG_ID_NUMBER"|"VAT_NUMBER"|"UK_CONTACT_TYPE"|"UK_COMPANY_NUMBER"|"EU_COUNTRY_OF_CITIZENSHIP"|"AU_PRIORITY_TOKEN",
      "Value": "string"
    }
    ...
  ]
}
```

`--tech-contact` (structure)

Provides detailed contact information.

FirstName -> (string)

First name of contact.

LastName -> (string)

Last name of contact.

ContactType -> (string)

Indicates whether the contact is a person, company, association, or public organization. Note the following:

- If you specify a value other than `PERSON` , you must also specify a value for `OrganizationName` .
- For some TLDs, the privacy protection available depends on the value that you specify for `Contact Type` . For the privacy protection settings for your TLD, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*
- For .es domains, the value of `ContactType` must be `PERSON` for all three contacts.

OrganizationName -> (string)

Name of the organization for contact types other than `PERSON` .

AddressLine1 -> (string)

First line of the contactâs address.

AddressLine2 -> (string)

Second line of contactâs address, if any.

City -> (string)

The city of the contactâs address.

State -> (string)

The state or province of the contactâs city.

CountryCode -> (string)

Code for the country of the contactâs address.

ZipCode -> (string)

The zip or postal code of the contactâs address.

PhoneNumber -> (string)

The phone number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code>]â. For example, a US phone number might appear as `"+1.1234567890"` .

Email -> (string)

Email address of the contact.

Fax -> (string)

Fax number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code]â. For example, a US phone number might appear as `"+1.1234567890"` .

ExtraParams -> (list)

A list of name-value pairs for parameters required by certain top-level domains.

(structure)

ExtraParam includes the following elements.

Name -> (string)

The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

- `AU_ID_NUMBER`
- `AU_ID_TYPE`   Valid values include the following:

- `ABN` (Australian business number)
- `ACN` (Australian company number)
- `TM` (Trademark number)

.ca
- `BRAND_NUMBER`
- `CA_BUSINESS_ENTITY_TYPE`   Valid values include the following:

- `BANK` (Bank)
- `COMMERCIAL_COMPANY` (Commercial company)
- `COMPANY` (Company)
- `COOPERATION` (Cooperation)
- `COOPERATIVE` (Cooperative)
- `COOPRIX` (Cooprix)
- `CORP` (Corporation)
- `CREDIT_UNION` (Credit union)
- `FOMIA` (Federation of mutual insurance associations)
- `INC` (Incorporated)
- `LTD` (Limited)
- `LTEE` (LimitÃ©e)
- `LLC` (Limited liability corporation)
- `LLP` (Limited liability partnership)
- `LTE` (Lte.)
- `MBA` (Mutual benefit association)
- `MIC` (Mutual insurance company)
- `NFP` (Not-for-profit corporation)
- `SA` (S.A.)
- `SAVINGS_COMPANY` (Savings company)
- `SAVINGS_UNION` (Savings union)
- `SARL` (SociÃ©tÃ© Ã  responsabilitÃ© limitÃ©e)
- `TRUST` (Trust)
- `ULC` (Unlimited liability corporation)
- `CA_LEGAL_TYPE`   When `ContactType` is `PERSON` , valid values include the following:

- `ABO` (Aboriginal Peoples indigenous to Canada)
- `CCT` (Canadian citizen)
- `LGR` (Legal Representative of a Canadian Citizen or Permanent Resident)
- `RES` (Permanent resident of Canada)

When `ContactType` is a value other than `PERSON` , valid values include the following:

- `ASS` (Canadian unincorporated association)
- `CCO` (Canadian corporation)
- `EDU` (Canadian educational institution)
- `GOV` (Government or government entity in Canada)
- `HOP` (Canadian Hospital)
- `INB` (Indian Band recognized by the Indian Act of Canada)
- `LAM` (Canadian Library, Archive, or Museum)
- `MAJ` (Her/His Majesty the Queen/King)
- `OMK` (Official mark registered in Canada)
- `PLT` (Canadian Political Party)
- `PRT` (Partnership Registered in Canada)
- `TDM` (Trademark registered in Canada)
- `TRD` (Canadian Trade Union)
- `TRS` (Trust established in Canada)

.es

- `ES_IDENTIFICATION`   The value of `ES_IDENTIFICATION` depends on the following values:
- The value of `ES_LEGAL_FORM`
- The value of `ES_IDENTIFICATION_TYPE`

**If ``ES_LEGAL_FORM`` is any value other than ``INDIVIDUAL`` :**

- Specify 1 letter + 8 numbers (CIF [Certificado de IdentificaciÃ³n Fiscal])
- Example: B12345678

**If ``ES_LEGAL_FORM`` is ``INDIVIDUAL`` , the value that you specify for ``ES_IDENTIFICATION`` depends on the value of ``ES_IDENTIFICATION_TYPE`` :**

- If `ES_IDENTIFICATION_TYPE` is `DNI_AND_NIF` (for Spanish contacts):
- Specify 8 numbers + 1 letter (DNI [Documento Nacional de Identidad], NIF [NÃºmero de IdentificaciÃ³n Fiscal])
- Example: 12345678M
- If `ES_IDENTIFICATION_TYPE` is `NIE` (for foreigners with legal residence):
- Specify 1 letter + 7 numbers + 1 letter ( NIE [NÃºmero de Identidad de Extranjero])
- Example: Y1234567X
- If `ES_IDENTIFICATION_TYPE` is `OTHER` (for contacts outside of Spain):
- Specify a passport number, drivers license number, or national identity card number

- `ES_IDENTIFICATION_TYPE`   Valid values include the following:

- `DNI_AND_NIF` (For Spanish contacts)
- `NIE` (For foreigners with legal residence)
- `OTHER` (For contacts outside of Spain)
- `ES_LEGAL_FORM`   Valid values include the following:

- `ASSOCIATION`
- `CENTRAL_GOVERNMENT_BODY`
- `CIVIL_SOCIETY`
- `COMMUNITY_OF_OWNERS`
- `COMMUNITY_PROPERTY`
- `CONSULATE`
- `COOPERATIVE`
- `DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL`
- `ECONOMIC_INTEREST_GROUP`
- `EMBASSY`
- `ENTITY_MANAGING_NATURAL_AREAS`
- `FARM_PARTNERSHIP`
- `FOUNDATION`
- `GENERAL_AND_LIMITED_PARTNERSHIP`
- `GENERAL_PARTNERSHIP`
- `INDIVIDUAL`
- `LIMITED_COMPANY`
- `LOCAL_AUTHORITY`
- `LOCAL_PUBLIC_ENTITY`
- `MUTUAL_INSURANCE_COMPANY`
- `NATIONAL_PUBLIC_ENTITY`
- `ORDER_OR_RELIGIOUS_INSTITUTION`
- `OTHERS (Only for contacts outside of Spain)`
- `POLITICAL_PARTY`
- `PROFESSIONAL_ASSOCIATION`
- `PUBLIC_LAW_ASSOCIATION`
- `PUBLIC_LIMITED_COMPANY`
- `REGIONAL_GOVERNMENT_BODY`
- `REGIONAL_PUBLIC_ENTITY`
- `SAVINGS_BANK`
- `SPANISH_OFFICE`
- `SPORTS_ASSOCIATION`
- `SPORTS_FEDERATION`
- `SPORTS_LIMITED_COMPANY`
- `TEMPORARY_ALLIANCE_OF_ENTERPRISES`
- `TRADE_UNION`
- `WORKER_OWNED_COMPANY`
- `WORKER_OWNED_LIMITED_COMPANY`

.eu
- `EU_COUNTRY_OF_CITIZENSHIP`

.fi
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `FI_BUSINESS_NUMBER`
- `FI_ID_NUMBER`
- `FI_NATIONALITY`   Valid values include the following:

- `FINNISH`
- `NOT_FINNISH`
- `FI_ORGANIZATION_TYPE`   Valid values include the following:

- `COMPANY`
- `CORPORATION`
- `GOVERNMENT`
- `INSTITUTION`
- `POLITICAL_PARTY`
- `PUBLIC_COMMUNITY`
- `TOWNSHIP`

.it
- `IT_NATIONALITY`
- `IT_PIN`
- `IT_REGISTRANT_ENTITY_TYPE`   Valid values include the following:

- `FOREIGNERS`
- `FREELANCE_WORKERS` (Freelance workers and professionals)
- `ITALIAN_COMPANIES` (Italian companies and one-person companies)
- `NON_PROFIT_ORGANIZATIONS`
- `OTHER_SUBJECTS`
- `PUBLIC_ORGANIZATIONS`

.ru
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `RU_PASSPORT_DATA`

.se
- `BIRTH_COUNTRY`
- `SE_ID_NUMBER`

.sg
- `SG_ID_NUMBER`

.uk, .co.uk, .me.uk, and .org.uk
- `UK_CONTACT_TYPE`   Valid values include the following:

- `CRC` (UK Corporation by Royal Charter)
- `FCORP` (Non-UK Corporation)
- `FIND` (Non-UK Individual, representing self)
- `FOTHER` (Non-UK Entity that does not fit into any other category)
- `GOV` (UK Government Body)
- `IND` (UK Individual (representing self))
- `IP` (UK Industrial/Provident Registered Company)
- `LLP` (UK Limited Liability Partnership)
- `LTD` (UK Limited Company)
- `OTHER` (UK Entity that does not fit into any other category)
- `PLC` (UK Public Limited Company)
- `PTNR` (UK Partnership)
- `RCHAR` (UK Registered Charity)
- `SCH` (UK School)
- `STAT` (UK Statutory Body)
- `STRA` (UK Sole Trader)
- `UK_COMPANY_NUMBER`

In addition, many TLDs require a `VAT_NUMBER` .

Value -> (string)

The value that corresponds with the name of an extra parameter.

Shorthand Syntax:

```
FirstName=string,LastName=string,ContactType=string,OrganizationName=string,AddressLine1=string,AddressLine2=string,City=string,State=string,CountryCode=string,ZipCode=string,PhoneNumber=string,Email=string,Fax=string,ExtraParams=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "FirstName": "string",
  "LastName": "string",
  "ContactType": "PERSON"|"COMPANY"|"ASSOCIATION"|"PUBLIC_BODY"|"RESELLER",
  "OrganizationName": "string",
  "AddressLine1": "string",
  "AddressLine2": "string",
  "City": "string",
  "State": "string",
  "CountryCode": "AC"|"AD"|"AE"|"AF"|"AG"|"AI"|"AL"|"AM"|"AN"|"AO"|"AQ"|"AR"|"AS"|"AT"|"AU"|"AW"|"AX"|"AZ"|"BA"|"BB"|"BD"|"BE"|"BF"|"BG"|"BH"|"BI"|"BJ"|"BL"|"BM"|"BN"|"BO"|"BQ"|"BR"|"BS"|"BT"|"BV"|"BW"|"BY"|"BZ"|"CA"|"CC"|"CD"|"CF"|"CG"|"CH"|"CI"|"CK"|"CL"|"CM"|"CN"|"CO"|"CR"|"CU"|"CV"|"CW"|"CX"|"CY"|"CZ"|"DE"|"DJ"|"DK"|"DM"|"DO"|"DZ"|"EC"|"EE"|"EG"|"EH"|"ER"|"ES"|"ET"|"FI"|"FJ"|"FK"|"FM"|"FO"|"FR"|"GA"|"GB"|"GD"|"GE"|"GF"|"GG"|"GH"|"GI"|"GL"|"GM"|"GN"|"GP"|"GQ"|"GR"|"GS"|"GT"|"GU"|"GW"|"GY"|"HK"|"HM"|"HN"|"HR"|"HT"|"HU"|"ID"|"IE"|"IL"|"IM"|"IN"|"IO"|"IQ"|"IR"|"IS"|"IT"|"JE"|"JM"|"JO"|"JP"|"KE"|"KG"|"KH"|"KI"|"KM"|"KN"|"KP"|"KR"|"KW"|"KY"|"KZ"|"LA"|"LB"|"LC"|"LI"|"LK"|"LR"|"LS"|"LT"|"LU"|"LV"|"LY"|"MA"|"MC"|"MD"|"ME"|"MF"|"MG"|"MH"|"MK"|"ML"|"MM"|"MN"|"MO"|"MP"|"MQ"|"MR"|"MS"|"MT"|"MU"|"MV"|"MW"|"MX"|"MY"|"MZ"|"NA"|"NC"|"NE"|"NF"|"NG"|"NI"|"NL"|"NO"|"NP"|"NR"|"NU"|"NZ"|"OM"|"PA"|"PE"|"PF"|"PG"|"PH"|"PK"|"PL"|"PM"|"PN"|"PR"|"PS"|"PT"|"PW"|"PY"|"QA"|"RE"|"RO"|"RS"|"RU"|"RW"|"SA"|"SB"|"SC"|"SD"|"SE"|"SG"|"SH"|"SI"|"SJ"|"SK"|"SL"|"SM"|"SN"|"SO"|"SR"|"SS"|"ST"|"SV"|"SX"|"SY"|"SZ"|"TC"|"TD"|"TF"|"TG"|"TH"|"TJ"|"TK"|"TL"|"TM"|"TN"|"TO"|"TP"|"TR"|"TT"|"TV"|"TW"|"TZ"|"UA"|"UG"|"US"|"UY"|"UZ"|"VA"|"VC"|"VE"|"VG"|"VI"|"VN"|"VU"|"WF"|"WS"|"YE"|"YT"|"ZA"|"ZM"|"ZW",
  "ZipCode": "string",
  "PhoneNumber": "string",
  "Email": "string",
  "Fax": "string",
  "ExtraParams": [
    {
      "Name": "DUNS_NUMBER"|"BRAND_NUMBER"|"BIRTH_DEPARTMENT"|"BIRTH_DATE_IN_YYYY_MM_DD"|"BIRTH_COUNTRY"|"BIRTH_CITY"|"DOCUMENT_NUMBER"|"AU_ID_NUMBER"|"AU_ID_TYPE"|"CA_LEGAL_TYPE"|"CA_BUSINESS_ENTITY_TYPE"|"CA_LEGAL_REPRESENTATIVE"|"CA_LEGAL_REPRESENTATIVE_CAPACITY"|"ES_IDENTIFICATION"|"ES_IDENTIFICATION_TYPE"|"ES_LEGAL_FORM"|"FI_BUSINESS_NUMBER"|"FI_ID_NUMBER"|"FI_NATIONALITY"|"FI_ORGANIZATION_TYPE"|"IT_NATIONALITY"|"IT_PIN"|"IT_REGISTRANT_ENTITY_TYPE"|"RU_PASSPORT_DATA"|"SE_ID_NUMBER"|"SG_ID_NUMBER"|"VAT_NUMBER"|"UK_CONTACT_TYPE"|"UK_COMPANY_NUMBER"|"EU_COUNTRY_OF_CITIZENSHIP"|"AU_PRIORITY_TOKEN",
      "Value": "string"
    }
    ...
  ]
}
```

`--privacy-protect-admin-contact` | `--no-privacy-protect-admin-contact` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information for the registrar, the phrase âREDACTED FOR PRIVACYâ, or âOn behalf of <domain name> owner.â.

### Note

While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.

Default: `true`

`--privacy-protect-registrant-contact` | `--no-privacy-protect-registrant-contact` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the registrant contact (domain owner).

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

Default: `true`

`--privacy-protect-tech-contact` | `--no-privacy-protect-tech-contact` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the technical contact.

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

Default: `true`

`--billing-contact` (structure)

Provides detailed contact information.

FirstName -> (string)

First name of contact.

LastName -> (string)

Last name of contact.

ContactType -> (string)

Indicates whether the contact is a person, company, association, or public organization. Note the following:

- If you specify a value other than `PERSON` , you must also specify a value for `OrganizationName` .
- For some TLDs, the privacy protection available depends on the value that you specify for `Contact Type` . For the privacy protection settings for your TLD, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*
- For .es domains, the value of `ContactType` must be `PERSON` for all three contacts.

OrganizationName -> (string)

Name of the organization for contact types other than `PERSON` .

AddressLine1 -> (string)

First line of the contactâs address.

AddressLine2 -> (string)

Second line of contactâs address, if any.

City -> (string)

The city of the contactâs address.

State -> (string)

The state or province of the contactâs city.

CountryCode -> (string)

Code for the country of the contactâs address.

ZipCode -> (string)

The zip or postal code of the contactâs address.

PhoneNumber -> (string)

The phone number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code>]â. For example, a US phone number might appear as `"+1.1234567890"` .

Email -> (string)

Email address of the contact.

Fax -> (string)

Fax number of the contact.

Constraints: Phone number must be specified in the format â+[country dialing code].[number including any area code]â. For example, a US phone number might appear as `"+1.1234567890"` .

ExtraParams -> (list)

A list of name-value pairs for parameters required by certain top-level domains.

(structure)

ExtraParam includes the following elements.

Name -> (string)

The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:

.com.au and .net.au

- `AU_ID_NUMBER`
- `AU_ID_TYPE`   Valid values include the following:

- `ABN` (Australian business number)
- `ACN` (Australian company number)
- `TM` (Trademark number)

.ca
- `BRAND_NUMBER`
- `CA_BUSINESS_ENTITY_TYPE`   Valid values include the following:

- `BANK` (Bank)
- `COMMERCIAL_COMPANY` (Commercial company)
- `COMPANY` (Company)
- `COOPERATION` (Cooperation)
- `COOPERATIVE` (Cooperative)
- `COOPRIX` (Cooprix)
- `CORP` (Corporation)
- `CREDIT_UNION` (Credit union)
- `FOMIA` (Federation of mutual insurance associations)
- `INC` (Incorporated)
- `LTD` (Limited)
- `LTEE` (LimitÃ©e)
- `LLC` (Limited liability corporation)
- `LLP` (Limited liability partnership)
- `LTE` (Lte.)
- `MBA` (Mutual benefit association)
- `MIC` (Mutual insurance company)
- `NFP` (Not-for-profit corporation)
- `SA` (S.A.)
- `SAVINGS_COMPANY` (Savings company)
- `SAVINGS_UNION` (Savings union)
- `SARL` (SociÃ©tÃ© Ã  responsabilitÃ© limitÃ©e)
- `TRUST` (Trust)
- `ULC` (Unlimited liability corporation)
- `CA_LEGAL_TYPE`   When `ContactType` is `PERSON` , valid values include the following:

- `ABO` (Aboriginal Peoples indigenous to Canada)
- `CCT` (Canadian citizen)
- `LGR` (Legal Representative of a Canadian Citizen or Permanent Resident)
- `RES` (Permanent resident of Canada)

When `ContactType` is a value other than `PERSON` , valid values include the following:

- `ASS` (Canadian unincorporated association)
- `CCO` (Canadian corporation)
- `EDU` (Canadian educational institution)
- `GOV` (Government or government entity in Canada)
- `HOP` (Canadian Hospital)
- `INB` (Indian Band recognized by the Indian Act of Canada)
- `LAM` (Canadian Library, Archive, or Museum)
- `MAJ` (Her/His Majesty the Queen/King)
- `OMK` (Official mark registered in Canada)
- `PLT` (Canadian Political Party)
- `PRT` (Partnership Registered in Canada)
- `TDM` (Trademark registered in Canada)
- `TRD` (Canadian Trade Union)
- `TRS` (Trust established in Canada)

.es

- `ES_IDENTIFICATION`   The value of `ES_IDENTIFICATION` depends on the following values:
- The value of `ES_LEGAL_FORM`
- The value of `ES_IDENTIFICATION_TYPE`

**If ``ES_LEGAL_FORM`` is any value other than ``INDIVIDUAL`` :**

- Specify 1 letter + 8 numbers (CIF [Certificado de IdentificaciÃ³n Fiscal])
- Example: B12345678

**If ``ES_LEGAL_FORM`` is ``INDIVIDUAL`` , the value that you specify for ``ES_IDENTIFICATION`` depends on the value of ``ES_IDENTIFICATION_TYPE`` :**

- If `ES_IDENTIFICATION_TYPE` is `DNI_AND_NIF` (for Spanish contacts):
- Specify 8 numbers + 1 letter (DNI [Documento Nacional de Identidad], NIF [NÃºmero de IdentificaciÃ³n Fiscal])
- Example: 12345678M
- If `ES_IDENTIFICATION_TYPE` is `NIE` (for foreigners with legal residence):
- Specify 1 letter + 7 numbers + 1 letter ( NIE [NÃºmero de Identidad de Extranjero])
- Example: Y1234567X
- If `ES_IDENTIFICATION_TYPE` is `OTHER` (for contacts outside of Spain):
- Specify a passport number, drivers license number, or national identity card number

- `ES_IDENTIFICATION_TYPE`   Valid values include the following:

- `DNI_AND_NIF` (For Spanish contacts)
- `NIE` (For foreigners with legal residence)
- `OTHER` (For contacts outside of Spain)
- `ES_LEGAL_FORM`   Valid values include the following:

- `ASSOCIATION`
- `CENTRAL_GOVERNMENT_BODY`
- `CIVIL_SOCIETY`
- `COMMUNITY_OF_OWNERS`
- `COMMUNITY_PROPERTY`
- `CONSULATE`
- `COOPERATIVE`
- `DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL`
- `ECONOMIC_INTEREST_GROUP`
- `EMBASSY`
- `ENTITY_MANAGING_NATURAL_AREAS`
- `FARM_PARTNERSHIP`
- `FOUNDATION`
- `GENERAL_AND_LIMITED_PARTNERSHIP`
- `GENERAL_PARTNERSHIP`
- `INDIVIDUAL`
- `LIMITED_COMPANY`
- `LOCAL_AUTHORITY`
- `LOCAL_PUBLIC_ENTITY`
- `MUTUAL_INSURANCE_COMPANY`
- `NATIONAL_PUBLIC_ENTITY`
- `ORDER_OR_RELIGIOUS_INSTITUTION`
- `OTHERS (Only for contacts outside of Spain)`
- `POLITICAL_PARTY`
- `PROFESSIONAL_ASSOCIATION`
- `PUBLIC_LAW_ASSOCIATION`
- `PUBLIC_LIMITED_COMPANY`
- `REGIONAL_GOVERNMENT_BODY`
- `REGIONAL_PUBLIC_ENTITY`
- `SAVINGS_BANK`
- `SPANISH_OFFICE`
- `SPORTS_ASSOCIATION`
- `SPORTS_FEDERATION`
- `SPORTS_LIMITED_COMPANY`
- `TEMPORARY_ALLIANCE_OF_ENTERPRISES`
- `TRADE_UNION`
- `WORKER_OWNED_COMPANY`
- `WORKER_OWNED_LIMITED_COMPANY`

.eu
- `EU_COUNTRY_OF_CITIZENSHIP`

.fi
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `FI_BUSINESS_NUMBER`
- `FI_ID_NUMBER`
- `FI_NATIONALITY`   Valid values include the following:

- `FINNISH`
- `NOT_FINNISH`
- `FI_ORGANIZATION_TYPE`   Valid values include the following:

- `COMPANY`
- `CORPORATION`
- `GOVERNMENT`
- `INSTITUTION`
- `POLITICAL_PARTY`
- `PUBLIC_COMMUNITY`
- `TOWNSHIP`

.it
- `IT_NATIONALITY`
- `IT_PIN`
- `IT_REGISTRANT_ENTITY_TYPE`   Valid values include the following:

- `FOREIGNERS`
- `FREELANCE_WORKERS` (Freelance workers and professionals)
- `ITALIAN_COMPANIES` (Italian companies and one-person companies)
- `NON_PROFIT_ORGANIZATIONS`
- `OTHER_SUBJECTS`
- `PUBLIC_ORGANIZATIONS`

.ru
- `BIRTH_DATE_IN_YYYY_MM_DD`
- `RU_PASSPORT_DATA`

.se
- `BIRTH_COUNTRY`
- `SE_ID_NUMBER`

.sg
- `SG_ID_NUMBER`

.uk, .co.uk, .me.uk, and .org.uk
- `UK_CONTACT_TYPE`   Valid values include the following:

- `CRC` (UK Corporation by Royal Charter)
- `FCORP` (Non-UK Corporation)
- `FIND` (Non-UK Individual, representing self)
- `FOTHER` (Non-UK Entity that does not fit into any other category)
- `GOV` (UK Government Body)
- `IND` (UK Individual (representing self))
- `IP` (UK Industrial/Provident Registered Company)
- `LLP` (UK Limited Liability Partnership)
- `LTD` (UK Limited Company)
- `OTHER` (UK Entity that does not fit into any other category)
- `PLC` (UK Public Limited Company)
- `PTNR` (UK Partnership)
- `RCHAR` (UK Registered Charity)
- `SCH` (UK School)
- `STAT` (UK Statutory Body)
- `STRA` (UK Sole Trader)
- `UK_COMPANY_NUMBER`

In addition, many TLDs require a `VAT_NUMBER` .

Value -> (string)

The value that corresponds with the name of an extra parameter.

Shorthand Syntax:

```
FirstName=string,LastName=string,ContactType=string,OrganizationName=string,AddressLine1=string,AddressLine2=string,City=string,State=string,CountryCode=string,ZipCode=string,PhoneNumber=string,Email=string,Fax=string,ExtraParams=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "FirstName": "string",
  "LastName": "string",
  "ContactType": "PERSON"|"COMPANY"|"ASSOCIATION"|"PUBLIC_BODY"|"RESELLER",
  "OrganizationName": "string",
  "AddressLine1": "string",
  "AddressLine2": "string",
  "City": "string",
  "State": "string",
  "CountryCode": "AC"|"AD"|"AE"|"AF"|"AG"|"AI"|"AL"|"AM"|"AN"|"AO"|"AQ"|"AR"|"AS"|"AT"|"AU"|"AW"|"AX"|"AZ"|"BA"|"BB"|"BD"|"BE"|"BF"|"BG"|"BH"|"BI"|"BJ"|"BL"|"BM"|"BN"|"BO"|"BQ"|"BR"|"BS"|"BT"|"BV"|"BW"|"BY"|"BZ"|"CA"|"CC"|"CD"|"CF"|"CG"|"CH"|"CI"|"CK"|"CL"|"CM"|"CN"|"CO"|"CR"|"CU"|"CV"|"CW"|"CX"|"CY"|"CZ"|"DE"|"DJ"|"DK"|"DM"|"DO"|"DZ"|"EC"|"EE"|"EG"|"EH"|"ER"|"ES"|"ET"|"FI"|"FJ"|"FK"|"FM"|"FO"|"FR"|"GA"|"GB"|"GD"|"GE"|"GF"|"GG"|"GH"|"GI"|"GL"|"GM"|"GN"|"GP"|"GQ"|"GR"|"GS"|"GT"|"GU"|"GW"|"GY"|"HK"|"HM"|"HN"|"HR"|"HT"|"HU"|"ID"|"IE"|"IL"|"IM"|"IN"|"IO"|"IQ"|"IR"|"IS"|"IT"|"JE"|"JM"|"JO"|"JP"|"KE"|"KG"|"KH"|"KI"|"KM"|"KN"|"KP"|"KR"|"KW"|"KY"|"KZ"|"LA"|"LB"|"LC"|"LI"|"LK"|"LR"|"LS"|"LT"|"LU"|"LV"|"LY"|"MA"|"MC"|"MD"|"ME"|"MF"|"MG"|"MH"|"MK"|"ML"|"MM"|"MN"|"MO"|"MP"|"MQ"|"MR"|"MS"|"MT"|"MU"|"MV"|"MW"|"MX"|"MY"|"MZ"|"NA"|"NC"|"NE"|"NF"|"NG"|"NI"|"NL"|"NO"|"NP"|"NR"|"NU"|"NZ"|"OM"|"PA"|"PE"|"PF"|"PG"|"PH"|"PK"|"PL"|"PM"|"PN"|"PR"|"PS"|"PT"|"PW"|"PY"|"QA"|"RE"|"RO"|"RS"|"RU"|"RW"|"SA"|"SB"|"SC"|"SD"|"SE"|"SG"|"SH"|"SI"|"SJ"|"SK"|"SL"|"SM"|"SN"|"SO"|"SR"|"SS"|"ST"|"SV"|"SX"|"SY"|"SZ"|"TC"|"TD"|"TF"|"TG"|"TH"|"TJ"|"TK"|"TL"|"TM"|"TN"|"TO"|"TP"|"TR"|"TT"|"TV"|"TW"|"TZ"|"UA"|"UG"|"US"|"UY"|"UZ"|"VA"|"VC"|"VE"|"VG"|"VI"|"VN"|"VU"|"WF"|"WS"|"YE"|"YT"|"ZA"|"ZM"|"ZW",
  "ZipCode": "string",
  "PhoneNumber": "string",
  "Email": "string",
  "Fax": "string",
  "ExtraParams": [
    {
      "Name": "DUNS_NUMBER"|"BRAND_NUMBER"|"BIRTH_DEPARTMENT"|"BIRTH_DATE_IN_YYYY_MM_DD"|"BIRTH_COUNTRY"|"BIRTH_CITY"|"DOCUMENT_NUMBER"|"AU_ID_NUMBER"|"AU_ID_TYPE"|"CA_LEGAL_TYPE"|"CA_BUSINESS_ENTITY_TYPE"|"CA_LEGAL_REPRESENTATIVE"|"CA_LEGAL_REPRESENTATIVE_CAPACITY"|"ES_IDENTIFICATION"|"ES_IDENTIFICATION_TYPE"|"ES_LEGAL_FORM"|"FI_BUSINESS_NUMBER"|"FI_ID_NUMBER"|"FI_NATIONALITY"|"FI_ORGANIZATION_TYPE"|"IT_NATIONALITY"|"IT_PIN"|"IT_REGISTRANT_ENTITY_TYPE"|"RU_PASSPORT_DATA"|"SE_ID_NUMBER"|"SG_ID_NUMBER"|"VAT_NUMBER"|"UK_CONTACT_TYPE"|"UK_COMPANY_NUMBER"|"EU_COUNTRY_OF_CITIZENSHIP"|"AU_PRIORITY_TOKEN",
      "Value": "string"
    }
    ...
  ]
}
```

`--privacy-protect-billing-contact` | `--no-privacy-protect-billing-contact` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the billing contact.

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To transfer a domain to Amazon Route 53**

The following `transfer-domain` command transfers a domain to Route 53, with the parameters provided by the JSON-formatted file `C:\temp\transfer-domain.json`.

This command runs only in the `us-east-1` Region. If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
aws route53domains transfer-domain \
    --region us-east-1 \
    --cli-input-json file://C:\temp\transfer-domain.json
```

Contents of `transfer-domain.json`:

```
{
    "DomainName": "example.com",
    "DurationInYears": 1,
    "Nameservers": [
        {
            "Name": "ns-2048.awsdns-64.com"
        },
        {
            "Name": "ns-2049.awsdns-65.net"
        },
        {
            "Name": "ns-2050.awsdns-66.org"
        },
        {
            "Name": "ns-2051.awsdns-67.co.uk"
        }
    ],
    "AuthCode": ")o!v3dJeXampLe",
    "AutoRenew": true,
    "AdminContact": {
        "FirstName": "Martha",
        "LastName": "Rivera",
        "ContactType": "PERSON",
        "OrganizationName": "Example",
        "AddressLine1": "1 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "mrivera@example.com"
    },
    "RegistrantContact": {
        "FirstName": "Li",
        "LastName": "Juan",
        "ContactType": "PERSON",
        "OrganizationName": "Example",
        "AddressLine1": "1 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "ljuan@example.com"
    },
    "TechContact": {
        "FirstName": "Mateo",
        "LastName": "Jackson",
        "ContactType": "PERSON",
        "OrganizationName": "Example",
        "AddressLine1": "1 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "mjackson@example.com"
    },
    "PrivacyProtectAdminContact": true,
    "PrivacyProtectRegistrantContact": true,
    "PrivacyProtectTechContact": true
}
```

Output:

```
{
    "OperationId": "b114c44a-9330-47d1-a6e8-a0b11example"
}
```

To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see [get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html) .

For more information, see [Transferring Registration for a Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html) in the *Amazon Route 53 Developer Guide*.

## Output

OperationId -> (string)

Identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html) .