# list-entitiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-entities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-entities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/index.html#cli-aws-marketplace-catalog) ]

# list-entities

## Description

Provides the list of entities of a given type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-catalog-2018-09-17/ListEntities)

`list-entities` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `EntitySummaryList`

## Synopsis

```
list-entities
--catalog <value>
--entity-type <value>
[--filter-list <value>]
[--sort <value>]
[--ownership-type <value>]
[--entity-type-filters <value>]
[--entity-type-sort <value>]
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

`--catalog` (string)

The catalog related to the request. Fixed value: `AWSMarketplace`

`--entity-type` (string)

The type of entities to retrieve. Valid values are: `AmiProduct` , `ContainerProduct` , `DataProduct` , `SaaSProduct` , `ProcurementPolicy` , `Experience` , `Audience` , `BrandingSettings` , `Offer` , `Seller` , `ResaleAuthorization` .

`--filter-list` (list)

An array of filter objects. Each filter object contains two attributes, `filterName` and `filterValues` .

(structure)

A filter object, used to optionally filter results from calls to the `ListEntities` and `ListChangeSets` actions.

Name -> (string)

For `ListEntities` , the supported value for this is an `EntityId` .

For `ListChangeSets` , the supported values are as follows:

ValueList -> (list)

`ListEntities` - This is a list of unique `EntityId` s.

`ListChangeSets` - The supported filter names and associated `ValueList` s is as follows:

- `ChangeSetName` - The supported `ValueList` is a list of non-unique `ChangeSetName` s. These are defined when you call the `StartChangeSet` action.
- `Status` - The supported `ValueList` is a list of statuses for all change set requests.
- `EntityId` - The supported `ValueList` is a list of unique `EntityId` s.
- `BeforeStartTime` - The supported `ValueList` is a list of all change sets that started before the filter value.
- `AfterStartTime` - The supported `ValueList` is a list of all change sets that started after the filter value.
- `BeforeEndTime` - The supported `ValueList` is a list of all change sets that ended before the filter value.
- `AfterEndTime` - The supported `ValueList` is a list of all change sets that ended after the filter value.

(string)

Shorthand Syntax:

```
Name=string,ValueList=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "ValueList": ["string", ...]
  }
  ...
]
```

`--sort` (structure)

An object that contains two attributes, `SortBy` and `SortOrder` .

SortBy -> (string)

For `ListEntities` , supported attributes include `LastModifiedDate` (default) and `EntityId` . In addition to `LastModifiedDate` and `EntityId` , each `EntityType` might support additional fields.

For `ListChangeSets` , supported attributes include `StartTime` and `EndTime` .

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

Shorthand Syntax:

```
SortBy=string,SortOrder=string
```

JSON Syntax:

```
{
  "SortBy": "string",
  "SortOrder": "ASCENDING"|"DESCENDING"
}
```

`--ownership-type` (string)

Filters the returned set of entities based on their owner. The default is `SELF` . To list entities shared with you through AWS Resource Access Manager (AWS RAM), set to `SHARED` . Entities shared through the AWS Marketplace Catalog API `PutResourcePolicy` operation canât be discovered through the `SHARED` parameter.

Possible values:

- `SELF`
- `SHARED`

`--entity-type-filters` (tagged union structure)

A Union object containing filter shapes for all `EntityType` s. Each `EntityTypeFilter` shape will have filters applicable for that `EntityType` that can be used to search or filter entities.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `DataProductFilters`, `SaaSProductFilters`, `AmiProductFilters`, `OfferFilters`, `ContainerProductFilters`, `ResaleAuthorizationFilters`.

DataProductFilters -> (structure)

A filter for data products.

EntityId -> (structure)

Unique identifier for the data product.

ValueList -> (list)

A string array of unique entity id values to be filtered on.

(string)

ProductTitle -> (structure)

The title of the data product.

ValueList -> (list)

A string array of unique product title values to be filtered on.

(string)

WildCardValue -> (string)

A string that will be the `wildCard` input for product tile filter. It matches the provided value as a substring in the actual value.

Visibility -> (structure)

The visibility of the data product.

ValueList -> (list)

A string array of unique visibility values to be filtered on.

(string)

LastModifiedDate -> (structure)

The last date on which the data product was modified.

DateRange -> (structure)

Dates between which the data product was last modified.

AfterValue -> (string)

Date after which the data product was last modified.

BeforeValue -> (string)

Date before which the data product was last modified.

SaaSProductFilters -> (structure)

A filter for SaaS products.

EntityId -> (structure)

Unique identifier for the SaaS product.

ValueList -> (list)

A string array of unique entity id values to be filtered on.

(string)

ProductTitle -> (structure)

The title of the SaaS product.

ValueList -> (list)

A string array of unique product title values to be filtered on.

(string)

WildCardValue -> (string)

A string that will be the `wildCard` input for product tile filter. It matches the provided value as a substring in the actual value.

Visibility -> (structure)

The visibility of the SaaS product.

ValueList -> (list)

A string array of unique visibility values to be filtered on.

(string)

LastModifiedDate -> (structure)

The last date on which the SaaS product was modified.

DateRange -> (structure)

Dates between which the SaaS product was last modified.

AfterValue -> (string)

Date after which the SaaS product was last modified.

BeforeValue -> (string)

Date before which the SaaS product was last modified.

AmiProductFilters -> (structure)

A filter for AMI products.

EntityId -> (structure)

Unique identifier for the AMI product.

ValueList -> (list)

A string array of unique entity id values to be filtered on.

(string)

LastModifiedDate -> (structure)

The last date on which the AMI product was modified.

DateRange -> (structure)

Dates between which the AMI product was last modified.

AfterValue -> (string)

Date after which the AMI product was last modified.

BeforeValue -> (string)

Date before which the AMI product was last modified.

ProductTitle -> (structure)

The title of the AMI product.

ValueList -> (list)

A string array of unique product title values to be filtered on.

(string)

WildCardValue -> (string)

A string that will be the `wildCard` input for product tile filter. It matches the provided value as a substring in the actual value.

Visibility -> (structure)

The visibility of the AMI product.

ValueList -> (list)

A string array of unique visibility values to be filtered on.

(string)

OfferFilters -> (structure)

A filter for offers.

EntityId -> (structure)

Allows filtering on `EntityId` of an offer.

ValueList -> (list)

Allows filtering on entity id of an offer with list input.

(string)

Name -> (structure)

Allows filtering on the `Name` of an offer.

ValueList -> (list)

Allows filtering on the `Name` of an offer with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `Name` of an offer with wild card input.

ProductId -> (structure)

Allows filtering on the `ProductId` of an offer.

ValueList -> (list)

Allows filtering on the `ProductId` of an offer with list input.

(string)

ResaleAuthorizationId -> (structure)

Allows filtering on the `ResaleAuthorizationId` of an offer.

### Note

Not all offers have a `ResaleAuthorizationId` . The response will only include offers for which you have permissions.

ValueList -> (list)

Allows filtering on the `ResaleAuthorizationId` of an offer with list input.

(string)

ReleaseDate -> (structure)

Allows filtering on the `ReleaseDate` of an offer.

DateRange -> (structure)

Allows filtering on the `ReleaseDate` of an offer with date range as input.

AfterValue -> (string)

Allows filtering on the `ReleaseDate` of offers after a date.

BeforeValue -> (string)

Allows filtering on the `ReleaseDate` of offers before a date.

AvailabilityEndDate -> (structure)

Allows filtering on the `AvailabilityEndDate` of an offer.

DateRange -> (structure)

Allows filtering on the `AvailabilityEndDate` of an offer with date range as input.

AfterValue -> (string)

Allows filtering on the `AvailabilityEndDate` of an offer after a date.

BeforeValue -> (string)

Allows filtering on the `AvailabilityEndDate` of an offer before a date.

BuyerAccounts -> (structure)

Allows filtering on the `BuyerAccounts` of an offer.

WildCardValue -> (string)

Allows filtering on the `BuyerAccounts` of an offer with wild card input.

State -> (structure)

Allows filtering on the `State` of an offer.

ValueList -> (list)

Allows filtering on the `State` of an offer with list input.

(string)

Targeting -> (structure)

Allows filtering on the `Targeting` of an offer.

ValueList -> (list)

Allows filtering on the `Targeting` of an offer with list input.

(string)

LastModifiedDate -> (structure)

Allows filtering on the `LastModifiedDate` of an offer.

DateRange -> (structure)

Allows filtering on the `LastModifiedDate` of an offer with date range as input.

AfterValue -> (string)

Allows filtering on the `LastModifiedDate` of an offer after a date.

BeforeValue -> (string)

Allows filtering on the `LastModifiedDate` of an offer before a date.

ContainerProductFilters -> (structure)

A filter for container products.

EntityId -> (structure)

Unique identifier for the container product.

ValueList -> (list)

A string array of unique entity id values to be filtered on.

(string)

LastModifiedDate -> (structure)

The last date on which the container product was modified.

DateRange -> (structure)

Dates between which the container product was last modified.

AfterValue -> (string)

Date after which the container product was last modified.

BeforeValue -> (string)

Date before which the container product was last modified.

ProductTitle -> (structure)

The title of the container product.

ValueList -> (list)

A string array of unique product title values to be filtered on.

(string)

WildCardValue -> (string)

A string that will be the `wildCard` input for product tile filter. It matches the provided value as a substring in the actual value.

Visibility -> (structure)

The visibility of the container product.

ValueList -> (list)

A string array of unique visibility values to be filtered on.

(string)

ResaleAuthorizationFilters -> (structure)

A filter for Resale Authorizations.

EntityId -> (structure)

Allows filtering on the `EntityId` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on `EntityId` of a ResaleAuthorization with list input.

(string)

Name -> (structure)

Allows filtering on the `Name` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `Name` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `Name` of a ResaleAuthorization with wild card input.

ProductId -> (structure)

Allows filtering on the `ProductId` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `ProductId` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `ProductId` of a ResaleAuthorization with wild card input.

CreatedDate -> (structure)

Allows filtering on the `CreatedDate` of a ResaleAuthorization.

DateRange -> (structure)

Allows filtering on `CreatedDate` of a ResaleAuthorization with date range as input.

AfterValue -> (string)

Allows filtering on `CreatedDate` of a ResaleAuthorization after a date.

BeforeValue -> (string)

Allows filtering on `CreatedDate` of a ResaleAuthorization before a date.

ValueList -> (list)

Allows filtering on `CreatedDate` of a ResaleAuthorization with date value as input.

(string)

AvailabilityEndDate -> (structure)

Allows filtering on the `AvailabilityEndDate` of a ResaleAuthorization.

DateRange -> (structure)

Allows filtering on `AvailabilityEndDate` of a ResaleAuthorization with date range as input

AfterValue -> (string)

Allows filtering on `AvailabilityEndDate` of a ResaleAuthorization after a date.

BeforeValue -> (string)

Allows filtering on `AvailabilityEndDate` of a ResaleAuthorization before a date.

ValueList -> (list)

Allows filtering on `AvailabilityEndDate` of a ResaleAuthorization with date value as input.

(string)

ManufacturerAccountId -> (structure)

Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization with wild card input.

ProductName -> (structure)

Allows filtering on the `ProductName` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `ProductName` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `ProductName` of a ResaleAuthorization with wild card input.

ManufacturerLegalName -> (structure)

Allows filtering on the `ManufacturerLegalName` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `ManufacturerLegalName` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `ManufacturerLegalName` of a ResaleAuthorization with wild card input.

ResellerAccountID -> (structure)

Allows filtering on the `ResellerAccountID` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `ResellerAccountID` of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the `ResellerAccountID` of a ResaleAuthorization with wild card input.

ResellerLegalName -> (structure)

Allows filtering on the `ResellerLegalName` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the ResellerLegalNameProductName of a ResaleAuthorization with list input.

(string)

WildCardValue -> (string)

Allows filtering on the ResellerLegalName of a ResaleAuthorization with wild card input.

Status -> (structure)

Allows filtering on the `Status` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `Status` of a ResaleAuthorization with list input.

(string)

OfferExtendedStatus -> (structure)

Allows filtering on the `OfferExtendedStatus` of a ResaleAuthorization.

ValueList -> (list)

Allows filtering on the `OfferExtendedStatus` of a ResaleAuthorization with list input.

(string)

LastModifiedDate -> (structure)

Allows filtering on the `LastModifiedDate` of a ResaleAuthorization.

DateRange -> (structure)

Allows filtering on the `LastModifiedDate` of a ResaleAuthorization with date range as input.

AfterValue -> (string)

Allows filtering on the `LastModifiedDate` of a ResaleAuthorization after a date.

BeforeValue -> (string)

Allows filtering on the `LastModifiedDate` of a ResaleAuthorization before a date.

JSON Syntax:

```
{
  "DataProductFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "ProductTitle": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "Visibility": {
      "ValueList": ["Limited"|"Public"|"Restricted"|"Unavailable"|"Draft", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    }
  },
  "SaaSProductFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "ProductTitle": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "Visibility": {
      "ValueList": ["Limited"|"Public"|"Restricted"|"Draft", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    }
  },
  "AmiProductFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    },
    "ProductTitle": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "Visibility": {
      "ValueList": ["Limited"|"Public"|"Restricted"|"Draft", ...]
    }
  },
  "OfferFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "Name": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ProductId": {
      "ValueList": ["string", ...]
    },
    "ResaleAuthorizationId": {
      "ValueList": ["string", ...]
    },
    "ReleaseDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    },
    "AvailabilityEndDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    },
    "BuyerAccounts": {
      "WildCardValue": "string"
    },
    "State": {
      "ValueList": ["Draft"|"Released", ...]
    },
    "Targeting": {
      "ValueList": ["BuyerAccounts"|"ParticipatingPrograms"|"CountryCodes"|"None", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    }
  },
  "ContainerProductFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    },
    "ProductTitle": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "Visibility": {
      "ValueList": ["Limited"|"Public"|"Restricted"|"Draft", ...]
    }
  },
  "ResaleAuthorizationFilters": {
    "EntityId": {
      "ValueList": ["string", ...]
    },
    "Name": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ProductId": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "CreatedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      },
      "ValueList": ["string", ...]
    },
    "AvailabilityEndDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      },
      "ValueList": ["string", ...]
    },
    "ManufacturerAccountId": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ProductName": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ManufacturerLegalName": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ResellerAccountID": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "ResellerLegalName": {
      "ValueList": ["string", ...],
      "WildCardValue": "string"
    },
    "Status": {
      "ValueList": ["Draft"|"Active"|"Restricted", ...]
    },
    "OfferExtendedStatus": {
      "ValueList": ["string", ...]
    },
    "LastModifiedDate": {
      "DateRange": {
        "AfterValue": "string",
        "BeforeValue": "string"
      }
    }
  }
}
```

`--entity-type-sort` (tagged union structure)

A Union object containing `Sort` shapes for all `EntityType` s. Each `EntityTypeSort` shape will have `SortBy` and `SortOrder` applicable for fields on that `EntityType` . This can be used to sort the results of the filter query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `DataProductSort`, `SaaSProductSort`, `AmiProductSort`, `OfferSort`, `ContainerProductSort`, `ResaleAuthorizationSort`.

DataProductSort -> (structure)

A sort for data products.

SortBy -> (string)

Field to sort the data products by.

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

SaaSProductSort -> (structure)

A sort for SaaS products.

SortBy -> (string)

Field to sort the SaaS products by.

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

AmiProductSort -> (structure)

A sort for AMI products.

SortBy -> (string)

Field to sort the AMI products by.

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

OfferSort -> (structure)

A sort for offers.

SortBy -> (string)

Allows to sort offers.

SortOrder -> (string)

Allows to sort offers.

ContainerProductSort -> (structure)

A sort for container products.

SortBy -> (string)

Field to sort the container products by.

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

ResaleAuthorizationSort -> (structure)

A sort for Resale Authorizations.

SortBy -> (string)

Allows to sort ResaleAuthorization.

SortOrder -> (string)

Allows to sort ResaleAuthorization.

Shorthand Syntax:

```
DataProductSort={SortBy=string,SortOrder=string},SaaSProductSort={SortBy=string,SortOrder=string},AmiProductSort={SortBy=string,SortOrder=string},OfferSort={SortBy=string,SortOrder=string},ContainerProductSort={SortBy=string,SortOrder=string},ResaleAuthorizationSort={SortBy=string,SortOrder=string}
```

JSON Syntax:

```
{
  "DataProductSort": {
    "SortBy": "EntityId"|"ProductTitle"|"Visibility"|"LastModifiedDate",
    "SortOrder": "ASCENDING"|"DESCENDING"
  },
  "SaaSProductSort": {
    "SortBy": "EntityId"|"ProductTitle"|"Visibility"|"LastModifiedDate",
    "SortOrder": "ASCENDING"|"DESCENDING"
  },
  "AmiProductSort": {
    "SortBy": "EntityId"|"LastModifiedDate"|"ProductTitle"|"Visibility",
    "SortOrder": "ASCENDING"|"DESCENDING"
  },
  "OfferSort": {
    "SortBy": "EntityId"|"Name"|"ProductId"|"ResaleAuthorizationId"|"ReleaseDate"|"AvailabilityEndDate"|"BuyerAccounts"|"State"|"Targeting"|"LastModifiedDate",
    "SortOrder": "ASCENDING"|"DESCENDING"
  },
  "ContainerProductSort": {
    "SortBy": "EntityId"|"LastModifiedDate"|"ProductTitle"|"Visibility",
    "SortOrder": "ASCENDING"|"DESCENDING"
  },
  "ResaleAuthorizationSort": {
    "SortBy": "EntityId"|"Name"|"ProductId"|"ProductName"|"ManufacturerAccountId"|"ManufacturerLegalName"|"ResellerAccountID"|"ResellerLegalName"|"Status"|"OfferExtendedStatus"|"CreatedDate"|"AvailabilityEndDate"|"LastModifiedDate",
    "SortOrder": "ASCENDING"|"DESCENDING"
  }
}
```

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

EntitySummaryList -> (list)

Array of `EntitySummary` objects.

(structure)

This object is a container for common summary information about the entity. The summary doesnât contain the whole entity structure, but it does contain information common across all entities.

Name -> (string)

The name for the entity. This value is not unique. It is defined by the seller.

EntityType -> (string)

The type of the entity.

EntityId -> (string)

The unique identifier for the entity.

EntityArn -> (string)

The ARN associated with the unique identifier for the entity.

LastModifiedDate -> (string)

The last time the entity was published, using ISO 8601 format (2018-02-27T13:45:22Z).

Visibility -> (string)

The visibility status of the entity to buyers. This value can be `Public` (everyone can view the entity), `Limited` (the entity is visible to limited accounts only), or `Restricted` (the entity was published and then unpublished and only existing buyers can view it).

AmiProductSummary -> (structure)

An object that contains summary information about the AMI product.

ProductTitle -> (string)

The title of the AMI product.

Visibility -> (string)

The lifecycle of the AMI product.

ContainerProductSummary -> (structure)

An object that contains summary information about the container product.

ProductTitle -> (string)

The title of the container product.

Visibility -> (string)

The lifecycle of the product.

DataProductSummary -> (structure)

An object that contains summary information about the data product.

ProductTitle -> (string)

The title of the data product.

Visibility -> (string)

The lifecycle of the data product.

SaaSProductSummary -> (structure)

An object that contains summary information about the SaaS product.

ProductTitle -> (string)

The title of the SaaS product.

Visibility -> (string)

The lifecycle of the SaaS product.

OfferSummary -> (structure)

An object that contains summary information about the offer.

Name -> (string)

The name of the offer.

ProductId -> (string)

The product ID of the offer.

ResaleAuthorizationId -> (string)

The ResaleAuthorizationId of the offer.

ReleaseDate -> (string)

The release date of the offer.

AvailabilityEndDate -> (string)

The availability end date of the offer.

BuyerAccounts -> (list)

The buyer accounts in the offer.

(string)

State -> (string)

The status of the offer.

Targeting -> (list)

The targeting in the offer.

(string)

ResaleAuthorizationSummary -> (structure)

An object that contains summary information about the Resale Authorization.

Name -> (string)

The name of the ResaleAuthorization.

ProductId -> (string)

The product ID of the ResaleAuthorization.

ProductName -> (string)

The product name of the ResaleAuthorization.

ManufacturerAccountId -> (string)

The manufacturer account ID of the ResaleAuthorization.

ManufacturerLegalName -> (string)

The manufacturer legal name of the ResaleAuthorization.

ResellerAccountID -> (string)

The reseller account ID of the ResaleAuthorization.

ResellerLegalName -> (string)

The reseller legal name of the ResaleAuthorization

Status -> (string)

The status of the ResaleAuthorization.

OfferExtendedStatus -> (string)

The offer extended status of the ResaleAuthorization

CreatedDate -> (string)

The created date of the ResaleAuthorization.

AvailabilityEndDate -> (string)

The availability end date of the ResaleAuthorization.

NextToken -> (string)

The value of the next token if it exists. Null if there is no more result.