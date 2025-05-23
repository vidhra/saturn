# list-tax-registrationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/list-tax-registrations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/list-tax-registrations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [taxsettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/index.html#cli-aws-taxsettings) ]

# list-tax-registrations

## Description

Retrieves the tax registration of accounts listed in a consolidated billing family. This can be used to retrieve up to 100 accountsâ tax registrations in one call (default 50).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/taxsettings-2018-05-10/ListTaxRegistrations)

`list-tax-registrations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `accountDetails`

## Synopsis

```
list-tax-registrations
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

accountDetails -> (list)

The list of account details. This contains account Ids and TRN Information for each of the linked accounts.

(structure)

An object with your `accountId` and TRN information.

accountId -> (string)

List of unique account identifiers.

accountMetaData -> (structure)

The meta data information associated with the account.

accountName -> (string)

The Amazon Web Services accounts name.

address -> (structure)

The details of the address associated with the TRN information.

addressLine1 -> (string)

The first line of the address.

addressLine2 -> (string)

The second line of the address, if applicable.

addressLine3 -> (string)

The third line of the address, if applicable. Currently, the Tax Settings API accepts the `addressLine3` parameter only for Saudi Arabia. When you specify a TRN in Saudi Arabia, you must enter the `addressLine3` and specify the building number for the address. For example, you might enter `1234` .

city -> (string)

The city that the address is in.

countryCode -> (string)

The country code for the country that the address is in.

districtOrCounty -> (string)

The district or county the address is located.

### Note

For addresses in Brazil, this parameter uses the name of the neighborhood. When you set a TRN in Brazil, use `districtOrCounty` for the neighborhood name.

postalCode -> (string)

The postal code associated with the address.

stateOrRegion -> (string)

The state, region, or province that the address is located. This field is only required for Canada, India, United Arab Emirates, Romania, and Brazil (CPF). It is optional for all other countries.

If this is required for tax settings, use the same name as shown on the **Tax Settings** page.

addressRoleMap -> (map)

Address roles associated with the account containing country code information.

key -> (string)

value -> (structure)

The jurisdiction details of the TRN information of the customers. This doesnât contain full legal address, and contains only country code and state/region/province.

countryCode -> (string)

The country code of the jurisdiction.

stateOrRegion -> (string)

The state, region, or province associated with the country of the jurisdiction, if applicable.

addressType -> (string)

The type of address associated with the legal profile.

seller -> (string)

Seller information associated with the account.

taxInheritanceDetails -> (structure)

Tax inheritance information associated with the account.

inheritanceObtainedReason -> (string)

Tax inheritance reason information associated with the account.

parentEntityId -> (string)

Tax inheritance parent account information associated with the account.

taxRegistration -> (structure)

Your TRN information. Instead of having full legal address, here TRN information will have jurisdiction details (for example, country code and state/region/province if applicable).

additionalTaxInformation -> (structure)

Additional tax information associated with your TRN.

brazilAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Brazil. The Tax Settings API returns this information in your response when any additional information is present with your TRN in Brazil.

ccmCode -> (string)

The Cadastro de Contribuintes MobiliÃ¡rios (CCM) code for your TRN in Brazil. This only applies for a CNPJ tax type for the SÃ£o Paulo municipality.

legalNatureCode -> (string)

Legal nature of business, based on your TRN in Brazil. This only applies for a CNPJ tax type.

canadaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Canada.

canadaQuebecSalesTaxNumber -> (string)

The Quebec Sales Tax ID number. Leave blank if you do not have a Quebec Sales Tax ID number.

canadaRetailSalesTaxNumber -> (string)

Manitoba Retail Sales Tax ID number. Customers purchasing Amazon Web Services services for resale in Manitoba must provide a valid Retail Sales Tax ID number for Manitoba. Leave this blank if you do not have a Retail Sales Tax ID number in Manitoba or are not purchasing Amazon Web Services services for resale.

isResellerAccount -> (boolean)

