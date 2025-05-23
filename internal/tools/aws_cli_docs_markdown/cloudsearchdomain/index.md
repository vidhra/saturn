# cloudsearchdomainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cloudsearchdomain

## Description

You use the AmazonCloudSearch2013 API to upload documents to a search domain and search those documents.

The endpoints for submitting `UploadDocuments` , `Search` , and `Suggest` requests are domain-specific. To get the endpoints for your domain, use the Amazon CloudSearch configuration service `DescribeDomains` action. The domain endpoints are also displayed on the domain dashboard in the Amazon CloudSearch console. You submit suggest requests to the search endpoint.

For more information, see the [Amazon CloudSearch Developer Guide](http://docs.aws.amazon.com/cloudsearch/latest/developerguide) .

## Available Commands

- [search](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/search.html)
- [suggest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/suggest.html)
- [upload-documents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/upload-documents.html)