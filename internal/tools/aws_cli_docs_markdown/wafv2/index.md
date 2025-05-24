# wafv2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# wafv2

## Description

### Note

This is the latest version of the **WAF** API, released in November, 2019. The names of the entities that you use to access this API, like endpoints and namespaces, all have the versioning information added, like âV2â or âv2â, to distinguish from the prior version. We recommend migrating your resources to this version, because it has a number of significant improvements.

If you used WAF prior to this release, you canât use this WAFV2 API to access any WAF resources that you created before. WAF Classic support will end on September 30, 2025.

For information about WAF, including how to migrate your WAF Classic resources to this version, see the [WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) .

WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to a protected resource. Protected resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner service, Amplify application, and Amazon Web Services Verified Access instance. WAF also lets you control access to your content, to protect the Amazon Web Services resource that WAF is monitoring. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, the protected resource responds to requests with either the requested content, an HTTP 403 status code (Forbidden), or with a custom response.

This API guide is for developers who need detailed information about WAF API actions, data types, and errors. For detailed information about WAF features and guidance for configuring and using WAF, see the [WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) .

You can make calls using the endpoints listed in [WAF endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/waf.html) .

- For regional resources, you can use any of the endpoints in the list. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AppSync GraphQL API, an Amazon Cognito user pool, an App Runner service, or an Amazon Web Services Verified Access instance.
- For Amazon CloudFront and Amplify, you must use the API endpoint listed for US East (N. Virginia): us-east-1.

Alternatively, you can use one of the Amazon Web Services SDKs to access an API thatâs tailored to the programming language or platform that youâre using. For more information, see [Amazon Web Services SDKs](http://aws.amazon.com/tools/#SDKs) .

## Available Commands

- [associate-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/associate-web-acl.html)
- [check-capacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/check-capacity.html)
- [create-api-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-api-key.html)
- [create-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-ip-set.html)
- [create-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-regex-pattern-set.html)
- [create-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-rule-group.html)
- [create-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-web-acl.html)
- [delete-api-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-api-key.html)
- [delete-firewall-manager-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-firewall-manager-rule-groups.html)
- [delete-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-ip-set.html)
- [delete-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-logging-configuration.html)
- [delete-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-permission-policy.html)
- [delete-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-regex-pattern-set.html)
- [delete-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-rule-group.html)
- [delete-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-web-acl.html)
- [describe-all-managed-products](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-all-managed-products.html)
- [describe-managed-products-by-vendor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-products-by-vendor.html)
- [describe-managed-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-rule-group.html)
- [disassociate-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/disassociate-web-acl.html)
- [generate-mobile-sdk-release-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/generate-mobile-sdk-release-url.html)
- [get-decrypted-api-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-decrypted-api-key.html)
- [get-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-ip-set.html)
- [get-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html)
- [get-managed-rule-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-managed-rule-set.html)
- [get-mobile-sdk-release](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-mobile-sdk-release.html)
- [get-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-permission-policy.html)
- [get-rate-based-statement-managed-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rate-based-statement-managed-keys.html)
- [get-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-regex-pattern-set.html)
- [get-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rule-group.html)
- [get-sampled-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-sampled-requests.html)
- [get-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-web-acl.html)
- [get-web-acl-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-web-acl-for-resource.html)
- [list-api-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-api-keys.html)
- [list-available-managed-rule-group-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-available-managed-rule-group-versions.html)
- [list-available-managed-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-available-managed-rule-groups.html)
- [list-ip-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-ip-sets.html)
- [list-logging-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-logging-configurations.html)
- [list-managed-rule-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-managed-rule-sets.html)
- [list-mobile-sdk-releases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-mobile-sdk-releases.html)
- [list-regex-pattern-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-regex-pattern-sets.html)
- [list-resources-for-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-resources-for-web-acl.html)
- [list-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-rule-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-tags-for-resource.html)
- [list-web-acls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-web-acls.html)
- [put-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-logging-configuration.html)
- [put-managed-rule-set-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-managed-rule-set-versions.html)
- [put-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-permission-policy.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/untag-resource.html)
- [update-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-ip-set.html)
- [update-managed-rule-set-version-expiry-date](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-managed-rule-set-version-expiry-date.html)
- [update-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-regex-pattern-set.html)
- [update-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-rule-group.html)
- [update-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-web-acl.html)