# update-guardrailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/update-guardrail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/update-guardrail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# update-guardrail

## Description

Updates a guardrail with the values you specify.

- Specify a `name` and optional `description` .
- Specify messages for when the guardrail successfully blocks a prompt or a model response in the `blockedInputMessaging` and `blockedOutputsMessaging` fields.
- Specify topics for the guardrail to deny in the `topicPolicyConfig` object. Each [GuardrailTopicConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html) object in the `topicsConfig` list pertains to one topic.
- Give a `name` and `description` so that the guardrail can properly identify the topic.
- Specify `DENY` in the `type` field.
- (Optional) Provide up to five prompts that you would categorize as belonging to the topic in the `examples` list.
- Specify filter strengths for the harmful categories defined in Amazon Bedrock in the `contentPolicyConfig` object. Each [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html) object in the `filtersConfig` list pertains to a harmful category. For more information, see [Content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters) . For more information about the fields in a content filter, see [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html) .
- Specify the category in the `type` field.
- Specify the strength of the filter for prompts in the `inputStrength` field and for model responses in the `strength` field of the [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html) .
- (Optional) For security, include the ARN of a KMS key in the `kmsKeyId` field.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/UpdateGuardrail)

## Synopsis

```
update-guardrail
--guardrail-identifier <value>
--name <value>
[--description <value>]
[--topic-policy-config <value>]
[--content-policy-config <value>]
[--word-policy-config <value>]
[--sensitive-information-policy-config <value>]
[--contextual-grounding-policy-config <value>]
[--cross-region-config <value>]
--blocked-input-messaging <value>
--blocked-outputs-messaging <value>
[--kms-key-id <value>]
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

`--guardrail-identifier` (string)

The unique identifier of the guardrail. This can be an ID or the ARN.

`--name` (string)

A name for the guardrail.

`--description` (string)

A description of the guardrail.

`--topic-policy-config` (structure)

The topic policy to configure for the guardrail.

topicsConfig -> (list)

A list of policies related to topics that the guardrail should deny.

(structure)

Details about topics for the guardrail to identify and deny.

name -> (string)

The name of the topic to deny.

definition -> (string)

A definition of the topic to deny.

examples -> (list)

A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.

(string)

type -> (string)

Specifies to deny the topic.

inputAction -> (string)

Specifies the action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

JSON Syntax:

```
{
  "topicsConfig": [
    {
      "name": "string",
      "definition": "string",
      "examples": ["string", ...],
      "type": "DENY",
      "inputAction": "BLOCK"|"NONE",
      "outputAction": "BLOCK"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ]
}
```

`--content-policy-config` (structure)

The content policy to configure for the guardrail.

filtersConfig -> (list)

Contains the type of the content filter and how strongly it should apply to prompts and model responses.

(structure)

Contains filter strengths for harmful content. Guardrails support the following content filters to detect and filter harmful user inputs and FM-generated outputs.

- **Hate** â Describes language or a statement that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
- **Insults** â Describes language or a statement that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
- **Sexual** â Describes language or a statement that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
- **Violence** â Describes language or a statement that includes glorification of or threats to inflict physical pain, hurt, or injury toward a person, group or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

For more information, see [Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-filters.html) .

type -> (string)

The harmful category that the content filter is applied to.

inputStrength -> (string)

The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

outputStrength -> (string)

The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

inputModalities -> (list)

The input modalities selected for the guardrail content filter configuration.

(string)

outputModalities -> (list)

The output modalities selected for the guardrail content filter configuration.

(string)

inputAction -> (string)

Specifies the action to take when harmful content is detected. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

JSON Syntax:

```
{
  "filtersConfig": [
    {
      "type": "SEXUAL"|"VIOLENCE"|"HATE"|"INSULTS"|"MISCONDUCT"|"PROMPT_ATTACK",
      "inputStrength": "NONE"|"LOW"|"MEDIUM"|"HIGH",
      "outputStrength": "NONE"|"LOW"|"MEDIUM"|"HIGH",
      "inputModalities": ["TEXT"|"IMAGE", ...],
      "outputModalities": ["TEXT"|"IMAGE", ...],
      "inputAction": "BLOCK"|"NONE",
      "outputAction": "BLOCK"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ]
}
```

`--word-policy-config` (structure)

The word policy to configure for the guardrail.

wordsConfig -> (list)

A list of words to configure for the guardrail.

(structure)

A word to configure for the guardrail.

text -> (string)

Text of the word configured for the guardrail to block.

inputAction -> (string)

Specifies the action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the intput. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

managedWordListsConfig -> (list)

A list of managed words to configure for the guardrail.

(structure)

The managed word list to configure for the guardrail.

type -> (string)

The managed word type to configure for the guardrail.

inputAction -> (string)

Specifies the action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

Shorthand Syntax:

```
wordsConfig=[{text=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean},{text=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean}],managedWordListsConfig=[{type=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean},{type=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean}]
```

JSON Syntax:

```
{
  "wordsConfig": [
    {
      "text": "string",
      "inputAction": "BLOCK"|"NONE",
      "outputAction": "BLOCK"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ],
  "managedWordListsConfig": [
    {
      "type": "PROFANITY",
      "inputAction": "BLOCK"|"NONE",
      "outputAction": "BLOCK"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ]
}
```

`--sensitive-information-policy-config` (structure)

The sensitive information policy to configure for the guardrail.

piiEntitiesConfig -> (list)

A list of PII entities to configure to the guardrail.

(structure)

The PII entity to configure for the guardrail.

type -> (string)

Configure guardrail type when the PII entity is detected.

The following PIIs are used to block or mask sensitive information:

- **General**
- **ADDRESS**   A physical address, such as â100 Main Street, Anytown, USAâ or âSuite #12, Building 123â. An address can include information such as the street, building, location, city, state, country, county, zip code, precinct, and neighborhood.
- **AGE**   An individualâs age, including the quantity and unit of time. For example, in the phrase âI am 40 years old,â Guardrails recognizes â40 yearsâ as an age.
- **NAME**   An individualâs name. This entity type does not include titles, such as Dr., Mr., Mrs., or Miss. guardrails doesnât apply this entity type to names that are part of organizations or addresses. For example, guardrails recognizes the âJohn Doe Organizationâ as an organization, and it recognizes âJane Doe Streetâ as an address.
- **EMAIL**   An email address, such as *marymajor@email.com* .
- **PHONE**   A phone number. This entity type also includes fax and pager numbers.
- **USERNAME**   A user name that identifies an account, such as a login name, screen name, nick name, or handle.
- **PASSWORD**   An alphanumeric string that is used as a password, such as â**very20special#pass** â.
- **DRIVER_ID**   The number assigned to a driverâs license, which is an official document permitting an individual to operate one or more motorized vehicles on a public road. A driverâs license number consists of alphanumeric characters.
- **LICENSE_PLATE**   A license plate for a vehicle is issued by the state or country where the vehicle is registered. The format for passenger vehicles is typically five to eight digits, consisting of upper-case letters and numbers. The format varies depending on the location of the issuing state or country.
- **VEHICLE_IDENTIFICATION_NUMBER**   A Vehicle Identification Number (VIN) uniquely identifies a vehicle. VIN content and format are defined in the *ISO 3779* specification. Each country has specific codes and formats for VINs.
- **Finance**
- **CREDIT_DEBIT_CARD_CVV**   A three-digit card verification code (CVV) that is present on VISA, MasterCard, and Discover credit and debit cards. For American Express credit or debit cards, the CVV is a four-digit numeric code.
- **CREDIT_DEBIT_CARD_EXPIRY**   The expiration date for a credit or debit card. This number is usually four digits long and is often formatted as *month/year* or *MM/YY* . Guardrails recognizes expiration dates such as *01/21* , *01/2021* , and *Jan 2021* .
- **CREDIT_DEBIT_CARD_NUMBER**   The number for a credit or debit card. These numbers can vary from 13 to 16 digits in length. However, Amazon Comprehend also recognizes credit or debit card numbers when only the last four digits are present.
- **PIN**   A four-digit personal identification number (PIN) with which you can access your bank account.
- **INTERNATIONAL_BANK_ACCOUNT_NUMBER**   An International Bank Account Number has specific formats in each country. For more information, see [www.iban.com/structure](https://www.iban.com/structure) .
- **SWIFT_CODE**   A SWIFT code is a standard format of Bank Identifier Code (BIC) used to specify a particular bank or branch. Banks use these codes for money transfers such as international wire transfers. SWIFT codes consist of eight or 11 characters. The 11-digit codes refer to specific branches, while eight-digit codes (or 11-digit codes ending in âXXXâ) refer to the head or primary office.
- **IT**
- **IP_ADDRESS**   An IPv4 address, such as *198.51.100.0* .
- **MAC_ADDRESS**   A *media access control* (MAC) address is a unique identifier assigned to a network interface controller (NIC).
- **URL**   A web address, such as *www.example.com* .
- **AWS_ACCESS_KEY**   A unique identifier thatâs associated with a secret access key; you use the access key ID and secret access key to sign programmatic Amazon Web Services requests cryptographically.
- **AWS_SECRET_KEY**   A unique identifier thatâs associated with an access key. You use the access key ID and secret access key to sign programmatic Amazon Web Services requests cryptographically.
- **USA specific**
- **US_BANK_ACCOUNT_NUMBER**   A US bank account number, which is typically 10 to 12 digits long.
- **US_BANK_ROUTING_NUMBER**   A US bank account routing number. These are typically nine digits long,
- **US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER**   A US Individual Taxpayer Identification Number (ITIN) is a nine-digit number that starts with a â9â and contain a â7â or â8â as the fourth digit. An ITIN can be formatted with a space or a dash after the third and forth digits.
- **US_PASSPORT_NUMBER**   A US passport number. Passport numbers range from six to nine alphanumeric characters.
- **US_SOCIAL_SECURITY_NUMBER**   A US Social Security Number (SSN) is a nine-digit number that is issued to US citizens, permanent residents, and temporary working residents.
- **Canada specific**
- **CA_HEALTH_NUMBER**   A Canadian Health Service Number is a 10-digit unique identifier, required for individuals to access healthcare benefits.
- **CA_SOCIAL_INSURANCE_NUMBER**   A Canadian Social Insurance Number (SIN) is a nine-digit unique identifier, required for individuals to access government programs and benefits. The SIN is formatted as three groups of three digits, such as *123-456-789* . A SIN can be validated through a simple check-digit process called the [Luhn algorithm](https://www.wikipedia.org/wiki/Luhn_algorithm) .
- **UK Specific**
- **UK_NATIONAL_HEALTH_SERVICE_NUMBER**   A UK National Health Service Number is a 10-17 digit number, such as *485 777 3456* . The current system formats the 10-digit number with spaces after the third and sixth digits. The final digit is an error-detecting checksum.
- **UK_NATIONAL_INSURANCE_NUMBER**   A UK National Insurance Number (NINO) provides individuals with access to National Insurance (social security) benefits. It is also used for some purposes in the UK tax system. The number is nine digits long and starts with two letters, followed by six numbers and one letter. A NINO can be formatted with a space or a dash after the two letters and after the second, forth, and sixth digits.
- **UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER**   A UK Unique Taxpayer Reference (UTR) is a 10-digit number that identifies a taxpayer or a business.
- **Custom**
- **Regex filter** - You can use a regular expressions to define patterns for a guardrail to recognize and act upon such as serial number, booking ID etc..

action -> (string)

Configure guardrail action when the PII entity is detected.

inputAction -> (string)

Specifies the action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `ANONYMIZE` â Mask the content and replace it with identifier tags.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `ANONYMIZE` â Mask the content and replace it with identifier tags.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

regexesConfig -> (list)

A list of regular expressions to configure to the guardrail.

(structure)

The regular expression to configure for the guardrail.

name -> (string)

The name of the regular expression to configure for the guardrail.

description -> (string)

The description of the regular expression to configure for the guardrail.

pattern -> (string)

The regular expression pattern to configure for the guardrail.

action -> (string)

The guardrail action to configure when matching regular expression is detected.

inputAction -> (string)

Specifies the action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

Specifies the action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Specifies whether to enable guardrail evaluation on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

Shorthand Syntax:

```
piiEntitiesConfig=[{type=string,action=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean},{type=string,action=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean}],regexesConfig=[{name=string,description=string,pattern=string,action=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean},{name=string,description=string,pattern=string,action=string,inputAction=string,outputAction=string,inputEnabled=boolean,outputEnabled=boolean}]
```

JSON Syntax:

```
{
  "piiEntitiesConfig": [
    {
      "type": "ADDRESS"|"AGE"|"AWS_ACCESS_KEY"|"AWS_SECRET_KEY"|"CA_HEALTH_NUMBER"|"CA_SOCIAL_INSURANCE_NUMBER"|"CREDIT_DEBIT_CARD_CVV"|"CREDIT_DEBIT_CARD_EXPIRY"|"CREDIT_DEBIT_CARD_NUMBER"|"DRIVER_ID"|"EMAIL"|"INTERNATIONAL_BANK_ACCOUNT_NUMBER"|"IP_ADDRESS"|"LICENSE_PLATE"|"MAC_ADDRESS"|"NAME"|"PASSWORD"|"PHONE"|"PIN"|"SWIFT_CODE"|"UK_NATIONAL_HEALTH_SERVICE_NUMBER"|"UK_NATIONAL_INSURANCE_NUMBER"|"UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"|"URL"|"USERNAME"|"US_BANK_ACCOUNT_NUMBER"|"US_BANK_ROUTING_NUMBER"|"US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"|"US_PASSPORT_NUMBER"|"US_SOCIAL_SECURITY_NUMBER"|"VEHICLE_IDENTIFICATION_NUMBER",
      "action": "BLOCK"|"ANONYMIZE"|"NONE",
      "inputAction": "BLOCK"|"ANONYMIZE"|"NONE",
      "outputAction": "BLOCK"|"ANONYMIZE"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ],
  "regexesConfig": [
    {
      "name": "string",
      "description": "string",
      "pattern": "string",
      "action": "BLOCK"|"ANONYMIZE"|"NONE",
      "inputAction": "BLOCK"|"ANONYMIZE"|"NONE",
      "outputAction": "BLOCK"|"ANONYMIZE"|"NONE",
      "inputEnabled": true|false,
      "outputEnabled": true|false
    }
    ...
  ]
}
```

`--contextual-grounding-policy-config` (structure)

The contextual grounding policy configuration used to update a guardrail.

filtersConfig -> (list)

The filter configuration details for the guardrails contextual grounding policy.

(structure)

The filter configuration details for the guardrails contextual grounding filter.

type -> (string)

The filter details for the guardrails contextual grounding filter.

threshold -> (double)

The threshold details for the guardrails contextual grounding filter.

action -> (string)

Specifies the action to take when content fails the contextual grounding evaluation. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

enabled -> (boolean)

Specifies whether to enable contextual grounding evaluation. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

Shorthand Syntax:

```
filtersConfig=[{type=string,threshold=double,action=string,enabled=boolean},{type=string,threshold=double,action=string,enabled=boolean}]
```

JSON Syntax:

```
{
  "filtersConfig": [
    {
      "type": "GROUNDING"|"RELEVANCE",
      "threshold": double,
      "action": "BLOCK"|"NONE",
      "enabled": true|false
    }
    ...
  ]
}
```

`--cross-region-config` (structure)

The system-defined guardrail profile that youâre using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.

For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html) .

guardrailProfileIdentifier -> (string)

The ID or Amazon Resource Name (ARN) of the guardrail profile that your guardrail is using. Guardrail profile availability depends on your current Amazon Web Services Region. For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html) .

Shorthand Syntax:

```
guardrailProfileIdentifier=string
```

JSON Syntax:

```
{
  "guardrailProfileIdentifier": "string"
}
```

`--blocked-input-messaging` (string)

The message to return when the guardrail blocks a prompt.

`--blocked-outputs-messaging` (string)

The message to return when the guardrail blocks a model response.

`--kms-key-id` (string)

The ARN of the KMS key with which to encrypt the guardrail.

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

guardrailId -> (string)

The unique identifier of the guardrail

guardrailArn -> (string)

The ARN of the guardrail.

version -> (string)

The version of the guardrail.

updatedAt -> (timestamp)

The date and time at which the guardrail was updated.