The value for this parameter must be `true` if the `provincialSalesTaxId` value is provided for a TRN in British Columbia, Saskatchewan, or Manitoba provinces.

To claim a provincial sales tax (PST) and retail sales tax (RST) reseller exemption, you must confirm that purchases from this account were made for resale. Otherwise, remove the PST or RST number from the `provincialSalesTaxId` parameter from your request.

provincialSalesTaxId -> (string)

The provincial sales tax ID for your TRN in Canada. This parameter can represent the following:

- Provincial sales tax ID number for British Columbia and Saskatchewan provinces
- Manitoba retail sales tax ID number for Manitoba province
- Quebec sales tax ID number for Quebec province

The Tax Setting API only accepts this parameter if the TRN is specified for the previous provinces. For other provinces, the Tax Settings API doesnât accept this parameter.

egyptAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Egypt.

uniqueIdentificationNumber -> (string)

The unique identification number provided by the Egypt Tax Authority.

uniqueIdentificationNumberExpirationDate -> (string)

The expiration date of the unique identification number provided by the Egypt Tax Authority.

estoniaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Estonia.

registryCommercialCode -> (string)

Registry commercial code (RCC) for your TRN in Estonia. This value is an eight-numeric string, such as `12345678` .

georgiaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Georgia.

personType -> (string)

The legal person or physical person assigned to this TRN in Georgia.

greeceAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Greece.

contractingAuthorityCode -> (string)

The code of contracting authority for e-invoicing.

indiaAdditionalInfo -> (structure)

Additional tax information in India.

pan -> (string)

India pan information associated with the account.

indonesiaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Indonesia.

decisionNumber -> (string)

VAT-exempt customers have a Directorate General of Taxation (DGT) exemption letter or certificate (Surat Keterangan Bebas) decision number. Non-collected VAT have a DGT letter or certificate (Surat Keterangan Tidak Dipungut).

ppnExceptionDesignationCode -> (string)

Exception code if you are designated by Directorate General of Taxation (DGT) as a VAT collector, non-collected VAT, or VAT-exempt customer.

taxRegistrationNumberType -> (string)

The tax registration number type.

israelAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Israel.

customerType -> (string)

Customer type for your TRN in Israel. The value can be `Business` or `Individual` . Use `Business` for entities such as not-for-profit and financial institutions.

dealerType -> (string)

Dealer type for your TRN in Israel. If youâre not a local authorized dealer with an Israeli VAT ID, specify your tax identification number so that Amazon Web Services can send you a compliant tax invoice.

italyAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Italy.

cigNumber -> (string)

The tender procedure identification code.

cupNumber -> (string)

Additional tax information to specify for a TRN in Italy. This is managed by the Interministerial Committee for Economic Planning (CIPE) which characterizes every public investment project (Individual Project Code).

sdiAccountId -> (string)

Additional tax information to specify for a TRN in Italy. Use CodiceDestinatario to receive your invoices via web service (API) or FTP.

taxCode -> (string)

List of service tax codes for your TRN in Italy. You can use your customer tax code as part of a VAT Group.

kenyaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Kenya.

personType -> (string)

The legal person or physical person assigned to this TRN in Kenya.

malaysiaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Malaysia.

businessRegistrationNumber -> (string)

The tax registration number (TRN) in Malaysia.

For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid MyKad or NRIC number. For business, you must specify a `businessRegistrationNumber` in `MalaysiaAdditionalInfo` with a TIN type and tax identification number. For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.

For business resellers with service codes, you must specify `businessRegistrationNumber` , `taxInformationNumber` , and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that youâre an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.

serviceTaxCodes -> (list)

List of service tax codes for your TRN in Malaysia.

(string)

taxInformationNumber -> (string)

The tax information number in Malaysia.

For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid MyKad or NRIC number. For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.

For business resellers with service codes, you must specify `businessRegistrationNumber` , `taxInformationNumber` , and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that youâre an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.

polandAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Poland.

individualRegistrationNumber -> (string)

The individual tax registration number (NIP). Individual NIP is valid for other taxes excluding VAT purposes.

