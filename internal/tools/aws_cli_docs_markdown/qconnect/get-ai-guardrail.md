# get-ai-guardrailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/get-ai-guardrail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/get-ai-guardrail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# get-ai-guardrail

## Description

Gets the Amazon Q in Connect AI Guardrail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/GetAIGuardrail)

## Synopsis

```
get-ai-guardrail
--assistant-id <value>
--ai-guardrail-id <value>
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

`--assistant-id` (string)

The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.

`--ai-guardrail-id` (string)

The identifier of the Amazon Q in Connect AI Guardrail.

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

aiGuardrail -> (structure)

The data of the AI Guardrail.

assistantId -> (string)

The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.

assistantArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

aiGuardrailArn -> (string)

The Amazon Resource Name (ARN) of the AI Guardrail.

aiGuardrailId -> (string)

The identifier of the Amazon Q in Connect AI Guardrail.

name -> (string)

The name of the AI Guardrail.

visibilityStatus -> (string)

The visibility status of the AI Guardrail.

blockedInputMessaging -> (string)

The message to return when the AI Guardrail blocks a prompt.

blockedOutputsMessaging -> (string)

The message to return when the AI Guardrail blocks a model response.

description -> (string)

A description of the AI Guardrail.

topicPolicyConfig -> (structure)

Contains details about topics that the AI Guardrail should identify and deny.

topicsConfig -> (list)

A list of policies related to topics that the AI Guardrail should deny.

(structure)

Details about topics for the AI Guardrail to identify and deny.

name -> (string)

The name of the topic to deny.

definition -> (string)

A definition of the topic to deny.

examples -> (list)

A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.

(string)

Text example in topic policy

type -> (string)

Specifies to deny the topic.

contentPolicyConfig -> (structure)

Contains details about how to handle harmful content.

filtersConfig -> (list)

Contains the type of the content filter and how strongly it should apply to prompts and model responses.

(structure)

Contains filter strengths for harmful content. AI Guardrailâs support the following content filters to detect and filter harmful user inputs and FM-generated outputs.

- **Hate** : Describes input prompts and model responses that discriminate, criticize, insult, denounce, or dehumanize a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
- **Insults** : Describes input prompts and model responses that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
- **Sexual** : Describes input prompts and model responses that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
- **Violence** : Describes input prompts and model responses that includes glorification of, or threats to inflict physical pain, hurt, or injury toward a person, group, or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

type -> (string)

The harmful category that the content filter is applied to.

inputStrength -> (string)

The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

outputStrength -> (string)

The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

wordPolicyConfig -> (structure)

Contains details about the word policy to configured for the AI Guardrail.

wordsConfig -> (list)

A list of words to configure for the AI Guardrail.

(structure)

A word to configure for the AI Guardrail.

text -> (string)

Text of the word configured for the AI Guardrail to block.

managedWordListsConfig -> (list)

A list of managed words to configure for the AI Guardrail.

(structure)

The managed word list to configure for the AI Guardrail.

type -> (string)

The managed word type to configure for the AI Guardrail.

sensitiveInformationPolicyConfig -> (structure)

Contains details about PII entities and regular expressions to configure for the AI Guardrail.

piiEntitiesConfig -> (list)

A list of PII entities to configure to the AI Guardrail.

(structure)

The PII entity to configure for the AI Guardrail.

type -> (string)

Configure AI Guardrail type when the PII entity is detected.

The following PIIs are used to block or mask sensitive information:

- **General**
- **ADDRESS**   A physical address, such as â100 Main Street, Anytown, USAâ or âSuite #12, Building 123â. An address can include information such as the street, building, location, city, state, country, county, zip code, precinct, and neighborhood.
- **AGE**   An individualâs age, including the quantity and unit of time. For example, in the phrase âI am 40 years old,â Guarrails recognizes â40 yearsâ as an age.
- **NAME**   An individualâs name. This entity type does not include titles, such as Dr., Mr., Mrs., or Miss. AI Guardrail doesnât apply this entity type to names that are part of organizations or addresses. For example, AI Guardrail recognizes the âJohn Doe Organizationâ as an organization, and it recognizes âJane Doe Streetâ as an address.
- **EMAIL**   An email address, such as *marymajor@email.com* .
- **PHONE**   A phone number. This entity type also includes fax and pager numbers.
- **USERNAME**   A user name that identifies an account, such as a login name, screen name, nick name, or handle.
- **PASSWORD**   An alphanumeric string that is used as a password, such as â**very20special#pass** â.
- **DRIVER_ID**   The number assigned to a driverâs license, which is an official document permitting an individual to operate one or more motorized vehicles on a public road. A driverâs license number consists of alphanumeric characters.
- **LICENSE_PLATE**   A license plate for a vehicle is issued by the state or country where the vehicle is registered. The format for passenger vehicles is typically five to eight digits, consisting of upper-case letters and numbers. The format varies depending on the location of the issuing state or country.
- **VEHICLE_IDENTIFICATION_NUMBER**   A Vehicle Identification Number (VIN) uniquely identifies a vehicle. VIN content and format are defined in the *ISO 3779* specification. Each country has specific codes and formats for VINs.
- **Finance**
- **CREDIT_DEBIT_CARD_CVV**   A three-digit card verification code (CVV) that is present on VISA, MasterCard, and Discover credit and debit cards. For American Express credit or debit cards, the CVV is a four-digit numeric code.
- **CREDIT_DEBIT_CARD_EXPIRY**   The expiration date for a credit or debit card. This number is usually four digits long and is often formatted as *month/year* or *MM/YY* . AI Guardrail recognizes expiration dates such as *01/21* , *01/2021* , and *Jan 2021* .
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
- **UK_NATIONAL_HEALTH_SERVICE_NUMBER**   A UK National Health Service Number is a 10-17 digit number, such as *485 555 3456* . The current system formats the 10-digit number with spaces after the third and sixth digits. The final digit is an error-detecting checksum.
- **UK_NATIONAL_INSURANCE_NUMBER**   A UK National Insurance Number (NINO) provides individuals with access to National Insurance (social security) benefits. It is also used for some purposes in the UK tax system. The number is nine digits long and starts with two letters, followed by six numbers and one letter. A NINO can be formatted with a space or a dash after the two letters and after the second, forth, and sixth digits.
- **UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER**   A UK Unique Taxpayer Reference (UTR) is a 10-digit number that identifies a taxpayer or a business.
- **Custom**
- **Regex filter** - You can use a regular expressions to define patterns for an AI Guardrail to recognize and act upon such as serial number, booking ID etc..

action -> (string)

Configure AI Guardrailâs action when the PII entity is detected.

regexesConfig -> (list)

A list of regular expressions to configure to the AI Guardrail.

(structure)

The regular expression to configure for the AI Guardrail.

name -> (string)

The name of the regular expression to configure for the AI Guardrail.

description -> (string)

The description of the regular expression to configure for the AI Guardrail.

pattern -> (string)

The regular expression pattern to configure for the AI Guardrail.

action -> (string)

The AI Guardrail action to configure when matching regular expression is detected.

contextualGroundingPolicyConfig -> (structure)

The policy configuration details for the AI Guardrailâs contextual grounding policy.

filtersConfig -> (list)

The filter configuration details for the AI Guardrails contextual grounding policy.

(structure)

The filter configuration details for the AI Guardrailâs contextual grounding filter.

type -> (string)

The filter type for the AI Guardrailâs contextual grounding filter.

threshold -> (double)

The threshold details for the AI Guardrailâs contextual grounding filter.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

status -> (string)

The status of the AI Guardrail.

modifiedTime -> (timestamp)

The time the AI Guardrail was last modified.

versionNumber -> (long)

The version number of the AI Guardrail version (returned if an AI Guardrail version was specified via use of a qualifier for the `aiGuardrailId` on the request).