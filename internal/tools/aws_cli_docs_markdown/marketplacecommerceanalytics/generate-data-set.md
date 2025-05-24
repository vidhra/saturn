# generate-data-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplacecommerceanalytics/generate-data-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplacecommerceanalytics/generate-data-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplacecommerceanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplacecommerceanalytics/index.html#cli-aws-marketplacecommerceanalytics) ]

# generate-data-set

## Description

Given a data set type and data set publication date, asynchronously publishes the requested data set to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplacecommerceanalytics-2015-07-01/GenerateDataSet)

## Synopsis

```
generate-data-set
--data-set-type <value>
--data-set-publication-date <value>
--role-name-arn <value>
--destination-s3-bucket-name <value>
[--destination-s3-prefix <value>]
--sns-topic-arn <value>
[--customer-defined-values <value>]
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

`--data-set-type` (string)

The desired data set type.

- customer_subscriber_hourly_monthly_subscriptions From 2017-09-15 to present: Available daily by 24:00 UTC.
- customer_subscriber_annual_subscriptions From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_usage_by_instance_type From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_fees From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_free_trial_conversions From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_new_instances From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_new_product_subscribers From 2017-09-15 to present: Available daily by 24:00 UTC.
- daily_business_canceled_product_subscribers From 2017-09-15 to present: Available daily by 24:00 UTC.
- monthly_revenue_billing_and_revenue_data From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior.
- monthly_revenue_annual_subscriptions From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes up-front software charges (e.g. annual) from one month prior.
- monthly_revenue_field_demonstration_usage From 2018-03-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.
- monthly_revenue_flexible_payment_schedule From 2018-11-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.
- disbursed_amount_by_product From 2017-09-15 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_instance_hours From 2017-09-15 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_customer_geo From 2017-09-15 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_age_of_uncollected_funds From 2017-09-15 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_age_of_disbursed_funds From 2017-09-15 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_age_of_past_due_funds From 2018-04-07 to present: Available every 30 days by 24:00 UTC.
- disbursed_amount_by_uncollected_funds_breakdown From 2019-10-04 to present: Available every 30 days by 24:00 UTC.
- sales_compensation_billed_revenue From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior, and up-front software charges (e.g. annual) from one month prior.
- us_sales_and_use_tax_records From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.
- disbursed_amount_by_product_with_uncollected_funds This data set is deprecated. Download related reports from AMMP instead!
- customer_profile_by_industry This data set is deprecated. Download related reports from AMMP instead!
- customer_profile_by_revenue This data set is deprecated. Download related reports from AMMP instead!
- customer_profile_by_geography This data set is deprecated. Download related reports from AMMP instead!

Possible values:

- `customer_subscriber_hourly_monthly_subscriptions`
- `customer_subscriber_annual_subscriptions`
- `daily_business_usage_by_instance_type`
- `daily_business_fees`
- `daily_business_free_trial_conversions`
- `daily_business_new_instances`
- `daily_business_new_product_subscribers`
- `daily_business_canceled_product_subscribers`
- `monthly_revenue_billing_and_revenue_data`
- `monthly_revenue_annual_subscriptions`
- `monthly_revenue_field_demonstration_usage`
- `monthly_revenue_flexible_payment_schedule`
- `disbursed_amount_by_product`
- `disbursed_amount_by_product_with_uncollected_funds`
- `disbursed_amount_by_instance_hours`
- `disbursed_amount_by_customer_geo`
- `disbursed_amount_by_age_of_uncollected_funds`
- `disbursed_amount_by_age_of_disbursed_funds`
- `disbursed_amount_by_age_of_past_due_funds`
- `disbursed_amount_by_uncollected_funds_breakdown`
- `customer_profile_by_industry`
- `customer_profile_by_revenue`
- `customer_profile_by_geography`
- `sales_compensation_billed_revenue`
- `us_sales_and_use_tax_records`

`--data-set-publication-date` (timestamp)
The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For monthly data sets except those with prefix disbursed_amount, provide a date with month-level granularity for the desired month (the day value will be ignored). For data sets with prefix disbursed_amount, provide a date with day-level granularity for the desired day. For these data sets we will look backwards in time over the range of 31 days until the first data set is found (the latest one).

`--role-name-arn` (string)
The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.

`--destination-s3-bucket-name` (string)
The name (friendly name, not ARN) of the destination S3 bucket.

`--destination-s3-prefix` (string)
(Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name âmybucketâ and the prefix âmyprefix/mydatasetsâ, the output file âoutputfileâ would be published to âs3://mybucket/myprefix/mydatasets/outputfileâ. If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.

`--sns-topic-arn` (string)
Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.

`--customer-defined-values` (map)
(Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems.key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

dataSetRequestId -> (string)

A unique identifier representing a specific request to the GenerateDataSet operation. This identifier can be used to correlate a request with notifications from the SNS topic.