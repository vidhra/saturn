# s3tablesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# s3tables

## Description

An Amazon S3 table represents a structured dataset consisting of tabular data in [Apache Parquet](https://parquet.apache.org/docs/) format and related metadata. This data is stored inside an S3 table as a subresource. All tables in a table bucket are stored in the [Apache Iceberg](https://iceberg.apache.org/docs/latest/) table format. Through integration with the [Amazon Web Services Glue Data Catalog](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) you can interact with your tables using Amazon Web Services analytics services, such as [Amazon Athena](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/athena/) and [Amazon Redshift](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/redshift/) . Amazon S3 manages maintenance of your tables through automatic file compaction and snapshot management. For more information, see [Amazon S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html) .

## Available Commands

- [create-namespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/create-namespace.html)
- [create-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/create-table.html)
- [create-table-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/create-table-bucket.html)
- [delete-namespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-namespace.html)
- [delete-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-table.html)
- [delete-table-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-table-bucket.html)
- [delete-table-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-table-bucket-encryption.html)
- [delete-table-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-table-bucket-policy.html)
- [delete-table-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/delete-table-policy.html)
- [get-namespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-namespace.html)
- [get-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table.html)
- [get-table-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-bucket.html)
- [get-table-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-bucket-encryption.html)
- [get-table-bucket-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-bucket-maintenance-configuration.html)
- [get-table-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-bucket-policy.html)
- [get-table-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-encryption.html)
- [get-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-maintenance-configuration.html)
- [get-table-maintenance-job-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-maintenance-job-status.html)
- [get-table-metadata-location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-metadata-location.html)
- [get-table-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-policy.html)
- [list-namespaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/list-namespaces.html)
- [list-table-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/list-table-buckets.html)
- [list-tables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/list-tables.html)
- [put-table-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-bucket-encryption.html)
- [put-table-bucket-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-bucket-maintenance-configuration.html)
- [put-table-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-bucket-policy.html)
- [put-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html)
- [put-table-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-policy.html)
- [rename-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/rename-table.html)
- [update-table-metadata-location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/update-table-metadata-location.html)