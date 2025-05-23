# esÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# es

## Description

Use the Amazon Elasticsearch Configuration API to create, configure, and manage Elasticsearch domains.

For sample code that uses the Configuration API, see the [Amazon Elasticsearch Service Developer Guide](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-configuration-samples.html) . The guide also contains [sample code for sending signed HTTP requests to the Elasticsearch APIs](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-request-signing.html) .

The endpoint for configuration service requests is region-specific: es.*region* .amazonaws.com. For example, es.us-east-1.amazonaws.com. For a current list of supported regions and endpoints, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticsearch-service-regions) .

## Available Commands

- [accept-inbound-cross-cluster-search-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/accept-inbound-cross-cluster-search-connection.html)
- [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/add-tags.html)
- [associate-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/associate-package.html)
- [authorize-vpc-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/authorize-vpc-endpoint-access.html)
- [cancel-domain-config-change](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/cancel-domain-config-change.html)
- [cancel-elasticsearch-service-software-update](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/cancel-elasticsearch-service-software-update.html)
- [create-elasticsearch-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-elasticsearch-domain.html)
- [create-outbound-cross-cluster-search-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-outbound-cross-cluster-search-connection.html)
- [create-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-package.html)
- [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-vpc-endpoint.html)
- [delete-elasticsearch-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-domain.html)
- [delete-elasticsearch-service-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-service-role.html)
- [delete-inbound-cross-cluster-search-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-inbound-cross-cluster-search-connection.html)
- [delete-outbound-cross-cluster-search-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-outbound-cross-cluster-search-connection.html)
- [delete-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-package.html)
- [delete-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-vpc-endpoint.html)
- [describe-domain-auto-tunes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-domain-auto-tunes.html)
- [describe-domain-change-progress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-domain-change-progress.html)
- [describe-elasticsearch-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain.html)
- [describe-elasticsearch-domain-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain-config.html)
- [describe-elasticsearch-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domains.html)
- [describe-elasticsearch-instance-type-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-instance-type-limits.html)
- [describe-inbound-cross-cluster-search-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-inbound-cross-cluster-search-connections.html)
- [describe-outbound-cross-cluster-search-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-outbound-cross-cluster-search-connections.html)
- [describe-packages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-packages.html)
- [describe-reserved-elasticsearch-instance-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-reserved-elasticsearch-instance-offerings.html)
- [describe-reserved-elasticsearch-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-reserved-elasticsearch-instances.html)
- [describe-vpc-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-vpc-endpoints.html)
- [dissociate-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/dissociate-package.html)
- [get-compatible-elasticsearch-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/get-compatible-elasticsearch-versions.html)
- [get-package-version-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/get-package-version-history.html)
- [get-upgrade-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/get-upgrade-history.html)
- [get-upgrade-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/get-upgrade-status.html)
- [list-domain-names](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-domain-names.html)
- [list-domains-for-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-domains-for-package.html)
- [list-elasticsearch-instance-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-elasticsearch-instance-types.html)
- [list-elasticsearch-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-elasticsearch-versions.html)
- [list-packages-for-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-packages-for-domain.html)
- [list-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-tags.html)
- [list-vpc-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-vpc-endpoint-access.html)
- [list-vpc-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-vpc-endpoints.html)
- [list-vpc-endpoints-for-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-vpc-endpoints-for-domain.html)
- [purchase-reserved-elasticsearch-instance-offering](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/purchase-reserved-elasticsearch-instance-offering.html)
- [reject-inbound-cross-cluster-search-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/reject-inbound-cross-cluster-search-connection.html)
- [remove-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/remove-tags.html)
- [revoke-vpc-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/revoke-vpc-endpoint-access.html)
- [start-elasticsearch-service-software-update](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/start-elasticsearch-service-software-update.html)
- [update-elasticsearch-domain-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-elasticsearch-domain-config.html)
- [update-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-package.html)
- [update-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-vpc-endpoint.html)
- [upgrade-elasticsearch-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/upgrade-elasticsearch-domain.html)