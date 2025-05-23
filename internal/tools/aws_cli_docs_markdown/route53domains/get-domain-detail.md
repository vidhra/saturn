# get-domain-detailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-domain-detail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-domain-detail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/index.html#cli-aws-route53domains) ]

# get-domain-detail

## Description

This operation returns detailed information about a specified domain that is associated with the current Amazon Web Services account. Contact information for the domain is also returned as part of the output.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/GetDomainDetail)

## Synopsis

```
get-domain-detail
--domain-name <value>
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

The name of the domain that you want to get detailed information about.

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

**To get detailed information about a specified domain**

The following `get-domain-detail` command displays detailed information about the specified domain.

This command runs only in the `us-east-1` Region. If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
aws route53domains get-domain-detail \
    --region us-east-1 \
    --domain-name example.com
```

Output:

```
{
    "DomainName": "example.com",
    "Nameservers": [
        {
            "Name": "ns-2048.awsdns-64.com",
            "GlueIps": []
        },
        {
            "Name": "ns-2049.awsdns-65.net",
            "GlueIps": []
        },
        {
            "Name": "ns-2050.awsdns-66.org",
            "GlueIps": []
        },
        {
            "Name": "ns-2051.awsdns-67.co.uk",
            "GlueIps": []
        }
    ],
    "AutoRenew": true,
    "AdminContact": {
        "FirstName": "Saanvi",
        "LastName": "Sarkar",
        "ContactType": "COMPANY",
        "OrganizationName": "Example",
        "AddressLine1": "123 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "ssarkar@example.com",
        "ExtraParams": []
    },
    "RegistrantContact": {
        "FirstName": "Alejandro",
        "LastName": "Rosalez",
        "ContactType": "COMPANY",
        "OrganizationName": "Example",
        "AddressLine1": "123 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "arosalez@example.com",
        "ExtraParams": []
    },
    "TechContact": {
        "FirstName": "Wang",
        "LastName": "Xiulan",
        "ContactType": "COMPANY",
        "OrganizationName": "Example",
        "AddressLine1": "123 Main Street",
        "City": "Anytown",
        "State": "WA",
        "CountryCode": "US",
        "ZipCode": "98101",
        "PhoneNumber": "+1.8005551212",
        "Email": "wxiulan@example.com",
        "ExtraParams": []
    },
    "AdminPrivacy": true,
    "RegistrantPrivacy": true,
    "TechPrivacy": true,
    "RegistrarName": "Amazon Registrar, Inc.",
    "WhoIsServer": "whois.registrar.amazon.com",
    "RegistrarUrl": "http://registrar.amazon.com",
    "AbuseContactEmail": "abuse@registrar.amazon.com",
    "AbuseContactPhone": "+1.2062661000",
    "CreationDate": 1444934889.601,
    "ExpirationDate": 1602787689.0,
    "StatusList": [
        "clientTransferProhibited"
    ]
}
```

## Output

DomainName -> (string)

The name of a domain.

Nameservers -> (list)

The name servers of the domain.

(structure)

Name server includes the following elements.

Name -> (string)

The fully qualified host name of the name server.

Constraint: Maximum 255 characters

GlueIps -> (list)

Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.

Constraints: The list can contain only one IPv4 and one IPv6 address.

(string)

AutoRenew -> (boolean)

Specifies whether the domain registration is set to renew automatically.

AdminContact -> (structure)

Provides details about the domain administrative contact.

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

RegistrantContact -> (structure)

Provides details about the domain registrant.

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

TechContact -> (structure)

Provides details about the domain technical contact.

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

AdminPrivacy -> (boolean)

Specifies whether contact information is concealed from WHOIS queries. If the value is `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false` , WHOIS queries return the information that you entered for the admin contact.

RegistrantPrivacy -> (boolean)

Specifies whether contact information is concealed from WHOIS queries. If the value is `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false` , WHOIS queries return the information that you entered for the registrant contact (domain owner).

TechPrivacy -> (boolean)

Specifies whether contact information is concealed from WHOIS queries. If the value is `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false` , WHOIS queries return the information that you entered for the technical contact.

RegistrarName -> (string)

Name of the registrar of the domain as identified in the registry.

WhoIsServer -> (string)

The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.

RegistrarUrl -> (string)

Web address of the registrar.

AbuseContactEmail -> (string)

Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.

AbuseContactPhone -> (string)

Phone number for reporting abuse.

RegistryDomainId -> (string)

Reserved for future use.

CreationDate -> (timestamp)

The date when the domain was created as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).

UpdatedDate -> (timestamp)

The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).

ExpirationDate -> (timestamp)

The date when the registration for the domain is set to expire. The date and time is in Unix time format and Coordinated Universal time (UTC).

Reseller -> (string)

Reseller of the domain. Domains registered or transferred using Route 53 domains will have `"Amazon"` as the reseller.

DnsSec -> (string)

Deprecated.

StatusList -> (list)

An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.

ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.

For a current list of domain name status codes and an explanation of what each code means, go to the [ICANN website](https://www.icann.org/) and search for `epp status codes` . (Search on the ICANN website; web searches sometimes return an old version of the document.)

(string)

DnssecKeys -> (list)

A complex type that contains information about the DNSSEC configuration.

(structure)

Information about the DNSSEC key.

You get this from your DNS provider and then give it to Route 53 (by using [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html) ) to pass it to the registry to establish the chain of trust.

Algorithm -> (integer)

The number of the public keyâs cryptographic algorithm according to an [IANA](https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xml) assignment.

If Route 53 is your DNS service, set this to 13.

For more information about enabling DNSSEC signing, see [Enabling DNSSEC signing and establishing a chain of trust](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-enable-signing.html) .

Flags -> (integer)

Defines the type of key. It can be either a KSK (key-signing-key, value 257) or ZSK (zone-signing-key, value 256). Using KSK is always encouraged. Only use ZSK if your DNS provider isnât Route 53 and you donât have KSK available.

If you have KSK and ZSK keys, always use KSK to create a delegations signer (DS) record. If you have ZSK keys only â use ZSK to create a DS record.

PublicKey -> (string)

The base64-encoded public key part of the key pair that is passed to the registry .

DigestType -> (integer)

The number of the DS digest algorithm according to an IANA assignment.

For more information, see [IANA](https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml) for DNSSEC Delegation Signer (DS) Resource Record (RR) Type Digest Algorithms.

Digest -> (string)

The delegation signer digest.

Digest is calculated from the public key provided using specified digest algorithm and this digest is the actual value returned from the registry nameservers as the value of DS records.

KeyTag -> (integer)

A numeric identification of the DNSKEY record referred to by this DS record.

Id -> (string)

An ID assigned to each DS record created by [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html) .

BillingContact -> (structure)

Provides details about the domain billing contact.

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

BillingPrivacy -> (boolean)

Specifies whether contact information is concealed from WHOIS queries. If the value is `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false` , WHOIS queries return the information that you entered for the billing contact.