isGroupVatEnabled -> (boolean)

True if your business is a member of a VAT group with a NIP active for VAT purposes. Otherwise, this is false.

romaniaAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Romania.

taxRegistrationNumberType -> (string)

The tax registration number type. The value can be `TaxRegistrationNumber` or `LocalRegistrationNumber` .

saudiArabiaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Saudi Arabia.

taxRegistrationNumberType -> (string)

The tax registration number type.

southKoreaAdditionalInfo -> (structure)

Additional tax information associated with your TRN in South Korea.

businessRepresentativeName -> (string)

The business legal name based on the most recently uploaded tax registration certificate.

itemOfBusiness -> (string)

Item of business based on the most recently uploaded tax registration certificate.

lineOfBusiness -> (string)

Line of business based on the most recently uploaded tax registration certificate.

spainAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Spain.

registrationType -> (string)

The registration type in Spain.

turkeyAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Turkey.

industries -> (string)

The industry information that tells the Tax Settings API if youâre subject to additional withholding taxes. This information required for business-to-business (B2B) customers. This information is conditionally mandatory for B2B customers who are subject to KDV tax.

kepEmailId -> (string)

The Registered Electronic Mail (REM) that is used to send notarized communication. This parameter is optional for business-to-business (B2B) and business-to-government (B2G) customers. Itâs not required for business-to-consumer (B2C) customers.

secondaryTaxId -> (string)

Secondary tax ID (âharcama birimi VKNâsiâ). If one isnât provided, we will use your VKN as the secondary ID.

taxOffice -> (string)

The tax office where youâre registered. You can enter this information as a string. The Tax Settings API will add this information to your invoice. This parameter is required for business-to-business (B2B) and business-to-government customers. Itâs not required for business-to-consumer (B2C) customers.

ukraineAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Ukraine.

ukraineTrnType -> (string)

The tax registration type.

uzbekistanAdditionalInfo -> (structure)

Additional tax information associated with your TRN in Uzbekistan.

taxRegistrationNumberType -> (string)

The tax registration number type. The tax registration number type valid values are `Business` and `Individual` .

vatRegistrationNumber -> (string)

The unique 12-digit number issued to identify VAT-registered identities in Uzbekistan.

vietnamAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Vietnam.

electronicTransactionCodeNumber -> (string)

The electronic transaction code number on the tax return document. This field must be provided for successful API operation.

enterpriseIdentificationNumber -> (string)

The enterprise identification number for tax registration. This field must be provided for successful API operation.

paymentVoucherNumber -> (string)

The payment voucher number on the tax return payment document. This field must be provided for successful API operation.

paymentVoucherNumberDate -> (string)

The date on the tax return payment document. This field must be provided for successful API operation.

certifiedEmailId -> (string)

The email address to receive VAT invoices.

jurisdiction -> (structure)

The jurisdiction associated with your TRN information.

countryCode -> (string)

The country code of the jurisdiction.

stateOrRegion -> (string)

The state, region, or province associated with the country of the jurisdiction, if applicable.

legalName -> (string)

The legal name associated with your TRN information.

registrationId -> (string)

Your tax registration unique identifier.

registrationType -> (string)

The type of your tax registration. This can be either `VAT` or `GST` .

sector -> (string)

The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document.

status -> (string)

The status of your TRN. This can be either `Verified` , `Pending` , `Deleted` , or `Rejected` .

taxDocumentMetadatas -> (list)

The metadata for your tax document.

(structure)

The metadata for your tax document.

taxDocumentAccessToken -> (string)

The tax document access token, which contains information that the Tax Settings API uses to locate the tax document.

### Note

If you update your tax registration, the existing `taxDocumentAccessToken` wonât be valid. To get the latest token, call the `GetTaxRegistration` or `ListTaxRegistrations` API operation. This token is valid for 24 hours.

taxDocumentName -> (string)

The name of your tax document.

nextToken -> (string)

The token to retrieve the next set of results.