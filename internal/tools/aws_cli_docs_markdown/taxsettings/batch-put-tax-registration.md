# batch-put-tax-registrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/batch-put-tax-registration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/batch-put-tax-registration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [taxsettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/index.html#cli-aws-taxsettings) ]

# batch-put-tax-registration

## Description

Adds or updates tax registration for multiple accounts in batch. This can be used to add or update tax registrations for up to five accounts in one batch. You canât set a TRN if thereâs a pending TRN. Youâll need to delete the pending TRN first.

To call this API operation for specific countries, see the following country-specific requirements.

**Bangladesh**

- You must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

**Brazil**

- You must complete the tax registration process in the [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods) page in the Billing and Cost Management console. After your TRN and billing address are verified, you can call this API operation.
- For Amazon Web Services accounts created through Organizations, you can call this API operation when you donât have a billing address.

**Georgia**

- The valid `personType` values are `Physical Person` and `Business` .

**Indonesia**

- `PutTaxRegistration` : The use of this operation to submit tax information is subject to the [Amazon Web Services service terms](http://aws.amazon.com/service-terms/) . By submitting, youâre providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022.
- `BatchPutTaxRegistration` : The use of this operation to submit tax information is subject to the [Amazon Web Services service terms](http://aws.amazon.com/service-terms/) . By submitting, youâre providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022, through our third-party partner PT Achilles Advanced Management (OnlinePajak).
- You must specify the `taxRegistrationNumberType` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object.
- If you specify `decisionNumber` , you must specify the `ppnExceptionDesignationCode` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object. If the `taxRegistrationNumberType` is set to NPWP or NITKU, valid values for `ppnExceptionDesignationCode` are either `01` , `02` , `03` , `07` , or `08` . For other `taxRegistrationNumberType` values, `ppnExceptionDesignationCode` must be either `01` , `07` , or `08` .
- If `ppnExceptionDesignationCode` is `07` , you must specify the `decisionNumber` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object.

**Kenya**

- You must specify the `personType` in the `kenyaAdditionalInfo` field of the `additionalTaxInformation` object.
- If the `personType` is `Physical Person` , you must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

**Malaysia**

- The sector valid values are `Business` and `Individual` .
- `RegistrationType` valid values are `NRIC` for individual, and TIN and sales and service tax (SST) for Business.
- For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid `MyKad` or NRIC number.
- For business, you must specify a `businessRegistrationNumber` in `MalaysiaAdditionalInfo` with a TIN type and tax identification number.
- For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.
- For business resellers with service codes, you must specify `businessRegistrationNumber` , `taxInformationNumber` , and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that youâre an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.
- Amazon Web Services reserves the right to seek additional information and/or take other actions to support your self-declaration as appropriate.
- Amazon Web Services is currently registered under the following service tax codes. You must include at least one of the service tax codes in the service tax code strings to declare yourself as an authorized registered business reseller. Taxable service and service tax codes: Consultancy - 9907061674 Training or coaching service - 9907071685 IT service - 9907101676 Digital services and electronic medium - 9907121690

**Nepal**

- The sector valid values are `Business` and `Individual` .

**Saudi Arabia**

- For `address` , you must specify `addressLine3` .

**South Korea**

- You must specify the `certifiedEmailId` and `legalName` in the `TaxRegistrationEntry` object. Use Korean characters for `legalName` .
- You must specify the `businessRepresentativeName` , `itemOfBusiness` , and `lineOfBusiness` in the `southKoreaAdditionalInfo` field of the `additionalTaxInformation` object. Use Korean characters for these fields.
- You must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.
- For the `address` object, use Korean characters for `addressLine1` , `addressLine2` `city` , `postalCode` , and `stateOrRegion` .

**Spain**

- You must specify the `registrationType` in the `spainAdditionalInfo` field of the `additionalTaxInformation` object.
- If the `registrationType` is `Local` , you must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

**Turkey**

- You must specify the `sector` in the `taxRegistrationEntry` object.
- If your `sector` is `Business` , `Individual` , or `Government` :
- Specify the `taxOffice` . If your `sector` is `Individual` , donât enter this value.
- (Optional) Specify the `kepEmailId` . If your `sector` is `Individual` , donât enter this value.
- **Note:** In the **Tax Settings** page of the Billing console, `Government` appears as **Public institutions**
- If your `sector` is `Business` and youâre subject to KDV tax, you must specify your industry in the `industries` field.
- For `address` , you must specify `districtOrCounty` .

**Ukraine**

- The sector valid values are `Business` and `Individual` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/taxsettings-2018-05-10/BatchPutTaxRegistration)

## Synopsis

```
batch-put-tax-registration
--account-ids <value>
--tax-registration-entry <value>
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

`--account-ids` (list)

List of unique account identifiers.

(string)

Syntax:

```
"string" "string" ...
```

`--tax-registration-entry` (structure)

Your TRN information that will be stored to the accounts mentioned in `putEntries` .

additionalTaxInformation -> (structure)

Additional tax information associated with your TRN. You only need to specify this parameter if Amazon Web Services collects any additional information for your country within  AdditionalInfoRequest .

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

Additional tax information to specify for a TRN in Estonia.

registryCommercialCode -> (string)

Registry commercial code (RCC) for your TRN in Estonia. This value is an eight-numeric string, such as `12345678` .

georgiaAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Georgia.

personType -> (string)

The legal person or physical person assigned to this TRN in Georgia.

greeceAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Greece.

contractingAuthorityCode -> (string)

The code of contracting authority for e-invoicing.

indonesiaAdditionalInfo -> (structure)

decisionNumber -> (string)

VAT-exempt customers have a Directorate General of Taxation (DGT) exemption letter or certificate (Surat Keterangan Bebas) decision number. Non-collected VAT have a DGT letter or certificate (Surat Keterangan Tidak Dipungut).

ppnExceptionDesignationCode -> (string)

Exception code if you are designated by Directorate General of Taxation (DGT) as a VAT collector, non-collected VAT, or VAT-exempt customer.

taxRegistrationNumberType -> (string)

The tax registration number type.

israelAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Israel.

customerType -> (string)

Customer type for your TRN in Israel. The value can be `Business` or `Individual` . Use `Business` for entities such as not-for-profit and financial institutions.

dealerType -> (string)

Dealer type for your TRN in Israel. If youâre not a local authorized dealer with an Israeli VAT ID, specify your tax identification number so that Amazon Web Services can send you a compliant tax invoice.

italyAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Italy.

cigNumber -> (string)

The tender procedure identification code.

cupNumber -> (string)

Additional tax information to specify for a TRN in Italy. This is managed by the Interministerial Committee for Economic Planning (CIPE) which characterizes every public investment project (Individual Project Code).

sdiAccountId -> (string)

Additional tax information to specify for a TRN in Italy. Use CodiceDestinatario to receive your invoices via web service (API) or FTP.

taxCode -> (string)

List of service tax codes for your TRN in Italy. You can use your customer tax code as part of a VAT Group.

kenyaAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Kenya.

personType -> (string)

The legal person or physical person assigned to this TRN in Kenya.

malaysiaAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Malaysia.

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

Additional tax information to specify for a TRN in South Korea.

businessRepresentativeName -> (string)

The business legal name based on the most recently uploaded tax registration certificate.

itemOfBusiness -> (string)

Item of business based on the most recently uploaded tax registration certificate.

lineOfBusiness -> (string)

Line of business based on the most recently uploaded tax registration certificate.

spainAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Spain.

registrationType -> (string)

The registration type in Spain.

turkeyAdditionalInfo -> (structure)

Additional tax information to specify for a TRN in Turkey.

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

Additional tax information to specify for a TRN in Uzbekistan.

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

legalAddress -> (structure)

The legal address associated with your TRN.

### Note

If youâre setting a TRN in Brazil for the CNPJ tax type, you donât need to specify the legal address.

For TRNs in other countries and for CPF tax types Brazil, you must specify the legal address.

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

legalName -> (string)

The legal name associated with your TRN.

### Note

If youâre setting a TRN in Brazil, you donât need to specify the legal name. For TRNs in other countries, you must specify the legal name.

registrationId -> (string)

Your tax registration unique identifier.

registrationType -> (string)

Your tax registration type. This can be either `VAT` or `GST` .

sector -> (string)

The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document.

verificationDetails -> (structure)

Additional details needed to verify your TRN information in Brazil. You only need to specify this parameter when you set a TRN in Brazil that is the CPF tax type.

### Note

Donât specify this parameter to set a TRN in Brazil of the CNPJ tax type or to set a TRN for another country.

dateOfBirth -> (string)

Date of birth to verify your submitted TRN. Use the `YYYY-MM-DD` format.

taxRegistrationDocuments -> (list)

The tax registration document, which is required for specific countries such as Bangladesh, Kenya, South Korea and Spain.

(structure)

Tax registration document information.

file -> (structure)

The tax registration document.

fileContent -> (blob)

The tax registration document content.

fileName -> (string)

The tax registration document name.

s3Location -> (structure)

The Amazon S3 location where your tax registration document is stored.

bucket -> (string)

The name of your Amazon S3 bucket that your tax document is located.

key -> (string)

The object key of your tax document object in Amazon S3.

JSON Syntax:

```
{
  "additionalTaxInformation": {
    "canadaAdditionalInfo": {
      "canadaQuebecSalesTaxNumber": "string",
      "canadaRetailSalesTaxNumber": "string",
      "isResellerAccount": true|false,
      "provincialSalesTaxId": "string"
    },
    "egyptAdditionalInfo": {
      "uniqueIdentificationNumber": "string",
      "uniqueIdentificationNumberExpirationDate": "string"
    },
    "estoniaAdditionalInfo": {
      "registryCommercialCode": "string"
    },
    "georgiaAdditionalInfo": {
      "personType": "Legal Person"|"Physical Person"|"Business"
    },
    "greeceAdditionalInfo": {
      "contractingAuthorityCode": "string"
    },
    "indonesiaAdditionalInfo": {
      "decisionNumber": "string",
      "ppnExceptionDesignationCode": "string",
      "taxRegistrationNumberType": "NIK"|"PassportNumber"|"NPWP"|"NITKU"
    },
    "israelAdditionalInfo": {
      "customerType": "Business"|"Individual",
      "dealerType": "Authorized"|"Non-authorized"
    },
    "italyAdditionalInfo": {
      "cigNumber": "string",
      "cupNumber": "string",
      "sdiAccountId": "string",
      "taxCode": "string"
    },
    "kenyaAdditionalInfo": {
      "personType": "Legal Person"|"Physical Person"|"Business"
    },
    "malaysiaAdditionalInfo": {
      "businessRegistrationNumber": "string",
      "serviceTaxCodes": ["Consultancy"|"Digital Service And Electronic Medium"|"IT Services"|"Training Or Coaching", ...],
      "taxInformationNumber": "string"
    },
    "polandAdditionalInfo": {
      "individualRegistrationNumber": "string",
      "isGroupVatEnabled": true|false
    },
    "romaniaAdditionalInfo": {
      "taxRegistrationNumberType": "TaxRegistrationNumber"|"LocalRegistrationNumber"
    },
    "saudiArabiaAdditionalInfo": {
      "taxRegistrationNumberType": "TaxRegistrationNumber"|"TaxIdentificationNumber"|"CommercialRegistrationNumber"
    },
    "southKoreaAdditionalInfo": {
      "businessRepresentativeName": "string",
      "itemOfBusiness": "string",
      "lineOfBusiness": "string"
    },
    "spainAdditionalInfo": {
      "registrationType": "Intra-EU"|"Local"
    },
    "turkeyAdditionalInfo": {
      "industries": "CirculatingOrg"|"ProfessionalOrg"|"Banks"|"Insurance"|"PensionAndBenefitFunds"|"DevelopmentAgencies",
      "kepEmailId": "string",
      "secondaryTaxId": "string",
      "taxOffice": "string"
    },
    "ukraineAdditionalInfo": {
      "ukraineTrnType": "Business"|"Individual"
    },
    "uzbekistanAdditionalInfo": {
      "taxRegistrationNumberType": "Business"|"Individual",
      "vatRegistrationNumber": "string"
    },
    "vietnamAdditionalInfo": {
      "electronicTransactionCodeNumber": "string",
      "enterpriseIdentificationNumber": "string",
      "paymentVoucherNumber": "string",
      "paymentVoucherNumberDate": "string"
    }
  },
  "certifiedEmailId": "string",
  "legalAddress": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "countryCode": "string",
    "districtOrCounty": "string",
    "postalCode": "string",
    "stateOrRegion": "string"
  },
  "legalName": "string",
  "registrationId": "string",
  "registrationType": "VAT"|"GST"|"CPF"|"CNPJ"|"SST"|"TIN"|"NRIC",
  "sector": "Business"|"Individual"|"Government",
  "verificationDetails": {
    "dateOfBirth": "string",
    "taxRegistrationDocuments": [
      {
        "file": {
          "fileContent": blob,
          "fileName": "string"
        },
        "s3Location": {
          "bucket": "string",
          "key": "string"
        }
      }
      ...
    ]
  }
}
```

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

errors -> (list)

List of errors for the accounts the TRN information could not be added or updated to.

(structure)

The error object for representing failures in the `BatchPutTaxRegistration` operation.

accountId -> (string)

The unique account identifier for the account that the tax registration couldnât be added, or updated during the `BatchPutTaxRegistration` operation.

code -> (string)

The error code for an individual failure in the `BatchPutTaxRegistration` operation.

message -> (string)

The error message for an individual failure in the `BatchPutTaxRegistration` operation.

status -> (string)

The status of your TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be `Verified` , `Pending` or `Rejected` .